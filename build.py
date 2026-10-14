#!/usr/bin/env python3
"""Builds the static pages of the Assan Alan portfolio site.

Edit the CONFIG / CONTENT blocks below, run `python3 build.py`,
and the .html files next to this script are regenerated.
Media files go in images/ and videos/ (see IMAGES-NEEDED.txt for the exact names).
"""
import html
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
esc = html.escape

# ------------------------------------------------------------------ CONFIG
SITE_NAME = "Assan Alan"
ROLE = "Animation Director & Artist"
EMAIL = "directedbyassanalan@gmail.com"      # contact + where the form sends messages
FORM_ENDPOINT = "https://formsubmit.co/ajax/" + EMAIL
# Fill these in later; icons with an empty link are not shown.
SOCIALS = {
    "linkedin": "",
    "instagram": "",
    "behance": "",
    "youtube": "",
    "vimeo": "",
}

# ------------------------------------------------------------------ CONTENT
PROJECTS = [
    {
        "slug": "chaplin",
        "title": "The Charlie Chaplin Gold Collection",
        "meta": [
            ("Project", "The Charlie Chaplin Gold Collection"),
            ("Role", "Animation Director"),
            ("Category", "Animated collection"),
            ("Films", "The Kid · The Gold Rush · City Lights · Modern Times · The Great Dictator"),
        ],
        "heading": "Synopsis",
        "text": [
            "A collection of great films by a legendary director. Revisit the great classics.",
        ],
        "extra": [],
    },
    {
        "slug": "the-word",
        "title": "The Word",
        "meta": [
            ("Project", "The Word (Сөз)"),
            ("Format", "Short animation film"),
            ("Runtime", "4.5 minutes"),
            ("Genre", "Philosophical Surrealism"),
            ("Audience", "All ages"),
        ],
        "heading": "Synopsis",
        "text": [
            "This is a story about Abai Kunanbaiuly, who, while trying to write a poem, journeys into his own mind. "
            "As he searches for the words he needs for his poem, he encounters a variety of strange and symbolic images along the way.",
        ],
        "extra": [],
    },
    {
        "slug": "faceless",
        "title": "Faceless",
        "meta": [
            ("Project", "Faceless"),
        ],
        "heading": "Synopsis",
        "text": [
            "Description to be added.",
        ],
        "todo": True,
        "extra": [],
    },
]

ILLUSTRATIONS = [
    {
        "title": "Warcraft III",
        "note": "Fan art. Characters belong to their respective owners.",
        "items": [
            ("warcraft-arthas-1.jpg", "Arthas, the knight",
             "Arthas: a knight who starts the game as a good character, but by the end of the game he turns to the forces of darkness."),
            ("warcraft-arthas-2.jpg", "Arthas, after the fall", ""),
            ("warcraft-arthas-3.jpg", "Arthas, the Lich King", ""),
            ("warcraft-rexxar-1.jpg", "Rexxar and his bear",
             "Rexxar: a character who lives in harmony with nature and has a pet and best friend, his bear."),
        ],
    },
    {
        "title": "Five Nights at Freddy's",
        "note": "Fan art. Characters belong to their respective owners.",
        "items": [
            ("fnaf4-plushtrap.jpg", "Plushtrap", "Plushtrap"),
            ("fnaf4-nightmare-freddy.jpg", "Nightmare Freddy", "Nightmare Freddy"),
            ("fnaf4-freddy.jpg", "Freddy", "Freddy"),
            ("fnaf4-nightmare-marionette.jpg", "Nightmare Marionette", "Nightmare Marionette"),
        ],
    },
    {
        "title": "Portraits",
        "note": "J. R. R. Tolkien was an English writer, philologist and professor, best known as the author of The Hobbit "
                "and The Lord of the Rings. Below him, three great directors who are also among my favorites.",
        "items": [
            ("portrait-tolkien.jpg", "J. R. R. Tolkien", "J. R. R. Tolkien"),
            ("portrait-scorsese.jpg", "Martin Scorsese", "Martin Scorsese"),
            ("portrait-hitchcock.jpg", "Alfred Hitchcock", "Alfred Hitchcock"),
            ("portrait-kubrick.jpg", "Stanley Kubrick", "Stanley Kubrick"),
        ],
    },
]
MOTION_CLIPS = ["illustrations-motion-1.mp4", "illustrations-motion-2.mp4"]

ABOUT_TEXT = [
    "Hello, my name is Alan. I have been passionate about cinema in general, and especially animation, since I was five years old.",
    "I studied Animation Directing at the Kazakh National University of Arts named after Kulash Baiseitova.",
    "Among my favorite directors are Martin Scorsese, Alfred Hitchcock and Stanley Kubrick.",
]

# ------------------------------------------------------------------ HELPERS
REG = []  # (kind, path, note) of media the site expects


def reg(path, note):
    if all(p != path for _, p, _ in REG):
        REG.append(("media", path, note))


def img(name, alt, note, eager=False):
    path = "images/" + name
    reg(path, note)
    loading = "" if eager else ' loading="lazy"'
    return '<img src="%s" alt="%s"%s>' % (path, esc(alt), loading)


def icon_svg(kind):
    if kind == "instagram":
        return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true">'
                '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/>'
                '<circle cx="17.4" cy="6.6" r=".9" fill="currentColor"/></svg>')
    if kind == "youtube":
        return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true">'
                '<rect x="2.5" y="5.5" width="19" height="13" rx="4"/><polygon points="10,9 16,12 10,15" fill="currentColor"/></svg>')
    if kind == "mail":
        return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true">'
                '<rect x="3" y="5" width="18" height="14" rx="2"/><polyline points="3.5,6.5 12,13 20.5,6.5"/></svg>')
    return ""


def social_links():
    out = []
    labels = {"linkedin": "LinkedIn", "instagram": "Instagram", "behance": "Behance", "youtube": "YouTube", "vimeo": "Vimeo"}
    glyph = {"linkedin": "in", "behance": "Bē", "vimeo": "Vi"}
    for key in ("linkedin", "instagram", "behance", "youtube", "vimeo"):
        url = SOCIALS.get(key, "").strip()
        if not url:
            continue
        inner = icon_svg(key) or '<span class="txt">%s</span>' % glyph[key]
        out.append('<li><a href="%s" target="_blank" rel="noopener" aria-label="%s">%s</a></li>' % (esc(url, True), labels[key], inner))
    out.append('<li><a href="mailto:%s" aria-label="Email">%s</a></li>' % (EMAIL, icon_svg("mail")))
    return "\n".join(out)


def header(active):
    def cls(key):
        return "nav-link active" if active == key else "nav-link"
    drop = "\n".join('<a href="%s.html">%s</a>' % (p["slug"], esc(p["title"])) for p in PROJECTS)
    return f'''<header class="site-header">
  <a class="brand" href="index.html">{esc(SITE_NAME)}</a>
  <button class="menu-toggle" type="button" aria-label="Menu" aria-expanded="false"><span></span></button>
  <nav aria-label="Main">
    <ul class="nav">
      <li class="nav-item"><a class="{cls('projects')}" href="index.html">My Projects</a>
        <div class="dropdown">
{drop}
        </div>
      </li>
      <li class="nav-item"><a class="{cls('illustrations')}" href="illustrations.html">Illustrations</a></li>
      <li class="nav-item"><a class="{cls('portfolio')}" href="portfolio.html">Portfolio</a></li>
      <li class="nav-item"><a class="{cls('resume')}" href="resume.html">Résumé</a></li>
      <li class="nav-item"><a class="{cls('about')}" href="about.html">About</a></li>
    </ul>
  </nav>
</header>'''


def footer():
    links = [(p["title"].split(",")[0], p["slug"] + ".html") for p in PROJECTS] + [("Illustrations", "illustrations.html")]
    li = "\n".join('<li><a href="%s">%s</a></li>' % (h, esc(t)) for t, h in links)
    return f'''<footer class="site-footer">
  <ul class="footer-links">
{li}
  </ul>
  <ul class="social">
{social_links()}
  </ul>
  <div class="copyright">{esc(SITE_NAME)} &nbsp;·&nbsp; {esc(ROLE)}</div>
</footer>'''


FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' fill='%23ffffff'/%3E%3Ctext x='32' y='45' font-size='40' text-anchor='middle' "
           "font-family='Georgia,serif' fill='%231c1c1c'%3EA%3C/text%3E%3C/svg%3E")


def page(filename, title, active, body, desc):
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc, True)}">
<meta property="og:title" content="{esc(title, True)}">
<meta property="og:description" content="{esc(desc, True)}">
<meta property="og:type" content="website">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
{header(active)}
{body}
{footer()}
<script src="script.js" defer></script>
</body>
</html>
'''
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(doc)


# ------------------------------------------------------------------ PAGES
def build_home():
    tiles = []
    entries = [(p["slug"], p["title"], p["slug"] + ".html") for p in PROJECTS] + [("illustrations", "Illustrations", "illustrations.html")]
    for slug, title, href in entries:
        reg("images/home-%s.jpg" % slug, "Home tile: %s (landscape 4:3, ~1600x1200)" % title)
        reg("videos/home-%s.mp4" % slug, "OPTIONAL short muted loop for the home tile: %s" % title)
        tiles.append(f'''    <a class="tile reveal" href="{href}">
      {img("home-%s.jpg" % slug, title, "", eager=True)}
      <video data-optional autoplay muted loop playsinline preload="metadata" src="videos/home-{slug}.mp4"></video>
      <span class="tile-title">{esc(title)}</span>
    </a>''')
    body = f'''<main>
  <h1 class="sr-only">{esc(SITE_NAME)} — {esc(ROLE)}</h1>
  <div class="tiles">
{chr(10).join(tiles)}
  </div>
</main>'''
    page("index.html", "%s — %s" % (SITE_NAME, ROLE), "projects", body,
         "Portfolio of %s, %s. Animation projects and illustrations." % (SITE_NAME, ROLE.lower()))


def gallery(names, alts, notes, cls=""):
    figs = []
    for n, a, note in zip(names, alts, notes):
        figs.append('<figure><div class="item">%s</div></figure>' % img(n, a, note))
    return '<div class="gallery %s">\n%s\n</div>' % (cls, "\n".join(figs))


def build_project(i, p):
    s = p["slug"]
    title = p["title"]
    meta = "\n".join('<li><b>%s</b> / %s</li>' % (esc(k), esc(v)) for k, v in p["meta"])
    p_cls = ' class="todo"' if p.get("todo") else ""
    text = "\n".join("<p%s>%s</p>" % (p_cls, esc(t)) for t in p["text"])
    cover =img("%s-cover.jpg" % s, title + " cover", "%s: cover image (16:9, ~2000x1125)" % title, eager=True)

    chars = gallery(["%s-character-%d.jpg" % (s, n) for n in (1, 2, 3)],
                    ["%s character %d" % (title, n) for n in (1, 2, 3)],
                    ["%s: character %d" % (title, n) for n in (1, 2, 3)], "cols-3")
    reg("videos/%s.mp4" % s, "%s: full video (mp4, H.264)" % title)
    reg("images/%s-poster.jpg" % s, "%s: video poster frame (16:9)" % title)
    video = ('<div class="videobox"><video controls preload="metadata" playsinline poster="images/%s-poster.jpg" '
             'src="videos/%s.mp4" data-label="videos/%s.mp4"></video></div>' % (s, s, s))
    process = gallery(["%s-process-%d.jpg" % (s, n) for n in (1, 2, 3, 4)],
                      ["%s process %d" % (title, n) for n in (1, 2, 3, 4)],
                      ["%s: process step %d" % (title, n) for n in (1, 2, 3, 4)], "cols-2")
    mock = gallery(["%s-mockup-%d.jpg" % (s, n) for n in (1, 2)],
                   ["%s mockup %d" % (title, n) for n in (1, 2)],
                   ["%s: mockup %d" % (title, n) for n in (1, 2)], "cols-2")

    prev_p = PROJECTS[(i - 1) % len(PROJECTS)]
    next_p = PROJECTS[(i + 1) % len(PROJECTS)]
    body = f'''<main>
  <ul class="meta">
{meta}
  </ul>
  <div class="cover">{cover}</div>
  <div class="project-head reveal">
    <h1>{esc(title)}</h1>
    <div class="copy">
      <h3>{esc(p["heading"])}</h3>
{text}
    </div>
  </div>
  <section class="block reveal"><h2>Characters</h2>
{chars}
  </section>
  <section class="block reveal"><h2>Video</h2>
{video}
  </section>
  <section class="block reveal"><h2>Process</h2>
{process}
  </section>
  <section class="block reveal"><h2>Mockup</h2>
{mock}
  </section>
  <div class="pager">
    <a href="{prev_p["slug"]}.html">← {esc(prev_p["title"])}</a>
    <a href="{next_p["slug"]}.html">{esc(next_p["title"])} →</a>
  </div>
</main>'''
    page("%s.html" % s, "%s — %s" % (title, SITE_NAME), "projects", body,
         "%s — %s" % (title, p["text"][0][:140]))


def build_illustrations():
    sections = []
    for ser in ILLUSTRATIONS:
        figs = []
        for fn, alt, cap in ser["items"]:
            cap_html = "<figcaption>%s</figcaption>" % esc(cap) if cap else ""
            figs.append('<figure><div class="item">%s</div>%s</figure>' % (img(fn, alt, "Illustration: %s / %s" % (ser["title"], alt)), cap_html))
        sections.append(f'''  <section class="series reveal">
    <h2>{esc(ser["title"])}</h2>
    <p class="note">{esc(ser["note"])}</p>
    <div class="gallery">
{chr(10).join(figs)}
    </div>
  </section>''')
    clips = []
    for c in MOTION_CLIPS:
        reg("videos/" + c, "Illustrations: short muted loop")
        clips.append('<figure><div class="item"><video autoplay muted loop playsinline preload="metadata" src="videos/%s" data-label="videos/%s"></video></div></figure>' % (c, c))
    sections.append(f'''  <section class="series reveal">
    <h2>In motion</h2>
    <p class="note">Short silent loops.</p>
    <div class="gallery motion">
{chr(10).join(clips)}
    </div>
  </section>''')
    body = f'''<main>
  <h1 class="page-title">Illustrations</h1>
  <p class="lead">Digital paintings and portraits. Click an image to enlarge it.</p>
{chr(10).join(sections)}
</main>'''
    page("illustrations.html", "Illustrations — %s" % SITE_NAME, "illustrations", body,
         "Illustrations and portraits by %s." % SITE_NAME)


def build_portfolio():
    body = '''<main>
  <h1 class="page-title">Portfolio</h1>
  <p class="lead">The full portfolio. You can also open or download it as a PDF.</p>
  <iframe class="pdf-frame" src="assets/portfolio.pdf#view=FitH" title="Portfolio PDF"></iframe>
  <div class="actions">
    <a class="btn" href="assets/portfolio.pdf" target="_blank" rel="noopener">Open PDF</a>
    <a class="btn" href="assets/portfolio.pdf" download>Download PDF</a>
  </div>
</main>'''
    page("portfolio.html", "Portfolio — %s" % SITE_NAME, "portfolio", body, "Portfolio of %s as a PDF." % SITE_NAME)


def build_resume():
    reg("images/resume-photo.jpg", "Résumé photo (portrait 4:5, ~1200x1500)")
    has_pdf = os.path.exists(os.path.join(ROOT, "assets", "resume.pdf"))
    dl = '<div class="actions"><a class="btn" href="assets/resume.pdf" download>Download PDF</a></div>' if has_pdf else ""
    if not has_pdf:
        REG.append(("media", "assets/resume.pdf", "OPTIONAL résumé PDF: when this file exists, rebuild and the Download button appears"))
    body = f'''<main>
  <div class="split">
    <div class="portrait">{img("resume-photo.jpg", SITE_NAME, "", eager=True)}</div>
    <div>
      <h1>{esc(SITE_NAME)}</h1>
      <p>{esc(ROLE)}. Studied Animation Directing at the Kazakh National University of Arts named after Kulash Baiseitova.</p>

      <h2>Work experience</h2>
      <div class="cv-item"><div class="what todo">Position, studio / client</div><div class="when todo">Years</div><p class="todo">Short description of the work. To be added.</p></div>

      <h2>Education</h2>
      <div class="cv-item"><div class="what">Kazakh National University of Arts named after Kulash Baiseitova</div><div class="when">Animation Directing</div></div>

      <h2>Skills &amp; software</h2>
      <p class="todo">To be added.</p>
{dl}
    </div>
  </div>
</main>'''
    page("resume.html", "Résumé — %s" % SITE_NAME, "resume", body, "Résumé of %s, %s." % (SITE_NAME, ROLE.lower()))


def build_about():
    reg("images/about-photo.jpg", "About page photo (portrait 4:5, ~1200x1500)")
    paras = "\n".join("<p>%s</p>" % esc(t) for t in ABOUT_TEXT)
    body = f'''<main>
  <div class="split">
    <div class="portrait">{img("about-photo.jpg", SITE_NAME, "", eager=True)}</div>
    <div>
      <h1>Hi!</h1>
{paras}

      <h2>Contact</h2>
      <p class="contact"><a class="mail" href="mailto:{EMAIL}">{EMAIL}</a></p>

      <form class="form" id="contact-form" data-endpoint="{FORM_ENDPOINT}" data-mailto="{EMAIL}">
        <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
        <input type="hidden" name="_subject" value="New message from the portfolio website">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <div><label for="f-name">Name</label><input id="f-name" name="name" type="text" required autocomplete="given-name"></div>
        <div><label for="f-last">Last name</label><input id="f-last" name="lastname" type="text" autocomplete="family-name"></div>
        <div class="full"><label for="f-email">E-mail</label><input id="f-email" name="email" type="email" required autocomplete="email"></div>
        <div class="full"><label for="f-subject">Subject</label><input id="f-subject" name="subject" type="text"></div>
        <div class="full"><label for="f-msg">Your message</label><textarea id="f-msg" name="message" required></textarea></div>
        <div class="full"><button class="btn" type="submit">Send</button></div>
      </form>
      <div class="form-status" id="form-status" role="status" aria-live="polite"></div>
    </div>
  </div>
</main>'''
    page("about.html", "About — %s" % SITE_NAME, "about", body, "About %s, %s." % (SITE_NAME, ROLE.lower()))


def write_file_list():
    lines = ["FILES THE SITE EXPECTS", "======================",
             "Put images in  images/  and videos in  videos/  using exactly these names.",
             "Until a file exists, its place on the site shows a striped box with the file name.",
             "Videos: mp4 (H.264), as small as you can make them. Tile loops and 'In motion' clips play without sound.",
             "Lines starting with OPTIONAL can be skipped.", ""]
    for _, path, note in REG:
        if not note:
            continue
        lines.append("%-48s %s" % (path, note))
    with open(os.path.join(ROOT, "IMAGES-NEEDED.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    build_home()
    for idx, proj in enumerate(PROJECTS):
        build_project(idx, proj)
    build_illustrations()
    build_portfolio()
    build_resume()
    build_about()
    write_file_list()
    print("Built OK")
