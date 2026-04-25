# Car Damage Classifier

A FastAI (PyTorch) image classifier that detects **car damage types** across **12 categories**, trained on **4,500+ images** and deployed with **Gradio on HuggingFace Spaces**.

## Live demo

- **Interactive web demo (this site)**: open `car_damage.html` in this `docs/` folder
- **HuggingFace Spaces**: `wrezachow/car-damage-classifier` (called via `@gradio/client`)

## Results summary

- **Best model**: ResNet50 — **78.03% accuracy**
- **Other models**: ResNet34 (77.93%), EfficientNet-B0 (72.18%)
- Strong classes include **Broken Side Mirror (98.9%)**, **Flat Tire (95.5%)**, **Rust/Corrosion (94.7%)**
- Harder classes include **Car Scratch (58.6%)** and **Fire Damage (66.7%)**

## Technical details

- **Framework**: FastAI + PyTorch
- **Exported model**: FastAI learner (`.pkl`) loaded in `app.py`
- **Deployment**: HuggingFace Spaces (Gradio)
- **Web UI**: `docs/car_damage.html` connects to the Space and calls the `/predict` API via `@gradio/client`

## Demo usage

1. Open `car_damage.html`
2. Upload a car image
3. Click **Predict**
4. Review the predicted class + confidence scores (top 5)

