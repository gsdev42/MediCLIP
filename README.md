# 🧠 MediCLIP: Multimodal AI for Medical Diagnosis and Question Summarization

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-API-lightgrey?style=flat&logo=flask)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface)
![Gemini](https://img.shields.io/badge/Google-Gemini-blue?logo=google)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🌟 Project Overview

**MediCLIP** is a research-inspired, web-based medical assistant that leverages the power of VLM's to provide **intelligent symptom analysis and potential diagnosis**. Users can input their symptoms and upload an image (e.g., of a rash, swelling, or eye irritation), and MediCLIP generates a medically relevant summary using advanced vision-language models.

> 💡 Inspired by the CLIPSyntel research paper and powered by **CLIP** + **Gemini**, MediCLIP bridges the gap between clinical data and AI understanding.

---

## 🚀 Features

- 🔍 **Symptom & Image Analysis** using OpenAI's CLIP
- 💬 **Medical Summary Generation** via Gemini (Google Generative AI)
- 🧠 Predefined medical disorder classes for improved grounding
- 🖼️ Upload and process real-world medical images (skin, eyes, etc.)
- 🧪 Fast, demo-ready Flask backend with CORS support
- 🖥️ Clean web interface for real-time interaction

---

## 🧩 Tech Stack

| Module        | Usage                                     |
|---------------|-------------------------------------------|
| 🐍 Python      | Backend logic, server-side processing     |
| 🔥 Flask       | RESTful API handling                      |
| 🤗 Transformers | CLIP model for image-text understanding |
| 🧠 Gemini AI   | Language model for diagnosis summaries    |
| 🌐 HTML/CSS/JS | Frontend for demo interaction             |

---

## 🛠️ How It Works

1. **User Inputs:**
   - Description of symptoms (e.g., "red itchy patch on leg")
   - Image of condition (e.g., rash, swelling)

2. **Processing Pipeline:**
   - CLIP compares image to a list of known disorders
   - Gemini LLM generates a summary using symptoms + predicted disorders

3. **Output:**
   - 📄 Medical summary
   - 🩺 Possible diagnosis (top 3 disorder classes)

---- 

For now, run locally:

```bash
git clone https://github.com/yourusername/mediCLIP
cd mediCLIP
pip install -r requirements.txt
python app.py
