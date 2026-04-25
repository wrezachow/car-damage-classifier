# Car Damage Classifier (FastAI + PyTorch)

End-to-end **car damage classification** across **12 categories** using **FastAI (PyTorch)**, deployed on **HuggingFace Spaces (Gradio)** with a lightweight **GitHub Pages** web demo.

- **Dataset**: 4,500+ labeled images across 12 damage/no-damage categories  
- **Best model**: **ResNet50 — 78.03% accuracy**  
- **Deployment**: HuggingFace Spaces (Gradio) + GitHub Pages UI (calls the Space API)

## Live demo

- **HuggingFace Spaces app**: `wrezachow/car-damage-classifier`  
- **GitHub Pages (web UI)**: (enable Pages on `/docs`)  
- **Web demo API**: called via `@gradio/client` (`/predict`)

## Categories (12)

1. Car Dent  
2. Car Scratch  
3. Cracked Windshield  
4. Broken Bumper  
5. Flat Tire  
6. Flood Damage  
7. Fire Damage  
8. Hail Damage  
9. Broken Side Mirror  
10. Rust/Corrosion  
11. Vandalism/Keyed  
12. No Damage

## Model comparison (trained models)

| Model | Framework | Top-1 Accuracy |
|---|---|---:|
| ResNet34 | FastAI + PyTorch | 77.93% |
| **ResNet50 (Best)** | FastAI + PyTorch | **78.03%** |
| EfficientNet-B0 | FastAI + PyTorch | 72.18% |

## Per-class accuracy (ResNet50 — best model)

| Class | Accuracy | Correct / Total |
|---|---:|---:|
| Broken Bumper | 89.3% | 67 / 75 |
| Broken Side Mirror | 98.9% | 90 / 91 |
| Car Dent | 80.3% | 59 / 91 |
| Car Scratch | 58.6% | 41 / 70 |
| Rust/Corrosion | 94.7% | 89 / 94 |
| Cracked Windshield | 89.0% | 65 / 73 |
| Fire Damage | 66.7% | 44 / 66 |
| Flat Tire | 95.5% | 84 / 88 |
| Flood Damage | 81.7% | 67 / 82 |
| Hail Damage | 79.4% | 54 / 68 |
| Vandalism/Keyed | 81.5% | 53 / 65 |
| No Damage | 79.7% | 47 / 59 |

## Most confused pairs (error patterns)

The most common confusions for visual damage classification typically come from **similar texture/shape cues**, **lighting**, and **small localized defects**. Based on the class semantics (and the usual failure modes for this task), the pairs most likely to be confused are:

- **Car Scratch ↔ Vandalism/Keyed**: both are linear paint damage; “keyed” often looks like a scratch without context.
- **Car Dent ↔ Broken Bumper**: bumper deformation vs dented panels can look similar depending on angle and crop.
- **Hail Damage ↔ Car Dent**: both can show multiple small dents; hail dents are often subtle.
- **No Damage ↔ (Car Scratch / Car Dent)**: minor scratches/dents are easy to miss at low resolution or under reflections.
- **Flood Damage ↔ No Damage**: many flood indicators are contextual (mud lines/interior water), which may not be visible in a tight crop.

If you have (or generate) a confusion matrix, replace this section with the **top-N confusion counts** for a data-driven breakdown.

## Project structure

```text
car-damage-classifier/
├─ deployment/
│  ├─ app.py
│  └─ requirements.txt
├─ models/
│  └─ CarDamageClassifierV1.pkl
└─ docs/
   ├─ index.md
   └─ car_damage.html
```

## Run locally

### 1) Create environment & install

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -r requirements.txt
```

### 2) Put the model export in the repo root

This project expects a FastAI export named:

- `models/CarDamageClassifierV1.pkl`

### 3) Start the Gradio app

```bash
python deployment/app.py
```

Open the printed local URL (usually `http://127.0.0.1:7860`).

## Deployment

### HuggingFace Spaces (Gradio)

1. Create a new Space (Gradio SDK).
2. Upload:
   - `app.py`
   - `requirements.txt`
   - `CarDamageClassifierV1.pkl`
3. The Space will launch automatically and expose an API endpoint compatible with the included GitHub Pages UI.

### GitHub Pages (docs/)

1. In GitHub repo settings, enable **Pages**:
   - Source: `main` branch  
   - Folder: `/docs`
2. Visit your Pages site and open the `car_damage.html` demo.

## License

Choose a license (e.g., MIT) and add `LICENSE` if you plan to open-source the project.

