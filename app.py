import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# Configure the Gemini API
#GOOGLE_API_KEY = "AIzaSyACjfESZsGJIo5ZaTWhEz3HgoRrsvxUKk4"
#genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('models/gemini-1.0-pro-vision-latest')
#Read the api key
with open("API Key.txt", "r") as f:
    key = f.read().strip()
# Define CSS for custom styling

# Custom CSS for styling
custom_css = """
<style>
/* Title */
.title {
    font-size: 36px;
    font-weight: bold;
    color: #333;
    text-align: center;
    margin-bottom: 30px;
}

/* Subtitle */
.subtitle {
    font-size: 24px;
    font-weight: bold;
    color: #666;
    margin-bottom: 20px;
}

/* Code area */
.code-area {
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 30px;
    background-color: #f9f9f9;
}

/* Button */
.button {
    display: inline-block;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    color: #fff;
    background-color: #0066cc;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.button:hover {
    background-color: #0056b3;
}

/* Form input */
input[type="text"] {
    padding: 10px;
    font-size: 16px;
    border-radius: 5px;
    border: 1px solid #ccc;
    width: 100%;
    margin-bottom: 20px;
}

/* Form button */
.form-button {
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    color: #fff;
    background-color: #00cc66;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.form-button:hover {
    background-color: #00b359;
}

</style>
"""
# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Title
st.markdown('<p class="title">IMAGE UNDERSTANDING AI-LIST OF ITEMS IN IMAGE </p>', unsafe_allow_html=True)



# Code area
st.markdown('<div class="code-area">You need to upload an Image in order to read', unsafe_allow_html=True)

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

def main():
    
    
    # File uploader widget to allow users to upload images
    uploaded_file = st.file_uploader("Upload image", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        try:
            # Convert bytes data to PIL Image
            image = Image.open(io.BytesIO(uploaded_file.read()))
            
            # Display the uploaded image
            st.image(image, caption='Uploaded image', use_column_width=True)
            
            # Generate AI response
            st.markdown("---")
            st.subheader("Image Explanation:")
            with st.spinner("Analyzing..."):
                 response = model.generate_content(image)
                
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

# Call the main function
if __name__ == "__main__":
    main()