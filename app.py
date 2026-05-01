from pathlib import Path
import base64
import html
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Sumith P Kotian | Video Editor Portfolio",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

APP_DIR = Path(__file__).parent
PROFILE_PATH = APP_DIR / "assets" / "profile_photo.jpeg"


def image_data_uri(path: Path) -> str:
    """Return a base64 data URI for the default profile image."""
    if not path.exists():
        return ""
    mime = "image/jpeg" if path.suffix.lower() in {".jpg", ".jpeg"} else "image/png"
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"


NAME = "SUMITH P KOTIAN"
EMAIL = "sumithktn@gmail.com"
PHONE = "+91 9448252164"
LINKEDIN = "https://www.linkedin.com/in/sumith-kotian-066a723a6"
LOCATION = "Manipal, Karnataka, India"
PROFILE_IMG = image_data_uri(PROFILE_PATH)

AUTO_VIDEO_SRC = "https://res.cloudinary.com/dy7y2t3bm/video/upload/q_auto,f_auto/auto_cinematic_reel_qvts7o.mp4"
YOUTUBE_VIDEO_SRC = "https://res.cloudinary.com/dy7y2t3bm/video/upload/q_auto,f_auto/you_w2zcuw.mp4"
BRAND_VIDEO_SRC = "https://res.cloudinary.com/dy7y2t3bm/video/upload/v1777671542/brand_ivyf8t.mp4"
INSTAGRAM_VIDEO_SRC = "https://res.cloudinary.com/dy7y2t3bm/video/upload/q_auto,f_mp4/insta_tow33x"
EVENT_VIDEO_SRC = "https://res.cloudinary.com/dy7y2t3bm/video/upload/q_auto/f_auto/AUTONEX_NITK_expo_2_mifewr.mp4"
PRODUCT_SHOWCASE_VIDEO_SRC = "https://res.cloudinary.com/dy7y2t3bm/video/upload/v1777671007/PRO_ti7opg.mp4"
portfolio_items = [
]


portfolio_video_card = f"""
    <article class="portfolio-card reveal featured-video-card">
      <div class="thumb video-thumb">
        <iframe class="portfolio-video"
  <iframe class="portfolio-video"
  src="{AUTO_VIDEO_SRC}"
  allowfullscreen>
</iframe>
      </div>
      <div class="card-body">
        <h3>Automotive Cinematic Reel</h3>
        <p>Car showcase · Motion + Color Grade</p>
      </div>
    </article>
    <article class="portfolio-card reveal featured-video-card youtube-video-card">
      <div class="thumb video-thumb">
        <video class="portfolio-video" controls preload="metadata" playsinline>
          <source src="{YOUTUBE_VIDEO_SRC}" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>
      <div class="card-body">
        <h3>YouTube Shorts Edit</h3>
        <p>Fast-paced · Jump Cuts + Beat Sync</p>
      </div>
    </article>
    <article class="portfolio-card reveal featured-video-card brand-video-card">
      <div class="thumb video-thumb">
        <video class="portfolio-video" controls preload="metadata" playsinline>
          <source src="{BRAND_VIDEO_SRC}" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>
      <div class="card-body">
        <h3>Brand Promo Video</h3>
        <p>Promotional · Motion Graphics + SFX</p>
      </div>
    </article>
    <article class="portfolio-card reveal featured-video-card instagram-video-card">
      <div class="thumb video-thumb">
        <video class="portfolio-video" controls preload="metadata" playsinline>
          <source src="{INSTAGRAM_VIDEO_SRC}" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>
      <div class="card-body">
        <h3>Instagram Reel</h3>
        <p>Social Media · Subtitles + Overlay</p>
      </div>
    </article>
    <article class="portfolio-card reveal featured-video-card event-video-card">
      <div class="thumb video-thumb">
        <video class="portfolio-video" controls preload="metadata" playsinline>
          <source src="{EVENT_VIDEO_SRC}" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>
      <div class="card-body">
        <h3>Event Highlight</h3>
        <p>Event · Cinematic Pacing + Color</p>
      </div>
    </article>
    <article class="portfolio-card reveal featured-video-card product-showcase-video-card">
      <div class="thumb video-thumb">
        <video class="portfolio-video" controls preload="metadata" playsinline>
          <source src="{PRODUCT_SHOWCASE_VIDEO_SRC}" type="video/mp4" />
           Your browser does not support the video tag.
        </video>
      </div>
      <div class="card-body">
        <h3>Product Showcase</h3>
        <p>Commercial · Smooth Transitions</p>
      </div>
    </article>

"""

portfolio_cards = portfolio_video_card + "".join(
    f"""
    <article class="portfolio-card reveal">
      <div class="thumb">
        <div class="play-icon">▶</div>
        <span class="duration">{html.escape(duration)}</span>
      </div>
      <div class="card-body">
        <h3>{html.escape(title)}</h3>
        <p>{html.escape(desc)}</p>
      </div>
    </article>
    """
    for title, desc, duration in portfolio_items
)


profile_markup = (
    f'<img src="{PROFILE_IMG}" alt="Sumith P Kotian profile photo" class="profile-photo" />'
    if PROFILE_IMG
    else '<div class="profile-placeholder">👤</div>'
)

# Hide Streamlit chrome. The actual portfolio UI is rendered through components.html below,
# so HTML is interpreted correctly instead of being displayed as visible source code.
st.markdown(
    """
    <style>
      [data-testid="stSidebar"], [data-testid="collapsedControl"],
      [data-testid="stHeader"], footer { display: none !important; }
      .block-container { padding: 0 !important; max-width: 100% !important; }
      .stApp { background: #0A0A0A; }
      iframe { display: block; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_doc = f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --gold: #D4A853;
      --gold-light: #F0D48A;
      --gold-soft: rgba(212,168,83,.14);
      --bg: #0A0A0A;
      --surface: #111111;
      --surface-2: #1A1A1A;
      --text: #F5F5F5;
      --muted: rgba(245,245,245,.68);
    }}

    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: 'Outfit', sans-serif;
      overflow-x: hidden;
    }}
    body::before {{
      content: '';
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 9999;
      opacity: .035;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='1'/%3E%3C/svg%3E");
    }}
    ::-webkit-scrollbar {{ width: 8px; }}
    ::-webkit-scrollbar-track {{ background: var(--bg); }}
    ::-webkit-scrollbar-thumb {{ background: var(--gold); border-radius: 999px; }}

    .navbar {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      z-index: 1000;
      background: rgba(10,10,10,.92);
      backdrop-filter: blur(18px);
      border-bottom: 1px solid rgba(212,168,83,.14);
    }}
    .nav-inner {{
      width: min(1160px, calc(100% - 36px));
      margin: 0 auto;
      padding: 16px 0;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 18px;
    }}
    .logo, .nav-btn {{
      border: 0;
      background: transparent;
      cursor: pointer;
      font-family: inherit;
    }}
    .logo {{
      color: var(--gold);
      font-family: 'Bebas Neue', cursive;
      font-size: 31px;
      letter-spacing: 1.7px;
      line-height: 1;
      white-space: nowrap;
      padding: 0;
    }}
    .logo span {{ color: var(--text); }}
    .nav-links {{
      display: flex;
      align-items: center;
      justify-content: flex-end;
      gap: 25px;
      flex-wrap: wrap;
    }}
    .nav-btn {{
      color: rgba(245,245,245,.74);
      text-transform: uppercase;
      letter-spacing: 1.45px;
      font-size: 12px;
      padding: 8px 0;
      position: relative;
      transition: color .25s ease;
    }}
    .nav-btn::after {{
      content: '';
      position: absolute;
      left: 0;
      bottom: 2px;
      height: 1px;
      width: 0;
      background: var(--gold);
      transition: width .25s ease;
    }}
    .nav-btn:hover {{ color: var(--gold); }}
    .nav-btn:hover::after {{ width: 100%; }}

    .hero {{
      position: relative;
      min-height: 100vh;
      padding: 140px 28px 84px;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      background: radial-gradient(circle at 80% 14%, rgba(212,168,83,.10), transparent 30%), var(--bg);
    }}
    .hero::after {{
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(120deg, transparent 0 40%, rgba(212,168,83,.035), transparent 60% 100%);
      pointer-events: none;
    }}
    .speed-line {{
      position: absolute;
      left: 0;
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--gold), transparent);
      opacity: .58;
      animation: speed 4s linear infinite;
    }}
    .speed-line:nth-child(1) {{ top: 24%; width: 230px; animation-delay: 0s; }}
    .speed-line:nth-child(2) {{ top: 47%; width: 310px; animation-delay: 1.2s; }}
    .speed-line:nth-child(3) {{ top: 71%; width: 190px; animation-delay: 2.3s; }}
    @keyframes speed {{
      0% {{ transform: translateX(-120%); opacity: 0; }}
      40% {{ opacity: .6; }}
      100% {{ transform: translateX(650%); opacity: 0; }}
    }}
    .hero-grid {{
      position: relative;
      z-index: 2;
      width: min(1120px, 100%);
      display: grid;
      grid-template-columns: 290px 1fr;
      gap: 58px;
      align-items: center;
    }}
    .profile-wrap {{ text-align: center; }}
    .profile-ring {{
      width: 242px;
      height: 242px;
      margin: 0 auto;
      border-radius: 50%;
      padding: 5px;
      background: conic-gradient(var(--gold), transparent, var(--gold), transparent, var(--gold));
      box-shadow: 0 0 35px rgba(212,168,83,.26);
      animation: float 3.6s ease-in-out infinite;
    }}
    @keyframes float {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-8px); }} }}
    .profile-inner {{
      width: 100%;
      height: 100%;
      border-radius: 50%;
      overflow: hidden;
      background: #151515;
    }}
    .profile-photo {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
    .profile-placeholder {{ width: 100%; height: 100%; display: grid; place-items: center; font-size: 60px; }}
    .photo-label {{ margin-top: 12px; color: rgba(212,168,83,.76); letter-spacing: 2px; font-size: 11px; text-transform: uppercase; }}
    .eyebrow {{ color: var(--gold); text-transform: uppercase; letter-spacing: 4px; font-size: 12px; margin-bottom: 14px; }}
    .hero h1 {{
      font-family: 'Bebas Neue', cursive;
      font-size: clamp(58px, 8vw, 105px);
      line-height: .9;
      margin: 0 0 18px;
      letter-spacing: 1px;
      text-shadow: 0 0 30px rgba(212,168,83,.38);
    }}
    .chips {{ display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 24px; }}
    .chips span {{ border: 1px solid rgba(212,168,83,.35); color: var(--gold); border-radius: 999px; padding: 7px 12px; font-size: 12px; letter-spacing: .6px; }}
    .tagline {{ max-width: 650px; color: var(--muted); line-height: 1.8; font-size: 18px; margin-bottom: 30px; }}
    .btn-row {{ display: flex; gap: 14px; flex-wrap: wrap; }}
    .btn {{
      border: 0;
      cursor: pointer;
      border-radius: 12px;
      padding: 13px 26px;
      font-family: 'Bebas Neue', cursive;
      font-size: 19px;
      letter-spacing: 1.1px;
      text-transform: uppercase;
      transition: transform .25s ease, box-shadow .25s ease, background .25s ease;
    }}
    .btn-primary {{ background: linear-gradient(135deg, var(--gold), #B8912F); color: #090909; box-shadow: 0 0 20px rgba(212,168,83,.20); }}
    .btn-outline {{ background: transparent; color: var(--gold); border: 1px solid var(--gold); }}
    .btn:hover {{ transform: translateY(-2px); box-shadow: 0 0 28px rgba(212,168,83,.32); }}

    .divider {{ width: min(860px, 76%); height: 1px; margin: 0 auto; background: linear-gradient(90deg, transparent, rgba(212,168,83,.45), transparent); }}
    .section {{ padding: 92px 28px; }}
    .container {{ width: min(1080px, 100%); margin: 0 auto; }}
    .section-label {{ color: var(--gold); text-transform: uppercase; letter-spacing: 4px; font-size: 12px; text-align: center; margin-bottom: 12px; }}
    .section-title {{
      font-family: 'Bebas Neue', cursive;
      font-size: clamp(52px, 6vw, 76px);
      letter-spacing: 1px;
      line-height: .95;
      margin: 0 0 58px;
      text-align: center;
    }}
    .section-title span {{ color: var(--gold); }}
    .about-grid {{ display: grid; grid-template-columns: 1.15fr .85fr; gap: 38px; align-items: start; }}
    .bio {{ color: rgba(245,245,245,.66); line-height: 1.9; margin: 0 0 30px; }}
    .stats {{ display: flex; gap: 24px; flex-wrap: wrap; }}
    .stat strong {{ display: block; color: var(--gold); font-family: 'Bebas Neue', cursive; font-size: 38px; font-weight: 400; }}
    .stat span {{ color: rgba(245,245,245,.44); text-transform: uppercase; letter-spacing: 1px; font-size: 11px; }}
    .panel {{ background: var(--surface); border: 1px solid rgba(212,168,83,.16); border-radius: 20px; padding: 28px; box-shadow: 0 18px 60px rgba(0,0,0,.28); }}
    .panel h3 {{ margin: 0 0 8px; color: var(--text); font-size: 22px; }}
    .panel p, .panel li {{ color: rgba(245,245,245,.62); line-height: 1.75; }}
    .meta {{ color: rgba(245,245,245,.42) !important; font-size: 13px; margin-top: 0; }}
    .note {{ margin-top: 18px; padding: 16px; border-radius: 14px; background: rgba(212,168,83,.06); border: 1px solid rgba(212,168,83,.14); font-size: 13px; }}
    .timeline {{ position: relative; max-width: 860px; margin: 0 auto; padding-left: 42px; }}
    .timeline::before {{ content: ''; position: absolute; left: 13px; top: 0; bottom: 0; width: 2px; background: linear-gradient(180deg, transparent, var(--gold), transparent); }}
    .dot {{ position: absolute; left: 4px; top: 0; width: 20px; height: 20px; border-radius: 50%; background: var(--bg); border: 2px solid var(--gold); box-shadow: 0 0 25px rgba(212,168,83,.5); }}
    .badge {{ display: inline-block; margin-left: 8px; font-family: 'Outfit', sans-serif; font-size: 12px; color: var(--gold); background: rgba(212,168,83,.12); padding: 4px 9px; border-radius: 999px; vertical-align: middle; }}
    .skills-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; }}
    .skill-card, .portfolio-card, .contact-card {{
      background: var(--surface);
      border: 1px solid rgba(212,168,83,.14);
      border-radius: 20px;
      padding: 22px;
      transition: transform .28s ease, border-color .28s ease, box-shadow .28s ease;
    }}
    .skill-card:hover, .portfolio-card:hover, .contact-card:hover {{ transform: translateY(-5px); border-color: var(--gold); box-shadow: 0 0 30px rgba(212,168,83,.13); }}
    .icon-box {{ width: 44px; height: 44px; display: grid; place-items: center; border-radius: 13px; background: rgba(212,168,83,.12); margin-bottom: 16px; }}
    .skill-card h3 {{ color: var(--gold); font-family: 'Bebas Neue', cursive; font-size: 23px; letter-spacing: 1px; margin: 0 0 14px; }}
    .skill-card ul, .timeline ul {{ margin: 0; padding-left: 18px; }}
    .skill-card li {{ color: rgba(245,245,245,.62); line-height: 1.9; font-size: 14px; }}
    .portfolio-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }}
    .portfolio-card {{ padding: 0; overflow: hidden; }}
    .thumb {{ height: 175px; position: relative; display: grid; place-items: center; background: linear-gradient(135deg, #21180e, #0d0d0d); }}
    .video-thumb {{ background: #050505; overflow: hidden; }}
    .portfolio-video {{ width: 100%; height: 100%; object-fit: cover; display: block; background: #000; }}
    .featured-video-card .card-body h3::after {{ content: "  • Video Added"; color: var(--gold); font-size: 11px; letter-spacing: .8px; text-transform: uppercase; }}
    .portfolio-card:nth-child(2) .thumb {{ background: linear-gradient(135deg, #10151f, #0d0d0d); }}
    .portfolio-card:nth-child(3) .thumb {{ background: linear-gradient(135deg, #1d1018, #0d0d0d); }}
    .portfolio-card:nth-child(4) .thumb {{ background: linear-gradient(135deg, #1b1a0d, #0d0d0d); }}
    .portfolio-card:nth-child(5) .thumb {{ background: linear-gradient(135deg, #0d181d, #0d0d0d); }}
    .portfolio-card:nth-child(6) .thumb {{ background: linear-gradient(135deg, #1d120d, #0d0d0d); }}
    .play-icon {{ color: var(--gold); width: 58px; height: 58px; border-radius: 50%; display: grid; place-items: center; border: 1px solid rgba(212,168,83,.32); background: rgba(0,0,0,.25); opacity: .88; }}
    .duration {{ position: absolute; bottom: 11px; right: 12px; color: var(--gold); background: rgba(0,0,0,.72); border-radius: 8px; padding: 5px 8px; font-size: 12px; }}
    .card-body {{ padding: 18px; }}
    .card-body h3 {{ margin: 0 0 7px; font-size: 16px; }}
    .card-body p {{ margin: 0; color: rgba(245,245,245,.44); font-size: 13px; }}
    .contact-panel {{ max-width: 800px; }}
    .contact-subtitle {{ text-align: center; color: rgba(245,245,245,.52); margin-top: -36px; margin-bottom: 36px; }}
    .contact-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }}
    .contact-card {{ text-decoration: none; color: rgba(245,245,245,.68); text-align: center; min-height: 110px; display: grid; place-items: center; gap: 8px; }}
    .contact-card b {{ color: var(--gold); font-size: 24px; }}
    .location {{ text-align: center; color: rgba(245,245,245,.52); margin-top: 24px; }}
    .footer {{ border-top: 1px solid rgba(212,168,83,.12); padding: 28px; }}
    .footer-inner {{ width: min(1080px, 100%); margin: 0 auto; display: flex; justify-content: space-between; align-items: center; gap: 16px; color: rgba(245,245,245,.34); font-size: 13px; }}
    .footer-logo {{ font-family: 'Bebas Neue', cursive; color: var(--gold); font-size: 25px; letter-spacing: 1px; }}
    .footer-logo span {{ color: var(--text); }}
    .reveal {{ opacity: 0; transform: translateY(26px); transition: opacity .7s ease, transform .7s ease; }}
    .reveal.visible {{ opacity: 1; transform: translateY(0); }}

    @media (max-width: 900px) {{
      .nav-inner {{ align-items: flex-start; flex-direction: column; }}
      .nav-links {{ gap: 15px; justify-content: flex-start; }}
      .hero-grid, .about-grid {{ grid-template-columns: 1fr; text-align: center; }}
      .chips, .btn-row, .stats {{ justify-content: center; }}
      .skills-grid, .portfolio-grid, .contact-grid {{ grid-template-columns: 1fr; }}
      .hero {{ padding-top: 178px; }}
      .footer-inner {{ flex-direction: column; }}
    }}
  </style>
</head>
<body>
  <nav class="navbar">
    <div class="nav-inner">
      <button class="logo" onclick="scrollToSection('home')">SUMITH<span>PK</span></button>
      <div class="nav-links" aria-label="Portfolio navigation">
        <button class="nav-btn" onclick="scrollToSection('home')">Home</button>
        <button class="nav-btn" onclick="scrollToSection('about')">About</button>
        <button class="nav-btn" onclick="scrollToSection('experience')">Experience</button>
        <button class="nav-btn" onclick="scrollToSection('skills')">Skills</button>
        <button class="nav-btn" onclick="scrollToSection('portfolio')">Portfolio</button>
        <button class="nav-btn" onclick="scrollToSection('contact')">Contact</button>
      </div>
    </div>
  </nav>

  <main>
    <section id="home" class="hero">
      <div class="speed-line"></div><div class="speed-line"></div><div class="speed-line"></div>
      <div class="hero-grid">
        <div class="profile-wrap reveal">
          <div class="profile-ring"><div class="profile-inner">{profile_markup}</div></div>
          <div class="photo-label">Profile Photo</div>
        </div>
        <div class="reveal">
          <div class="eyebrow">Freelance Videographer/Video Editor</div>
          <h1>{html.escape(NAME)}</h1>
          <div class="chips">
            <span>Short-Form Content</span><span>YouTube Editing</span><span>Automotive Video</span><span>Motion Graphics</span>
          </div>
          <p class="tagline">Turning raw footage into cinematic, engaging, and platform-ready video content.</p>
          <div class="btn-row">
            <button class="btn btn-primary" onclick="scrollToSection('portfolio')">View Portfolio</button>
            <button class="btn btn-outline" onclick="scrollToSection('contact')">Contact Me</button>
          </div>
        </div>
      </div>
    </section>

    <div class="divider"></div>

    <section id="about" class="section">
      <div class="container">
        <div class="section-label reveal">Get to Know Me</div>
        <h2 class="section-title reveal">ABOUT <span>ME</span></h2>
        <div class="about-grid">
          <div class="reveal">
            <p class="bio">Sumith P Kotian is a creative and detail-oriented freelance video editor with a strong interest in short-form content, YouTube editing, promotional videos, reels, subtitles, motion graphics, automotive visuals, and social media storytelling. He turns raw footage into engaging, clean, and audience-focused videos using smooth transitions, proper pacing, color correction, audio syncing, and platform-ready exports.</p>
            <div class="stats">
              <div class="stat"><strong>3+</strong><span>Years Editing</span></div>
              <div class="stat"><strong>50+</strong><span>Projects Done</span></div>
              <div class="stat"><strong>100%</strong><span>Dedication</span></div>
            </div>
          </div>
          <div class="panel reveal">
            <h3>🎓 Dr. T.M.A. Pai Polytechnic</h3>
            <p class="meta">Diploma in Automobile Engineering · Manipal, Karnataka · 2023 – 2026</p>
            <p>His automobile engineering background gives him a unique edge in automotive video production by combining technical understanding of vehicles with cinematic storytelling.</p>
            <div class="note">⚡ Focus: cars, bikes, showroom visuals, cinematic shots, rolling shots, reels, shorts, promos, motion text, and luxury-style edits.</div>
          </div>
        </div>
      </div>
    </section>

    <div class="divider"></div>

    <section id="experience" class="section">
      <div class="container">
        <div class="section-label reveal">Work History</div>
        <h2 class="section-title reveal">EXPERI<span>ENCE</span></h2>
        <div class="timeline reveal">
          <div class="dot"></div>
          <div class="panel">
            <h3>Freelance Video Editor <span class="badge">Current</span></h3>
            <p class="meta">Independent Client Projects — Remote / India · 2023 – Present</p>
            <ul>
              <li>Edited short-form videos, Instagram Reels, YouTube Shorts, promotional clips, showroom visuals, real estate property videos, and event-style content.</li>
              <li>Created engaging edits with hooks, jump cuts, beat sync, captions, speed ramps, overlays, B-roll, and sound effects.</li>
              <li>Produced real estate video edits including property walkthroughs, cinematic tours, listing promos, and drone footage integration for agents and builders.</li>
              <li>Improved video flow through storytelling, clean pacing, trimming, audio balancing, color grading, and export optimization.</li>
              <li>Managed client requirements, feedback, revisions, and final delivery for platform-ready videos.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <div class="divider"></div>

    <section id="skills" class="section">
      <div class="container">
        <div class="section-label reveal">What I Use</div>
        <h2 class="section-title reveal">SK<span>ILLS</span></h2>
        <div class="skills-grid">
  <article class="skill-card reveal">
    <div class="icon-box">🎞️</div>
    <h3>Video Editing</h3>
    <ul>
      <li>Adobe Premiere Pro</li>
      <li>DaVinci Resolve</li>
      <li>CapCut</li>
      <li>VN Editor</li>
    </ul>
  </article>

  <article class="skill-card reveal">
    <div class="icon-box">✨</div>
    <h3>Motion & Design</h3>
    <ul>
      <li>After Effects</li>
      <li>Canva</li>
      <li>Photoshop</li>
      <li>Basic Animation</li>
    </ul>
  </article>

  <article class="skill-card reveal">
    <div class="icon-box">🎚️</div>
    <h3>Editing Skills</h3>
    <ul>
      <li>Color Grading</li>
      <li>Audio Syncing</li>
      <li>Beat Sync</li>
      <li>Transitions</li>
    </ul>
  </article>

  <article class="skill-card reveal">
    <div class="icon-box">🎥</div>
    <h3>Videography</h3>
    <ul>
      <li>Camera Handling</li>
      <li>Cinematic Shot Composition</li>
      <li>Lighting Setup</li>
      <li>Drone Footage</li>
    </ul>
  </article>

  <article class="skill-card reveal">
    <div class="icon-box">🤝</div>
    <h3>Soft Skills</h3>
    <ul>
      <li>Client Communication</li>
      <li>Deadline Management</li>
      <li>Storytelling</li>
      <li>Feedback Handling</li>
    </ul>
  </article>
</div>
      </div>
    </section>

    <div class="divider"></div>

    <section id="portfolio" class="section">
      <div class="container">
        <div class="section-label reveal">Selected Works</div>
        <h2 class="section-title reveal">PORT<span>FOLIO</span></h2>
        <div class="portfolio-grid">{portfolio_cards}</div>
      </div>
    </section>

    <div class="divider"></div>

    <section id="contact" class="section">
      <div class="container contact-panel">
        <div class="section-label reveal">Let's Work Together</div>
        <h2 class="section-title reveal">GET IN <span>TOUCH</span></h2>
        <p class="contact-subtitle reveal">Have a project in mind? Let's create something cinematic together.</p>
        <div class="panel reveal">
          <div class="contact-grid">
            <a class="contact-card" href="mailto:{html.escape(EMAIL)}" target="_blank"><b>✉</b>{html.escape(EMAIL)}</a>
            <a class="contact-card" href="tel:{html.escape(PHONE)}"><b>☎</b>{html.escape(PHONE)}</a>
            <a class="contact-card" href="{html.escape(LINKEDIN)}" target="_blank" rel="noopener"><b>in</b>LinkedIn</a>
          </div>
          <p class="location">📍 {html.escape(LOCATION)}</p>
          <div style="text-align:center;margin-top:22px;">
            <a class="btn btn-primary" style="display:inline-block;text-decoration:none;" href="mailto:{html.escape(EMAIL)}?subject=Video%20Editing%20Project%20Inquiry" target="_blank">Send Project Inquiry</a>
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="footer-inner">
      <div class="footer-logo">SUMITH<span>PK</span></div>
      <div>© 2026 {html.escape(NAME)}. All rights reserved.</div>
    </div>
  </footer>

  <script>
    function scrollToSection(id) {{
      const element = document.getElementById(id);
      if (!element) return;
      const top = element.getBoundingClientRect().top + window.pageYOffset - 76;
      window.scrollTo({{ top: top, behavior: 'smooth' }});
    }}

    const observer = new IntersectionObserver((entries) => {{
      entries.forEach((entry) => {{
        if (entry.isIntersecting) entry.target.classList.add('visible');
      }});
    }}, {{ threshold: 0.12 }});

    document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
  </script>
</body>
</html>
"""

components.html(html_doc, height=950, scrolling=True)
