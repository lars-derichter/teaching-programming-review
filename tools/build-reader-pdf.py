#!/usr/bin/env python3
import os, re, sys, subprocess, pathlib, html as htmlmod
import fitz  # PyMuPDF

HERE = pathlib.Path(__file__).resolve().parent          # tools/
PROJECT = HERE.parent                                   # project root
ROOT = PROJECT / "reader"                               # the reader sources
PARTS = HERE / ".build" / "parts"                       # intermediates (gitignored)
PARTS.mkdir(parents=True, exist_ok=True)
CSS = (HERE / "style.css").read_text()
CHROME = os.environ.get("CHROME_BIN",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
GENTIUM = str(pathlib.Path.home() / "Library/Fonts/GentiumBookPlus-Regular.ttf")
GENTIUM_IT = str(pathlib.Path.home() / "Library/Fonts/GentiumBookPlus-Italic.ttf")
OUT = ROOT / "teaching-programming-to-beginners-reader.pdf"

THEME_FILES = ["01-orientation.md","02-what-makes-programming-hard.md",
    "03-is-programming-ability-innate.md","04-how-people-learn-to-program.md",
    "05-evidence-based-practice.md","06-feedback-and-assessment.md",
    "07-the-learner.md","08-vocational-context.md","09-generative-ai.md"]

# ---------- helpers ----------
def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stdout + r.stderr); raise SystemExit(f"cmd failed: {cmd[:3]}")
    return r.stdout

def md_to_html_fragment(md):
    r = subprocess.run(["pandoc","-f","markdown","-t","html5","--wrap=none"],
                       input=md, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr); raise SystemExit("pandoc failed")
    return r.stdout

def eyebrowize(html):
    # h1 "Theme N — Title" -> eyebrow + ruled h1
    def h1(m):
        t = m.group(1)
        mt = re.match(r'Theme\s+(\d+)\s+—\s+(.*)', t)
        if mt:
            return f'<p class="eyebrow">Theme {mt.group(1)}</p><h1 class="ruled">{mt.group(2)}</h1>'
        return f'<p class="eyebrow">The reader</p><h1 class="ruled">{t}</h1>'
    html = re.sub(r'<h1[^>]*>(.*?)</h1>', h1, html, count=1, flags=re.S)
    # h2 "Reading N — ..." -> eyebrow Reading N + ruled h2
    def h2(m):
        t = m.group(1)
        mr = re.match(r'Reading\s+(\d+)\s+—\s+(.*)', t, re.S)
        if mr:
            return f'<p class="eyebrow sage">Reading {mr.group(1)}</p><h2 class="ruled">{mr.group(2)}</h2>'
        return f'<h2 class="ruled">{t}</h2>'
    html = re.sub(r'<h2[^>]*>(.*?)</h2>', h2, html, flags=re.S)
    return html

def keep_with_next(html):
    # Bind each heading (plus a preceding eyebrow) to its following block in a
    # .keep group (break-inside:avoid). break-after:avoid alone is unreliable in
    # Chrome once a full page of content precedes the heading.
    pat = re.compile(
        r'(?:(<p class="eyebrow[^"]*">.*?</p>)\s*)?'      # 1: optional eyebrow
        r'(<h[1-4][^>]*>.*?</h[1-4]>)\s*'                 # 2: heading
        r'(<(p|ul|ol|blockquote|pre|div)\b[^>]*>.*?</\4>)',  # 3: next block
        re.S)
    return pat.sub(lambda m: '<div class="keep">'
                   + (m.group(1) or "") + m.group(2) + m.group(3) + '</div>', html)

def transform_pdf_notes(md, follows):
    # replace *PDF: [..](..) — citation.* italic paragraph with a fenced article-source div
    pat = re.compile(r'\*PDF:\s*\[[^\]]*\]\([^)]*\)\s*(.*?)\*', re.S)
    def repl(m):
        cit = re.sub(r'\s+', ' ', m.group(1)).strip()
        cit = re.sub(r'^[—-]\s*', '', cit).rstrip('.')
        cit = htmlmod.unescape(cit)
        return (f'::: article-source\n**Source.** {cit}.\n\n'
                f'[{follows}]{{.follows}}\n:::')
    return pat.sub(repl, md)

def wrap(fragment, bodyclass, extra_head=""):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style>'
            f'{extra_head}</head><body class="{bodyclass}"><div class="wrap">'
            f'{fragment}</div></body></html>')

def render(name, html):
    hp = PARTS / f"{name}.html"; pp = PARTS / f"{name}.pdf"
    hp.write_text(html)
    subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-pdf-header-footer",
        f"--print-to-pdf={pp}", f"file://{hp}"], capture_output=True)
    if not pp.exists(): raise SystemExit(f"render failed: {name}")
    return pp

def npages(pdf):
    d = fitz.open(pdf); n = d.page_count; d.close(); return n

def short_reading(heading):  # "Reading 1 — Brown & Wilson (2018), long" -> up to year
    m = re.match(r'(Reading\s+\d+\s+—\s+.*?\(\d{4}\))', heading)
    return m.group(1) if m else heading

def short_article(heading):  # "Porter, Bailey Lee & Simon (2013), long" -> up to year
    m = re.match(r'(.*?\(\d{4}\))', heading)
    return m.group(1) if m else heading

def art_path(text):
    m = re.search(r'\]\((articles/[^)]+\.pdf)\)', text)
    return ROOT / m.group(1)

# ---------- build ordered parts ----------
# part = dict(pdf=Path, kind='cover'|'prose'|'article', label=str, toc=[(level,title,is_front)])
parts = []
def add(pdf, kind, label, toc=None):
    parts.append(dict(pdf=(pathlib.Path(pdf) if pdf else None), kind=kind, label=label, toc=toc or []))

TITLE = "Teaching programming to beginners"
SUB = "A reader — fifteen key studies from computing education research, with introductions"

# --- title page ---
title_html = wrap(f'''
<div class="title-page">
  <p class="kicker">Reader</p>
  <h1>{TITLE}</h1>
  <p class="sub">{SUB}</p>
  <div class="rule"></div>
  <p class="meta"><span class="who">Lars De Richter</span><br>
  Thomas More Hogeschool<br>Groundwork for an educational-sciences research
  project on teaching programming to beginners in tertiary education<br>2026</p>
  <p class="ornament">&#10047; <span class="c">&#10048;</span> &#10047;</p>
</div>''', "cover")
add(render("00-title", title_html), "cover", "")

# --- colophon ---
colophon_html = wrap('''
<div class="colophon">
<p class="eyebrow">About this document</p>
<h1 class="ruled">Colophon &amp; licence</h1>

<div class="note-block">
<span class="lbl">On the use of AI</span>
<p>This reader was compiled with substantial assistance from AI. The article
selection derives from a human-authored literature review; every article was
read in full before inclusion. The theme and article introductions were drafted
with AI support and edited for use in teaching. As the introductions summarise
and interpret the original studies, verify any claim against the original
publication before citing it in formal academic work.</p>
</div>

<div class="note-block">
<span class="lbl">An experiment in the making</span>
<p>Producing this integrated document was itself part of an ongoing experiment
to test the capabilities of Claude Fable 5 — including the assembly of this
PDF, its typographic styling, and the interleaving of the source articles.
It is shared in that spirit: a working document, openly built.</p>
</div>

<div class="note-block license">
<span class="lbl">Licence</span>
<p>The original material in this reader — the selection, the compilation, and
all theme and article introductions — is released by Lars De Richter under
<span class="cc">CC BY-NC-SA 4.0</span> (Attribution &ndash; NonCommercial &ndash;
ShareAlike).</p>
<p>The fifteen main articles and the six additional papers reproduced here are
<em>not</em> covered by that licence. Each remains under its own copyright,
held by its authors and publishers, and is included for educational use only.
Obtain the appropriate permissions before any wider distribution. Where an
article is open access, its own licence governs its reuse.</p>
</div>
</div>''', "parchment")
add(render("00-colophon", colophon_html), "cover", "")

# --- TOC placeholder (rendered after entries known) ---
toc_index = len(parts)
add(None, "cover", "")   # filled later

# --- content: introduction (theme 0) ---
intro_md = (ROOT / "00-introduction.md").read_text()
intro_html = wrap(keep_with_next(eyebrowize(md_to_html_fragment(intro_md))), "prose")
add(render("c00-intro", intro_html), "prose", "Introduction",
    toc=[(1, "Introduction to this reader")])

# --- themes 1..9 ---
for tf in THEME_FILES:
    md = (ROOT / tf).read_text()
    lines = md.split("\n")
    h1line = next(l for l in lines if l.startswith("# "))
    mth = re.match(r'#\s+Theme\s+(\d+)\s+—\s+(.*)', h1line)
    tnum, ttitle = mth.group(1), mth.group(2)
    idx = [i for i,l in enumerate(lines) if l.startswith("## Reading")]
    pre = "\n".join(lines[:idx[0]])
    for k, start in enumerate(idx):
        end = idx[k+1] if k+1 < len(idx) else len(lines)
        chunk = "\n".join(lines[start:end])
        rhead = re.match(r'##\s+(.*)', lines[start]).group(1)
        rtitle = short_reading(rhead)
        body_md = (pre + "\n\n" + chunk) if k == 0 else chunk
        body_md = transform_pdf_notes(body_md,
                    "The full paper is reproduced on the following pages.")
        h = wrap(keep_with_next(eyebrowize(md_to_html_fragment(body_md))), "prose")
        stem = f"c{tnum}-r{k}"
        toc = ([(1, f"Theme {tnum} · {ttitle}"), (2, rtitle)] if k == 0
               else [(2, rtitle)])
        add(render(stem, h), "prose", f"Theme {tnum} · {ttitle}", toc=toc)
        add(art_path(chunk), "article", "")

# --- theme 10 extra: all intros, then all articles ---
extra_md = (ROOT / "10-extra.md").read_text()
elines = extra_md.split("\n")
eidx = [i for i,l in enumerate(elines) if l.startswith("## ")]
extra_articles = []  # (short_title, path)
for k, s in enumerate(eidx):
    e = eidx[k+1] if k+1 < len(eidx) else len(elines)
    sec = "\n".join(elines[s:e])
    head = re.match(r'##\s+(.*)', elines[s]).group(1)
    extra_articles.append((short_article(head), art_path(sec)))
extra_body = transform_pdf_notes(extra_md,
    "The full paper is reproduced in the articles that follow this section.")
extra_html = wrap(keep_with_next(eyebrowize(md_to_html_fragment(extra_body))), "prose")
add(render("c10-extra", extra_html), "prose", "Theme 10 · Extra",
    toc=[(1, "Theme 10 · Extra: going deeper")])
for i,(stitle, p) in enumerate(extra_articles):
    add(p, "article", "", toc=[(2, stitle)])

# ---------- build TOC entries list (in document order) ----------
# front entries (fixed targets: colophon)
toc_entries = []  # (level, title, target_part_index, is_front)
toc_entries.append((1, "Colophon &amp; licence", 1, True))
for pi, part in enumerate(parts):
    for (lvl, title) in part["toc"]:
        toc_entries.append((lvl, title, pi, False))

# ---------- render TOC ----------
def toc_html_build():
    # group each level-1 entry with its level-2 rows in a .grp (break-inside:avoid)
    # so a theme heading never splits from its readings across a page break.
    rows = []
    open_grp = False
    def close():
        nonlocal open_grp
        if open_grp: rows.append('</div>'); open_grp = False
    for (lvl, title, tgt, front) in toc_entries:
        cls = "front" if front else ("l1" if lvl == 1 else "l2")
        num = ""
        if lvl == 1 and not front:
            m = re.match(r'Theme\s+(\d+)', title)
            if m: num = m.group(1)
            elif title.startswith("Introduction"): num = "0"
        numspan = f'<span class="num">{num}</span>' if num else ""
        row = (f'<li class="{cls}"><a href="#e_end">'
               f'{numspan}<span class="t">{title}</span>'
               f'<span class="dots"></span></a></li>')
        if front:
            close(); rows.append(row)
        elif lvl == 1:
            close(); rows.append('<div class="grp">'); open_grp = True; rows.append(row)
        else:
            rows.append(row)
    close()
    body = ('<div class="toc"><p class="eyebrow">Contents</p>'
            '<h1 class="ruled">What is inside</h1>'
            '<p class="lead">Every entry is a link. The introductions are set in '
            'this typeface; each source article follows its introduction in its '
            'original published form.</p><ul>' + "\n".join(rows) + '</ul>'
            '<p id="e_end"></p></div>')
    return wrap(body, "parchment")

toc_pdf = render("00-toc", toc_html_build())
parts[toc_index]["pdf"] = toc_pdf

# ---------- merge ----------
final = fitz.open()
start_page = []
for part in parts:
    start_page.append(final.page_count)
    src = fitz.open(part["pdf"])
    final.insert_pdf(src)
    src.close()

# ---------- full-bleed parchment beneath cover/colophon/TOC pages ----------
# These render on a transparent ground with normal per-page margins; paint the
# parchment under the content so it bleeds to the sheet edges.
PARCHMENT = (0xF4/255, 0xED/255, 0xDC/255)
for pi, part in enumerate(parts):
    if part["kind"] != "cover": continue
    p1 = start_page[pi+1] if pi+1 < len(parts) else final.page_count
    for pno in range(start_page[pi], p1):
        pg = final[pno]
        pg.draw_rect(pg.rect, color=PARCHMENT, fill=PARCHMENT, overlay=False)

# ---------- retarget TOC links ----------
# insert_pdf does not carry the source link annots reliably, so read the rects
# from the source TOC (page sizes are identical) and add fresh links on the
# merged pages pointing to the computed target pages.
toc_start = start_page[toc_index]
src_toc = fitz.open(parts[toc_index]["pdf"])
src_links = []
for i in range(src_toc.page_count):
    ls = [l for l in src_toc[i].get_links() if "from" in l]
    ls.sort(key=lambda l: l["from"].y0)
    for l in ls:
        src_links.append((i, fitz.Rect(l["from"])))
src_toc.close()

if len(src_links) != len(toc_entries):
    print(f"WARN: {len(src_links)} link rects vs {len(toc_entries)} entries")

for (local_pno, rect), entry in zip(src_links, toc_entries):
    pg = final[toc_start + local_pno]
    for l in pg.get_links():   # clear any carried-over links first
        pg.delete_link(l)
    pg.insert_link({"kind": fitz.LINK_GOTO, "from": rect,
                    "page": start_page[entry[2]], "to": fitz.Point(0, 20)})

# ---------- outline / bookmarks ----------
toc_tree = []
toc_tree.append([1, "Title", start_page[0] + 1])
toc_tree.append([1, "Colophon & licence", start_page[1] + 1])
toc_tree.append([1, "Contents", toc_start + 1])
for (lvl, title, tgt, front) in toc_entries:
    if front: continue
    clean = htmlmod.unescape(re.sub("<[^>]+>", "", title)).replace(" · ", " — ")
    toc_tree.append([lvl, clean, start_page[tgt] + 1])
final.set_toc(toc_tree)

# ---------- footers on prose pages ----------
gfont = fitz.Font(fontfile=GENTIUM)
FAINT = (0x8A/255, 0x82/255, 0x70/255)
SAGE = (0x7E/255, 0x9A/255, 0x7C/255)
for pi, part in enumerate(parts):
    if part["kind"] != "prose": continue
    p0 = start_page[pi]; p1 = (start_page[pi+1] if pi+1 < len(parts) else final.page_count)
    for pno in range(p0, p1):
        pg = final[pno]; r = pg.rect
        y = r.height - 34
        pg.draw_line(fitz.Point(74, y-8), fitz.Point(r.width-74, y-8),
                     color=SAGE, width=0.5)
        pg.insert_text(fitz.Point(74, y+4), TITLE, fontfile=GENTIUM,
                       fontname="gent", fontsize=7.5, color=FAINT)
        lbl = htmlmod.unescape(re.sub("<[^>]+>", "", part["label"]))
        tw = gfont.text_length(lbl, fontsize=7.5)
        pg.insert_text(fitz.Point(r.width-74-tw, y+4), lbl, fontfile=GENTIUM,
                       fontname="gent", fontsize=7.5, color=FAINT)

final.set_metadata({"title": TITLE, "author": "Lars De Richter",
                    "subject": SUB, "keywords": "programming education, CS1, reader"})
final.save(str(OUT), deflate=True, garbage=3)
final.close()
print("WROTE", OUT, "pages:", npages(OUT))
