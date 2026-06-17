from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

# ── NEWS DATA ──────────────────────────────────────────────
BREAKING_TICKER = [
    "Pakistan's economy grows 3.8% in Q2 amid reform momentum",
    "UN calls for immediate ceasefire as Gaza death toll surpasses 42,000",
    "Stock Exchange hits 87,000 points for the first time in history",
    "Monsoon rains forecast to arrive early this year, warns Met Department",
    "Global oil prices drop below $70 per barrel amid demand concerns",
]

HERO_MAIN = {
    "tag": "Breaking News",
    "title": "Pakistan Secures Historic $8 Billion IMF Bailout Package to Stabilise Economy",
    "author": "Ahmed Raza",
    "time": "14 mins ago",
    "img": "https://images.unsplash.com/photo-1521295121783-8a321d551ad2?w=900&q=80",
}

HERO_SIDE = [
    {
        "tag": "World",
        "title": "UN Emergency Meeting Called Over Escalating Middle East Tensions",
        "img": "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=500&q=80",
    },
    {
        "tag": "Business",
        "title": "PSX Crosses 87,000 Mark, Investors Celebrate Record High",
        "img": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=500&q=80",
    },
]

TOP_STORIES = [
    {
        "tag": "Pakistan",
        "title": "PM Chairs Emergency Cabinet Session on Flood Preparedness",
        "excerpt": "Senior ministers and provincial chief ministers attended the session as early monsoon warnings have been issued across the country.",
        "time": "2 hours ago",
        "read": "4 min read",
        "img": "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?w=400&q=80",
    },
    {
        "tag": "Technology",
        "title": "Apple Unveils AI-Powered iPhone 18 With Real-Time Translation",
        "excerpt": "The new flagship device introduces on-device large language models, marking a major leap in mobile artificial intelligence.",
        "time": "4 hours ago",
        "read": "3 min read",
        "img": "https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=400&q=80",
    },
    {
        "tag": "Sports",
        "title": "Pakistan Cricket Team Announced for England Tour — Stars Return",
        "excerpt": "The PCB confirmed the 17-man squad, with surprise recalls for three experienced batters who were dropped last season.",
        "time": "6 hours ago",
        "read": "5 min read",
        "img": "https://images.unsplash.com/photo-1574169208507-84376144848b?w=400&q=80",
    },
    {
        "tag": "Health",
        "title": "WHO Warns of Rising Dengue Cases Across South Asia This Summer",
        "excerpt": "Health authorities in Pakistan, India, and Bangladesh are ramping up mosquito control programmes ahead of peak season.",
        "time": "8 hours ago",
        "read": "3 min read",
        "img": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=400&q=80",
    },
]

LATEST_NEWS = [
    {
        "tag": "Politics",
        "title": "Opposition Leaders Demand Immediate Snap Elections as Protests Spread to 12 Cities",
        "date": "June 17, 2026",
        "read": "6 min read",
        "img": "https://images.unsplash.com/photo-1523906834658-6e24ef2386f9?w=300&q=80",
    },
    {
        "tag": "Business",
        "title": "Rupee Strengthens to 275 Against Dollar Following IMF Loan Tranche Release",
        "date": "June 17, 2026",
        "read": "4 min read",
        "img": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=300&q=80",
    },
    {
        "tag": "Technology",
        "title": "Pakistan Launches First Domestically Developed Satellite in Partnership With Space Agency",
        "date": "June 17, 2026",
        "read": "5 min read",
        "img": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=300&q=80",
    },
    {
        "tag": "Entertainment",
        "title": "Lollywood Blockbuster Crosses Rs 1 Billion at Box Office in Opening Weekend",
        "date": "June 16, 2026",
        "read": "3 min read",
        "img": "https://images.unsplash.com/photo-1444628838545-ac4016a5418a?w=300&q=80",
    },
    {
        "tag": "Health",
        "title": "Government Unveils Rs 50 Billion Universal Healthcare Coverage Plan for Low-Income Families",
        "date": "June 16, 2026",
        "read": "4 min read",
        "img": "https://images.unsplash.com/photo-1434682772747-f16d3ea162c3?w=300&q=80",
    },
]

TRENDING = [
    "IMF Deal Brings Immediate Relief to Pakistani Rupee",
    "Pakistan vs England Test Series — Full Schedule Revealed",
    "Karachi Braces for Severe Heatwave as Temperatures Hit 48°C",
    "WhatsApp Introduces Major Privacy Update Across All Platforms",
    "Gold Prices Fall Rs 2,000 Per Tola in Local Markets",
]

VIDEOS = [
    {
        "tag": "Analysis",
        "title": "What the IMF Deal Means for Pakistan's Future — Expert Breakdown",
        "views": "12,400",
        "time": "3 hours ago",
        "duration": "4:27",
        "img": "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=500&q=80",
    },
    {
        "tag": "Tech",
        "title": "iPhone 18 Hands-On: Is the AI Upgrade Actually Useful?",
        "views": "8,900",
        "time": "5 hours ago",
        "duration": "7:14",
        "img": "https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=500&q=80",
    },
    {
        "tag": "Sports",
        "title": "Pakistan Cricket Squad for England Tour — Reactions & Analysis",
        "views": "22,100",
        "time": "6 hours ago",
        "duration": "2:58",
        "img": "https://images.unsplash.com/photo-1574169208507-84376144848b?w=500&q=80",
    },
]

OPINIONS = [
    {
        "name": "Dr. Farhan Malik",
        "title": "Senior Economic Analyst",
        "avatar": "https://randomuser.me/api/portraits/men/32.jpg",
        "heading": "Pakistan's IMF Dependency: A Cycle We Must Break for Good",
        "excerpt": "Repeated bailouts without structural reform only delay the inevitable. Here's what genuine fiscal independence looks like and why the political will is finally emerging.",
    },
    {
        "name": "Sana Iqbal",
        "title": "Foreign Policy Commentator",
        "avatar": "https://randomuser.me/api/portraits/women/44.jpg",
        "heading": "How Pakistan Can Rebalance Its Geopolitical Position Between East and West",
        "excerpt": "A new foreign policy doctrine is emerging in Islamabad — one that refuses to choose between Washington and Beijing and instead plays both to its advantage.",
    },
    {
        "name": "Zubair Ahmed",
        "title": "Technology Correspondent",
        "avatar": "https://randomuser.me/api/portraits/men/67.jpg",
        "heading": "The Digital Divide Is Pakistan's Biggest Obstacle to Becoming a Tech Hub",
        "excerpt": "With only 38% internet penetration in rural areas, ambitious IT export targets are meaningless without investing first in grassroots digital literacy.",
    },
]

NAV_LINKS = ["Home", "Pakistan", "World", "Politics", "Business", "Sports", "Technology", "Entertainment", "Health", "Opinion", "Videos"]

# ── HTML TEMPLATE ──────────────────────────────────────────
HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>TrueVista News – Stay Informed. Stay Ahead.</title>
  <link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Inter:wght@300;400;500;600;700&family=Oswald:wght@500;600;700&display=swap" rel="stylesheet"/>
  <style>
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
    :root{--red:#CC0000;--red-dark:#990000;--black:#0D0D0D;--charcoal:#1A1A1A;--mid:#2E2E2E;--steel:#4A4A4A;--muted:#888;--silver:#C8C8C8;--offwhite:#F5F5F0;--white:#FFFFFF}
    html{scroll-behavior:smooth}
    body{font-family:'Inter',sans-serif;background:var(--offwhite);color:var(--black)}
    .ticker-wrap{background:var(--red);color:var(--white);display:flex;align-items:center;overflow:hidden;height:36px;font-size:13px;font-weight:600;letter-spacing:.03em}
    .ticker-label{background:var(--black);padding:0 16px;height:100%;display:flex;align-items:center;flex-shrink:0;text-transform:uppercase;letter-spacing:.08em;font-size:11px}
    .ticker-track{flex:1;overflow:hidden}
    .ticker-inner{display:flex;white-space:nowrap;animation:tickerScroll 40s linear infinite}
    .ticker-inner span{padding:0 40px}
    @keyframes tickerScroll{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
    header{background:var(--black);padding:0 24px;display:flex;align-items:center;justify-content:space-between;height:72px;position:sticky;top:0;z-index:1000;border-bottom:3px solid var(--red)}
    .logo{display:flex;align-items:center;gap:10px;text-decoration:none}
    .logo-badge{background:var(--red);color:var(--white);font-family:'Oswald',sans-serif;font-size:22px;font-weight:700;padding:4px 10px;letter-spacing:.04em}
    .logo-text{font-family:'Oswald',sans-serif;font-size:26px;font-weight:700;color:var(--white);letter-spacing:.06em}
    .logo-text span{color:var(--red)}
    .header-right{display:flex;align-items:center;gap:20px}
    .header-date{color:var(--silver);font-size:12px}
    .header-live{display:flex;align-items:center;gap:6px;background:var(--red);color:var(--white);font-size:11px;font-weight:700;padding:5px 12px;text-transform:uppercase;letter-spacing:.08em}
    .live-dot{width:7px;height:7px;background:var(--white);border-radius:50%;animation:pulse 1.2s ease-in-out infinite}
    @keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}
    nav{background:var(--charcoal);border-bottom:1px solid #333;overflow-x:auto}
    .nav-inner{display:flex;align-items:center;max-width:1280px;margin:0 auto;padding:0 24px}
    nav a{color:var(--silver);text-decoration:none;font-family:'Oswald',sans-serif;font-size:13px;font-weight:500;letter-spacing:.06em;text-transform:uppercase;padding:13px 16px;display:block;white-space:nowrap;border-bottom:3px solid transparent;transition:color .2s,border-color .2s}
    nav a:hover,nav a.active{color:var(--white);border-bottom-color:var(--red)}
    .container{max-width:1280px;margin:0 auto;padding:0 24px}
    .section{padding:32px 0}
    .section-head{display:flex;align-items:center;gap:12px;margin-bottom:20px;padding-bottom:10px;border-bottom:2px solid var(--silver)}
    .section-head h2{font-family:'Oswald',sans-serif;font-size:20px;font-weight:700;letter-spacing:.05em;text-transform:uppercase}
    .section-head .bar{width:4px;height:22px;background:var(--red);flex-shrink:0}
    .section-head a.see-all{margin-left:auto;font-size:12px;font-weight:600;color:var(--red);text-decoration:none;text-transform:uppercase;letter-spacing:.04em}
    .hero{background:var(--black);padding:28px 0}
    .hero-grid{display:grid;grid-template-columns:1fr 340px;grid-template-rows:auto auto;gap:2px}
    .hero-main{position:relative;overflow:hidden;grid-row:1/3;cursor:pointer}
    .hero-main img,.hero-side img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .4s ease}
    .hero-main:hover img{transform:scale(1.03)}
    .hero-main-img-wrap{height:420px;overflow:hidden}
    .hero-overlay{position:absolute;bottom:0;left:0;right:0;background:linear-gradient(transparent,rgba(0,0,0,.88) 60%);padding:32px 24px 24px}
    .hero-tag{background:var(--red);color:var(--white);font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:3px 8px;display:inline-block;margin-bottom:8px}
    .hero-main h1{font-family:'Merriweather',serif;font-size:26px;font-weight:900;color:var(--white);line-height:1.3;margin-bottom:8px}
    .hero-meta{color:var(--silver);font-size:12px}
    .hero-side{display:flex;flex-direction:column;gap:2px}
    .hero-side-item{position:relative;overflow:hidden;cursor:pointer;height:209px}
    .hero-side-item:hover img{transform:scale(1.04)}
    .side-overlay{position:absolute;bottom:0;left:0;right:0;background:linear-gradient(transparent,rgba(0,0,0,.85));padding:20px 14px 14px}
    .side-tag{background:var(--red);color:var(--white);font-size:9px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:2px 6px;display:inline-block;margin-bottom:5px}
    .hero-side-item h3{font-family:'Merriweather',serif;font-size:14px;font-weight:700;color:var(--white);line-height:1.4}
    .top-stories-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
    .story-card{background:var(--white);border:1px solid #E0E0E0;overflow:hidden;cursor:pointer;transition:box-shadow .2s}
    .story-card:hover{box-shadow:0 4px 20px rgba(0,0,0,.12)}
    .story-card img{width:100%;height:180px;object-fit:cover;display:block}
    .story-card-body{padding:14px}
    .story-tag{font-size:10px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--red);margin-bottom:6px}
    .story-card h3{font-family:'Merriweather',serif;font-size:15px;font-weight:700;line-height:1.45;color:var(--black);margin-bottom:8px}
    .story-card p{font-size:13px;color:var(--steel);line-height:1.6;margin-bottom:10px}
    .story-meta{font-size:11px;color:var(--muted);font-weight:500}
    .content-wrap{display:grid;grid-template-columns:1fr 320px;gap:32px;align-items:start}
    .list-card{display:flex;gap:14px;padding:14px 0;border-bottom:1px solid #E8E8E8;cursor:pointer}
    .list-card:last-child{border-bottom:none}
    .list-card img{width:110px;height:78px;object-fit:cover;flex-shrink:0}
    .list-card h4{font-family:'Merriweather',serif;font-size:14px;font-weight:700;line-height:1.45;color:var(--black);margin-bottom:4px;transition:color .15s}
    .list-card:hover h4{color:var(--red)}
    .list-card-meta{font-size:11px;color:var(--muted)}
    .featured-large{background:var(--white);border:1px solid #E0E0E0;overflow:hidden;cursor:pointer;margin-bottom:24px}
    .featured-large img{width:100%;height:260px;object-fit:cover;display:block}
    .featured-large-body{padding:18px}
    .featured-large h2{font-family:'Merriweather',serif;font-size:20px;font-weight:900;line-height:1.4;margin-bottom:10px}
    .featured-large p{font-size:14px;color:var(--steel);line-height:1.7;margin-bottom:12px}
    .read-more{font-size:12px;font-weight:700;color:var(--red);text-transform:uppercase;letter-spacing:.06em;text-decoration:none}
    .sidebar-widget{background:var(--white);border:1px solid #E0E0E0;margin-bottom:24px;overflow:hidden}
    .widget-head{background:var(--black);padding:10px 16px;display:flex;align-items:center;gap:8px}
    .widget-head h3{font-family:'Oswald',sans-serif;font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--white)}
    .widget-head .wbar{width:3px;height:16px;background:var(--red)}
    .widget-body{padding:14px 16px}
    .trending-item{display:flex;align-items:flex-start;gap:10px;padding:10px 0;border-bottom:1px solid #F0F0F0;cursor:pointer}
    .trending-item:last-child{border-bottom:none}
    .trend-num{font-family:'Oswald',sans-serif;font-size:22px;font-weight:700;color:#E0E0E0;line-height:1;flex-shrink:0;width:24px}
    .trending-item h4{font-family:'Merriweather',serif;font-size:13px;font-weight:700;line-height:1.45}
    .trending-item:hover h4{color:var(--red)}
    .weather-main{display:flex;align-items:center;gap:16px;padding-bottom:12px;border-bottom:1px solid #F0F0F0;margin-bottom:12px}
    .weather-icon{font-size:48px}
    .weather-temp{font-family:'Oswald',sans-serif;font-size:42px;font-weight:700}
    .weather-city{font-size:13px;color:var(--steel);font-weight:600}
    .weather-desc{font-size:12px;color:var(--muted)}
    .weather-row{display:flex;justify-content:space-between;font-size:12px;color:var(--steel);padding:4px 0}
    .weather-row span:last-child{font-weight:600}
    .video-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
    .video-card{background:var(--white);border:1px solid #E0E0E0;overflow:hidden;cursor:pointer}
    .video-thumb{position:relative;height:170px;overflow:hidden;background:var(--black)}
    .video-thumb img{width:100%;height:100%;object-fit:cover;opacity:.85}
    .play-btn{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:48px;height:48px;background:rgba(204,0,0,.9);border-radius:50%;display:flex;align-items:center;justify-content:center}
    .play-btn::after{content:'';border-left:16px solid white;border-top:10px solid transparent;border-bottom:10px solid transparent;margin-left:4px}
    .video-dur{position:absolute;bottom:8px;right:8px;background:rgba(0,0,0,.75);color:var(--white);font-size:11px;font-weight:600;padding:2px 6px}
    .video-body{padding:12px}
    .video-body h4{font-family:'Merriweather',serif;font-size:14px;font-weight:700;line-height:1.45;color:var(--black);margin-bottom:6px}
    .opinion-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
    .opinion-card{background:var(--white);border:1px solid #E0E0E0;padding:20px}
    .opinion-author{display:flex;align-items:center;gap:10px;margin-bottom:12px}
    .author-avatar{width:48px;height:48px;border-radius:50%;object-fit:cover}
    .author-name{font-size:14px;font-weight:700}
    .author-title{font-size:11px;color:var(--muted)}
    .opinion-card h4{font-family:'Merriweather',serif;font-size:15px;font-weight:700;line-height:1.5;margin-bottom:8px}
    .opinion-card p{font-size:13px;color:var(--steel);line-height:1.65;margin-bottom:12px}
    .subscribe-banner{background:linear-gradient(135deg,var(--black) 60%,var(--red-dark));padding:48px 32px;text-align:center;margin:32px 0}
    .subscribe-banner h2{font-family:'Oswald',sans-serif;font-size:32px;font-weight:700;color:var(--white);letter-spacing:.04em;margin-bottom:10px}
    .subscribe-banner p{color:var(--silver);font-size:15px;margin-bottom:24px}
    .sub-form{display:flex;justify-content:center;gap:0;max-width:480px;margin:0 auto}
    .sub-form input{flex:1;padding:13px 18px;font-size:14px;border:none;outline:none}
    .sub-form button{background:var(--red);color:var(--white);border:none;padding:13px 24px;font-family:'Oswald',sans-serif;font-size:14px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;cursor:pointer}
    footer{background:var(--black);color:var(--silver);padding:40px 0 0}
    .footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:32px;padding-bottom:32px;border-bottom:1px solid #2A2A2A}
    .footer-brand h3{font-family:'Oswald',sans-serif;font-size:22px;font-weight:700;color:var(--white);letter-spacing:.05em;margin-bottom:12px}
    .footer-brand h3 span{color:var(--red)}
    .footer-brand p{font-size:13px;line-height:1.7;color:var(--muted);margin-bottom:16px}
    .social-row{display:flex;gap:10px}
    .social-btn{width:34px;height:34px;background:#222;border:1px solid #333;display:flex;align-items:center;justify-content:center;color:var(--silver);font-size:13px;font-weight:700;cursor:pointer;transition:background .2s,color .2s}
    .social-btn:hover{background:var(--red);color:var(--white);border-color:var(--red)}
    .footer-col h4{font-family:'Oswald',sans-serif;font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--white);margin-bottom:14px;padding-bottom:8px;border-bottom:2px solid var(--red);display:inline-block}
    .footer-col ul{list-style:none}
    .footer-col ul li{margin-bottom:8px}
    .footer-col ul li a{color:var(--muted);text-decoration:none;font-size:13px;transition:color .15s}
    .footer-col ul li a:hover{color:var(--red)}
    .footer-bottom{padding:16px 0;display:flex;justify-content:space-between;align-items:center;font-size:12px;color:var(--muted)}
    .footer-bottom a{color:var(--muted);text-decoration:none}
    .footer-bottom a:hover{color:var(--white)}
    @media(max-width:1024px){.hero-grid{grid-template-columns:1fr}.hero-side{flex-direction:row}.hero-side-item{height:180px;flex:1}.top-stories-grid{grid-template-columns:repeat(2,1fr)}.content-wrap{grid-template-columns:1fr}.footer-grid{grid-template-columns:1fr 1fr}.video-grid{grid-template-columns:repeat(2,1fr)}.opinion-grid{grid-template-columns:1fr 1fr}}
    @media(max-width:640px){.top-stories-grid{grid-template-columns:1fr}.video-grid{grid-template-columns:1fr}.opinion-grid{grid-template-columns:1fr}.footer-grid{grid-template-columns:1fr}.hero-side{flex-direction:column}.sub-form{flex-direction:column}}
  </style>
</head>
<body>

<!-- TICKER -->
<div class="ticker-wrap">
  <div class="ticker-label">🔴 Breaking</div>
  <div class="ticker-track">
    <div class="ticker-inner">
      {% for item in ticker %}
        <span>{{ item }}</span><span>•</span>
      {% endfor %}
      {% for item in ticker %}
        <span>{{ item }}</span><span>•</span>
      {% endfor %}
    </div>
  </div>
</div>

<!-- HEADER -->
<header>
  <a class="logo" href="/">
    <span class="logo-badge">TV</span>
    <span class="logo-text">TrueVista <span>News</span></span>
  </a>
  <div class="header-right">
    <span class="header-date">{{ date }}</span>
    <div class="header-live"><div class="live-dot"></div> Live</div>
  </div>
</header>

<!-- NAV -->
<nav>
  <div class="nav-inner">
    {% for link in nav_links %}
    <a href="#" {% if loop.first %}class="active"{% endif %}>{{ link }}</a>
    {% endfor %}
  </div>
</nav>

<!-- HERO -->
<div class="hero">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-main">
        <div class="hero-main-img-wrap">
          <img src="{{ hero_main.img }}" alt="Main Story"/>
        </div>
        <div class="hero-overlay">
          <span class="hero-tag">{{ hero_main.tag }}</span>
          <h1>{{ hero_main.title }}</h1>
          <div class="hero-meta">By <strong>{{ hero_main.author }}</strong> &nbsp;|&nbsp; {{ date }} &nbsp;|&nbsp; {{ hero_main.time }}</div>
        </div>
      </div>
      <div class="hero-side">
        {% for s in hero_side %}
        <div class="hero-side-item">
          <img src="{{ s.img }}" alt=""/>
          <div class="side-overlay">
            <span class="side-tag">{{ s.tag }}</span>
            <h3>{{ s.title }}</h3>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
  </div>
</div>

<!-- TOP STORIES -->
<div class="container section">
  <div class="section-head">
    <div class="bar"></div>
    <h2>Top Stories</h2>
    <a class="see-all" href="#">See All →</a>
  </div>
  <div class="top-stories-grid">
    {% for s in top_stories %}
    <div class="story-card">
      <img src="{{ s.img }}" alt=""/>
      <div class="story-card-body">
        <div class="story-tag">{{ s.tag }}</div>
        <h3>{{ s.title }}</h3>
        <p>{{ s.excerpt }}</p>
        <div class="story-meta">{{ s.time }} &nbsp;·&nbsp; {{ s.read }}</div>
      </div>
    </div>
    {% endfor %}
  </div>
</div>

<!-- MAIN + SIDEBAR -->
<div class="container section" style="padding-top:0">
  <div class="content-wrap">
    <div>
      <div class="section-head"><div class="bar"></div><h2>Latest News</h2></div>
      <div class="featured-large">
        <img src="https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=800&q=80" alt=""/>
        <div class="featured-large-body">
          <div class="story-tag">World Affairs</div>
          <h2>G20 Summit Concludes With Landmark Agreement on Climate Finance for Developing Nations</h2>
          <p>World leaders signed a binding commitment to channel $500 billion annually toward green energy transitions in vulnerable economies — the most consequential climate deal since Paris 2015.</p>
          <a class="read-more" href="#">Read Full Story →</a>
        </div>
      </div>
      {% for n in latest_news %}
      <div class="list-card">
        <img src="{{ n.img }}" alt=""/>
        <div class="list-card-body">
          <div class="story-tag">{{ n.tag }}</div>
          <h4>{{ n.title }}</h4>
          <div class="list-card-meta">{{ n.date }} &nbsp;·&nbsp; {{ n.read }}</div>
        </div>
      </div>
      {% endfor %}
    </div>
    <aside>
      <!-- Trending -->
      <div class="sidebar-widget">
        <div class="widget-head"><div class="wbar"></div><h3>Trending Now</h3></div>
        <div class="widget-body">
          {% for i, t in trending %}
          <div class="trending-item">
            <span class="trend-num">0{{ i }}</span>
            <h4>{{ t }}</h4>
          </div>
          {% endfor %}
        </div>
      </div>
      <!-- Weather -->
      <div class="sidebar-widget">
        <div class="widget-head"><div class="wbar"></div><h3>Weather — Islamabad</h3></div>
        <div class="widget-body">
          <div class="weather-main">
            <span class="weather-icon">⛅</span>
            <div>
              <div class="weather-temp">34°C</div>
              <div class="weather-city">Islamabad, Pakistan</div>
              <div class="weather-desc">Partly Cloudy &nbsp;·&nbsp; Wednesday</div>
            </div>
          </div>
          <div class="weather-row"><span>Humidity</span><span>62%</span></div>
          <div class="weather-row"><span>Wind</span><span>18 km/h NW</span></div>
          <div class="weather-row"><span>UV Index</span><span>High (8)</span></div>
          <div class="weather-row"><span>Sunrise / Sunset</span><span>5:18 AM / 7:41 PM</span></div>
        </div>
      </div>
    </aside>
  </div>
</div>

<!-- VIDEOS -->
<div style="background:var(--charcoal);padding:32px 0">
  <div class="container">
    <div class="section-head" style="border-color:#444">
      <div class="bar"></div>
      <h2 style="color:var(--white)">Latest Videos</h2>
      <a class="see-all" href="#">See All →</a>
    </div>
    <div class="video-grid">
      {% for v in videos %}
      <div class="video-card">
        <div class="video-thumb">
          <img src="{{ v.img }}" alt=""/>
          <div class="play-btn"></div>
          <div class="video-dur">{{ v.duration }}</div>
        </div>
        <div class="video-body">
          <div class="story-tag">{{ v.tag }}</div>
          <h4>{{ v.title }}</h4>
          <div class="story-meta">{{ v.views }} views &nbsp;·&nbsp; {{ v.time }}</div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</div>

<!-- OPINION -->
<div class="container section">
  <div class="section-head"><div class="bar"></div><h2>Opinion & Analysis</h2><a class="see-all" href="#">See All →</a></div>
  <div class="opinion-grid">
    {% for o in opinions %}
    <div class="opinion-card">
      <div class="opinion-author">
        <img class="author-avatar" src="{{ o.avatar }}" alt=""/>
        <div><div class="author-name">{{ o.name }}</div><div class="author-title">{{ o.title }}</div></div>
      </div>
      <h4>{{ o.heading }}</h4>
      <p>{{ o.excerpt }}</p>
      <a class="read-more" href="#">Read More →</a>
    </div>
    {% endfor %}
  </div>
</div>

<!-- SUBSCRIBE -->
<div class="container">
  <div class="subscribe-banner">
    <h2>Stay Informed. Stay Ahead.</h2>
    <p>Subscribe to TrueVista News and get breaking stories delivered to your inbox every morning.</p>
    <div class="sub-form">
      <input type="email" placeholder="Enter your email address…"/>
      <button>Subscribe Free</button>
    </div>
  </div>
</div>

<!-- FOOTER -->
<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <h3>TrueVista <span>News</span></h3>
        <p>Your trusted source for breaking news, global affairs, politics, business, technology, and in-depth analysis. Accurate. Unbiased. Timely.</p>
        <div class="social-row">
          <div class="social-btn">f</div>
          <div class="social-btn">𝕏</div>
          <div class="social-btn">in</div>
          <div class="social-btn">▶</div>
        </div>
      </div>
      <div class="footer-col">
        <h4>Sections</h4>
        <ul>
          {% for link in nav_links[1:] %}
          <li><a href="#">{{ link }}</a></li>
          {% endfor %}
        </ul>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <ul>
          <li><a href="#">About Us</a></li>
          <li><a href="#">Our Team</a></li>
          <li><a href="#">Advertise</a></li>
          <li><a href="#">Careers</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Follow Live</h4>
        <ul>
          <li><a href="#">YouTube Channel</a></li>
          <li><a href="#">TrueVista Live TV</a></li>
          <li><a href="#">Podcasts</a></li>
          <li><a href="#">Newsletter</a></li>
          <li><a href="#">RSS Feed</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© {{ year }} TrueVista News. All rights reserved.</span>
      <div style="display:flex;gap:20px">
        <a href="#">Privacy Policy</a>
        <a href="#">Terms of Use</a>
      </div>
    </div>
  </div>
</footer>
</body>
</html>"""


@app.route("/")
def home():
    now = datetime.now()
    return render_template_string(
        HTML,
        ticker=BREAKING_TICKER,
        hero_main=HERO_MAIN,
        hero_side=HERO_SIDE,
        top_stories=TOP_STORIES,
        latest_news=LATEST_NEWS,
        trending=list(enumerate(TRENDING, 1)),
        videos=VIDEOS,
        opinions=OPINIONS,
        nav_links=NAV_LINKS,
        date=now.strftime("%A, %B %d, %Y"),
        year=now.year,
    )


if __name__ == "__main__":
    app.run(debug=True)
