import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Output directory
output_dir = Path('../docs/assets/charts')
output_dir.mkdir(parents=True, exist_ok=True)

# Set style
plt.style.use('dark_background')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.facecolor'] = '#0b1220'
plt.rcParams['axes.facecolor'] = '#0b1220'

# 1. Model Comparison Chart
models = ['ResNet34', 'ResNet50', 'EfficientNet-B0']
accuracies = [77.93, 78.03, 72.18]
colors = ['#7c3aed', '#a855f7', '#22c55e']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(models, accuracies, color=colors, edgecolor='white', linewidth=0.5)
ax.set_xlabel('Accuracy (%)', fontsize=12, color='white')
ax.set_title('Model Accuracy Comparison', fontsize=16, color='white', pad=20)
ax.set_xlim(0, 100)

# Add value labels
for bar, acc in zip(bars, accuracies):
    ax.text(acc + 1, bar.get_y() + bar.get_height()/2,
            f'{acc:.2f}%', va='center', fontsize=11, color='white')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('white')
ax.spines['bottom'].set_color('white')
ax.tick_params(colors='white')

plt.tight_layout()
plt.savefig(output_dir / 'model-comparison.png', dpi=150,
            facecolor='#0b1220', transparent=False)
print("[OK] Generated model-comparison.png")
plt.close()

# 2. Per-Class Accuracy Chart
classes = [
    'Broken Side Mirror', 'Flat Tire', 'Rust/Corrosion',
    'Broken Bumper', 'Cracked Windshield', 'Vandalism/Keyed',
    'Flood Damage', 'Car Dent', 'Hail Damage', 'No Damage',
    'Fire Damage', 'Car Scratch'
]
class_accs = [98.9, 95.5, 94.7, 89.3, 89.0, 81.5, 81.7, 80.3, 79.4, 79.7, 66.7, 58.6]

# Sort by accuracy
sorted_data = sorted(zip(classes, class_accs), key=lambda x: x[1], reverse=True)
sorted_classes, sorted_accs = zip(*sorted_data)

# Color code by accuracy
colors = ['#22c55e' if acc > 90 else '#f59e0b' if acc > 70 else '#ef4444'
          for acc in sorted_accs]

fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.barh(sorted_classes, sorted_accs, color=colors, edgecolor='white', linewidth=0.5)
ax.set_xlabel('Accuracy (%)', fontsize=12, color='white')
ax.set_title('Per-Class Accuracy (ResNet50)', fontsize=16, color='white', pad=20)
ax.set_xlim(0, 100)

# Add value labels
for bar, acc in zip(bars, sorted_accs):
    ax.text(acc + 1, bar.get_y() + bar.get_height()/2,
            f'{acc:.1f}%', va='center', fontsize=10, color='white')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('white')
ax.spines['bottom'].set_color('white')
ax.tick_params(colors='white')

plt.tight_layout()
plt.savefig(output_dir / 'per-class-accuracy.png', dpi=150,
            facecolor='#0b1220', transparent=False)
print("[OK] Generated per-class-accuracy.png")
plt.close()

print("\nAll charts generated successfully!")
