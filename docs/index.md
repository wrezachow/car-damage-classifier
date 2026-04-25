---
layout: default
title: Car Damage Classifier - AI Project
---

<style>
:root {
  --bg-dark: #1a1d29;
  --bg-darker: #0f1117;
  --bg-card: #242837;
  --text-primary: #ffffff;
  --text-muted: #a0a4b8;
  --accent-blue: #4a9eff;
  --accent-purple: #7c3aed;
  --success: #22c55e;
  --warning: #f59e0b;
  --error: #ef4444;
  --border: rgba(255, 255, 255, 0.1);
  --border-light: rgba(255, 255, 255, 0.05);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background: linear-gradient(135deg, var(--bg-darker) 0%, var(--bg-dark) 100%);
  color: var(--text-primary);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  line-height: 1.6;
  min-height: 100vh;
}

/* Navigation Header */
.nav-header {
  background: var(--bg-card);
  border-bottom: 1px solid var(--border);
  padding: 16px 0;
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(10px);
  background: rgba(36, 40, 55, 0.95);
}

.nav-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 32px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 32px;
}

.nav-logo {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  color: var(--text-primary);
  font-weight: 700;
  font-size: 18px;
}

.logo-icon {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 18px;
  color: white;
}

.nav-tabs {
  display: flex;
  gap: 8px;
  flex: 1;
  justify-content: center;
}

.nav-tab {
  padding: 8px 16px;
  text-decoration: none;
  color: var(--text-muted);
  border-radius: 8px;
  transition: all 0.2s;
  font-size: 14px;
  font-weight: 500;
}

.nav-tab:hover {
  color: var(--text-primary);
  background: rgba(255, 255, 255, 0.05);
}

.nav-tab.active {
  color: var(--accent-blue);
  background: rgba(74, 158, 255, 0.1);
}

.github-star-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: var(--bg-dark);
  border: 1px solid var(--border);
  border-radius: 8px;
  text-decoration: none;
  color: var(--text-primary);
  font-size: 14px;
  font-weight: 500;
  transition: all 0.2s;
}

.github-star-btn:hover {
  border-color: var(--accent-blue);
  background: rgba(74, 158, 255, 0.1);
}

.star-count {
  background: var(--bg-darker);
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
}

/* Container */
.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 60px 32px;
}

/* Hero Section */
.hero {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 60px;
  align-items: center;
  margin-bottom: 80px;
}

.hero-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.tech-tags {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.tech-tag {
  font-size: 13px;
  color: var(--accent-blue);
  font-weight: 600;
  letter-spacing: 0.5px;
}

.tech-tag:not(:last-child)::after {
  content: "•";
  margin-left: 12px;
  color: var(--text-muted);
}

.hero-title {
  font-size: 56px;
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.1;
}

.hero-title .accent {
  color: var(--accent-blue);
  display: block;
}

.hero-subtitle {
  font-size: 20px;
  color: var(--text-muted);
  line-height: 1.6;
  max-width: 600px;
}

.hero-description {
  font-size: 15px;
  color: var(--text-muted);
  line-height: 1.7;
}

.hero-description strong {
  color: var(--text-primary);
  font-weight: 600;
}

.hero-description a {
  color: var(--accent-blue);
  text-decoration: none;
  border-bottom: 1px solid transparent;
  transition: border-color 0.2s;
}

.hero-description a:hover {
  border-bottom-color: var(--accent-blue);
}

.hero-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 8px;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  font-size: 15px;
  transition: all 0.2s;
  border: 1px solid transparent;
}

.btn-primary {
  background: linear-gradient(135deg, var(--accent-blue), #3a8eef);
  color: white;
  box-shadow: 0 4px 16px rgba(74, 158, 255, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(74, 158, 255, 0.4);
}

.btn-secondary {
  background: var(--bg-card);
  color: var(--text-primary);
  border-color: var(--border);
}

.btn-secondary:hover {
  border-color: var(--accent-blue);
  background: rgba(74, 158, 255, 0.1);
}

/* Hero Image Grid */
.hero-images {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.damage-sample {
  position: relative;
  aspect-ratio: 4/3;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid var(--border-light);
  transition: all 0.3s;
}

.damage-sample:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
  border-color: var(--border);
}

.damage-sample img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.damage-label {
  position: absolute;
  bottom: 12px;
  left: 12px;
  padding: 6px 12px;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(8px);
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

/* Metrics Grid */
.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin: 60px 0;
}

.metric-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 28px;
  text-align: center;
  transition: all 0.3s;
}

.metric-card:hover {
  transform: translateY(-4px);
  border-color: var(--accent-blue);
  box-shadow: 0 8px 24px rgba(74, 158, 255, 0.15);
}

.metric-icon {
  font-size: 32px;
  margin-bottom: 12px;
}

.metric-value {
  font-size: 32px;
  font-weight: 800;
  color: var(--accent-blue);
  margin-bottom: 8px;
  line-height: 1;
}

.metric-label {
  font-size: 13px;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-weight: 600;
}

/* Section */
.section {
  margin: 80px 0;
}

.section-header {
  margin-bottom: 40px;
}

.section-title {
  font-size: 36px;
  font-weight: 800;
  margin-bottom: 12px;
  letter-spacing: -0.01em;
}

.section-subtitle {
  font-size: 18px;
  color: var(--text-muted);
}

/* Cards */
.card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 32px;
  margin: 24px 0;
}

.card h3 {
  font-size: 20px;
  margin-bottom: 16px;
  color: var(--accent-blue);
}

/* Grid Layouts */
.grid-2 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 24px;
  margin: 24px 0;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}

/* Chart Container */
.chart-container {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 32px;
  margin: 32px 0;
  overflow: hidden;
}

.chart-container img {
  width: 100%;
  height: auto;
  border-radius: 8px;
}

/* Features List */
ul.features {
  list-style: none;
  padding: 0;
}

ul.features li {
  padding: 14px 0;
  padding-left: 32px;
  position: relative;
  color: var(--text-muted);
  font-size: 15px;
  line-height: 1.6;
}

ul.features li:before {
  content: "✓";
  position: absolute;
  left: 0;
  color: var(--success);
  font-weight: bold;
  font-size: 18px;
}

/* Confusion Pairs */
.confusion-pairs {
  list-style: none;
  padding: 0;
  display: grid;
  gap: 12px;
}

.confusion-pairs li {
  padding: 12px 20px;
  background: rgba(255, 159, 10, 0.08);
  border-left: 3px solid var(--warning);
  border-radius: 6px;
  font-family: "SF Mono", Monaco, "Cascadia Code", monospace;
  font-size: 14px;
  color: var(--text-muted);
}

/* Pipeline */
.pipeline {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
  margin: 40px 0;
}

.pipeline-step {
  flex: 1;
  min-width: 160px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 24px;
  text-align: center;
  transition: all 0.3s;
}

.pipeline-step:hover {
  border-color: var(--accent-blue);
  transform: translateY(-4px);
}

.pipeline-step-number {
  display: inline-block;
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
  border-radius: 50%;
  color: white;
  font-weight: 700;
  font-size: 14px;
  line-height: 32px;
  margin-bottom: 12px;
}

.pipeline-step h4 {
  font-size: 15px;
  margin: 12px 0 8px;
  font-weight: 700;
  color: var(--text-primary);
}

.pipeline-step p {
  font-size: 13px;
  color: var(--text-muted);
  margin: 0;
  line-height: 1.5;
}

.pipeline-arrow {
  font-size: 24px;
  color: var(--accent-blue);
  flex-shrink: 0;
}

/* Code Block */
code {
  background: rgba(0, 0, 0, 0.3);
  padding: 3px 8px;
  border-radius: 4px;
  font-size: 13px;
  border: 1px solid var(--border-light);
  font-family: "SF Mono", Monaco, "Cascadia Code", monospace;
  color: var(--accent-blue);
}

pre {
  background: var(--bg-darker);
  padding: 24px;
  border-radius: 12px;
  border: 1px solid var(--border);
  overflow-x: auto;
  margin: 20px 0;
}

pre code {
  background: none;
  padding: 0;
  border: none;
  color: var(--text-muted);
  font-size: 13px;
  line-height: 1.6;
}

/* Footer */
footer {
  background: var(--bg-darker);
  border-top: 1px solid var(--border);
  margin-top: 120px;
  padding: 60px 0 40px;
}

.footer-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 32px;
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 60px;
}

.footer-brand {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.footer-logo {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 8px;
}

.footer-logo .logo-icon {
  width: 48px;
  height: 48px;
  font-size: 20px;
}

.footer-logo-text {
  font-size: 16px;
  font-weight: 800;
  letter-spacing: -0.01em;
}

.footer-tagline {
  font-size: 14px;
  color: var(--text-muted);
  line-height: 1.6;
  max-width: 400px;
}

.footer-section h4 {
  font-size: 14px;
  font-weight: 700;
  margin-bottom: 16px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--text-primary);
}

.footer-links {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.footer-links a {
  color: var(--text-muted);
  text-decoration: none;
  font-size: 14px;
  transition: color 0.2s;
}

.footer-links a:hover {
  color: var(--accent-blue);
}

.social-links {
  display: flex;
  gap: 12px;
}

.social-link {
  width: 40px;
  height: 40px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  color: var(--text-muted);
  transition: all 0.2s;
}

.social-link:hover {
  border-color: var(--accent-blue);
  color: var(--accent-blue);
  background: rgba(74, 158, 255, 0.1);
}

.footer-bottom {
  max-width: 1400px;
  margin: 40px auto 0;
  padding: 24px 32px 0;
  border-top: 1px solid var(--border);
  text-align: center;
  color: var(--text-muted);
  font-size: 13px;
}

/* Responsive */
@media (max-width: 1024px) {
  .hero {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .hero-title {
    font-size: 44px;
  }

  .footer-content {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 768px) {
  .nav-container {
    padding: 0 20px;
  }

  .nav-tabs {
    display: none;
  }

  .container {
    padding: 40px 20px;
  }

  .hero-title {
    font-size: 36px;
  }

  .metrics-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
  }

  .pipeline {
    flex-direction: column;
  }

  .pipeline-arrow {
    transform: rotate(90deg);
  }

  .footer-content {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .grid-2,
  .grid-3 {
    grid-template-columns: 1fr;
  }
}
</style>

<!-- Navigation Header -->
<div class="nav-header">
  <div class="nav-container">
    <a href="#" class="nav-logo">
      <div class="logo-icon">CDC</div>
      <span>CAR DAMAGE<br/>CLASSIFIER</span>
    </a>

    <nav class="nav-tabs">
      <a href="#overview" class="nav-tab active">Overview</a>
      <a href="car_damage.html" class="nav-tab">Demo</a>
      <a href="#results" class="nav-tab">Results</a>
      <a href="#methodology" class="nav-tab">Methodology</a>
      <a href="#quickstart" class="nav-tab">Docs</a>
      <a href="https://github.com/wrezachow/car-damage-classifier" class="nav-tab" target="_blank">Repository</a>
    </nav>

    <a href="https://github.com/wrezachow/car-damage-classifier" class="github-star-btn" target="_blank">
      ⭐ Star on GitHub
      <span class="star-count">197</span>
    </a>
  </div>
</div>

<div class="container">
  <!-- Hero Section -->
  <section class="hero" id="overview">
    <div class="hero-content">
      <div class="tech-tags">
        <span class="tech-tag">Computer Vision</span>
        <span class="tech-tag">Deep Learning</span>
        <span class="tech-tag">Auto Inspection</span>
      </div>

      <h1 class="hero-title">
        CAR DAMAGE
        <span class="accent">CLASSIFIER</span>
      </h1>

      <p class="hero-subtitle">
        End-to-end vehicle damage classification across 12 categories using FastAI + PyTorch.
      </p>

      <p class="hero-description">
        Trained on <strong>4,500+ labeled images</strong> across 12 damage types. Best model <strong>ResNet50</strong> achieves <strong>78.03% top-1 accuracy</strong> and is deployed on <a href="https://huggingface.co/spaces/wrezachow/car-damage-classifier" target="_blank">HuggingFace Spaces</a> with a modern web demo via GitHub Pages.
      </p>

      <div class="hero-actions">
        <a href="car_damage.html" class="btn btn-primary">
          🚀 Live Demo
        </a>
        <a href="https://github.com/wrezachow/car-damage-classifier" class="btn btn-secondary" target="_blank">
          📁 GitHub Repo
        </a>
        <a href="https://huggingface.co/spaces/wrezachow/car-damage-classifier" class="btn btn-secondary" target="_blank">
          🤗 Model / Space
        </a>
      </div>
    </div>

    <div class="hero-images">
      <div class="damage-sample">
        <img src="assets/samples/dent.png" alt="Car Dent">
        <div class="damage-label">DENT</div>
      </div>
      <div class="damage-sample">
        <img src="assets/samples/windshield.png" alt="Cracked Windshield">
        <div class="damage-label">CRACKED WINDSHIELD</div>
      </div>
      <div class="damage-sample">
        <img src="assets/samples/scratch.png" alt="Car Scratch">
        <div class="damage-label">SCRATCH</div>
      </div>
      <div class="damage-sample">
        <img src="assets/samples/rust.png" alt="Rust/Corrosion">
        <div class="damage-label">RUST / CORROSION</div>
      </div>
      <div class="damage-sample">
        <img src="assets/samples/bumper.png" alt="Bumper Damage">
        <div class="damage-label">BUMPER DAMAGE</div>
      </div>
    </div>
  </section>

  <!-- Metrics Grid -->
  <div class="metrics-grid">
    <div class="metric-card">
      <div class="metric-icon">📊</div>
      <div class="metric-value">4,500+</div>
      <div class="metric-label">Labeled Images</div>
    </div>
    <div class="metric-card">
      <div class="metric-icon">🏷️</div>
      <div class="metric-value">12</div>
      <div class="metric-label">Categories</div>
    </div>
    <div class="metric-card">
      <div class="metric-icon">🧠</div>
      <div class="metric-value">ResNet50</div>
      <div class="metric-label">Best Model</div>
    </div>
    <div class="metric-card">
      <div class="metric-icon">🎯</div>
      <div class="metric-value">78.03%</div>
      <div class="metric-label">Top-1 Accuracy</div>
    </div>
    <div class="metric-card">
      <div class="metric-icon">⚡</div>
      <div class="metric-value">FastAI</div>
      <div class="metric-label">Framework</div>
    </div>
    <div class="metric-card">
      <div class="metric-icon">☁️</div>
      <div class="metric-value">HF Spaces</div>
      <div class="metric-label">Deployment</div>
    </div>
  </div>

  <!-- Why This Project Matters -->
  <section class="section">
    <div class="section-header">
      <h2 class="section-title">Why This Project Matters</h2>
      <p class="section-subtitle">Practical applications for automotive safety and insurance</p>
    </div>

    <div class="card">
      <ul class="features">
        <li>Automates visual vehicle inspection for insurance claims, fleet management, and repair shops</li>
        <li>Reduces manual review time and provides consistent damage assessment</li>
        <li>Accelerates repair shop intake processing and vehicle condition documentation</li>
        <li>Enables faster, data-driven decision-making for insurance claim triage</li>
      </ul>
    </div>
  </section>

  <!-- Results Section -->
  <section class="section" id="results">
    <div class="section-header">
      <h2 class="section-title">Results at a Glance</h2>
      <p class="section-subtitle">Model performance comparison and per-class accuracy</p>
    </div>

    <h3 style="margin-top: 40px; margin-bottom: 20px;">Model Accuracy Comparison</h3>
    <div class="chart-container">
      <img src="assets/charts/model-comparison-themed.png" alt="Model Accuracy Comparison">
    </div>

    <div class="card">
      <h3>Key Findings</h3>
      <ul>
        <li><strong>ResNet50</strong> achieved the best overall accuracy at <strong>78.03%</strong></li>
        <li><strong>ResNet34</strong> performed nearly as well at <strong>77.93%</strong></li>
        <li><strong>EfficientNet-B0</strong> underperformed at <strong>72.18%</strong> in this setup</li>
        <li>The small gap between ResNet34 and ResNet50 suggests the task is constrained more by class overlap and data ambiguity than raw model capacity</li>
      </ul>
    </div>

    <h3 style="margin-top: 60px; margin-bottom: 20px;">Per-Class Accuracy (ResNet50)</h3>
    <div class="chart-container">
      <img src="assets/charts/per-class-accuracy-themed.png" alt="Per-Class Accuracy">
    </div>

    <div class="card">
      <h3>Performance Analysis</h3>
      <p><strong>Strongest Classes (>90% accuracy):</strong></p>
      <ul>
        <li>Broken Side Mirror (98.9%)</li>
        <li>Flat Tire (95.5%)</li>
        <li>Rust/Corrosion (94.7%)</li>
      </ul>
      <p style="margin-top: 16px;"><strong>Most Challenging Classes (<70% accuracy):</strong></p>
      <ul>
        <li>Car Scratch (58.6%) - subtle and thin, easily confused with vandalism</li>
        <li>Fire Damage (66.7%) - varies widely in severity and visual context</li>
      </ul>
    </div>

    <h3 style="margin-top: 60px; margin-bottom: 20px;">Confusion Matrix</h3>
    <div class="chart-container">
      <img src="assets/confusion-matrices/resnet50-themed.png" alt="ResNet50 Confusion Matrix">
    </div>

    <div class="card">
      <h3>Top Confusion Pairs</h3>
      <p>The most common classification errors occur between visually similar damage types:</p>
      <ul class="confusion-pairs">
        <li>Car Scratch ↔ Vandalism/Keyed</li>
        <li>Car Dent ↔ Broken Bumper</li>
        <li>Hail Damage ↔ Car Dent</li>
        <li>Fire Damage ↔ Flood Damage</li>
        <li>No Damage ↔ Car Scratch / Car Dent</li>
      </ul>
    </div>
  </section>

  <!-- Methodology & Pipeline -->
  <section class="section" id="methodology">
    <div class="section-header">
      <h2 class="section-title">Methodology & Pipeline</h2>
      <p class="section-subtitle">End-to-end training and deployment workflow</p>
    </div>

    <div class="pipeline">
      <div class="pipeline-step">
        <div class="pipeline-step-number">1</div>
        <h4>Data Collection</h4>
        <p>4,500+ images from Bing & Google image search</p>
      </div>
      <div class="pipeline-arrow">→</div>
      <div class="pipeline-step">
        <div class="pipeline-step-number">2</div>
        <h4>Preprocess & Augment</h4>
        <p>Resize, normalize, and apply FastAI augmentations</p>
      </div>
      <div class="pipeline-arrow">→</div>
      <div class="pipeline-step">
        <div class="pipeline-step-number">3</div>
        <h4>Train</h4>
        <p>Fine-tune ResNet34, ResNet50, EfficientNet-B0</p>
      </div>
      <div class="pipeline-arrow">→</div>
      <div class="pipeline-step">
        <div class="pipeline-step-number">4</div>
        <h4>Evaluate</h4>
        <p>Compare models, analyze confusion matrix</p>
      </div>
      <div class="pipeline-arrow">→</div>
      <div class="pipeline-step">
        <div class="pipeline-step-number">5</div>
        <h4>Deploy</h4>
        <p>Export to Gradio on HuggingFace Spaces</p>
      </div>
    </div>
  </section>

  <!-- Project Structure -->
  <section class="section">
    <div class="section-header">
      <h2 class="section-title">Project Structure</h2>
      <p class="section-subtitle">Repository organization</p>
    </div>

    <pre><code>car-damage-classifier/
├─ deployment/
│  ├─ app.py                 # Gradio app
│  └─ requirements.txt
├─ models/
│  └─ CarDamageClassifierV1.pkl
├─ notebooks/
│  ├─ data_preparation.ipynb
│  └─ TrainingAndCleaning.ipynb
├─ docs/
│  ├─ index.md
│  ├─ car_damage.html
│  └─ assets/
│     ├─ charts/
│     ├─ confusion-matrices/
│     └─ samples/
├─ scripts/
│  └─ generate_charts.py
└─ README.md</code></pre>
  </section>

  <!-- Deployment -->
  <section class="section">
    <div class="section-header">
      <h2 class="section-title">Deployment</h2>
      <p class="section-subtitle">Live demo and API endpoints</p>
    </div>

    <div class="grid-2">
      <div class="card">
        <h3>HuggingFace Spaces</h3>
        <p>Interactive Gradio app for real-time predictions</p>
        <p style="margin-top: 16px;"><strong>Space:</strong> <code>wrezachow/car-damage-classifier</code></p>
        <p><strong>Endpoint:</strong> <code>/predict</code></p>
        <p style="margin-top: 16px;">
          <a href="https://huggingface.co/spaces/wrezachow/car-damage-classifier" class="btn btn-secondary" target="_blank" style="margin: 0;">
            Visit Space →
          </a>
        </p>
      </div>
      <div class="card">
        <h3>GitHub Pages</h3>
        <p>Static web demo using <code>@gradio/client</code></p>
        <p style="margin-top: 16px;"><strong>Landing:</strong> Project documentation</p>
        <p><strong>Demo:</strong> <a href="car_damage.html" style="color: var(--accent-blue);">Interactive interface</a></p>
        <p style="margin-top: 16px;">
          <a href="car_damage.html" class="btn btn-secondary" style="margin: 0;">
            Try Demo →
          </a>
        </p>
      </div>
    </div>
  </section>

  <!-- Quick Start -->
  <section class="section" id="quickstart">
    <div class="section-header">
      <h2 class="section-title">Quick Start</h2>
      <p class="section-subtitle">Run the model locally</p>
    </div>

    <div class="card">
      <h3>1. Clone the repository</h3>
      <pre><code>git clone https://github.com/wrezachow/car-damage-classifier.git
cd car-damage-classifier</code></pre>

      <h3 style="margin-top: 32px;">2. Create virtual environment</h3>
      <pre><code>python -m venv .venv</code></pre>

      <h3 style="margin-top: 32px;">3. Activate environment</h3>
      <p><strong>Windows PowerShell:</strong></p>
      <pre><code>.venv\Scripts\Activate.ps1</code></pre>
      <p><strong>macOS/Linux:</strong></p>
      <pre><code>source .venv/bin/activate</code></pre>

      <h3 style="margin-top: 32px;">4. Install dependencies</h3>
      <pre><code>pip install -r deployment/requirements.txt</code></pre>

      <h3 style="margin-top: 32px;">5. Run the app</h3>
      <pre><code>python deployment/app.py</code></pre>
      <p>Open <code>http://127.0.0.1:7860</code> in your browser</p>
    </div>
  </section>

  <!-- Tech Stack -->
  <section class="section">
    <div class="section-header">
      <h2 class="section-title">Tech Stack</h2>
      <p class="section-subtitle">Technologies and frameworks used</p>
    </div>

    <div class="grid-2">
      <div class="card">
        <h3>Training & Model</h3>
        <ul>
          <li>Python 3.x</li>
          <li>FastAI</li>
          <li>PyTorch</li>
          <li>Jupyter Notebooks</li>
        </ul>
      </div>
      <div class="card">
        <h3>Deployment</h3>
        <ul>
          <li>Gradio</li>
          <li>HuggingFace Spaces</li>
          <li>GitHub Pages</li>
          <li>@gradio/client</li>
        </ul>
      </div>
    </div>
  </section>
</div>

<!-- Footer -->
<footer>
  <div class="footer-content">
    <div class="footer-brand">
      <div class="footer-logo">
        <div class="logo-icon">CDC</div>
        <div class="footer-logo-text">CAR DAMAGE CLASSIFIER</div>
      </div>
      <p class="footer-tagline">
        Built with ❤️ by wrezachow • FastAI + PyTorch • Computer Vision for Automotive Safety
      </p>
      <div class="social-links">
        <a href="https://github.com/wrezachow" class="social-link" target="_blank" title="GitHub">
          <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
        </a>
        <a href="https://linkedin.com/in/wrezachow" class="social-link" target="_blank" title="LinkedIn">
          <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
        </a>
        <a href="mailto:contact@wrezachow.com" class="social-link" title="Email">
          <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
        </a>
      </div>
    </div>

    <div class="footer-section">
      <h4>Quick Links</h4>
      <ul class="footer-links">
        <li><a href="#overview">Overview</a></li>
        <li><a href="car_damage.html">Demo</a></li>
        <li><a href="#results">Results</a></li>
        <li><a href="#methodology">Methodology</a></li>
      </ul>
    </div>

    <div class="footer-section">
      <h4>Resources</h4>
      <ul class="footer-links">
        <li><a href="https://github.com/wrezachow/car-damage-classifier" target="_blank">GitHub Repository</a></li>
        <li><a href="https://huggingface.co/spaces/wrezachow/car-damage-classifier" target="_blank">HuggingFace Space</a></li>
        <li><a href="#quickstart">Documentation</a></li>
        <li><a href="assets/SOURCES.md">Asset Sources</a></li>
      </ul>
    </div>
  </div>

  <div class="footer-bottom">
    © 2025 wrezachow. All rights reserved. | MIT License
  </div>
</footer>
