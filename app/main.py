from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from ultralytics import YOLO
from PIL import Image
import os
import shutil

# ======================================
# Paths
# ======================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "best.pt")
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")
UI_DIR = os.path.join(BASE_DIR, "ui")

os.makedirs(OUTPUTS_DIR, exist_ok=True)

# ======================================
# Load Model
# ======================================

print("🔄 Loading Tomato Detection Model...")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Model not found in models/best.pt")

model = YOLO(MODEL_PATH)

print("✅ Model Loaded Successfully!")

# ======================================
# FastAPI App
# ======================================

app = FastAPI(title="Tomato Disease Detection Platform")

app.mount("/outputs", StaticFiles(directory=OUTPUTS_DIR), name="outputs")

@app.get("/", response_class=HTMLResponse)
def home():
    with open(os.path.join(UI_DIR, "index.html"), "r", encoding="utf-8") as f:
        return f.read()

# ======================================
# Detection Endpoint
# ======================================

@app.post("/detect-image")
async def detect_image(file: UploadFile = File(...)):

    input_path = os.path.join(OUTPUTS_DIR, file.filename)

    # Save uploaded image
    with open(input_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Run detection
    results = model.predict(source=input_path, conf=0.25)

    result = results[0]

    # If nothing detected
    if result.boxes is None or len(result.boxes) == 0:
        return {
            "message": "لم يتم اكتشاف أي مرض",
            "num_detections": 0,
            "label": "No Detection",
            "confidence": 0,
            "result_image": file.filename
        }

    # Draw bounding boxes
    plotted = result.plot()

    output_name = "result_" + file.filename
    output_path = os.path.join(OUTPUTS_DIR, output_name)

    Image.fromarray(plotted).save(output_path)

    # Get first detection
    box = result.boxes[0]
    class_id = int(box.cls[0])
    confidence = float(box.conf[0])
    label = model.names[class_id]

    return {
        "message": "تم تحليل الصورة بنجاح",
        "num_detections": len(result.boxes),
        "label": label,
        "confidence": round(confidence * 100, 2),
        "result_image": output_name
    }