import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

st.set_page_config(
    page_title="DPWH – About",
    page_icon="🏗️",
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


# ── Logo ─────────────────────────────────────────────────────────────────
LOGO_PATH = "pages/Dashboard figures/DPWH_LOGO.png"

def get_logo_src():
    try:
        data = Path(LOGO_PATH).read_bytes()
        b64  = base64.b64encode(data).decode()
        return f"data:image/png;base64,{b64}"
    except Exception:
        return ""

LOGO_SRC = get_logo_src()


TEAM_PHOTO_PATH = "pages/Dashboard figures/team_photo.jpg"

def get_image_b64(img_path, mime="image/png"):
    try:
        data = Path(img_path).read_bytes()
        b64  = base64.b64encode(data).decode()
        return f"data:{mime};base64,{b64}"
    except Exception:
        return ""

TEAM_PHOTO_SRC  = get_image_b64(TEAM_PHOTO_PATH, "image/jpg")
DPWH_BG_IMG     = get_image_b64("pages/Dashboard figures/dpwh_workers.jpg", "image/jpeg")
DPWH_WORKERS_IMG = get_image_b64("pages/Dashboard figures/dpwh_logo_bg.jpg", "image/jpeg")


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
<title>DPWH – About</title>
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
    --border:    rgba(255,255,255,0.07);
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

/* ══════════════ HERO BANNER ══════════════ */
.about-hero {
    position: relative;
    min-height: 420px;
    display: flex; align-items: flex-start;
    overflow: hidden;
    padding: 100px 60px 60px;
}

/*
 * FIX 1 – Team photo background
 * Removed the broken `var(--team-photo)` CSS variable approach.
 * The image is now injected directly by JS into style.backgroundImage.
 * opacity is set to a valid value (0.35) so it's visible but subtle.
 * z-index: 0 keeps it behind the overlay (z-index: 1) and content (z-index: 3).
 */

.about-hero-bg {
    background-size: contain;        /* ← shows full image, no cropping */
    background-position: center center;
    background-repeat: no-repeat;
    z-index: 0;
}

.team-strip {
    position: absolute;
    top: 120px;
    left: 655px;
    width: 53%;
    height: 70%;
    display: flex;
    flex-direction: row;
    z-index: 0;
}
.team-member {
    flex: 1;
    position: relative;
    background-size: cover;
    background-position: center top;
    background-repeat: no-repeat;
    height: 100%;
    overflow: hidden;
}
.team-member::before {
    content: '';
    position: absolute; inset: 0;
    background: linear-gradient(90deg,
        rgba(6,5,23,0.6) 0%,
        transparent 40%,
        transparent 100%);
    z-index: 1;
}
.member-role {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    padding: 28px 10px 12px;
    background: linear-gradient(0deg,
        rgba(6,5,23,0.92) 0%,
        transparent 100%);
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--fire);
    text-align: center;
    z-index: 2;
}


/* Dark overlay so text stays readable — kept intentionally lighter on the right
   so the team photo peeks through */
.about-hero::before {
    content: '';
    position: absolute; inset: 0;
    background:
        linear-gradient(90deg,
            rgba(6,5,23,0.97) 0%,
            rgba(6,5,23,0.85) 40%,
            rgba(6,5,23,0.45) 70%,
            rgba(6,5,23,0.25) 100%);
    z-index: 1;
}

/* Decorative grid lines */
.about-hero::after {
    content: '';
    position: absolute; inset: 0;
    background-image:
        linear-gradient(rgba(208,91,55,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(208,91,55,0.04) 1px, transparent 1px);
    background-size: 60px 60px;
    z-index: 2;
    pointer-events: none;
}

.about-hero-inner {
    position: relative; z-index: 3;
    max-width: 1300px; margin: 0 auto; width: 100%;
    display: grid;
    grid-template-columns: 1fr auto;
    grid-template-rows: auto auto;
    gap: 0 60px;
    align-items: start;
}

.hero-left {
    grid-column: 1;
    grid-row: 1;
}

.hero-crumb {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 11px; font-weight: 700;
    letter-spacing: 3.5px; text-transform: uppercase;
    color: var(--fire); margin-bottom: 14px;
    display: flex; align-items: center; gap: 8px;
}
.hero-crumb span { color: rgba(208,91,55,0.35); }
.hero-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: clamp(56px, 8vw, 100px);
    font-weight: 800; line-height: .88;
    letter-spacing: -1px; color: var(--light);
    margin-bottom: 20px;
}
.hero-title em { color: var(--fire); font-style: normal; }
.hero-sub {
    font-size: 14px; color: var(--muted);
    line-height: 1.8; max-width: 500px;
    border-left: 3px solid var(--fire);
    padding-left: 18px;
    text-align: justify;
}
/* Stat pills right side */

.hero-right {
    grid-column: 1;
    grid-row: 2;
    display: flex;
    flex-direction: row;
    width: 100%;           /* ← stretch to full column width */
    max-width: 600px;      /* ← cap it so it doesn't get too wide */
    overflow: hidden;
    margin-top: 16px;
    margin-left: -60px; 
}

.stat-pill {
    flex: 1;
    padding: 20px 16px;
    border-right: 1px solid var(--border);  /* ← vertical dividers */
    transition: background .25s;
    text-align: center;
}

.stat-pill:last-child { border-right: none; }
.stat-pill:hover { background: rgba(208,91,55,0.08); }

.stat-num {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 28px; font-weight: 800;
    color: var(--fire); line-height: 1; letter-spacing: -1px;
}
.stat-lbl {
    font-size: 8px; letter-spacing: 1.5px;
    text-transform: uppercase; color: var(--muted); margin-top: 3px;
}

/* ══════════════ FULL-WIDTH DIVIDER STRIP ══════════════ */
.fire-strip {
    background: var(--fire); padding: 22px 60px;
    display: flex; align-items: center; gap: 40px;
    overflow: hidden;
}
.strip-text {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: clamp(22px, 3vw, 34px); font-weight: 800;
    color: #fff; letter-spacing: .5px; white-space: nowrap;
}
.strip-line { flex: 1; height: 1px; background: rgba(255,255,255,0.3); }

/* ══════════════ ABOUT SECTION: 2-col ══════════════ */
.about-wrap {
    padding: 72px 60px;
    max-width: 1300px; margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 64px;
    align-items: start;
}
.about-left {}
.about-img-stack {
    position: relative;
    height: 480px;
}
.about-img-main {
    position: absolute;
    top: 0; left: 0;
    width: 80%; height: 360px;
    object-fit: cover;
    border: 3px solid var(--border);
    filter: brightness(.85) saturate(.9);
    transition: filter .3s;
}
.about-img-main:hover { filter: brightness(1) saturate(1); }
.about-img-accent {
    position: absolute;
    bottom: 0; right: 0;
    width: 55%; height: 240px;
    object-fit: cover;
    border: 3px solid var(--fire);
    filter: brightness(.85) saturate(.9);
    transition: filter .3s;
}
.about-img-accent:hover { filter: brightness(1) saturate(1); }
/* orange badge over images */
.about-badge {
    position: absolute; bottom: 56px; left: 0;
    background: var(--fire); color: #fff;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 12px; font-weight: 700;
    letter-spacing: 2px; text-transform: uppercase;
    padding: 10px 18px;
    clip-path: polygon(0 0,100% 0,calc(100% - 8px) 100%,0 100%);
    z-index: 5;
}

.about-right {}
.about-body {
    font-size: 14px; color: var(--muted);
    line-height: 1.9; margin-bottom: 20px;
}
.about-body + .about-body { margin-top: 0; }
/* Feature checklist */
.feature-list {
    display: flex; flex-direction: column;
    gap: 12px; margin: 24px 0 32px;
}
.feature-item {
    display: flex; align-items: flex-start; gap: 12px;
    font-size: 13px; color: var(--light); line-height: 1.5;
}
.feature-dot {
    width: 20px; height: 20px; flex-shrink: 0;
    background: rgba(208,91,55,0.15);
    border: 1px solid rgba(208,91,55,0.4);
    display: flex; align-items: center; justify-content: center;
    font-size: 10px; color: var(--fire); margin-top: 1px;
}

/* ══════════════ MISSION STRIP ══════════════ */
.mission-strip {
    padding: 64px 60px;
    background: var(--card);
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
}
.mission-inner {
    max-width: 1300px; margin: 0 auto;
    display: grid; grid-template-columns: 1fr 2fr;
    gap: 60px; align-items: center;
}
.mission-label {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 10px; font-weight: 700;
    letter-spacing: 3.5px; text-transform: uppercase;
    color: var(--fire); margin-bottom: 10px;
}
.mission-heading {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: clamp(32px, 4vw, 48px); font-weight: 800;
    color: var(--light); line-height: .95; letter-spacing: -.5px;
}
.mission-body {
    font-size: 14px; color: var(--muted); line-height: 1.85;
}
.mission-body + .mission-body { margin-top: 16px; }

/* ══════════════ PILLARS / PRINCIPLES ══════════════ */
.pillars-section {
    padding: 72px 60px;
    max-width: 1300px; margin: 0 auto;
}
.pillars-grid {
    display: grid; grid-template-columns: repeat(4,1fr); gap: 16px;
    margin-top: 36px;
}
.pillar {
    border: 1px solid var(--border);
    padding: 28px 22px;
    position: relative; overflow: hidden;
    transition: border-color .3s, transform .3s;
}
.pillar::after {
    content: '';
    position: absolute; bottom: 0; left: 0; right: 0;
    height: 0; background: rgba(208,91,55,0.06);
    transition: height .4s;
}
.pillar:hover { border-color: var(--border-h); transform: translateY(-3px); }
.pillar:hover::after { height: 100%; }
.pillar-icon { font-size: 26px; margin-bottom: 14px; display: block; position: relative; z-index: 1; }
.pillar-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 18px; font-weight: 700;
    color: var(--light); margin-bottom: 8px;
    position: relative; z-index: 1;
}
.pillar-body { font-size: 12px; color: var(--muted); line-height: 1.7; position: relative; z-index: 1; }
.pillar-n {
    position: absolute; top: 18px; right: 18px;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 28px; font-weight: 800;
    color: rgba(208,91,55,0.1); line-height: 1;
}

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
@media (max-width: 1024px) {
    .services-grid { grid-template-columns: 1fr 1fr; }
    .pillars-grid  { grid-template-columns: 1fr 1fr; }
    .about-wrap    { grid-template-columns: 1fr; }
    .about-img-stack { height: 300px; margin-bottom: 20px; }
    .mission-inner { grid-template-columns: 1fr; gap: 24px; }
}

@media (max-width: 700px) {
    .about-hero-inner {
        grid-template-columns: 1fr;
    }
    .about-hero-bg { display: none; }
    .hero-right    { display: none; }
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
        <li><a class="active" onclick="navigate('about')">About</a></li>
        <li><a onclick="navigate('projects')">Projects</a></li>
        <li><a onclick="navigate('contacts')">Contacts</a></li>
    </ul>
</nav>

<!-- ═══════════════════ HERO ═══════════════════ -->
<!-- ═══════════════════ HERO ═══════════════════ -->
<div class="about-hero" id="about-hero-section">
    <div class="about-hero-inner">
        <div class="hero-left">
            <div class="hero-crumb">LANES & LEDGERS <span>/</span> About </div>
            <h1 class="hero-title">ABOUT US</h1>
            <p class="hero-sub">
                This dashboard is the result of our 
                project dedicated to enhancing transparency 
                and tracking the progress of 
                Department of Public Works and Highways (DPWH) 
                infrastructure developments across the districts of Iloilo. 
                Our main objective is to transform raw project 
                data into a clear, accessible visual interface. 
                By bringing all these details together, 
                our project aims to give users a straightforward 
                way to monitor local growth, ensuring that public 
                infrastructure investments are easily visible and understandable.

                To provide a complete picture of these developments, 
                our dashboard carefully tracks all the essential 
                details for each DPWH initiative. It allows users 
                to see exactly what kind of project is being built, 
                which specific district in Iloilo it belongs to, 
                and the private contractors assigned to execute the work. 
                Additionally, we designed the dashboard to monitor the 
                financial and operational scope by displaying the total cost, 
                the expected duration of the work, and the current overall 
                percentage of project progress. Through this project, we 
                hope to demonstrate how organized data can be used to 
                foster accountability and keep the community informed.
            </p>
        </div>
        <div class="hero-right">
            <div class="stat-pill">
                <div class="stat-num">5</div>
                <div class="stat-lbl">District Engineering Offices</div>
            </div>
            <div class="stat-pill">
                <div class="stat-num">14</div>
                <div class="stat-lbl">Active Projects</div>
            </div>
            <div class="stat-pill">
                <div class="stat-num">175</div>
                <div class="stat-lbl">Completed Projects</div>
            </div>
            <div class="stat-pill">
                <div class="stat-num">&#8369;4.8B</div>
                <div class="stat-lbl">Total Budget</div>
            </div>
        </div>
    </div>

    <!-- Team photo with role overlays -->
    <div class="team-strip" id="hero-bg">
        <div class="team-member">
            <div class="member-role">BI Analyst</div>
        </div>
        <div class="team-member">
            <div class="member-role">UI/UX Designer</div>
        </div>
        <div class="team-member">
            <div class="member-role">BI Developer</div>
        </div>
        <div class="team-member">
            <div class="member-role">Product Manager</div>
        </div>
        <div class="team-member">
            <div class="member-role">Data Engineer</div>
        </div>
    </div>
</div>

<!-- ═══════════════════ FIRE STRIP ═══════════════════ -->
<div class="fire-strip">
    <div class="strip-text">RIGHT PROJECTS &bull; RIGHT COST &bull; RIGHT QUALITY &bull; RIGHT TIME &bull; RIGHT PEOPLE</div>
    <div class="strip-line"></div>
</div>

<!-- ═══════════════════ ABOUT THIS DASHBOARD ═══════════════════ -->
<div class="about-wrap">
    <!-- Left: stacked images -->
    <div class="about-left">
        <div class="about-img-stack">
            <img class="about-img-main"
                src="%%DPWH_BG_IMG%%"
                alt="DPWH Road Project"
                onerror="this.style.background='#1a1838';this.removeAttribute('src');">
            <img class="about-img-accent"
                src="%%DPWH_WORKERS_IMG%%"
                alt="Construction Site"
                onerror="this.style.background='#D05B37';this.removeAttribute('src');">
            <div class="about-badge">Iloilo District Projects</div>
        </div>
    </div>

    <!-- Right: text -->
    <div class="about-right">
        <div class="section-tag">About This Dashboard</div>
        <h2 class="section-title" style="font-size:clamp(28px,3.5vw,42px);margin-bottom:20px;">
            BUILT FOR<br><em style="color:var(--fire);font-style:normal;">ACCOUNTABILITY</em>
        </h2>
        <p class="about-body">
            This dashboard is the result of our project dedicated to enhancing transparency
            and tracking the progress of Department of Public Works and Highways (DPWH)
            infrastructure developments across the districts of Iloilo. Our main objective
            is to transform raw project data into a clear, accessible visual interface.
        </p>
        <p class="about-body">
            By bringing all these details together, our project aims to give users a
            straightforward way to monitor local growth, ensuring that public infrastructure
            investments are easily visible and understandable.
        </p>

        <div class="feature-list">
            <div class="feature-item">
                <div class="feature-dot">✓</div>
                Project type classification — road widening, bridges, flood control, public facilities
            </div>
            <div class="feature-item">
                <div class="feature-dot">✓</div>
                District-level filtering across all Iloilo legislative districts
            </div>
            <div class="feature-item">
                <div class="feature-dot">✓</div>
                Contractor and construction firm identification per project
            </div>
            <div class="feature-item">
                <div class="feature-dot">✓</div>
                Total cost, duration, and real-time completion percentage tracking
            </div>
            <div class="feature-item">
                <div class="feature-dot">✓</div>
                Open data access for citizens, stakeholders, and policymakers
            </div>
        </div>

        <p class="about-body">
            To keep the public fully informed on the pace of development, the system accurately
            tracks project durations from their official start dates right through to their
            targeted completion deadlines. Ultimately, this tool is built on the principle that
            open data empowers communities — ensuring every public works initiative in Iloilo
            operates with the highest level of integrity and efficiency.
        </p>
    </div>
</div>

<!-- ═══════════════════ MISSION ═══════════════════ -->
<div class="mission-strip">
    <div class="mission-inner">
        <div>
            <div class="mission-label">Our Mission</div>
            <h2 class="mission-heading">
                OPEN DATA<br>
                <span style="color:var(--fire);">EMPOWERS</span><br>
                COMMUNITIES
            </h2>
        </div>
        <div>
            <p class="mission-body">
                This dashboard serves as a central transparency portal dedicated to tracking the
                progress, scope, and financial details of DPWH infrastructure projects across the
                various districts of Iloilo. Designed to foster public accountability and civic
                engagement, the platform provides citizens, stakeholders, and policymakers with a
                clear, real-time overview of local development.
            </p>
            <p class="mission-body">
                By consolidating critical project data into an accessible interface, we aim to
                ensure that public infrastructure investments are visible, monitorable, and
                delivered efficiently. Through this project, we hope to demonstrate how organized
                data can be used to foster accountability and keep the community informed.
            </p>
        </div>
    </div>
</div>

<!-- ═══════════════════ PILLARS ═══════════════════ -->
<div class="pillars-section">
    <div class="section-tag">Our Principles</div>
    <h2 class="section-title">PILLARS OF<br><em style="color:var(--fire);font-style:normal;">ACCOUNTABILITY</em></h2>
    <div class="pillars-grid">
        <div class="pillar">
            <div class="pillar-n">01</div>
            <div class="pillar-title">Transparency</div>
            <div class="pillar-body">
                Full disclosure of project details, contractor information, costs, and timelines
                — accessible to every Filipino citizen without restriction.
            </div>
        </div>
        <div class="pillar">
            <div class="pillar-n">02</div>
            <div class="pillar-title">Accountability</div>
            <div class="pillar-body">
                Real-time monitoring of project milestones, budget utilization, and delivery
                compliance across all district offices in Iloilo.
            </div>
        </div>
        <div class="pillar">
            <div class="pillar-n">03</div>
            <div class="pillar-title">Participation</div>
            <div class="pillar-body">
                Community feedback mechanisms and public reporting channels to ensure projects
                serve the genuine needs of every locality and district.
            </div>
        </div>
        <div class="pillar">
            <div class="pillar-n">04</div>
            <div class="pillar-title">Excellence</div>
            <div class="pillar-body">
                Commitment to right projects, right cost, right quality, right time, and
                right people — the five pillars of DPWH infrastructure delivery.
            </div>
        </div>
    </div>
</div>

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

<script>
/*
 * FIX 1 – Team photo background
 * Directly set backgroundImage on the element after the page loads.
 * This is the only reliable method when the src is a long base64 string.
 */

(function() {
    var src = "%%TEAM_PHOTO%%";
    if (src && src.startsWith("data:")) {
        var members = document.querySelectorAll(".team-member");
        var total = members.length;
        members.forEach(function(el, i) {
            el.style.backgroundImage    = "url('" + src + "')";
            el.style.backgroundSize     = (total * 100) + "% 100%";
            el.style.backgroundPosition = ((i / (total - 1)) * 100) + "% center";
        });
    }
})();


function navigate(page) {
    try {
        window.top.location.href = "/?navigate=" + page;
    } catch(e) {
        // Fallback for cross-origin iframe restrictions (shouldn't happen on
        // localhost / same-origin Streamlit deployments)
        window.location.href = "/?navigate=" + page;
    }
}
</script>
</body>
</html>
"""

HTML = HTML.replace("%%DPWH_LOGO%%", LOGO_TAG)
HTML = HTML.replace("%%TEAM_PHOTO%%", TEAM_PHOTO_SRC)
HTML = HTML.replace("%%DPWH_BG_IMG%%", DPWH_BG_IMG)
HTML = HTML.replace("%%DPWH_WORKERS_IMG%%", DPWH_WORKERS_IMG)


components.html(HTML, height=0, scrolling=False)