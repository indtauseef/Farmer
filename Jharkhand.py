import streamlit as st
import random

# --- Page Config (Black Background) ---
st.set_page_config(page_title="AI Crop Recommender", page_icon="🌾", layout="centered")

# Custom CSS for black background & white text
st.markdown(
    """
    <style>
        .stApp {
            background-color: black;
            color: white;
        }
        .stMarkdown, .stSelectbox, .stButton button, .stSuccess {
            color: white;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #00FF7F; /* Greenish title color */
        }
        /* make image captions more readable on dark bg */
        .stImage > figcaption {
            color: #ddd !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title & Description ---
st.title("🌾 AI Crop Recommendation for Farmers")
st.write("Get the best crop recommendation based on your state, region, resources, and past crop.")

# --- State Selection ---
state = st.selectbox("Select State", ["Uttar Pradesh", "Jharkhand"])

# --- Region Selection Based on State ---
if state == "Uttar Pradesh":
    region = st.selectbox("Select Region", ["North UP", "South UP", "East UP", "West UP", "Central UP"])
elif state == "Jharkhand":
    region = st.selectbox("Select Region", ["North Jharkhand", "South Jharkhand", "East Jharkhand", "West Jharkhand", "Central Jharkhand"])
else:
    region = "Unknown"

# --- Other Inputs ---
season = st.selectbox("Select Season", ["Kharif", "Rabi", "Zaid"])
water = st.selectbox("Water Availability", ["Low", "Medium", "High"])
land_size = st.selectbox("Land Size", ["Small", "Medium", "Large"])
budget = st.selectbox("Budget", ["Low", "Medium", "High"])
previous_crop = st.selectbox("Previous Crop", [
    "Wheat", "Rice", "Maize", "Sugarcane", "Cotton",
    "Barley", "Pulses", "Millets", "Mustard", "Groundnut"
])

# --- Crop Images ---
crop_images = {
    "Rice": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Rice_paddy_in_Japan.JPG",
    "Wheat": "https://upload.wikimedia.org/wikipedia/commons/4/47/Wheat_close-up.JPG",
    "Maize": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Corncobs.jpg",
    "Sugarcane": "https://upload.wikimedia.org/wikipedia/commons/5/54/Sugarcane_field_in_India.jpg",
    "Cotton": "https://upload.wikimedia.org/wikipedia/commons/1/19/CottonPlant.JPG",
    "Barley": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Barley_field_in_England.jpg",
    "Pulses": "https://upload.wikimedia.org/wikipedia/commons/8/87/Various_legumes.jpg",
    "Millets": "https://upload.wikimedia.org/wikipedia/commons/8/87/Millet_Field_India.jpg",
    "Mustard": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Mustard_fields_in_Punjab.jpg",
    "Groundnut": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Peanut_field.jpg"
}

# --- Rule-Based Recommendation ---
def recommend_crop(state, region, season, water, land_size, budget, previous_crop):
    # Uttar Pradesh logic
    if state == "Uttar Pradesh":
        if region == "West UP" and season == "Kharif":
            return random.choice(["Sugarcane", "Rice", "Maize"])
        elif region == "East UP" and season == "Rabi":
            return random.choice(["Wheat", "Pulses", "Mustard"])
        elif region == "North UP" and season == "Rabi":
            return random.choice(["Wheat", "Barley"])
        elif region == "South UP" and season == "Kharif":
            return random.choice(["Rice", "Cotton"])
        elif region == "Central UP":
            return random.choice(["Wheat", "Rice", "Maize"])
    
    # Jharkhand logic
    elif state == "Jharkhand":
        if region == "North Jharkhand" and season == "Kharif":
            return random.choice(["Rice", "Maize", "Pulses"])
        elif region == "South Jharkhand" and season == "Rabi":
            return random.choice(["Wheat", "Mustard"])
        elif region == "East Jharkhand":
            return random.choice(["Rice", "Pulses", "Millets"])
        elif region == "West Jharkhand":
            return random.choice(["Maize", "Groundnut"])
        elif region == "Central Jharkhand":
            return random.choice(["Rice", "Wheat", "Pulses"])
    
    # Default fallback
    return random.choice(["Rice", "Wheat", "Maize"])

# --- Prediction Button ---
if st.button("🔍 Get Recommendation"):
    crop = recommend_crop(state, region, season, water, land_size, budget, previous_crop)

    st.success(f"✅ Recommended Crop for **{state} - {region} ({season} season)**: **{crop}**")
    
    if crop in crop_images:
        # <--- replaced deprecated use_column_width with use_container_width
        st.image(crop_images[crop], caption=f"{crop} grown in {state} - {region}", use_container_width=True)
    else:
        st.info("No image available for the recommended crop.")
