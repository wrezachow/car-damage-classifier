---
layout: default
title: Car Damage Classifier - AI Project
---

<style>
:root {
  --bg: #0b1220;
  --panel: rgba(255, 255, 255, 0.06);
  --panel-2: rgba(255, 255, 255, 0.1);
  --text: rgba(255, 255, 255, 0.92);
  --muted: rgba(255, 255, 255, 0.68);
  --brand: #7c3aed;
  --good: #22c55e;
  --warn: #f59e0b;
  --bad: #ef4444;
  --border: rgba(255, 255, 255, 0.14);
}

* {
  box-sizing: border-box;
}

body {
  background: radial-gradient(
      1200px 600px at 20% -10%,
      rgba(124, 58, 237, 0.35),
      transparent 60%
    ),
    radial-gradient(
      900px 500px at 90% 0%,
      rgba(34, 197, 94, 0.18),
      transparent 55%
    ),
    var(--bg);
  color: var(--text);
  font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  line-height: 1.6;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
}

.badge {
  display: inline-block;
  padding: 8px 16px;
  background: linear-gradient(135deg, var(--brand), #a855f7);
  color: white;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.5px;
  margin-bottom: 20px;
  text-transform: uppercase;
}

.hero {
  text-align: center;
  margin-bottom: 60px;
}

.hero h1 {
  font-size: 48px;
  margin: 20px 0 16px;
  letter-spacing: -0.02em;
  font-weight: 800;
}

.hero p {
  font-size: 20px;
  color: var(--muted);
  max-width: 700px;
  margin: 0 auto;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 16px;
  margin: 40px 0;
}

.stat-card {
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.04));
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 24px;
  text-align: center;
}

.stat-value {
  font-size: 32px;
  font-weight: 800;
  color: var(--brand);
  margin-bottom: 8px;
}

.stat-label {
  font-size: 14px;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.section {
  margin: 60px 0;
}

.section h2 {
  font-size: 32px;
  margin-bottom: 24px;
  font-weight: 700;
}

.section h3 {
  font-size: 24px;
  margin-bottom: 16px;
  font-weight: 600;
}

.card {
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.04));
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 32px;
  margin: 24px 0;
}

.grid-2 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
  margin: 24px 0;
}

.chart-container {
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.04));
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 24px;
  margin: 24px 0;
}

.chart-container img {
  width: 100%;
  height: auto;
  border-radius: 12px;
}

.pipeline {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
  margin: 32px 0;
}

.pipeline-step {
  flex: 1;
  min-width: 150px;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.04));
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px;
  text-align: center;
}

.pipeline-step h4 {
  font-size: 16px;
  margin: 12px 0 8px;
  font-weight: 600;
}

.pipeline-step p {
  font-size: 13px;
  color: var(--muted);
  margin: 0;
}

.pipeline-arrow {
  font-size: 24px;
  color: var(--brand);
  flex-shrink: 0;
}

ul.features {
  list-style: none;
  padding: 0;
}

ul.features li {
  padding: 12px 0;
  padding-left: 32px;
  position: relative;
}

ul.features li:before {
  content: "→";
  position: absolute;
  left: 0;
  color: var(--brand);
  font-weight: bold;
  font-size: 18px;
}

.confusion-pairs {
  list-style: none;
  padding: 0;
}

.confusion-pairs li {
  padding: 8px 16px;
  background: rgba(255, 255, 255, 0.04);
  border-left: 3px solid var(--warn);
  margin-bottom: 8px;
  border-radius: 4px;
  font-family: monospace;
}

code {
  background: rgba(0, 0, 0, 0.3);
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 14px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

pre {
  background: rgba(0, 0, 0, 0.3);
  padding: 20px;
  border-radius: 12px;
  border: 1px solid var(--border);
  overflow-x: auto;
}

pre code {
  background: none;
  padding: 0;
  border: none;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

table th,
table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid var(--border);
}

table th {
  background: rgba(255, 255, 255, 0.06);
  font-weight: 600;
  color: var(--text);
}

table tr:last-child td {
  border-bottom: none;
}

footer {
  text-align: center;
  margin-top: 80px;
  padding: 40px 0;
  color: var(--muted);
  font-size: 14px;
}

.btn {
  display: inline-block;
  padding: 12px 24px;
  background: linear-gradient(135deg, var(--brand), #a855f7);
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  margin: 8px;
  transition: transform 0.2s;
}

.btn:hover {
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 36px;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .pipeline {
    flex-direction: column;
  }

  .pipeline-arrow {
    transform: rotate(90deg);
  }
}
</style>

<div class="container">
  <div class="hero">
    <div class="badge">AI PROJECT</div>
    <h1>Car Damage Classifier</h1>
    <p>End-to-end vehicle damage classification across 12 categories using FastAI + PyTorch</p>
  </div>

  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-value">4,500+</div>
      <div class="stat-label">Labeled Images</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">12</div>
      <div class="stat-label">Categories</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">ResNet50</div>
      <div class="stat-label">Best Model</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">78.03%</div>
      <div class="stat-label">Top-1 Accuracy</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">FastAI</div>
      <div class="stat-label">Framework</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">HF Spaces</div>
      <div class="stat-label">Deployment</div>
    </div>
  </div>

  <div class="section">
    <h2>Try the Demo</h2>
    <div style="text-align: center;">
      <a href="car_damage.html" class="btn">Interactive Web Demo</a>
      <a href="https://huggingface.co/spaces/wrezachow/car-damage-classifier" class="btn" target="_blank">HuggingFace Space</a>
    </div>
  </div>

  <div class="section">
    <h2>Why This Project Matters</h2>
    <div class="card">
      <ul class="features">
        <li>Automates visual vehicle inspection for insurance claims, fleet management, and repair shops</li>
        <li>Reduces manual review time and provides consistent damage assessment</li>
        <li>Accelerates repair shop intake processing and vehicle condition documentation</li>
        <li>Enables faster, data-driven decision-making for insurance claim triage</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>Dataset Categories (12)</h2>
    <div class="grid-2">
      <div>
        <ol>
          <li>Car Dent</li>
          <li>Car Scratch</li>
          <li>Cracked Windshield</li>
          <li>Broken Bumper</li>
          <li>Flat Tire</li>
          <li>Flood Damage</li>
        </ol>
      </div>
      <div>
        <ol start="7">
          <li>Fire Damage</li>
          <li>Hail Damage</li>
          <li>Broken Side Mirror</li>
          <li>Rust/Corrosion</li>
          <li>Vandalism/Keyed</li>
          <li>No Damage</li>
        </ol>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Results at a Glance</h2>

    <h3>Model Accuracy Comparison</h3>
    <div class="chart-container">
      <img src="assets/charts/model-comparison.png" alt="Model Accuracy Comparison">
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
  </div>

  <div class="section">
    <h2>Per-Class Accuracy (ResNet50)</h2>
    <div class="chart-container">
      <img src="assets/charts/per-class-accuracy.png" alt="Per-Class Accuracy">
    </div>

    <div class="card">
      <h3>Performance Analysis</h3>
      <p><strong>Strongest Classes (>90% accuracy):</strong></p>
      <ul>
        <li>Broken Side Mirror (98.9%)</li>
        <li>Flat Tire (95.5%)</li>
        <li>Rust/Corrosion (94.7%)</li>
      </ul>
      <p><strong>Most Challenging Classes (<70% accuracy):</strong></p>
      <ul>
        <li>Car Scratch (58.6%) - subtle and thin, easily confused with vandalism</li>
        <li>Fire Damage (66.7%) - varies widely in severity and visual context</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>Confusion Matrix</h2>
    <div class="chart-container">
      <img src="assets/confusion-matrices/resnet50.png" alt="ResNet50 Confusion Matrix">
    </div>
  </div>

  <div class="section">
    <h2>Top Confusion Pairs</h2>
    <div class="card">
      <p>The most common classification errors occur between visually similar damage types:</p>
      <ul class="confusion-pairs">
        <li>Car Scratch ↔ Vandalism/Keyed</li>
        <li>Car Dent ↔ Broken Bumper</li>
        <li>Hail Damage ↔ Car Dent</li>
        <li>Fire Damage ↔ Flood Damage</li>
        <li>No Damage ↔ Car Scratch / Car Dent</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <h2>Methodology & Pipeline</h2>
    <div class="pipeline">
      <div class="pipeline-step">
        <h4>1. Data Collection</h4>
        <p>4,500+ images from Bing & Google image search</p>
      </div>
      <div class="pipeline-arrow">→</div>
      <div class="pipeline-step">
        <h4>2. Preprocess & Augment</h4>
        <p>Resize, normalize, and apply FastAI augmentations</p>
      </div>
      <div class="pipeline-arrow">→</div>
      <div class="pipeline-step">
        <h4>3. Train</h4>
        <p>Fine-tune ResNet34, ResNet50, EfficientNet-B0</p>
      </div>
      <div class="pipeline-arrow">→</div>
      <div class="pipeline-step">
        <h4>4. Evaluate</h4>
        <p>Compare models, analyze confusion matrix</p>
      </div>
      <div class="pipeline-arrow">→</div>
      <div class="pipeline-step">
        <h4>5. Deploy</h4>
        <p>Export to Gradio on HuggingFace Spaces</p>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Project Structure</h2>
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
  </div>

  <div class="section">
    <h2>Deployment</h2>
    <div class="grid-2">
      <div class="card">
        <h3>HuggingFace Spaces</h3>
        <p>Interactive Gradio app for real-time predictions</p>
        <p><strong>Space:</strong> <code>wrezachow/car-damage-classifier</code></p>
        <p><strong>Endpoint:</strong> <code>/predict</code></p>
      </div>
      <div class="card">
        <h3>GitHub Pages</h3>
        <p>Static web demo using <code>@gradio/client</code></p>
        <p><strong>Landing:</strong> Project documentation</p>
        <p><strong>Demo:</strong> <a href="car_damage.html">Interactive interface</a></p>
      </div>
    </div>
  </div>

  <div class="section">
    <h2>Quick Start</h2>
    <div class="card">
      <h3>1. Clone the repository</h3>
      <pre><code>git clone https://github.com/wrezachow/car-damage-classifier.git
cd car-damage-classifier</code></pre>

      <h3>2. Create virtual environment</h3>
      <pre><code>python -m venv .venv</code></pre>

      <h3>3. Activate environment</h3>
      <p><strong>Windows PowerShell:</strong></p>
      <pre><code>.venv\Scripts\Activate.ps1</code></pre>
      <p><strong>macOS/Linux:</strong></p>
      <pre><code>source .venv/bin/activate</code></pre>

      <h3>4. Install dependencies</h3>
      <pre><code>pip install -r deployment/requirements.txt</code></pre>

      <h3>5. Run the app</h3>
      <pre><code>python deployment/app.py</code></pre>
      <p>Open <code>http://127.0.0.1:7860</code> in your browser</p>
    </div>
  </div>

  <div class="section">
    <h2>Tech Stack</h2>
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
  </div>

  <footer>
    <p><strong>Built with FastAI, PyTorch & Gradio</strong></p>
    <p>© 2025 Wasef Chowdhury | MIT License</p>
    <p><a href="https://github.com/wrezachow/car-damage-classifier" target="_blank">View on GitHub</a></p>
  </footer>
</div>
