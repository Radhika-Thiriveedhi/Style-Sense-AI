import streamlit as st
from stylesense.llm_engine import generate_outfits, analyze_user_image
from stylesense.image_engine import generate_image

st.set_page_config(page_title="StyleSense AI", layout="wide")

st.title(" StyleSense AI")
st.subheader("AI Powered Fashion Recommendation System")

st.sidebar.header("Style Preferences")

gender = st.sidebar.selectbox("Select Gender", ["Male", "Female"])
occasion = st.sidebar.text_input("Enter Occasion")
budget = st.sidebar.number_input("Enter Budget (INR)", min_value=500, step=500)
color = st.sidebar.text_input("Preferred Color")

uploaded_image = st.sidebar.camera_input("Take Your Picture")

generate = st.sidebar.button("Generate Recommendations")

if generate:

    if not occasion or not color:
        st.warning("Please fill all fields.")
    else:

        with st.spinner("Generating stylish looks..."):

            image_analysis = None

            if uploaded_image is not None:
                image_bytes = uploaded_image.getvalue()
                image_analysis = analyze_user_image(image_bytes)

            result = generate_outfits(
                gender,
                occasion,
                budget,
                color,
                image_analysis
            )

            outfits = result.split("Outfit ")[1:]

            st.markdown("##  Recommended Looks")

            cols = st.columns(3)

            for col, outfit in zip(cols, outfits):

                lines = [line.strip() for line in outfit.split("\n") if line.strip()]

                title = ""
                description = ""
                accessories = ""

                for line in lines:
                    if line.startswith("Title:"):
                        title = line.replace("Title:", "").strip()
                    elif line.startswith("Description:"):
                        description = line.replace("Description:", "").strip()
                    elif line.lower().startswith("grand accessories"):
                       accessories = line.split(":", 1)[1].strip()

                image_prompt = f"Full body fashion photo of {description}, high quality, modern style, clean background"

                image = generate_image(image_prompt)

                with col:
                    if image:
                        st.image(image)
                    else:
                        st.write("Image generation failed")

                    st.subheader(title)
                    st.write(description)
                    st.write("✨ Grand Accessories:")
                    st.write(accessories)