---
layout: default
title: Car Damage Classifier
---

<style>
:root {
  --page-bg: #070b14;
  --page-bg-2: #0b1020;
  --panel: rgba(16, 24, 44, 0.78);
  --panel-strong: rgba(20, 31, 57, 0.92);
  --panel-soft: rgba(255, 255, 255, 0.055);
  --line: rgba(148, 163, 184, 0.18);
  --line-strong: rgba(125, 211, 252, 0.34);
  --text: rgba(248, 250, 252, 0.96);
  --muted: rgba(203, 213, 225, 0.74);
  --subtle: rgba(148, 163, 184, 0.86);
  --blue: #38bdf8;
  --blue-strong: #2563eb;
  --violet: #8b5cf6;
  --violet-strong: #6d28d9;
  --green: #22c55e;
  --amber: #f59e0b;
  --shadow: 0 28px 90px rgba(0, 0, 0, 0.42);
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  color: var(--text);
  background:
    radial-gradient(900px 520px at 10% -10%, rgba(37, 99, 235, 0.38), transparent 62%),
    radial-gradient(780px 520px at 92% 2%, rgba(139, 92, 246, 0.3), transparent 58%),
    linear-gradient(180deg, var(--page-bg), var(--page-bg-2) 45%, #060912);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

body::before {
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  opacity: 0.32;
  background-image:
    linear-gradient(rgba(148, 163, 184, 0.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(148, 163, 184, 0.06) 1px, transparent 1px);
  background-size: 56px 56px;
  mask-image: linear-gradient(to bottom, black, transparent 78%);
}

.page-header,
.site-footer {
  display: none;
}

.main-content {
  max-width: none;
  margin: 0;
  padding: 0;
}

.cd-page {
  min-height: 100vh;
}

.cd-wrap {
  width: min(1180px, calc(100% - 40px));
  margin: 0 auto;
}

.cd-nav {
  position: sticky;
  top: 0;
  z-index: 20;
  border-bottom: 1px solid var(--line);
  background: rgba(7, 11, 20, 0.78);
  backdrop-filter: blur(18px);
}

.cd-nav-inner {
  min-height: 74px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 22px;
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  color: var(--text);
  text-decoration: none;
}

.brand-mark {
  width: 42px;
  height: 42px;
  display: grid;
  place-items: center;
  border: 1px solid rgba(56, 189, 248, 0.42);
  border-radius: 14px;
  background:
    linear-gradient(135deg, rgba(56, 189, 248, 0.24), rgba(139, 92, 246, 0.24)),
    rgba(255, 255, 255, 0.05);
  box-shadow: 0 0 34px rgba(56, 189, 248, 0.16);
  font-weight: 900;
  letter-spacing: -0.04em;
}

.brand-title {
  display: block;
  font-size: 13px;
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: 0.08em;
}

.brand-subtitle {
  display: block;
  margin-top: 4px;
  color: var(--subtle);
  font-size: 11px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 4px;
}

.nav-links a {
  color: var(--muted);
  border: 0;
  border-radius: 999px;
  padding: 9px 12px;
  font-size: 13px;
  font-weight: 650;
  text-decoration: none;
}

.nav-links a:hover {
  color: var(--text);
  background: rgba(255, 255, 255, 0.07);
}

.nav-cta {
  color: white !important;
  background: linear-gradient(135deg, var(--blue-strong), var(--violet-strong));
  box-shadow: 0 14px 36px rgba(37, 99, 235, 0.28);
}

.hero {
  position: relative;
  padding: 86px 0 42px;
}

.hero-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.02fr) minmax(420px, 0.98fr);
  gap: 52px;
  align-items: center;
}

.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  width: fit-content;
  margin: 0 0 22px;
  padding: 8px 13px;
  border: 1px solid var(--line-strong);
  border-radius: 999px;
  color: #dbeafe;
  background: rgba(37, 99, 235, 0.16);
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 0.13em;
  text-transform: uppercase;
}

.pulse {
  width: 8px;
  height: 8px;
  border-radius: 999px;
  background: var(--green);
  box-shadow: 0 0 0 8px rgba(34, 197, 94, 0.12);
}

.hero h1 {
  margin: 0;
  color: white;
  font-size: clamp(46px, 7vw, 86px);
  line-height: 0.92;
  letter-spacing: -0.075em;
}

.hero h1 span {
  display: block;
  color: transparent;
  background: linear-gradient(90deg, var(--blue), #c4b5fd 56%, var(--violet));
  -webkit-background-clip: text;
  background-clip: text;
}

.hero-lede {
  max-width: 680px;
  margin: 26px 0 0;
  color: rgba(226, 232, 240, 0.86);
  font-size: 20px;
  line-height: 1.65;
}

.hero-copy {
  max-width: 680px;
  margin: 18px 0 0;
  color: var(--muted);
  font-size: 15.5px;
  line-height: 1.75;
}

.hero-copy strong,
.panel strong,
.result-note strong {
  color: white;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 30px;
}

.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 46px;
  padding: 0 18px;
  border: 1px solid var(--line);
  border-radius: 14px;
  color: white;
  background: rgba(255, 255, 255, 0.06);
  text-decoration: none;
  font-size: 14px;
  font-weight: 800;
}

.button:hover {
  transform: translateY(-1px);
  border-color: rgba(56, 189, 248, 0.5);
  background: rgba(56, 189, 248, 0.1);
}

.button.primary {
  border-color: transparent;
  background: linear-gradient(135deg, var(--blue-strong), var(--violet-strong));
  box-shadow: 0 18px 44px rgba(37, 99, 235, 0.35);
}

.button.primary:hover {
  background: linear-gradient(135deg, #1d4ed8, #7c3aed);
}

.hero-visual {
  position: relative;
  padding: 18px;
  border: 1px solid var(--line);
  border-radius: 30px;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.035)),
    rgba(15, 23, 42, 0.74);
  box-shadow: var(--shadow);
}

.hero-visual::before {
  content: "";
  position: absolute;
  inset: -1px;
  z-index: -1;
  border-radius: 30px;
  background: linear-gradient(135deg, rgba(56, 189, 248, 0.48), transparent 34%, rgba(139, 92, 246, 0.52));
  filter: blur(18px);
  opacity: 0.42;
}

.scan-card {
  margin-bottom: 14px;
  padding: 15px;
  border: 1px solid var(--line);
  border-radius: 22px;
  background: rgba(2, 6, 23, 0.56);
}

.scan-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  margin-bottom: 12px;
  color: var(--subtle);
  font-size: 12px;
  font-weight: 750;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.scan-status {
  color: #bbf7d0;
}

.sample-grid {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  grid-template-rows: 138px 138px 138px;
  gap: 12px;
}

.sample-tile {
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 18px;
  background: #111827;
}

.sample-tile:first-child {
  grid-row: span 2;
}

.sample-tile img {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  filter: saturate(1.08) contrast(1.05);
  transition: transform 0.35s ease;
}

.sample-tile:hover img {
  transform: scale(1.045);
}

.sample-tile::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(2, 6, 23, 0.84), transparent 56%);
}

.sample-label {
  position: absolute;
  left: 12px;
  right: 12px;
  bottom: 11px;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  color: white;
  font-size: 12px;
  font-weight: 850;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.confidence {
  color: #bae6fd;
  font-size: 11px;
}

.visual-footer {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  margin-top: 14px;
}

.mini-metric {
  padding: 12px;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: rgba(255, 255, 255, 0.055);
}

.mini-metric b {
  display: block;
  color: white;
  font-size: 18px;
  letter-spacing: -0.03em;
}

.mini-metric span {
  color: var(--subtle);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.stats {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 14px;
  padding: 30px 0 38px;
}

.stat-card {
  padding: 20px 16px;
  border: 1px solid var(--line);
  border-radius: 20px;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.035));
  box-shadow: 0 16px 50px rgba(0, 0, 0, 0.18);
}

.stat-card b {
  display: block;
  margin-bottom: 8px;
  color: white;
  font-size: 27px;
  line-height: 1;
  letter-spacing: -0.045em;
}

.stat-card span {
  color: var(--subtle);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.section {
  padding: 58px 0;
}

.section-head {
  display: grid;
  grid-template-columns: minmax(0, 0.84fr) minmax(280px, 0.46fr);
  gap: 28px;
  align-items: end;
  margin-bottom: 26px;
}

.section-kicker {
  margin: 0 0 10px;
  color: var(--blue);
  font-size: 12px;
  font-weight: 900;
  letter-spacing: 0.15em;
  text-transform: uppercase;
}

.section h2 {
  margin: 0;
  color: white;
  font-size: clamp(30px, 4.4vw, 52px);
  line-height: 1.02;
  letter-spacing: -0.055em;
}

.section-desc {
  margin: 0;
  color: var(--muted);
  font-size: 16px;
  line-height: 1.7;
}

.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
}

.panel {
  border: 1px solid var(--line);
  border-radius: 24px;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.075), rgba(255, 255, 255, 0.032)),
    rgba(15, 23, 42, 0.72);
  box-shadow: 0 18px 60px rgba(0, 0, 0, 0.2);
}

.panel-pad {
  padding: 24px;
}

.panel h3 {
  margin: 0 0 12px;
  color: white;
  font-size: 20px;
  letter-spacing: -0.03em;
}

.panel p,
.panel li {
  color: var(--muted);
  line-height: 1.7;
}

.panel ul {
  margin: 14px 0 0;
  padding-left: 20px;
}

.use-card {
  min-height: 100%;
}

.use-card .tag {
  display: inline-flex;
  margin-bottom: 16px;
  padding: 6px 10px;
  border: 1px solid rgba(56, 189, 248, 0.25);
  border-radius: 999px;
  color: #bfdbfe;
  background: rgba(37, 99, 235, 0.12);
  font-size: 11px;
  font-weight: 850;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.category-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 12px;
}

.category {
  padding: 15px;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: rgba(255, 255, 255, 0.045);
}

.category b {
  display: block;
  color: white;
  font-size: 14px;
}

.category span {
  display: block;
  margin-top: 6px;
  color: var(--subtle);
  font-size: 12px;
}

.result-strip {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 12px;
  margin-bottom: 18px;
}

.result-pill {
  padding: 16px;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: rgba(255, 255, 255, 0.045);
}

.result-pill b {
  display: block;
  color: white;
  font-size: 24px;
  letter-spacing: -0.04em;
}

.result-pill span {
  color: var(--subtle);
  font-size: 12px;
  font-weight: 800;
  text-transform: uppercase;
}

.chart-card {
  overflow: hidden;
}

.chart-card img {
  width: 100%;
  display: block;
  border-radius: 18px;
  background: rgba(2, 6, 23, 0.56);
}

.chart-caption {
  margin-top: 14px;
  color: var(--muted);
  font-size: 14px;
  line-height: 1.65;
}

.confusion-list {
  display: grid;
  gap: 10px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.confusion-list li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 13px 14px;
  border: 1px solid rgba(245, 158, 11, 0.24);
  border-radius: 16px;
  background: rgba(245, 158, 11, 0.07);
  color: #fde68a;
  font-size: 14px;
}

.confusion-list span {
  color: var(--muted);
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.pipeline {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 12px;
}

.pipe-step {
  position: relative;
  padding: 18px;
  border: 1px solid var(--line);
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.045);
}

.pipe-step b {
  display: grid;
  place-items: center;
  width: 34px;
  height: 34px;
  margin-bottom: 14px;
  border-radius: 12px;
  color: white;
  background: linear-gradient(135deg, var(--blue-strong), var(--violet-strong));
}

.pipe-step h3 {
  margin-bottom: 8px;
  font-size: 16px;
}

.pipe-step p {
  margin: 0;
  font-size: 13px;
}

.code-panel {
  margin: 0;
  padding: 22px;
  overflow-x: auto;
  border: 1px solid var(--line);
  border-radius: 24px;
  color: rgba(226, 232, 240, 0.86);
  background: rgba(2, 6, 23, 0.68);
  font-size: 13px;
  line-height: 1.65;
}

.code-panel code {
  color: inherit;
  background: transparent;
}

code {
  padding: 2px 6px;
  border: 1px solid var(--line);
  border-radius: 7px;
  color: #bae6fd;
  background: rgba(2, 6, 23, 0.5);
  font-size: 0.92em;
}

.deploy-card {
  display: flex;
  flex-direction: column;
  min-height: 100%;
}

.deploy-card .button {
  width: fit-content;
  margin-top: auto;
}

.stack-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.stack-list span {
  padding: 10px 12px;
  border: 1px solid var(--line);
  border-radius: 999px;
  color: rgba(226, 232, 240, 0.9);
  background: rgba(255, 255, 255, 0.045);
  font-size: 13px;
  font-weight: 750;
}

.footer {
  margin-top: 40px;
  border-top: 1px solid var(--line);
  padding: 34px 0 42px;
  color: var(--subtle);
}

.footer-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
}

.footer a {
  color: #bae6fd;
  text-decoration: none;
  border: 0;
}

@media (max-width: 1080px) {
  .hero-grid,
  .section-head {
    grid-template-columns: 1fr;
  }

  .hero-visual {
    max-width: 720px;
  }

  .stats {
    grid-template-columns: repeat(3, 1fr);
  }

  .pipeline,
  .category-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 820px) {
  .cd-wrap {
    width: min(100% - 28px, 1180px);
  }

  .nav-links {
    display: none;
  }

  .hero {
    padding-top: 58px;
  }

  .hero-grid,
  .grid-2,
  .grid-3,
  .result-strip {
    grid-template-columns: 1fr;
  }

  .sample-grid {
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 132px 132px 132px;
  }

  .stats {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 560px) {
  .hero h1 {
    font-size: 44px;
  }

  .hero-actions .button {
    width: 100%;
  }

  .sample-grid,
  .stats,
  .pipeline,
  .category-grid,
  .visual-footer {
    grid-template-columns: 1fr;
  }

  .sample-tile:first-child {
    grid-row: auto;
  }
}
</style>

<div class="cd-page">
  <header class="cd-nav">
    <div class="cd-wrap cd-nav-inner">
      <a class="brand" href="#top" aria-label="Car Damage Classifier home">
        <span class="brand-mark">CD</span>
        <span>
          <span class="brand-title">CAR DAMAGE CLASSIFIER</span>
          <span class="brand-subtitle">AI Vehicle Inspection</span>
        </span>
      </a>
      <nav class="nav-links" aria-label="Primary navigation">
        <a href="#why">Why</a>
        <a href="#dataset">Dataset</a>
        <a href="#results">Results</a>
        <a href="#methodology">Methodology</a>
        <a href="#deployment">Deployment</a>
        <a class="nav-cta" href="car_damage.html">Live Demo</a>
      </nav>
    </div>
  </header>

  <main id="top">
    <section class="hero">
      <div class="cd-wrap hero-grid">
        <div>
          <div class="eyebrow"><span class="pulse"></span> Research-grade CV portfolio project</div>
          <h1>AI vehicle damage <span>inspection.</span></h1>
          <p class="hero-lede">
            A polished end-to-end computer vision system for classifying car damage across 12 real-world categories.
          </p>
          <p class="hero-copy">
            The project trains and evaluates transfer-learning models with <strong>FastAI + PyTorch</strong>, selects
            <strong>ResNet50</strong> as the best backbone at <strong>78.03% top-1 accuracy</strong>, and deploys the
            model through <strong>HuggingFace Spaces</strong> with a GitHub Pages web demo.
          </p>
          <div class="hero-actions">
            <a class="button primary" href="car_damage.html">Live Demo</a>
            <a class="button" href="https://github.com/wrezachow/car-damage-classifier" target="_blank" rel="noreferrer">GitHub Repo</a>
            <a class="button" href="https://huggingface.co/spaces/wrezachow/car-damage-classifier" target="_blank" rel="noreferrer">Model / Space</a>
          </div>
        </div>

        <aside class="hero-visual" aria-label="Sample vehicle damage detections">
          <div class="scan-card">
            <div class="scan-top">
              <span>Damage sample review</span>
              <span class="scan-status">Model online</span>
            </div>
            <div class="sample-grid">
              <figure class="sample-tile">
                <img src="assets/samples/dent.png" alt="Car dent sample">
                <figcaption class="sample-label">Dent <span class="confidence">surface deformation</span></figcaption>
              </figure>
              <figure class="sample-tile">
                <img src="assets/samples/windshield.png" alt="Cracked windshield sample">
                <figcaption class="sample-label">Windshield <span class="confidence">glass crack</span></figcaption>
              </figure>
              <figure class="sample-tile">
                <img src="assets/samples/scratch.png" alt="Car scratch sample">
                <figcaption class="sample-label">Scratch <span class="confidence">paint defect</span></figcaption>
              </figure>
              <figure class="sample-tile">
                <img src="assets/samples/rust.png" alt="Rust and corrosion sample">
                <figcaption class="sample-label">Rust <span class="confidence">corrosion</span></figcaption>
              </figure>
              <figure class="sample-tile">
                <img src="assets/samples/bumper.png" alt="Broken bumper sample">
                <figcaption class="sample-label">Bumper <span class="confidence">impact damage</span></figcaption>
              </figure>
            </div>
          </div>
          <div class="visual-footer">
            <div class="mini-metric"><b>Top-5</b><span>predictions</span></div>
            <div class="mini-metric"><b>Gradio</b><span>API backend</span></div>
            <div class="mini-metric"><b>Static</b><span>Pages frontend</span></div>
          </div>
        </aside>
      </div>
    </section>

    <section class="cd-wrap stats" aria-label="Project statistics">
      <div class="stat-card"><b>4,500+</b><span>Labeled images</span></div>
      <div class="stat-card"><b>12</b><span>Damage categories</span></div>
      <div class="stat-card"><b>ResNet50</b><span>Best model</span></div>
      <div class="stat-card"><b>78.03%</b><span>Top-1 accuracy</span></div>
      <div class="stat-card"><b>FastAI</b><span>PyTorch training</span></div>
      <div class="stat-card"><b>HF Spaces</b><span>Deployment</span></div>
    </section>

    <section class="section" id="why">
      <div class="cd-wrap">
        <div class="section-head">
          <div>
            <p class="section-kicker">Problem context</p>
            <h2>Why this project matters</h2>
          </div>
          <p class="section-desc">
            Vehicle damage inspection is a high-volume visual workflow where consistency, speed, and traceability matter.
            This project frames the model as an applied inspection assistant rather than a generic image classifier.
          </p>
        </div>
        <div class="grid-3">
          <article class="panel panel-pad use-card">
            <span class="tag">Insurance</span>
            <h3>Claim triage</h3>
            <p>First-pass classification can route obvious cases quickly while flagging ambiguous images for manual review.</p>
          </article>
          <article class="panel panel-pad use-card">
            <span class="tag">Operations</span>
            <h3>Fleet inspection</h3>
            <p>Standardized category predictions help document vehicle condition across repeated inspection workflows.</p>
          </article>
          <article class="panel panel-pad use-card">
            <span class="tag">Repair</span>
            <h3>Shop intake</h3>
            <p>Structured predictions make repair intake faster by turning uploaded photos into searchable damage labels.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section" id="dataset">
      <div class="cd-wrap">
        <div class="section-head">
          <div>
            <p class="section-kicker">Dataset categories</p>
            <h2>12-class vehicle damage taxonomy</h2>
          </div>
          <p class="section-desc">
            The dataset covers cosmetic, structural, environmental, tire, glass, and no-damage cases across
            <strong>4,500+ labeled images</strong>.
          </p>
        </div>
        <div class="category-grid">
          <div class="category"><b>Car Dent</b><span>Panel deformation</span></div>
          <div class="category"><b>Car Scratch</b><span>Surface paint damage</span></div>
          <div class="category"><b>Cracked Windshield</b><span>Glass fracture</span></div>
          <div class="category"><b>Broken Bumper</b><span>Impact damage</span></div>
          <div class="category"><b>Flat Tire</b><span>Tire failure</span></div>
          <div class="category"><b>Flood Damage</b><span>Water exposure</span></div>
          <div class="category"><b>Fire Damage</b><span>Burn and smoke damage</span></div>
          <div class="category"><b>Hail Damage</b><span>Repeated dents</span></div>
          <div class="category"><b>Broken Side Mirror</b><span>Mirror assembly damage</span></div>
          <div class="category"><b>Rust/Corrosion</b><span>Oxidation and decay</span></div>
          <div class="category"><b>Vandalism/Keyed</b><span>Intentional surface marks</span></div>
          <div class="category"><b>No Damage</b><span>Negative class</span></div>
        </div>
      </div>
    </section>

    <section class="section" id="results">
      <div class="cd-wrap">
        <div class="section-head">
          <div>
            <p class="section-kicker">Evaluation</p>
            <h2>Results at a glance</h2>
          </div>
          <p class="section-desc">
            ResNet50 is the strongest model, but the detailed class-level view shows where the real inspection difficulty sits:
            subtle scratches, ambiguous dents, and context-dependent damage.
          </p>
        </div>

        <div class="result-strip">
          <div class="result-pill"><b>78.03%</b><span>ResNet50 top-1</span></div>
          <div class="result-pill"><b>77.93%</b><span>ResNet34 top-1</span></div>
          <div class="result-pill"><b>72.18%</b><span>EfficientNet-B0 top-1</span></div>
        </div>

        <div class="grid-2">
          <article class="panel panel-pad chart-card">
            <h3>Model comparison</h3>
            <img src="assets/charts/model-comparison-themed.png" alt="Model comparison chart">
            <p class="chart-caption">
              ResNet50 narrowly outperforms ResNet34. The small gap suggests the task is constrained by visual ambiguity and label overlap, not only backbone capacity.
            </p>
          </article>
          <article class="panel panel-pad">
            <h3>Model comparison takeaways</h3>
            <ul>
              <li><strong>ResNet50</strong> is selected as the best model at <strong>78.03%</strong> top-1 accuracy.</li>
              <li><strong>ResNet34</strong> is nearly tied at <strong>77.93%</strong>, making it a strong lightweight baseline.</li>
              <li><strong>EfficientNet-B0</strong> underperforms in this training setup at <strong>72.18%</strong>.</li>
              <li>The outcome points toward data quality, class definition, and image ambiguity as important next levers.</li>
            </ul>
          </article>
        </div>

        <div style="height: 18px"></div>

        <div class="grid-2">
          <article class="panel panel-pad chart-card">
            <h3>Per-class accuracy</h3>
            <img src="assets/charts/per-class-accuracy-themed.png" alt="Per-class accuracy chart">
            <p class="chart-caption">
              Visually distinctive classes are strongest. Thin or ambiguous surface-level defects remain the hardest classes.
            </p>
          </article>
          <article class="panel panel-pad">
            <h3>Class-level interpretation</h3>
            <p><strong>Strongest classes:</strong> Broken Side Mirror (98.9%), Flat Tire (95.5%), Rust/Corrosion (94.7%), Broken Bumper (89.3%), Cracked Windshield (89.0%).</p>
            <p><strong>Most challenging classes:</strong> Car Scratch (58.6%) and Fire Damage (66.7%). These categories vary heavily in scale, lighting, texture, and context.</p>
            <p class="result-note">This is the research value of the project: the presentation does not stop at top-line accuracy; it shows failure modes that matter for deployment.</p>
          </article>
        </div>

        <div style="height: 18px"></div>

        <div class="grid-2">
          <article class="panel panel-pad chart-card">
            <h3>Confusion matrix</h3>
            <img src="assets/confusion-matrices/resnet50-themed.png" alt="ResNet50 confusion matrix">
            <p class="chart-caption">
              The confusion matrix exposes semantically meaningful errors between visually similar damage classes.
            </p>
          </article>
          <article class="panel panel-pad">
            <h3>Top confusion pairs</h3>
            <ul class="confusion-list">
              <li>Car Scratch to Vandalism/Keyed <span>surface lines</span></li>
              <li>Car Dent to Broken Bumper <span>deformation</span></li>
              <li>Hail Damage to Car Dent <span>small dents</span></li>
              <li>Fire Damage to Flood Damage <span>context</span></li>
              <li>No Damage to Scratch / Dent <span>subtle defects</span></li>
            </ul>
          </article>
        </div>
      </div>
    </section>

    <section class="section" id="methodology">
      <div class="cd-wrap">
        <div class="section-head">
          <div>
            <p class="section-kicker">Methodology and pipeline</p>
            <h2>From raw images to deployed model</h2>
          </div>
          <p class="section-desc">
            The workflow follows a practical applied ML pipeline: collect, clean, augment, train, evaluate, export, and deploy.
          </p>
        </div>
        <div class="pipeline">
          <article class="pipe-step"><b>1</b><h3>Collect</h3><p>Build a labeled image dataset across 12 vehicle condition categories.</p></article>
          <article class="pipe-step"><b>2</b><h3>Prepare</h3><p>Split data, resize images, normalize inputs, and apply FastAI augmentations.</p></article>
          <article class="pipe-step"><b>3</b><h3>Train</h3><p>Fine-tune ResNet34, ResNet50, and EfficientNet-B0 with PyTorch-backed FastAI.</p></article>
          <article class="pipe-step"><b>4</b><h3>Evaluate</h3><p>Compare model accuracy, inspect per-class behavior, and analyze confusion patterns.</p></article>
          <article class="pipe-step"><b>5</b><h3>Deploy</h3><p>Export the best model and serve inference through Gradio on HuggingFace Spaces.</p></article>
        </div>
        <div style="height: 18px"></div>
        <article class="panel panel-pad chart-card">
          <h3>Pipeline overview</h3>
          <img src="assets/sections/pipeline-themed.png" alt="Training and deployment pipeline diagram">
        </article>
      </div>
    </section>

    <section class="section" id="structure">
      <div class="cd-wrap">
        <div class="section-head">
          <div>
            <p class="section-kicker">Repository</p>
            <h2>Project structure</h2>
          </div>
          <p class="section-desc">
            The repository separates notebooks, deployment code, model artifacts, generated documentation assets, and the GitHub Pages frontend.
          </p>
        </div>
<pre class="code-panel"><code>car-damage-classifier/
|-- deployment/
|   |-- app.py
|   `-- requirements.txt
|-- models/
|   `-- CarDamageClassifierV1.pkl
|-- notebooks/
|   |-- data_preparation.ipynb
|   `-- TrainingAndCleaning.ipynb
|-- docs/
|   |-- index.md
|   |-- car_damage.html
|   `-- assets/
|       |-- charts/
|       |-- confusion-matrices/
|       |-- samples/
|       `-- sections/
|-- scripts/
|   `-- generate_charts.py
`-- README.md</code></pre>
      </div>
    </section>

    <section class="section" id="deployment">
      <div class="cd-wrap">
        <div class="section-head">
          <div>
            <p class="section-kicker">Deployment</p>
            <h2>Static portfolio frontend, hosted ML backend</h2>
          </div>
          <p class="section-desc">
            GitHub Pages presents the project and demo UI. HuggingFace Spaces hosts the Gradio inference backend and model runtime.
          </p>
        </div>
        <div class="grid-2">
          <article class="panel panel-pad deploy-card">
            <h3>HuggingFace Spaces</h3>
            <p>Interactive Gradio deployment for real-time image classification using the exported FastAI model.</p>
            <p><strong>Space:</strong> <code>wrezachow/car-damage-classifier</code></p>
            <p><strong>Model:</strong> <code>models/CarDamageClassifierV1.pkl</code></p>
            <a class="button" href="https://huggingface.co/spaces/wrezachow/car-damage-classifier" target="_blank" rel="noreferrer">Open Model / Space</a>
          </article>
          <article class="panel panel-pad deploy-card">
            <h3>GitHub Pages</h3>
            <p>Research-style landing page plus a browser demo that calls the Space API through <code>@gradio/client</code>.</p>
            <p><strong>Landing:</strong> <code>docs/index.md</code></p>
            <p><strong>Demo:</strong> <code>docs/car_damage.html</code></p>
            <a class="button" href="car_damage.html">Open Live Demo</a>
          </article>
        </div>
      </div>
    </section>

    <section class="section" id="quickstart">
      <div class="cd-wrap">
        <div class="section-head">
          <div>
            <p class="section-kicker">Quick start</p>
            <h2>Run locally</h2>
          </div>
          <p class="section-desc">
            Use the deployment requirements and exported FastAI model to launch the Gradio app on your machine.
          </p>
        </div>
<pre class="code-panel"><code>git clone https://github.com/wrezachow/car-damage-classifier.git
cd car-damage-classifier

python -m venv .venv
.venv\Scripts\Activate.ps1

pip install -r deployment/requirements.txt
python deployment/app.py</code></pre>
      </div>
    </section>

    <section class="section" id="tech-stack">
      <div class="cd-wrap">
        <div class="section-head">
          <div>
            <p class="section-kicker">Tech stack</p>
            <h2>Applied ML tooling</h2>
          </div>
          <p class="section-desc">
            The stack is intentionally pragmatic: mature transfer-learning tooling for training and simple hosted deployment for inference access.
          </p>
        </div>
        <div class="panel panel-pad">
          <div class="stack-list">
            <span>Python</span>
            <span>FastAI</span>
            <span>PyTorch</span>
            <span>ResNet50</span>
            <span>EfficientNet-B0</span>
            <span>Jupyter</span>
            <span>Gradio</span>
            <span>HuggingFace Spaces</span>
            <span>GitHub Pages</span>
            <span>@gradio/client</span>
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="cd-wrap footer-inner">
      <span>Car Damage Classifier. FastAI + PyTorch computer vision for AI vehicle inspection.</span>
      <span><a href="https://github.com/wrezachow/car-damage-classifier" target="_blank" rel="noreferrer">GitHub</a> / <a href="https://huggingface.co/spaces/wrezachow/car-damage-classifier" target="_blank" rel="noreferrer">HuggingFace Space</a></span>
    </div>
  </footer>
</div>
