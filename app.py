import io
import streamlit as st 
from PIL import Image
import time

st.header("PNG to JPG converter🖼️➡️📷")
st.write("Easily converts you PNG file to JPG file allowing to manipulate and modify the image.🌆")
def convert_png_to_jpg(image):
    # Convert the image to RGB mode (JPG doesn't support transparency)
    rgb_image = image.convert("RGB")
    return rgb_image
image_uploader = st.file_uploader("📤 Upload your PNG file", type=["png"])
if image_uploader  is not None:
    im = Image.open(image_uploader)
    st.image(im, caption="Uploaded PNG", use_container_width=True)
    # Resize the image
    st.subheader("Resize Image")
    new_width = st.number_input("New Width", value=im.width, min_value=1)
    new_height = st.number_input("New Height", value=im.height, min_value=1)
    resized_image = im.resize((new_width, new_height))
    st.image(resized_image, caption="Resized Image", use_container_width=True)
    st.header("🛠️🔄converting PNG to JPG")
    if im != resized_image:
        with st.status("Converting"):
            time.sleep(7)
            jpg = convert_png_to_jpg(resized_image)
            st.success("Conversion complete!✅")

        st.image(jpg, caption="Converted JPG and Resized Image", use_container_width=True)

        buffer = io.BytesIO()
        jpg.save(buffer, format="JPEG")
        dataBytes = buffer.getvalue()

        st.download_button(
        label="Download JPG File",
        data=dataBytes,
        file_name="convert_png_to_jpg",
        mime="Image/jpeg"
       
        )
    else:
        print("Something went wrong!!!⚠️⚠️")

st.markdown("---")  # Adds a horizontal line
st.markdown("© 2025 PNG to JPG converter. All rights reserved.")     


