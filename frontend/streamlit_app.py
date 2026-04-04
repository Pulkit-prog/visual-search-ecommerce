import streamlit as st
import requests
from PIL import Image

# -----------------------------------
# URLs
# -----------------------------------

# Used inside Docker (frontend -> backend)
API_URL = "http://backend:8000"

# Used by browser to render images
IMAGE_URL = "http://localhost:8000"


# -----------------------------------
# Page configuration
# -----------------------------------

st.set_page_config(
    page_title="AI Visual Search",
    layout="wide"
)

st.title("🛒 AI Visual Search Engine (E-Commerce)")
st.write("Upload an image and find visually similar products.")


# -----------------------------------
# Rebuild Index Section
# -----------------------------------

st.header("1️⃣ Rebuild Catalog Index")

if st.button("Rebuild Index"):

    with st.spinner("Rebuilding FAISS index..."):

        try:
            response = requests.post(f"{API_URL}/index/rebuild")

            if response.status_code == 200:
                st.success("Index rebuilt successfully!")
            else:
                st.error(f"Error rebuilding index: {response.text}")

        except Exception as e:
            st.error(f"Backend connection failed: {e}")


# -----------------------------------
# Upload Image Section
# -----------------------------------

st.header("2️⃣ Upload Query Image")

uploaded_file = st.file_uploader(
    "Upload product image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.subheader("Query Image")
    st.image(image, width=250)

    if st.button("Search Similar Products"):

        with st.spinner("Searching similar products..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }

            try:

                response = requests.post(
                    f"{API_URL}/search",
                    files=files
                )

                if response.status_code != 200:
                    st.error(f"Search failed: {response.text}")
                    st.stop()

                data = response.json()
                results = data.get("results", [])

                if not results:
                    st.warning("No similar products found.")
                    st.stop()

                st.subheader("🔎 Similar Products")

                cols = st.columns(4)

                for i, item in enumerate(results):

                    filename = item["image"]
                    score = item["score"]

                    img_url = f"{IMAGE_URL}/images/{filename}"

                    with cols[i % 4]:
                        st.image(img_url, use_container_width=True)
                        st.caption(f"Similarity Score: {score:.4f}")

            except Exception as e:
                st.error(f"Search request failed: {e}")


# -----------------------------------
# Footer
# -----------------------------------

st.markdown("---")

st.subheader("⚙️ Technology Stack")

st.markdown("""
• **ResNet50** feature embeddings  
• **FAISS** similarity search  
• **FastAPI** backend  
• **Streamlit** frontend  
• **Docker** containerized deployment  
""")