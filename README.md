# 👗 StyleSense AI  
### Generative AI–Powered Fashion Recommendation System

StyleSense AI is an intelligent fashion recommendation system that generates personalized outfit suggestions based on user preferences and optional camera input.

It combines:
- 🧠 LLM-based outfit generation (Groq - LLaMA)
- 🎨 AI image generation (Stability AI)
- 📸 Camera-based personalization (Streamlit)

---

## 🚀 Features

- Gender-based outfit recommendations
- Occasion-based styling
- Budget-aware suggestions
- Preferred color matching
- Camera-enabled personalization
- AI-generated outfit visuals
- Grand accessory recommendations

---

## 🛠 Tech Stack

- **Frontend:** Streamlit  
- **LLM Engine:** Groq (LLaMA 3.1 8B)  
- **Image Generation:** Stability AI  
- **Language:** Python  

---

## 📂 Project Structure

```
genAI hackton/
│
├── app.py
├── requirements.txt
└── stylesense/
      ├── __init__.py
      ├── llm_engine.py
      └── image_engine.py
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone <your-repo-link>
cd genAI-hackton
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 API Keys Setup

Add your API keys directly inside:

### 📌 stylesense/llm_engine.py

```python
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
```

### 📌 stylesense/image_engine.py

```python
STABILITY_API_KEY = "YOUR_STABILITY_API_KEY"
```

⚠️ Do NOT push API keys to public GitHub.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

App will open at:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. User selects preferences (gender, occasion, budget, color)
2. Optional: User uploads photo via camera
3. LLM generates 3 structured outfit recommendations
4. Stability AI generates visual representation
5. Accessories are included for premium styling

---

## 🎯 Use Case

- Personal styling assistant
- E-commerce fashion recommendation
- Wedding / event outfit planner
- Hackathon GenAI demo project

---

## 📸 Demo Output

- AI-generated fashion images
- Structured outfit descriptions
- Grand accessory suggestions

---

## 🔮 Future Improvements

- Real body-type detection using vision models
- Skin tone color harmony matching
- Outfit saving & rating system
- User preference memory
- AR virtual try-on integration

---

## 👩‍💻 Developed For

GenAI Hackathon Challenge  
Theme: Generative AI in Fashion Technology

---

## 📄 License

This project is built for educational and hackathon purposes.
