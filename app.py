import streamlit as st

st.set_page_config(
    page_title="Digital Marketing Chatbot", page_icon="📰", layout="wide"
)

import os
from PIL import Image
import base64
from io import BytesIO
import tempfile
from dotenv import load_dotenv

load_dotenv(".env")

from scripts.ImageDescription import GetImageDescription
from scripts.ProductContent import GenerateProductContent


# Functions
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


@st.cache_data
def generate_content(user_inputs):
    st.session_state["product_content"] = GenerateProductContent(user_inputs)
    content = st.session_state["product_content"].generate_content()

    return content


# ---------------------------------------------------------------------------------------
# Session States


# ---------------------------------------------------------------------------------------
css_file_path = os.path.join("assets", "styles.css")
load_css(css_file_path)

st.title("Digital Marketing Chatbot")
st.write("A simplified tool to create content for product advertising")

image = st.file_uploader(
    label="Upload the image of the product that you want to advertise",
    type=["jpg"],
    accept_multiple_files=False,
)
if image is not None:
    st.session_state["uploaded_image"] = Image.open(image)

    # Saving the image temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        st.session_state["uploaded_image"].save(temp_file.name)
        image_path = temp_file.name

    if "image_description" not in st.session_state:
        st.session_state["image_description"] = GetImageDescription.describe(image_path)
        os.remove(image_path)

# if "uploaded_image" in st.session_state:
#     col2.markdown(
#         f'<link href="assets/styles.css" rel="stylesheet">',
#         unsafe_allow_html=True,
#     )
#     col2.image(
#         st.session_state["uploaded_image"],
#         use_column_width=False,
#         caption="Uploaded Image",
#         output_format="PNG",
#         width=150,
#     )

# st.divider()
# st.session_state
st.divider()
button = False

if "image_description" in st.session_state:

    with st.form("user-params"):

        col1, col2, col3 = st.columns([3, 1, 1], gap="small", vertical_alignment="top")
        buff, img_col = col1.columns([0.1, 0.55], gap="large")

        img_col.markdown(
            f'<link href="assets/styles.css" rel="stylesheet">',
            unsafe_allow_html=True,
        )
        img_col.image(
            st.session_state["uploaded_image"],
            use_column_width="never",
            caption="Uploaded Image",
            output_format="PNG",
            width=400,
        )

        st.session_state["user_description"] = col1.text_area(
            label="Image Description",
            value=st.session_state["image_description"],
            height=220,
        )

        user_inputs = {}
        user_inputs["image_description"] = st.session_state["user_description"]

        user_inputs["product_name"] = col2.text_input(
            label="Product Name", placeholder="Enter product name"
        )
        user_inputs["business_name"] = col3.text_input(
            label="Business Name",
            placeholder="Business name and type",
        )
        age_group = col2.slider(
            label="Target Age Group", min_value=0, max_value=100, value=(18, 65)
        )
        user_inputs["min_age"] = age_group[0]
        user_inputs["max_age"] = age_group[1]
        user_inputs["content_duration"] = col3.slider(
            label="Content Duration (seconds)",
            min_value=0,
            max_value=300,
            value=60,
            step=5,
        )
        content_goal = col2.multiselect(
            label="Content Goal",
            options=["Brand Awareness", "Sales", "Engagement"],
            max_selections=3,
            placeholder="Choose upto 3 goals",
        )
        user_inputs["content_goal"] = ", ".join(content_goal)

        hooks = col3.multiselect(
            label="Hooks",
            options=[
                "Emotional",
                "Story-telling",
                "Curiosity",
                "Comparison",
                "Cultural",
                "Quotation",
                "Question",
                "Humor",
                "Statistics",
                "Eye",
            ],
            placeholder="Choose upto 2 hooks",
            max_selections=2,
        )
        user_inputs["hooks"] = ", ".join(hooks)

        user_inputs["region"] = col2.text_input(
            label="Target Region", placeholder="State/Country"
        )
        user_inputs["occasion_type"] = col3.text_input(
            label="Special Occasion", placeholder="Special day if any"
        )

        user_inputs["language"] = col2.selectbox(
            label="Language", options=["English", "Hindi", "Tamil"]
        )
        user_inputs["social_media"] = col3.selectbox(
            label="Social Media",
            options=["Facebook", "Instagram", "YouTube", "Twitter"],
        )
        user_inputs["word_count"] = col2.slider(
            label="Word Count", min_value=150, max_value=500, value=150, step=50
        )
        user_inputs["temperature"] = col3.slider(
            label="Model Creativity",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.1,
        )
        user_inputs["target_customer"] = col2.selectbox(
            label="Target Customer", options=["Wholesaler", "Retailer"]
        )
        user_inputs["content_type"] = col3.selectbox(
            label="Content Type",
            options=["Voiceover Script", "Post Caption"],
            placeholder="Select content type",
        )

        button = st.form_submit_button("Generate Content")

if button is True:
    content = generate_content(user_inputs)

    st.markdown(
        f"""
        <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px; background-color: #f8f8f8;">
            <p style="white-space: pre-wrap;">{content}</p> 
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Create a download button
    st.download_button(
        label="Download Content",
        data=content,
        file_name="generated_content.txt",
        mime="text/plain",
    )

    # st.write(content)
    # st.write("Content Generated Successfully!")
