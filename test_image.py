from stylesense.image_engine import generate_image

print("Starting Stable Diffusion test...")

prompt = "Full body fashion photo of a stylish woman wearing pastel blazer and denim, modern fashion, clean studio background"

image = generate_image(prompt)

if image:
    with open("test_output.png", "wb") as f:
        f.write(image)
    print("Image saved as test_output.png")
else:
    print("Image generation failed")