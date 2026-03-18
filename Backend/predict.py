import os
import pickle
import numpy as np

# -------------------------------
# Load Model (SAFE PATH HANDLING)
# -------------------------------
current_dir = os.path.dirname(__file__)

# Go to project root -> Model/model.pkl
model_path = os.path.abspath(
    os.path.join(current_dir, "..", "Model", "model.pkl")
)

# Check if file exists (prevents crash)
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at: {model_path}")

# Load model once (global)
with open(model_path, "rb") as f:
    model = pickle.load(f)


# -------------------------------
# Prediction Function
# -------------------------------
def predict_output(input_data: dict):
    """
    input_data: dictionary coming from API (JSON)
    Example:
    {
        "feature1": value1,
        "feature2": value2,
        ...
    }
    """

    try:
        # Convert dict → ordered list (IMPORTANT: match training order)
        features = list(input_data.values())

        # Convert to numpy array & reshape for model
        final_input = np.array(features).reshape(1, -1)

        # Prediction
        prediction = model.predict(final_input)

        # If classification → return label
        return {
            "prediction": prediction[0]
        }

    except Exception as e:
        return {
            "error": str(e)
        }