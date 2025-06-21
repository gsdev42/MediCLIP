from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import google.generativeai as genai
import os
import uuid
from dotenv import load_dotenv

load_dotenv()  
API_KEY = os.getenv("API_KEY")
app = Flask(__name__)
CORS(app)  
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Initialize CLIP model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# List of disorders
disorders = [
    'lip swelling', 'mouth ulcer', 'swollen tonsil', 'swollen eye', 'eye redness',
    'itchy eyelid', 'edema', 'foot swelling', 'knee swelling', 'hand lumps',
    'neck swelling', 'skin rash', 'skin irritation', 'skin growth', 'dry scalp',
    'cyanosis', 'eye inflammation', 'skin dryness'
]


genai.configure(api_key=API_KEY)  
gemini_model = genai.GenerativeModel(model_name="gemini-1.5-flash")

print(gemini_model.generate_content("hello world").text)



def predict_disorders(image_path, description):
    image = Image.open(image_path).convert("RGB")
    inputs = clip_processor(text=disorders, images=image, return_tensors="pt", padding=True).to(device)

    with torch.no_grad():
        outputs = clip_model(**inputs)
        logits_per_image = outputs.logits_per_image
        probs = logits_per_image.softmax(dim=1).cpu().numpy()
    
    top_indices = probs.argsort()[0][-3:][::-1]  # Top 3 predictions
    top_disorders = [disorders[i] for i in top_indices]
    return top_disorders


def generate_summary(symptoms, disorders):
    prompt = f"Summarize the following symptoms and possible disorders in a concise medical report:\nSymptoms: {symptoms}\nPossible Disorders: {', '.join(disorders)}"
    response = gemini_model.generate_content(prompt)
    return response.text


@app.route('/api/analyze', methods=['POST'])
def analyze():
    print("Image received:", image.filename)
    print("Symptoms:", symptoms)

    if 'image' not in request.files or 'symptoms' not in request.form:
        return jsonify({"error": "Missing image or symptoms"}), 400
    
    image = request.files['image']
    symptoms = request.form['symptoms']
    
   
    image_path = f"temp_upload_{uuid.uuid4()}.jpg"
    image.save(image_path)

    try:
       
        predicted_disorders = predict_disorders(image_path, symptoms)
        

        summary = generate_summary(symptoms, predicted_disorders)
        

        return jsonify({
            "analysis": summary,
            "diagnosis": ", ".join(predicted_disorders)
        })
    except Exception as e:
        print(e)  
        return jsonify({"error": str(e)}), 500
    finally:
      
        if os.path.exists(image_path):
            os.remove(image_path)

@app.route('/')
def home():
    return "Welcome to the MediCLIP API! Use /api/analyze to submit your symptoms and image."

if __name__ == '__main__':
    app.run(debug=True, port=5000)



