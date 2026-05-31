import streamlit as st
import base64
from pathlib import Path
import streamlit.components.v1 as components


st.set_page_config(
    page_title="DPWH – Home",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Handle navigation query params FIRST ─────────────────────────────────
nav = st.query_params.get("navigate", "")
if nav == "home":
    st.query_params.clear()
elif nav == "projects":
    st.switch_page("pages/projects1.py")
elif nav == "about":
    st.switch_page("pages/about.py")
elif nav == "contacts":
    st.switch_page("pages/contacts.py")


LOGO_PATH = "pages/Dashboard figures/DPWH_LOGO.png"

def get_logo_src():
    try:
        data = Path(LOGO_PATH).read_bytes()
        b64  = base64.b64encode(data).decode()
        return f"data:image/png;base64,{b64}"
    except Exception:
        return ""

LOGO_SRC = get_logo_src()

def get_image_base64(path, mime="image/jpeg"):
    try:
        with open(path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
            return f"data:{mime};base64,{encoded}"
    except Exception:
        return ""

HEX1_IMG   = get_image_base64("pages/Dashboard figures/DPWHhp.jpg")
HEX2_IMG   = get_image_base64("pages/Dashboard figures/DPWHhp1.jpg")
HEX3_IMG   = get_image_base64("pages/Dashboard figures/DPWHhp2.jpg")
HEX4_IMG   = get_image_base64("pages/Dashboard figures/DPWHhp3.jpg")
HEX5_IMG   = get_image_base64("pages/Dashboard figures/DPWHhp4.jpg")
HEX6_IMG   = get_image_base64("pages/Dashboard figures/DPWHhp5.jpg")
HEX7_IMG   = get_image_base64("pages/Dashboard figures/DPWHhp6.jpg")
HOMEBG_IMG = get_image_base64("pages/Dashboard figures/homebg.jpg")



# ── Hide all Streamlit chrome ─────────────────────────────────────────────
st.markdown("""
<style>
#MainMenu, header,
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
section.main,
section.main > div,
div[class*="css"] {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
    width: 100% !important;
    background: #060517 !important;
}

iframe {
    display: block !important;
    width: 100vw !important;
    min-height: 100vh !important;
    border: none !important;
    position: fixed !important;
    top: 0 !important; left: 0 !important;
    z-index: 999 !important;
}
</style>
""", unsafe_allow_html=True)

# ── Build the logo tag ────────────────────────────────────────────────────
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
<title>DPWH Transparency Board</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@300;400;600;700;800&family=Barlow:wght@300;400;500&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
    color: #e8e4df;
    font-family: 'Barlow', sans-serif;
    overflow-x: hidden;
    min-height: 100vh;
    background: #060517;
}

:root {
    --bg:        #060517;
    --fire:      #D05B37;
    --fire-dark: #a8421f;
    --light:     #e8e4df;
    --muted:     #9b9590;
}

/* ── Navbar ── */
.dpwh-nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 40px; height: 68px;
    background: rgba(6,5,23,0.88);
    backdrop-filter: blur(14px);
    border-bottom: 1px solid rgba(208,91,55,0.18);
}
.nav-logo {
    display: flex; align-items: center; gap: 12px;
    text-decoration: none; cursor: pointer;
}
.nav-logo-icon {
    width: 44px; height: 44px;
    background: var(--fire);
    clip-path: polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);
    display: flex; align-items: center; justify-content: center;
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 800; font-size: 11px; color: #fff;
    letter-spacing: .5px; flex-shrink: 0;
}
.nav-logo-text { display: flex; flex-direction: column; line-height: 1.1; }
.nav-logo-text .t1 {
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 800; font-size: 17px;
    color: var(--fire); letter-spacing: 1.5px;
}
.nav-logo-text .t2 {
    font-size: 9px; color: var(--muted);
    letter-spacing: 2px; text-transform: uppercase;
}
.nav-links { display: flex; gap: 36px; list-style: none; }
.nav-links a {
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 600; font-size: 14px;
    letter-spacing: 2px; text-transform: uppercase;
    color: var(--light); text-decoration: none;
    position: relative; padding-bottom: 3px;
    transition: color .25s;
    cursor: pointer;
}
.nav-links a::after {
    content: ''; position: absolute;
    bottom: 0; left: 0; width: 0; height: 2px;
    background: var(--fire); transition: width .3s ease;
}
.nav-links a:hover,
.nav-links a.active { color: var(--fire); }
.nav-links a:hover::after,
.nav-links a.active::after { width: 100%; }

/* ── Hero ── */
.hero-wrapper {
    position: relative;
    min-height: 100vh;
    display: flex; align-items: center;
    padding: 0;
    overflow: hidden;
}
.hero-wrapper::before {
    content: '';
    position: absolute; inset: 0;
    background: url('%%HOMEBG_IMG%%') center/cover no-repeat;
    z-index: 0;
}
.hero-wrapper::after {
    content: '';
    position: absolute; inset: 0;
    background: rgba(6, 5, 23, 0.72);
    z-index: 1;
}

.hero-inner {
    position: relative;
    z-index: 2;
    width: 100%;
    max-width: 1600px;
    margin: 0 auto;
    display: flex;
    align-items: center;
}

.hero-scene {
    position: relative;
    width: 100%;
    height: 100vh;
    min-height: 600px;
}

/* ── Text block ── */
.hero-text-wrap {
    position: absolute;
    top: calc(50% + 60px);
    left: 60px;
    transform: translateY(-50%);
    z-index: 10;
    display: flex;
    flex-direction: row;
    align-items: stretch;
    gap: 0;
    max-width: 540px;
}
.orange-bar {
    width: 4px;
    background: var(--fire);
    border-radius: 2px;
    margin-right: 20px;
    align-self: stretch;
    flex-shrink: 0;
}
.hero-text {
    display: flex; flex-direction: column;
    justify-content: center; gap: 12px;
}
.hero-dept {
    font-size: 11px; font-weight: 500;
    letter-spacing: 3px; text-transform: uppercase;
    color: var(--muted);
}
.hero-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: clamp(60px, 7.5vw, 105px);
    line-height: 0.85; margin: 0;
    text-shadow: 0 2px 30px rgba(6,5,23,0.65);
}
.hero-title .accent { color: var(--fire); }
.hero-tagline {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: clamp(12px, 1.4vw, 16px);
    font-weight: 300; letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--muted); line-height: 2;
}
.hero-tagline .dot { color: var(--fire); font-weight: 700; }

.hero-cta-row { display: flex; gap: 16px; align-items: center; margin-top: 8px; }

.btn-primary {
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 700; font-size: 13px;
    letter-spacing: 2.5px; text-transform: uppercase;
    padding: 14px 32px;
    background: var(--fire); color: #fff;
    border: none; cursor: pointer; text-decoration: none;
    clip-path: polygon(8px 0%,100% 0%,calc(100% - 8px) 100%,0% 100%);
    transition: background .25s, transform .2s; display: inline-block;
}
.btn-primary:hover { background: var(--fire-dark); transform: translateY(-2px); }
.btn-outline {
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 600; font-size: 13px;
    letter-spacing: 2.5px; text-transform: uppercase;
    padding: 13px 28px; background: transparent;
    color: var(--light); border: 1px solid rgba(232,228,223,0.25);
    cursor: pointer; text-decoration: none;
    transition: border-color .25s, color .25s; display: inline-block;
}
.btn-outline:hover { border-color: var(--fire); color: var(--fire); }

/* ── Hex base ── */
.hex {
    position: absolute;
    clip-path: polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);
    overflow: hidden;
    transition: transform .4s ease, filter .4s ease;
}
.hex:hover {
    transform: scale(1.06) !important;
    filter: brightness(1.18);
    z-index: 15 !important;
}

.hex-1 { width: 400px; height: 460px; top: calc(50vh - 180px); left: calc(50% - 120px); z-index: 2; }
.hex-2 { width: 230px; height: 265px; top: calc(50vh - 350px); left: calc(50% + 200px); z-index: 3; }
.hex-3 { width: 530px; height: 580px; top: -250px; right: -240px; z-index: 1; }
.hex-4 { width: 250px; height: 280px; top: calc(50vh - 100px); left: calc(50% + 350px); z-index: 4; }
.hex-5 { width: 380px; height: 420px; top: calc(50vh + 200px); left: calc(50% + 160px); z-index: 3; }
.hex-6 { width: 400px; height: 460px; top: calc(50vh + 80px); left: calc(50% + 590px); z-index: 3; }

.hex-dots {
    position: absolute; inset: 0;
    width: 100%; height: 100%;
    pointer-events: none; z-index: 0;
    overflow: visible;
}

/* ── Ticker ── */
.ticker-strip {
    background: var(--fire); padding: 10px 0; overflow: hidden;
    position: relative; z-index: 2;
}
.ticker-inner {
    display: flex; gap: 60px; white-space: nowrap;
    animation: ticker 28s linear infinite; width: max-content;
}
.ticker-inner:hover { animation-play-state: paused; }
@keyframes ticker {
    from { transform: translateX(0); }
    to   { transform: translateX(-50%); }
}
.ticker-item {
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 700; font-size: 13px;
    letter-spacing: 2.5px; text-transform: uppercase;
    color: rgba(255,255,255,0.9);
    display: flex; align-items: center; gap: 18px;
}
.ticker-sep { color: rgba(255,255,255,0.5); font-size: 8px; }


/* ── Mobile ── */
@media (max-width: 900px) {
    .hero-scene { height: auto; min-height: 100vh; padding-bottom: 60px; }
    .hero-text-wrap { position: relative; top: auto; left: auto; transform: none; margin: 90px 18px 40px; max-width: 100%; }
    .hex-1 { width:200px; height:230px; top:80px;  left:10px; }
    .hex-2 { width:130px; height:150px; top:20px;  left:200px; }
    .hex-3 { width:180px; height:207px; top:-60px; right:-40px; }
    .hex-4 { width:130px; height:150px; top:260px; left:200px; }
    .hex-5 { width:120px; height:138px; top:320px; left:280px; }
    .hex-6 { width:150px; height:173px; top:300px; right:10px; }
    .ticker-strip { display: none; }
}
@media (max-width: 480px) {
    .hero-cta-row { flex-direction: column; align-items: flex-start; }
    .btn-primary, .btn-outline { width: 100%; text-align: center; }
}

@media (max-width: 768px) {{
  .dpwh-nav {{ padding: 0 16px; height: 56px; }}
  .nav-links {{ gap: 14px; }}
  .nav-links a {{ font-size: 11px; letter-spacing: 1px; }}
  .nav-logo-text .t2 {{ display: none; }}

  .hero-scene {{ height: auto; min-height: 100vh; }}
  .hero-text-wrap {{
    position: relative; top: auto; left: auto;
    transform: none; margin: 80px 18px 40px;
    max-width: 100%;
  }}
  .hex-1, .hex-2, .hex-3,
  .hex-4, .hex-5, .hex-6 {{ display: none; }}
  .btn-primary, .btn-outline {{
    width: 100%; text-align: center; display: block;
  }}
  .hero-cta-row {{ flex-direction: column; }}
}}

@media (max-width: 480px) {{
  .hero-title {{ font-size: 52px !important; }}
  .nav-links a {{ font-size: 10px; }}
}}

</style>
</head>
<body>

<!-- ═══ NAVBAR ═══ -->
<nav class="dpwh-nav">
    <a class="nav-logo" onclick="navigate('home')">
        %%DPWH_LOGO%%
        <div class="nav-logo-text">
            <span class="t1">DPWH</span>
            <span class="t2">Republic of the Philippines</span>
        </div>
    </a>
    <ul class="nav-links">
        <li><a class="active" onclick="navigate('home')">Home</a></li>
        <li><a onclick="navigate('about')">About</a></li>
        <li><a onclick="navigate('projects')">Projects</a></li>
        <li><a onclick="navigate('contacts')">Contacts</a></li>
    </ul>
</nav>

<!-- ═══ HERO ═══ -->
<section class="hero-wrapper">
    <div class="hero-inner">
        <div class="hero-scene">

            <svg class="hex-dots" viewBox="0 0 1600 900" xmlns="http://www.w3.org/2000/svg">
                <line x1="760"  y1="335" x2="880"  y2="335" stroke="rgba(208,91,55,0.12)" stroke-width="1" stroke-dasharray="4,6"/>
                <line x1="880"  y1="450" x2="980"  y2="410" stroke="rgba(208,91,55,0.10)" stroke-width="1" stroke-dasharray="4,6"/>
                <line x1="880"  y1="565" x2="980"  y2="630" stroke="rgba(208,91,55,0.10)" stroke-width="1" stroke-dasharray="4,6"/>
                <circle cx="880"  cy="335" r="3" fill="rgba(208,91,55,0.30)"/>
                <circle cx="880"  cy="565" r="3" fill="rgba(208,91,55,0.30)"/>
                <circle cx="980"  cy="410" r="3" fill="rgba(208,91,55,0.30)"/>
            </svg>

            <div class="hex hex-1" style="background: linear-gradient(rgba(0,0,0,0.28), rgba(0,0,0,0.28)), url('%%HEX1_IMG%%') center/cover no-repeat;"></div>
            <div class="hex hex-2" style="background: linear-gradient(rgba(0,0,0,0.32), rgba(0,0,0,0.32)), url('%%HEX2_IMG%%') center/cover no-repeat;"></div>
            <div class="hex hex-3" style="background: linear-gradient(rgba(0,0,0,0.28), rgba(0,0,0,0.28)), url('%%HEX3_IMG%%') center/cover no-repeat;"></div>
            <div class="hex hex-4" style="background: linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35)), url('%%HEX4_IMG%%') center/cover no-repeat;"></div>
            <div class="hex hex-5" style="background: linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35)), url('%%HEX5_IMG%%') center/cover no-repeat;"></div>
            <div class="hex hex-6" style="background: linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35)), url('%%HEX6_IMG%%') center/cover no-repeat;"></div>

            <div class="hero-text-wrap">
                <div class="orange-bar"></div>
                <div class="hero-text">
                    <p class="hero-dept">Department of Public Works and Highways | ILOILO</p>
                    <h1 class="hero-title">
                        TRANS<span class="accent">PARENCY</span><br>
                        BOARD
                    </h1>
                    <p class="hero-tagline">
                        Right Projects <span class="dot"> &bull; </span> Right Cost <span class="dot"> &bull; </span> Right Quality<br>
                        Right Time <span class="dot"> &bull; </span> Right People
                    </p>
                    <div class="hero-cta-row">
                        <button onclick="navigate('projects')" class="btn-primary">&#9654; View Projects</button>
                        <button onclick="navigate('about')" class="btn-outline">Learn More</button>
                    </div>
                </div>
            </div>

        </div>
    </div>
</section>

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
</script>

</body>
</html>
"""
# ── Inject all assets ─────────────────────────────────────────────────────
HTML = HTML.replace("%%DPWH_LOGO%%",  LOGO_TAG)
HTML = HTML.replace("%%HOMEBG_IMG%%", HOMEBG_IMG)
HTML = HTML.replace("%%HEX1_IMG%%",   HEX1_IMG)
HTML = HTML.replace("%%HEX2_IMG%%",   HEX2_IMG)
HTML = HTML.replace("%%HEX3_IMG%%",   HEX3_IMG)
HTML = HTML.replace("%%HEX4_IMG%%",   HEX4_IMG)
HTML = HTML.replace("%%HEX5_IMG%%",   HEX5_IMG)
HTML = HTML.replace("%%HEX6_IMG%%",   HEX6_IMG)


components.html(HTML, height=0, scrolling=False)