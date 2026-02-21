from groq import Groq

# 🔐 PASTE YOUR GROQ API KEY HERE
GROQ_API_KEY = "GROQ_API_KEY"

client = Groq(api_key=GROQ_API_KEY)


def analyze_user_image(image_bytes):
    """
    Stable hackathon-safe version.
    No vision model dependency.
    """
    return "User uploaded a personal photo. Suggest well-fitted, modern and flattering outfits accordingly."


def generate_outfits(gender, occasion, budget, color, image_analysis=None):

    prompt = f"""
You are a professional fashion stylist.

Generate 3 simple and easy-to-understand outfit recommendations.

Details:
Gender: {gender}
Occasion: {occasion}
Budget: {budget} INR
Preferred Color: {color}
Image Analysis: {image_analysis if image_analysis else "No image provided"}

For each outfit include:
- Title
- Description (max 2 simple lines)
-For each outfit include:

- Title:
- Description:
- Grand Accessories: (must list at least 3 specific items separated by commas)

Important:
You MUST fill Grand Accessories with actual items like jewelry, footwear, clutch, watch, etc.
Do not leave it empty.

Return clearly structured text like:

Outfit 1:
Title:
Description:
Grand Accessories:

Outfit 2:
Title:
Description:
Grand Accessories:

Outfit 3:
Title:
Description:
Grand Accessories:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content