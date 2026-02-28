# 🍅 Production-Grade Tomato Leaf Disease Classification Platform

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![YOLOv8](https://img.shields.io/badge/YOLOv8-DeepLearning-red)
![Agriculture AI](https://img.shields.io/badge/Domain-Smart%20Agriculture-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚜 Overview

A production-oriented computer vision platform for detecting tomato leaf diseases using deep learning.

This system enables farmers, researchers, and agricultural engineers to upload tomato leaf images and instantly receive disease classification predictions with confidence scores.

The project demonstrates real-world AI deployment principles including:

- Clean architecture
- Model separation
- Inference pipeline design
- REST API implementation
- Deployment readiness

---

## 🎯 Key Features

- 🍅 Multi-class tomato leaf disease classification
- ⚡ Fast inference using YOLOv8
- 🌐 Web-based user interface
- 📦 Modular and scalable backend
- 🧠 Production-ready architecture
- 🐳 Docker support

---

## 🏗 System Architecture

```
User Upload
    ↓
FastAPI Backend
    ↓
YOLOv8 Classification Model
    ↓
Prediction + Confidence Score
    ↓
Web Interface Display
```

This separation ensures scalability and maintainability.

---

## 📂 Project Structure

```
tomato-disease-ai/
│
├── app/
│   ├── main.py          # FastAPI backend logic
│   └── __init__.py
│
├── ui/
│   └── index.html       # Frontend interface
│
├── assets/              # Demo images for README
│
├── models/              # Place best.pt here (excluded)
│
├── outputs/             # Runtime inference outputs
│
├── requirements.txt
├── .gitignore
├── Dockerfile
├── LICENSE
└── README.md
```

---

## 🧠 Model Information

- Architecture: YOLOv8 Classification
- Framework: PyTorch
- Training Environment: Custom dataset (Tomato Leaf Diseases)
- Inference Mode: CPU / GPU supported

> Model weights are excluded due to size limitations.

### 📥 Setup Model

Place the trained model file as:

```
models/best.pt
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR-USERNAME/tomato-disease-ai.git
cd tomato-disease-ai
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
uvicorn app.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 🐳 Docker Deployment

Build image:

```bash
docker build -t tomato-ai .
```

Run container:

```bash
docker run -p 8000:8000 tomato-ai
```

---

## 📊 Model Validation

The model was validated using YOLOv8 built-in evaluation pipeline during training.

Detailed evaluation metrics are not included due to dataset constraints.

Validation can be reproduced using:

```python
from ultralytics import YOLO

model = YOLO("best.pt")
model.val(data="data.yaml")
```

---

## 🚀 Future Enhancements

- Real-time mobile integration
- Edge device deployment (Raspberry Pi / Jetson)
- Drone-based crop monitoring
- Agricultural analytics dashboard
- Disease severity estimation

---

## 🧑‍💻 Author

**Nader Al shawki**  
AI & Computer Vision Engineer  

Specialized in:
- Computer Vision
- Deep Learning
- AI Deployment
- Medical & Agricultural AI Systems

---

## 📜 License

This project is licensed under the MIT License.