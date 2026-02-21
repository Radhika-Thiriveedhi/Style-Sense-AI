import requests
import base64

# 🔐 PASTE YOUR STABILITY API KEY HERE
STABILITY_API_KEY = "stability_API_Key"

API_URL = "https://api.stability.ai/v2beta/stable-image/generate/core"

headers = {
    "Authorization": f"Bearer {STABILITY_API_KEY}",
    "Accept": "application/json"
}


def generate_image(prompt):

    response = requests.post(
        API_URL,
        headers=headers,
        files={
            "prompt": (None, prompt),
            "output_format": (None, "png"),
            "aspect_ratio": (None, "1:1")
        },
        timeout=60
    )

    if response.status_code != 200:
        print("Stability Error:", response.text)
        return None

    data = response.json()

    if "image" in data:
        image_base64 = data["image"]
    elif "artifacts" in data:
        image_base64 = data["artifacts"][0]["base64"]
    else:
        return None

    return base64.b64decode(image_base64)