import os
from fastai.vision.all import PILImage, load_learner
import gradio as gr


def find_model():
    """Look for the model file"""
    here = os.path.dirname(os.path.abspath(__file__))

    # check different locations where it might be
    search_paths = [
        os.path.join(here, "CarDamageClassifierV1.pkl"),
        os.path.join(here, "models", "CarDamageClassifierV1.pkl"),
        os.path.join(here, "..", "models", "CarDamageClassifierV1.pkl"),
        os.path.join(os.getcwd(), "CarDamageClassifierV1.pkl"),
        os.path.join(os.getcwd(), "models", "CarDamageClassifierV1.pkl"),
    ]

    for path in search_paths:
        if os.path.exists(path):
            return path

    raise FileNotFoundError(f"Model file not found. Tried: {search_paths}")


# Load model and get class labels
learner = load_learner(find_model())
class_names = list(learner.dls.vocab)


def predict_damage(image_input):
    """Predict car damage type from image"""

    # convert input to PIL image
    img = PILImage.create(image_input)

    # get predictions
    predicted_class, class_idx, probabilities = learner.predict(img)
    confidence = probabilities[class_idx].item()

    # build results dict with all class probabilities
    results = dict(zip(class_names, map(float, probabilities)))

    # add a warning if confidence is low
    if confidence < 0.6:
        results["Low Confidence - Review Needed"] = 1 - confidence

    return results


# Build gradio interface
with gr.Blocks(title="Car Damage Classifier") as demo:
    gr.Markdown("# Car Damage Classifier")
    gr.Markdown(
        "Upload an image of a damaged car. "
        "The model will classify the type of damage. "
        "Predictions below 60% confidence will be flagged for review."
    )

    with gr.Row():
        with gr.Column():
            image = gr.Image(type="filepath", label="Upload Image")
        with gr.Column():
            output = gr.Label(num_top_classes=5, label="Results")

    with gr.Row():
        gr.Examples(
            examples=[
                "example_flood.jpg",
                "example_hail.avif",
                "example_rust.jpg",
                "example_windshield.jpg"
            ],
            inputs=image,
            label="Click an example to test"
        )
    
    with gr.Row():
        submit = gr.Button("Classify Damage", variant="primary", size="lg")
        clear = gr.Button("Clear", size="lg")

    # connect buttons to functions
    submit.click(predict_damage, inputs=image, outputs=output)
    clear.click(lambda: (None, None), outputs=[image, output])


if __name__ == "__main__":
    # launch the app
    # server_name and port are important for HF Spaces
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
    )