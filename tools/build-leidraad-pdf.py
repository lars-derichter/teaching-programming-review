#!/usr/bin/env python3
"""Assemble the leidraad into a single styled PDF, in the same ldr house style
as the reader (tools/build-reader-pdf.py). Front matter (title, colophon, TOC)
mirrors the reader; the body flows as one continuous document with the four
hand-drawn SVG figures inline and a handful of warm section-opener photographs.
The TOC carries real, verifiable page numbers (also stamped as folios)."""
import os, re, sys, subprocess, pathlib, html as htmlmod
import fitz  # PyMuPDF

HERE = pathlib.Path(__file__).resolve().parent          # tools/
PROJECT = HERE.parent                                   # project root
LDR = PROJECT / "leidraad"                               # leidraad sources
FIG = LDR / "figuren"
IMG = LDR / "beelden"
SRC = LDR / "leidraad-programmeeronderwijs.md"
PARTS = HERE / ".build" / "parts-leidraad"
PARTS.mkdir(parents=True, exist_ok=True)
CSS = (HERE / "style.css").read_text() + "\n" + (HERE / "style-leidraad.css").read_text()
CHROME = os.environ.get("CHROME_BIN",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
GENTIUM = str(pathlib.Path.home() / "Library/Fonts/GentiumBookPlus-Regular.ttf")
OUT = LDR / "leidraad-programmeeronderwijs.pdf"

TITLE = "Hoe leer je beginners effectief programmeren?"
SUB = "Praktijkaanbevelingen voor docenten in het professioneel hoger onderwijs"

# section -> opener photograph (by exact heading text)
SECTION_PHOTOS = {
    "Voorwoord": "02-voorwoord-schrijven.jpg",
    "Wat zegt het onderzoek?": "03-onderzoek-notities.jpg",
    "Aanbevelingen": "04-aanbevelingen-samenwerken.jpg",
}

# ---------- shell / pandoc ----------
def md_to_html_fragment(md):
    r = subprocess.run(["pandoc","-f","markdown","-t","html5","--wrap=none"],
                       input=md, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr); raise SystemExit("pandoc failed")
    return r.stdout

def render(name, html):
    hp = PARTS / f"{name}.html"; pp = PARTS / f"{name}.pdf"
    hp.write_text(html)
    subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-pdf-header-footer",
        f"--print-to-pdf={pp}", f"file://{hp}"], capture_output=True)
    if not pp.exists(): raise SystemExit(f"render failed: {name}")
    return pp

def wrap(fragment, bodyclass):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style>'
            f'</head><body class="{bodyclass}"><div class="wrap">{fragment}</div>'
            f'</body></html>')

# ---------- markdown preparation ----------
def load_body_md():
    """Strip front matter and the licence note (moved to the colophon); keep the
    body from Voorwoord onward. Inject section-opener photos after their H2."""
    lines = SRC.read_text().split("\n")
    start = next(i for i,l in enumerate(lines) if l.strip() == "## Voorwoord")
    lines = lines[start:]
    # drop the "Noot over AI-gebruik en licentie" section (front colophon covers it)
    out, skip = [], False
    for l in lines:
        if l.startswith("## "):
            skip = l.strip().startswith("## Noot over AI-gebruik")
        if not skip:
            out.append(l)
    # inject photos right after matching H2 headings
    injected = []
    for l in out:
        injected.append(l)
        m = re.match(r'##\s+(.*)', l)
        if m and m.group(1).strip() in SECTION_PHOTOS:
            fn = SECTION_PHOTOS[m.group(1).strip()]
            injected += ["", f'<figure class="section-photo">',
                         f'<img src="file://{IMG/fn}" alt="">', "</figure>", ""]
    return "\n".join(injected)

def toc_from_md(md):
    """Ordered TOC entries (level, text) from ## / ### headings (## excluded when
    injected as raw HTML). Matches heading order in the rendered HTML 1:1."""
    entries = []
    for l in md.split("\n"):
        m = re.match(r'(#{2,3})\s+(.*)', l)
        if m:
            entries.append((len(m.group(1)) - 1, m.group(2).strip()))
    return entries

# ---------- HTML transforms ----------
def rewrite_fig_src(html):
    return html.replace('src="figuren/', f'src="file://{FIG}/')

def transform_kaders(html):
    """Turn Definitie/Verdieping/Werkvorm blockquotes into labelled callouts."""
    pat = re.compile(
        r'<blockquote>\s*<p>\s*<strong>\s*(Definitie|Verdieping|Werkvorm)\s*[—-]\s*'
        r'(.*?)</strong>(.*?)</blockquote>', re.S)
    def repl(m):
        typ, sub, rest = m.group(1), m.group(2), m.group(3)
        return (f'<div class="kader {typ.lower()}"><p class="kader-h">'
                f'<span class="tag">{typ}</span> <strong>{sub}</strong>{rest}</div>')
    return pat.sub(repl, html)

def process_headings(html):
    """Add the ruled accent class and inject an ordered invisible page-marker at
    the start of every h2/h3 (used to compute TOC page numbers)."""
    counter = [0]
    def hrepl(m):
        lvl, attrs = m.group(1), m.group(2)
        i = counter[0]; counter[0] += 1
        cls = "ruled" if lvl == "2" else "sub"
        if 'class="' in attrs:
            attrs = attrs.replace('class="', f'class="{cls} ', 1)
        else:
            attrs = attrs + f' class="{cls}"'
        marker = f'<span class="pmark">QZX{i}QZX</span>'
        return f'<h{lvl}{attrs}>{marker}'
    return re.sub(r'<h([23])([^>]*)>', hrepl, html), counter[0]

def keep_with_next(html):
    pat = re.compile(
        r'(<h[1-4][^>]*>.*?</h[1-4]>)\s*'
        r'(<(p|ul|ol|blockquote|pre|div|figure|table)\b[^>]*>.*?</\3>)', re.S)
    return pat.sub(lambda m: '<div class="keep">' + m.group(1) + m.group(2) + '</div>',
                   html)

# ---------- build body ----------
body_md = load_body_md()
toc_entries = toc_from_md(body_md)          # [(level, text), ...] in document order
h = md_to_html_fragment(body_md)
h = rewrite_fig_src(h)
h = transform_kaders(h)
h, n_headings = process_headings(h)
h = keep_with_next(h)
assert n_headings == len(toc_entries), f"{n_headings} headings vs {len(toc_entries)} toc"
body_pdf = render("body", wrap(h, "prose"))
bdoc = fitz.open(body_pdf); n_body = bdoc.page_count

# marker -> local page (0-based) within the body PDF
local_page = {}
for i in range(len(toc_entries)):
    tok = f"QZX{i}QZX"
    for pno in range(n_body):
        if bdoc[pno].search_for(tok):
            local_page[i] = pno; break
    else:
        local_page[i] = 0
        print(f"WARN: marker {i} ({toc_entries[i][1]!r}) not found")
bdoc.close()

# ---------- title page ----------
title_html = wrap(f'''
<div class="title-page">
  <p class="kicker">Leidraad</p>
  <h1>{TITLE}</h1>
  <p class="sub">{SUB}</p>
  <div class="rule"></div>
  <img class="hero" src="file://{IMG}/01-titel-toetsenbord.jpg" alt="">
  <p class="meta"><span class="who">Lars De Richter</span><br>
  Thomas More Hogeschool<br>Derde luik van een drieluik met de literatuurstudie
  en de reader over het onderwijzen van programmeren aan beginners<br>
  Juli 2026 &middot; werkdocument</p>
  <p class="ornament">&#10047; <span class="c">&#10048;</span> &#10047;</p>
</div>''', "cover")
title_pdf = render("00-title", title_html)
n_title = fitz.open(title_pdf).page_count

# ---------- colophon (AI-note + licence, Flemish) ----------
colophon_html = wrap('''
<div class="colophon">
<p class="eyebrow">Over dit document</p>
<h1 class="ruled">Colofon &amp; licentie</h1>

<div class="note-block">
<span class="lbl">Over het gebruik van AI</span>
<p>Deze leidraad werd samengesteld met substantiële AI-assistentie (Claude
Fable&nbsp;5, Anthropic). De selectie en clustering van de aanbevelingen steunt
op de literatuurstudie in deze repository — zelf een werkdocument dat met
AI-assistentie werd samengesteld; de tekst werd met AI-ondersteuning opgesteld
en redactioneel bewerkt voor gebruik in het onderwijs. Omdat de tekst originele
studies samenvat en interpreteert, geldt: verifieer elke claim tegen de
originele publicatie vóór je ze citeert in formeel academisch werk.</p>
</div>

<div class="note-block">
<span class="lbl">Derde luik van een drieluik</span>
<p>Deze leidraad vormt een drieluik met de literatuurstudie (de volledige
evidentie) en de reader (de sleutelpublicaties zelf, met leeswijzers). Wie wil
weten <em>waarom</em> een aanbeveling geldt, vindt de onderbouwing in de
literatuurstudie; wie de bronnen zelf wil bestuderen, vindt ze in de reader. De
opmaak van dit document is gebouwd in dezelfde huisstijl als de reader.</p>
</div>

<div class="note-block license">
<span class="lbl">Licentie</span>
<p>Het originele materiaal in dit document — de tekst, de structuur en de
figuren — wordt door Lars De Richter vrijgegeven onder
<span class="cc">CC BY-NC-SA 4.0</span> (Naamsvermelding &ndash; NietCommercieel
&ndash; GelijkDelen).</p>
<p>De geciteerde publicaties vallen <em>niet</em> onder die licentie; elk blijft
onder het auteursrecht van de eigen auteurs en uitgevers. De fotografie is
CC0/publiek domein (zie de beeldverantwoording in de repository).</p>
</div>
</div>''', "parchment")
colophon_pdf = render("00-colophon", colophon_html)
n_col = fitz.open(colophon_pdf).page_count

# ---------- TOC (rendered with page numbers; iterate until page count stable) ----------
def toc_html_build(folios):
    rows = []
    open_grp = False
    def close():
        nonlocal open_grp
        if open_grp: rows.append('</div>'); open_grp = False
    # fixed front entry: colophon
    rows.append(f'<li class="front"><a href="#e"><span class="t">Colofon &amp; '
                f'licentie</span><span class="dots"></span>'
                f'<span class="pageno">{n_title+1}</span></a></li>')
    for i,(lvl, text) in enumerate(toc_entries):
        cls = "l1" if lvl == 1 else "l2"
        row = (f'<li class="{cls}"><a href="#e"><span class="t">{htmlmod.escape(text)}'
               f'</span><span class="dots"></span>'
               f'<span class="pageno">{folios[i]}</span></a></li>')
        if lvl == 1:
            close(); rows.append('<div class="grp">'); open_grp = True; rows.append(row)
        else:
            rows.append(row)
    close()
    body = ('<div class="toc"><p class="eyebrow">Inhoud</p>'
            '<h1 class="ruled">Wat vind je hier</h1>'
            '<p class="lead">Elke regel is een link. De paginanummers verwijzen '
            'naar de genummerde bladzijden verderop in dit document.</p><ul>'
            + "\n".join(rows) + '</ul><p id="e"></p></div>')
    return wrap(body, "parchment")

n_toc = 1
for _ in range(4):
    body_start = n_title + n_col + n_toc          # 0-based index of first body page
    folios = [body_start + local_page[i] + 1 for i in range(len(toc_entries))]
    toc_pdf = render("00-toc", toc_html_build(folios))
    new_n_toc = fitz.open(toc_pdf).page_count
    if new_n_toc == n_toc: break
    n_toc = new_n_toc

# ---------- merge: title, colophon, toc, body ----------
final = fitz.open()
parts = [("cover", title_pdf), ("cover", colophon_pdf),
         ("cover", toc_pdf), ("body", body_pdf)]
start_page = []
for kind, pdf in parts:
    start_page.append(final.page_count)
    src = fitz.open(pdf); final.insert_pdf(src); src.close()
toc_start = start_page[2]
body_start = start_page[3]
assert body_start == n_title + n_col + n_toc

# ---------- parchment bleed under cover/colophon/toc ----------
PARCHMENT = (0xF4/255, 0xED/255, 0xDC/255)
for (kind, _), s0, i in zip(parts, start_page, range(len(parts))):
    if kind != "cover": continue
    s1 = start_page[i+1] if i+1 < len(parts) else final.page_count
    for pno in range(s0, s1):
        pg = final[pno]
        pg.draw_rect(pg.rect, color=PARCHMENT, fill=PARCHMENT, overlay=False)

# ---------- TOC links (retarget to computed pages) ----------
src_toc = fitz.open(toc_pdf)
src_links = []
for i in range(src_toc.page_count):
    ls = [l for l in src_toc[i].get_links() if "from" in l]
    ls.sort(key=lambda l: l["from"].y0)
    for l in ls:
        src_links.append((i, fitz.Rect(l["from"])))
src_toc.close()
targets = [start_page[1]] + [body_start + local_page[i] for i in range(len(toc_entries))]
if len(src_links) != len(targets):
    print(f"WARN: {len(src_links)} link rects vs {len(targets)} targets")
for (local_pno, rect), tgt in zip(src_links, targets):
    pg = final[toc_start + local_pno]
    for l in pg.get_links(): pg.delete_link(l)
    pg.insert_link({"kind": fitz.LINK_GOTO, "from": rect,
                    "page": tgt, "to": fitz.Point(0, 20)})

# ---------- outline / bookmarks ----------
tree = [[1, "Titel", start_page[0] + 1],
        [1, "Colofon & licentie", start_page[1] + 1],
        [1, "Inhoud", toc_start + 1]]
for i,(lvl, text) in enumerate(toc_entries):
    tree.append([lvl, htmlmod.unescape(text), body_start + local_page[i] + 1])
final.set_toc(tree)

# ---------- footers with folio numbers on body pages ----------
FAINT = (0x8A/255, 0x82/255, 0x70/255)
SAGE = (0x7E/255, 0x9A/255, 0x7C/255)
gfont = fitz.Font(fontfile=GENTIUM)
# map each body page to its current section label
sec_by_local = {}
cur = TITLE
order = sorted(range(len(toc_entries)), key=lambda i: local_page[i])
labels = {}
for i in order:
    if toc_entries[i][0] == 1:
        labels[local_page[i]] = htmlmod.unescape(toc_entries[i][1])
for lp in range(n_body):
    if lp in labels: cur = labels[lp]
    sec_by_local[lp] = cur
for lp in range(n_body):
    pg = final[body_start + lp]; r = pg.rect
    y = r.height - 34
    pg.draw_line(fitz.Point(74, y-8), fitz.Point(r.width-74, y-8),
                 color=SAGE, width=0.5)
    pg.insert_text(fitz.Point(74, y+4), TITLE, fontfile=GENTIUM,
                   fontname="gent", fontsize=7.5, color=FAINT)
    folio = str(body_start + lp + 1)
    lbl = sec_by_local[lp]
    tw = gfont.text_length(lbl, fontsize=7.5)
    pg.insert_text(fitz.Point(r.width-74-tw, y+4), lbl, fontfile=GENTIUM,
                   fontname="gent", fontsize=7.5, color=FAINT)
    # folio centred
    fw = gfont.text_length(folio, fontsize=8)
    pg.insert_text(fitz.Point((r.width-fw)/2, y+4), folio, fontfile=GENTIUM,
                   fontname="gent", fontsize=8, color=FAINT)

final.set_metadata({"title": TITLE, "author": "Lars De Richter", "subject": SUB,
    "keywords": "programmeeronderwijs, didactiek, CS1, leidraad"})
final.save(str(OUT), deflate=True, garbage=3)
n_final = final.page_count
final.close()
print("WROTE", OUT, "pages:", n_final,
      f"(front {n_title+n_col+n_toc}, body {n_body})")
