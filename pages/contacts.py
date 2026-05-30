import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

# ── Logo ─────────────────────────────────────────────────────────────────
LOGO_PATH = "pages\Dashboard figures\DPWH_LOGO.png"

def get_logo_src():
    try:
        data = Path(LOGO_PATH).read_bytes()
        b64  = base64.b64encode(data).decode()
        return f"data:image/png;base64,{b64}"
    except Exception:
        return ""

LOGO_SRC = get_logo_src()

st.set_page_config(
    page_title="DPWH – Contacts",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Query param navigation ────────────────────────────────────────────────
nav = st.query_params.get("navigate", "")
if nav == "home":
    st.switch_page("homepage.py")
elif nav == "projects":
    st.switch_page("pages/projects1.py")
elif nav == "about":
    st.switch_page("pages/about.py")
elif nav == "contacts":
    st.switch_page("pages/contacts.py")


# ── Hide Streamlit chrome ─────────────────────────────────────────────────
st.markdown("""
<style>
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="stHeader"],
[data-testid="stSidebarNav"],
[data-testid="collapsedControl"] { display: none !important; }

html, body,
[data-testid="stApp"],
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
[data-testid="block-container"],
.main, .main > div,
section.main, section.main > div,
div[class*="css"] {
    padding: 0 !important; margin: 0 !important;
    max-width: 100% !important; width: 100% !important;
    background: #060517 !important;
}
iframe {
    display: block !important;
    width: 100vw !important;
    height: 100vh !important;
    border: none !important;
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    z-index: 999 !important;
    overflow: hidden !important;
}
</style>
""", unsafe_allow_html=True)

if LOGO_SRC:
    LOGO_TAG = f'<img src="{LOGO_SRC}" alt="DPWH Logo" style="height:44px;width:auto;object-fit:contain;">'
else:
    LOGO_TAG = '<div class="nav-logo-icon">DPWH</div>'

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DPWH – Contacts</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@300;400;600;700;800&family=Barlow:wght@300;400;500&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; height: 100%; overflow-y: auto; }

:root {
    --bg:        #060517;
    --fire:      #D05B37;
    --fire-dark: #a8421f;
    --light:     #e8e4df;
    --muted:     #9b9590;
    --card:      #0d0c23;
    --card-hover:#111029;
    --border:    rgba(255,255,255,0.08);
    --border-h:  rgba(208,91,55,0.4);
}

body {
    font-family: 'Barlow', sans-serif;
    background: var(--bg);
    color: var(--light);
    min-height: 100vh;
    overflow-x: hidden;
    overflow-y: auto;
    height: 100vh;
}

/* ══════════════ NAVBAR ══════════════ */
.dpwh-nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 40px; height: 68px;
    background: rgba(6,5,23,0.95);
    backdrop-filter: blur(16px);
    border-bottom: 1px solid rgba(208,91,55,0.18);
}
.nav-logo { display: flex; align-items: center; gap: 12px; cursor: pointer; text-decoration: none; }
.nav-logo-icon {
    width: 44px; height: 44px;
    background: var(--fire);
    clip-path: polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);
    display: flex; align-items: center; justify-content: center;
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 800; font-size: 11px; color: #fff; letter-spacing: .5px;
}
.nav-logo-text { display: flex; flex-direction: column; line-height: 1.1; }
.nav-logo-text .t1 { font-family: 'Barlow Condensed', sans-serif; font-weight: 800; font-size: 17px; color: var(--fire); letter-spacing: 1.5px; }
.nav-logo-text .t2 { font-size: 9px; color: var(--muted); letter-spacing: 2px; text-transform: uppercase; }
.nav-links { display: flex; gap: 36px; list-style: none; }
.nav-links a {
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 600; font-size: 14px;
    letter-spacing: 2px; text-transform: uppercase;
    color: var(--light); text-decoration: none;
    position: relative; padding-bottom: 3px;
    transition: color .25s; cursor: pointer;
}
.nav-links a::after {
    content: ''; position: absolute; bottom: 0; left: 0;
    width: 0; height: 2px; background: var(--fire); transition: width .3s;
}
.nav-links a:hover, .nav-links a.active { color: var(--fire); }
.nav-links a:hover::after, .nav-links a.active::after { width: 100%; }

/* ══════════════ PAGE HEADER ══════════════ */
.page-header {
    padding: 108px 60px 50px;
    border-bottom: 1px solid var(--border);
    position: relative; overflow: hidden;
}
.page-header::after {
    content: '';
    position: absolute; top: 0; right: 0; bottom: 0;
    width: 45%;
    background: radial-gradient(ellipse at 80% 50%, rgba(208,91,55,0.08) 0%, transparent 65%);
    pointer-events: none;
}
.header-inner {
    max-width: 1300px; margin: 0 auto;
    display: flex; align-items: flex-end; justify-content: space-between;
    gap: 40px; flex-wrap: wrap;
}
.header-left {}
.header-crumb {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 11px; font-weight: 600;
    letter-spacing: 3.5px; text-transform: uppercase;
    color: var(--fire); margin-bottom: 12px;
    display: flex; align-items: center; gap: 8px;
}
.header-crumb span { color: rgba(208,91,55,0.4); }
.header-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: clamp(54px, 8vw, 96px);
    font-weight: 800; line-height: .88;
    letter-spacing: -1px; color: var(--light);
}
.header-title em { color: var(--fire); font-style: normal; }
.header-sub {
    font-size: 14px; color: var(--muted);
    line-height: 1.8; margin-top: 16px; max-width: 420px;
}
.header-stats {
    display: flex; gap: 40px; padding-bottom: 6px;
}
.stat { text-align: right; }
.stat-num {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 56px;
    text-align: center;
    font-weight: 800;
    color: var(--fire); line-height: 2; letter-spacing: -1px;
}
.stat-lbl {
    font-size: 9px;
    text-align: center; 
    letter-spacing: 2.5px;
    text-transform: uppercase; color: var(--muted); margin-top: 5px;
}

/* ══════════════ CARDS WRAPPER ══════════════ */
.cards-wrap {
    max-width: 1300px; margin: 0 auto;
    padding: 52px 60px 80px;
}

/* ── Section label above grid ── */
.grid-label {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 10px; font-weight: 700;
    letter-spacing: 3.5px; text-transform: uppercase;
    color: var(--muted); margin-bottom: 24px;
    display: flex; align-items: center; gap: 14px;
}
.grid-label::after {
    content: ''; flex: 1; height: 1px;
    background: var(--border);
}

/* ── The 2-column top row + 3-column bottom row ── */
.grid-row {
    display: grid; gap: 20px;
    margin-bottom: 20px;
}
.grid-row.two   { grid-template-columns: 1fr 1fr; }
.grid-row.three { grid-template-columns: 1fr 1fr 1fr; }

/* ══════════════ CARD BASE ══════════════ */
.c-card {
    background: var(--card);
    border: 1px solid var(--border);
    padding: 40px 36px 36px;
    position: relative; overflow: hidden;
    transition: border-color .3s, background .3s, transform .3s;
    cursor: default;
    display: flex; flex-direction: column;
    min-height: 320px;
}
.c-card::before {
    content: ''; position: absolute; top: 0; left: 0;
    width: 0; height: 3px; background: var(--fire);
    transition: width .4s ease;
}
.c-card:hover {
    border-color: var(--border-h);
    background: var(--card-hover);
    transform: translateY(-3px);
}
.c-card:hover::before { width: 100%; }

/* card top tag */
.c-tag {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 10px; font-weight: 700;
    letter-spacing: 3px; text-transform: uppercase;
    color: var(--fire); opacity: .75;
    margin-bottom: 20px;
}

/* icon area */
.c-icon {
    font-size: 32px; margin-bottom: 16px;
    display: block; line-height: 1;
    filter: grayscale(20%);
}

/* card title */
.c-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 24px; font-weight: 700;
    color: var(--light); letter-spacing: .3px;
    margin-bottom: 10px;
}

/* card body text */
.c-body {
    font-size: 13px; color: var(--muted);
    line-height: 1.75; flex: 1;
    margin-bottom: 24px;
}

/* ══════════════ BUTTON ══════════════ */
.btn {
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 700; font-size: 12px;
    letter-spacing: 2.5px; text-transform: uppercase;
    padding: 13px 28px;
    background: var(--fire); color: #fff;
    border: none; cursor: pointer; text-decoration: none;
    clip-path: polygon(7px 0%, 100% 0%, calc(100% - 7px) 100%, 0% 100%);
    transition: background .25s, transform .2s;
    display: inline-block; align-self: flex-start;
}
.btn:hover { background: var(--fire-dark); transform: translateY(-2px); }
.btn.outline {
    background: transparent; color: var(--light);
    border: 1px solid rgba(232,228,223,0.2);
    clip-path: none;
    transition: border-color .25s, color .25s, transform .2s;
}
.btn.outline:hover { border-color: var(--fire); color: var(--fire); background: transparent; transform: translateY(-2px); }

/* ══════════════ CARD 1: GET HELP ══════════════ */
.help-bullets { list-style: none; margin-bottom: 24px; display: flex; flex-direction: column; gap: 8px; }
.help-bullets li {
    font-size: 12px; color: var(--muted);
    display: flex; align-items: center; gap: 10px;
}
.help-bullets li::before {
    content: ''; width: 4px; height: 4px;
    border-radius: 50%; background: var(--fire);
    flex-shrink: 0;
}

/* ══════════════ CARD 2: MESSAGE FORM ══════════════ */
.form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 10px; }
.f-group { display: flex; flex-direction: column; gap: 5px; }
.f-group.full { grid-column: 1 / -1; }
.f-label {
    font-size: 9px; letter-spacing: 2px; text-transform: uppercase;
    color: var(--muted);
}
.f-group input,
.f-group textarea {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.09);
    color: var(--light);
    font-family: 'Barlow', sans-serif; font-size: 13px;
    padding: 10px 13px; outline: none; resize: none;
    transition: border-color .25s, background .25s;
    width: 100%;
}
.f-group input::placeholder,
.f-group textarea::placeholder { color: rgba(155,149,144,0.4); }
.f-group input:focus,
.f-group textarea:focus {
    border-color: rgba(208,91,55,0.5);
    background: rgba(208,91,55,0.04);
}
.f-group textarea { min-height: 90px; }
.form-footer { display: flex; align-items: center; justify-content: space-between; margin-top: 10px; }
.char-ct { font-size: 10px; color: var(--muted); letter-spacing: 1px; }

/* ══════════════ CARD 3: OFFICIAL CONTACTS ══════════════ */
.info-list { display: flex; flex-direction: column; gap: 18px; flex: 1; }
.info-item-label {
    font-size: 9px; letter-spacing: 2.5px; text-transform: uppercase;
    color: var(--fire); opacity: .85; margin-bottom: 3px;
}
.info-item-val { font-size: 13px; color: var(--light); line-height: 1.6; }
.info-item-val a { color: var(--light); text-decoration: none; transition: color .2s; }
.info-item-val a:hover { color: var(--fire); }
.info-divider { height: 1px; background: var(--border); }

/* ══════════════ CARD 4: DEVELOPERS ══════════════ */
.dev-list { display: flex; flex-direction: column; gap: 16px; flex: 1; }
.dev-row { display: flex; align-items: flex-start; gap: 14px; }
.dev-hex {
    width: 40px; height: 40px; flex-shrink: 0;
    background: rgba(208,91,55,0.15);
    clip-path: polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);
    display: flex; align-items: center; justify-content: center;
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 800; font-size: 12px; color: var(--fire);
}
.dev-name {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 16px; font-weight: 700; color: var(--light); letter-spacing: .3px;
}
.dev-role { font-size: 11px; color: var(--muted); letter-spacing: 1px; text-transform: uppercase; margin-bottom: 6px; }
.dev-links { display: flex; gap: 6px; flex-wrap: wrap; }
.dev-link {
    font-size: 9px; letter-spacing: 1.5px; text-transform: uppercase;
    color: var(--fire); text-decoration: none;
    padding: 3px 9px; border: 1px solid rgba(208,91,55,0.3);
    transition: background .2s, color .2s;
}
.dev-link:hover { background: var(--fire); color: #fff; border-color: var(--fire); }

/* ══════════════ CARD 5: NEWS ══════════════ */
.news-list { display: flex; flex-direction: column; flex: 1; }
.news-item {
    display: flex; align-items: flex-start; gap: 14px;
    padding: 14px 0;
    border-bottom: 1px solid var(--border);
    cursor: pointer; transition: background .2s;
}
.news-item:last-of-type { border-bottom: none; }
.news-item:hover .news-title { color: var(--fire); }
.news-item:hover .news-arr { opacity: 1; transform: translateX(0); }
.news-date {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 10px; font-weight: 700; letter-spacing: 1.5px;
    text-transform: uppercase; color: var(--fire);
    flex-shrink: 0; width: 40px; text-align: center; line-height: 1.3; padding-top: 2px;
}
.news-content { flex: 1; }
.news-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 15px; font-weight: 700; color: var(--light);
    line-height: 1.2; margin-bottom: 3px; transition: color .2s;
}
.news-badge {
    font-size: 9px; letter-spacing: 2px; text-transform: uppercase;
    color: var(--muted); background: rgba(255,255,255,0.05);
    padding: 2px 7px; display: inline-block;
}
.news-arr {
    color: var(--fire); font-size: 14px;
    opacity: 0; transition: opacity .2s, transform .2s;
    transform: translateX(-6px); padding-top: 2px; flex-shrink: 0;
}

/* ══════════════ TOAST ══════════════ */
.toast {
    display: none; position: fixed; bottom: 32px; right: 32px;
    background: var(--fire); color: #fff;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 13px; font-weight: 700; letter-spacing: 2px;
    text-transform: uppercase; padding: 14px 28px;
    clip-path: polygon(7px 0%,100% 0%,calc(100% - 7px) 100%,0% 100%);
    z-index: 9999; animation: slideUp .3s ease;
}
@keyframes slideUp { from { opacity:0; transform:translateY(12px); } to { opacity:1; transform:translateY(0); } }

/* ══════════════ FOOTER ══════════════ */
.dpwh-footer {
    border-top: 1px solid var(--border); padding: 36px 60px;
    display: flex; align-items: center; justify-content: space-between;
    flex-wrap: wrap; gap: 16px;
}
.footer-l { font-size: 11px; color: var(--muted); letter-spacing: 1px; }
.footer-r { display: flex; gap: 24px; }
.footer-link {
    font-size: 11px; letter-spacing: 2px; text-transform: uppercase;
    color: var(--muted); text-decoration: none; transition: color .2s; cursor: pointer;
}
.footer-link:hover { color: var(--fire); }

/* ══════════════ RESPONSIVE ══════════════ */
@media (max-width: 960px) {
    .cards-wrap { padding: 40px 24px 60px; }
    .grid-row.two   { grid-template-columns: 1fr; }
    .grid-row.three { grid-template-columns: 1fr; }
    .header-stats { display: none; }
    .page-header { padding: 96px 24px 40px; }
    .form-grid { grid-template-columns: 1fr; }
    .dpwh-footer { padding: 28px 24px; flex-direction: column; align-items: flex-start; }
}
@media (max-width: 600px) {
    .dpwh-nav { padding: 0 18px; }
    .nav-links { gap: 18px; }
    .nav-links a { font-size: 12px; letter-spacing: 1px; }
    .c-card { padding: 28px 22px 26px; min-height: auto; }
}
</style>
</head>
<body>

<!-- ═══════════════════ NAVBAR ═══════════════════ -->
<nav class="dpwh-nav">
    <a class="nav-logo" onclick="navigate('home')">
        %%DPWH_LOGO%%
        <div class="nav-logo-text">
            <span class="t1">DPWH</span>
            <span class="t2">Republic of the Philippines</span>
        </div>
    </a>
    <ul class="nav-links">
        <li><a onclick="navigate('home')">Home</a></li>
        <li><a onclick="navigate('about')">About</a></li>
        <li><a onclick="navigate('projects')">Projects</a></li>
        <li><a class="active" onclick="navigate('contacts')">Contacts</a></li>
    </ul>
</nav>

<!-- ═══════════════════ PAGE HEADER ═══════════════════ -->
<div class="page-header">
    <div class="header-inner">
        <div class="header-left">
            <div class="header-crumb">LANES & LEDGERS <span>/</span> Contacts</div>
            <h1 class="header-title">LET'S <em>TALK</em></h1>
            <p class="header-sub">
                Reach out for project inquiries, official communications, citizen
                feedback, or media requests. We are committed to open dialogue
                with every Filipino.
            </p>
        </div>
        <div class="header-stats">
            <div class="stat">
                <div class="stat-num">5</div>
                <div class="stat-lbl">District
                <br>Engineering Offices</br></div>
            </div>
            <div class="stat">
                <div class="stat-num">24/7</div>
                <div class="stat-lbl">Online Support</div>
            </div>
            <div class="stat">
                <div class="stat-num">189</div>
                <div class="stat-lbl">Total Projects</div>
            </div>
        </div>
    </div>
</div>

<!-- ═══════════════════ CARDS ═══════════════════ -->
<div class="cards-wrap">

    <div class="grid-label">Get in Touch</div>

    <!-- ROW 1: 2 equal cards -->
    <div class="grid-row two">

        <!-- ── CARD 1: GET HELP ── -->
        <div class="c-card">
            <div class="c-tag">01 / Support</div>
            <div class="c-title">Get Help</div>
            <!-- ✏️ EDITABLE SUBTITLE BELOW -->
            <div class="c-body">
                Have questions about an ongoing DPWH project, contractor
                performance, or a procurement concern? Our team is ready to
                assist every citizen. Click below to reach us directly by email.
            </div>
            <ul class="help-bullets">
                <li>Project status &amp; progress inquiries</li>
                <li>Contractor complaints &amp; violations</li>
                <li>Budget &amp; procurement questions</li>
                <li>FOI document requests</li>
            </ul>
            <a href="mailto:lanes.ledgers@gmail.com" class="btn">&#9993;&nbsp; Send us an Email</a>
        </div>

        <!-- ── CARD 2: DROP A MESSAGE ── -->
        <div class="c-card">
            <div class="c-tag">02 / Feedback</div>
            <div class="c-title">Drop a Message</div>
            <div class="c-body" style="margin-bottom:14px;">
                Share feedback, suggestions, or concerns about this dashboard
                or any DPWH project nationwide.
            </div>
            <div class="form-grid">
                <div class="f-group">
                    <label class="f-label">Your Name</label>
                    <input type="text" id="f-name" placeholder="Juan dela Cruz">
                </div>
                <div class="f-group">
                    <label class="f-label">Email Address</label>
                    <input type="email" id="f-email" placeholder="juan@example.com">
                </div>
                <div class="f-group full">
                    <label class="f-label">Subject</label>
                    <input type="text" id="f-subject" placeholder="e.g. Project Update Request">
                </div>
                <div class="f-group full">
                    <label class="f-label">Your Message</label>
                    <textarea id="f-body" placeholder="Write your message here…" oninput="updateCount(this)"></textarea>
                </div>
            </div>
            <div class="form-footer">
                <button class="btn" onclick="submitMsg()">&#9654;&nbsp; Submit Feedback</button>
                <span class="char-ct" id="char-ct">0 / 500</span>
            </div>
        </div>

    </div><!-- end row 1 -->

    <!-- ROW 2: 3 equal cards -->
    <div class="grid-row three">

        <!-- ── CARD 3: OFFICIAL DPWH CONTACT ── -->
        <div class="c-card">
            <div class="c-tag">03 / Official Contact</div>
            <div class="c-title">DPWH Official</div>
            <div class="c-body" style="margin-bottom:18px;">
                Reach the Department through its official government channels.
            </div>
            <div class="info-list">
                <!-- ✏️ EDITABLE entries below -->
                <div>
                    <div class="info-item-label">Official Website</div>
                    <div class="info-item-val">
                        <a href="https://www.dpwh.gov.ph" target="_blank">www.dpwh.gov.ph ↗</a>
                    </div>
                </div>
                <div class="info-divider"></div>
                <div>
                    <div class="info-item-label">Trunk Line</div>
                    <div class="info-item-val">
                        <a href="tel:+63224062900">(02) 4062-9000</a>
                    </div>
                </div>
                <div class="info-divider"></div>
                <div>
                    <div class="info-item-label">Central Office Address</div>
                    <div class="info-item-val">
                        Bonifacio Drive, Port Area,<br>Manila 1018, Philippines
                    </div>
                </div>
                <div class="info-divider"></div>
                <!-- ✏️ EDITABLE: Add/change district office addresses here -->
                <div>
                    <div class="info-item-label">District Office — Iloilo</div>
                    <div class="info-item-val">
                        DPWH Iloilo 1st DEO, Molo, Iloilo City
                    </div>
                </div>
                <div class="info-divider"></div>
                <div>
                    <div class="info-item-label">All District Offices</div>
                    <div class="info-item-val">
                        <a href="https://www.dpwh.gov.ph/dpwh/reg/6/dir" target="_blank">
                            View Region VI &amp; District Offices ↗
                        </a>
                    </div>
                </div>
            </div>
        </div>

        <!-- ── CARD 4: DEVELOPERS ── -->
        <div class="c-card">
            <div class="c-tag">04 / Site Developers</div>
            <div class="c-title">Dashboard Team</div>
            <div class="c-body" style="margin-bottom:18px;">
                For technical issues, bugs, or feature requests on this transparency dashboard.
            </div>
            <div class="dev-list">
                <div class="dev-row">
                    <div class="dev-hex">FA</div>
                    <div>
                        <div class="dev-name">Franchezca Nel C. Alvarez</div>
                        <div class="dev-role">Product Manager</div>
                        <div class="dev-links">
                            <a href="mailto:franchezcanel.alvarez@students.isatu.edu.ph" class="dev-link">Email</a>
                            <a href="https://www.facebook.com/share/1aPE4yTig5/" target="_blank" class="dev-link">Facebook</a>
                        </div>
                    </div>
                </div>
                <div class="dev-row">
                    <div class="dev-hex">SB</div>
                    <div>
                        <div class="dev-name">Sharlon Aron B. Beliran</div>
                        <div class="dev-role">Data Engineer</div>
                        <div class="dev-links">
                            <a href="mailto:sharlonaron.beliran@students.isatu.edu.ph" class="dev-link">Email</a>
                            <a href="https://www.facebook.com/share/17ZtRA6CmK/" target="_blank" class="dev-link">Facebook</a>
                        </div>
                    </div>
                </div>
                <div class="dev-row">
                    <div class="dev-hex">CB</div>
                    <div>
                        <div class="dev-name">Sanjay Chris M. Benes</div>
                        <div class="dev-role">BI Analyst</div>
                        <div class="dev-links">
                            <a href="mailto:sanjaycris.benes@students.isatu.edu.ph" class="dev-link">Email</a>
                            <a href="https://www.facebook.com/share/1FZeELgq2u/" target="_blank" class="dev-link">Facebook</a>
                        </div>
                    </div>
                </div>
                <div class="dev-row">
                    <div class="dev-hex">PE</div>
                    <div>
                        <div class="dev-name">Pauline Fate E. Encio</div>
                        <div class="dev-role">UI/UX Designer</div>
                        <div class="dev-links">
                            <a href="mailto:paulinefate.encio@students.isatu.edu.ph" class="dev-link">Email</a>
                            <a href="https://www.facebook.com/share/1DzvmJdaX4/" target="_blank" class="dev-link">Facebook</a>
                        </div>
                    </div>
                </div>
                <div class="dev-row">
                    <div class="dev-hex">RE</div>
                    <div>
                        <div class="dev-name">Rhiz Ann L. Estillena</div>
                        <div class="dev-role">BI Developer</div>
                        <div class="dev-links">
                            <a href="mailto:rhizann.estillena@students.isatu.edu.ph" class="dev-link">Email</a>
                            <a href="https://www.facebook.com/share/16sbwcqDty/" target="_blank" class="dev-link">Facebook</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- ── CARD 5: DPWH NEWS ── -->
        <div class="c-card">
            <div class="c-tag">05 / Official Updates</div>
            <div class="c-title">DPWH News &amp; Updates</div>
            <div class="c-body" style="margin-bottom:14px;">
                Latest announcements from the Department of Public Works and Highways.
            </div>
            <div class="news-list">
                <div class="news-item" onclick="window.open('https://www.dpwh.gov.ph/dpwh/news/37709','_blank')">
                    <div class="news-date">MAY<br>2026</div>
                    <div class="news-content">
                        <div class="news-title">Upgraded Road Boosts Agri Logistics in Central Iloilo</div>
                        <span class="news-badge">Infrastructure, Budget</span>
                    </div>
                    <div class="news-arr">→</div>
                </div>
                <div class="news-item" onclick="window.open('https://www.dpwh.gov.ph/dpwh/news/41153','_blank')">
                    <div class="news-date">APR<br>2026</div>
                    <div class="news-content">
                        <div class="news-title">PBBM: Bilisan ang Konstruksyon ng Dalawang Kritikal na Flyover sa Iloilo City</div>
                        <span class="news-badge">Procurement, Roads</span>
                    </div>
                    <div class="news-arr">→</div>
                </div>
                <div class="news-item" onclick="window.open('https://www.dpwh.gov.ph/dpwh/news/41148','_blank')">
                    <div class="news-date">APR<br>2026</div>
                    <div class="news-content">
                        <div class="news-title">Sec. Dizon, Nadismaya sa Nakitang Nakatiwangwang na Kalsada sa Molo, Iloilo; Iniutos ang Agarang Pagsasaayos</div>
                        <span class="news-badge">Roads</span>
                    </div>
                    <div class="news-arr">→</div>
                </div>
                <div class="news-item" onclick="window.open('https://www.dpwh.gov.ph/dpwh/news/37549','_blank')">
                    <div class="news-date">APR<br>2025</div>
                    <div class="news-content">
                        <div class="news-title">DPWH Improves Flood Resilience along Major Rivers in Capiz</div>
                        <span class="news-badge">Flood Control</span>
                    </div>
                    <div class="news-arr">→</div>
                </div>
            </div>
            <br>
            <a href="https://www.dpwh.gov.ph/dpwh/news" target="_blank" class="btn outline" style="align-self:stretch;text-align:center;">
                View All News ↗
            </a>
        </div>

    </div><!-- end row 2 -->

</div><!-- end cards-wrap -->

<!-- ═══════════════════ FOOTER ═══════════════════ -->
<footer class="dpwh-footer">
    <div class="footer-l">&copy; 2024 Department of Public Works and Highways &mdash; Republic of the Philippines</div>
    <div class="footer-r">
        <a class="footer-link">Privacy Policy</a>
        <a class="footer-link">Accessibility</a>
        <a class="footer-link" onclick="navigate('contacts')">Contact Us</a>
        <a class="footer-link">FOI Portal</a>
    </div>
</footer>

<div class="toast" id="toast">&#10003;&nbsp;&nbsp;Message sent! Thank you.</div>

<script>
function navigate(page) {
    try {
        window.top.location.href = "/?navigate=" + page;
    } catch(e) {
        // Fallback for cross-origin iframe restrictions (shouldn't happen on
        // localhost / same-origin Streamlit deployments)
        window.location.href = "/?navigate=" + page;
    }
}

function updateCount(el) {
    var max = 500;
    if (el.value.length > max) el.value = el.value.slice(0, max);
    document.getElementById('char-ct').textContent = el.value.length + ' / ' + max;
}

function submitMsg() {
    var name  = document.getElementById('f-name').value.trim();
    var email = document.getElementById('f-email').value.trim();
    var body  = document.getElementById('f-body').value.trim();
    if (!name || !email || !body) {
        alert('Please fill in your name, email, and message before submitting.');
        return;
    }
    document.getElementById('f-name').value    = '';
    document.getElementById('f-email').value   = '';
    document.getElementById('f-subject').value = '';
    document.getElementById('f-body').value    = '';
    document.getElementById('char-ct').textContent = '0 / 500';
    var t = document.getElementById('toast');
    t.style.display = 'block';
    setTimeout(function(){ t.style.display = 'none'; }, 3500);
}
</script>
</body>
</html>
"""

HTML = HTML.replace("%%DPWH_LOGO%%", LOGO_TAG)
components.html(HTML, height=0, scrolling=False)