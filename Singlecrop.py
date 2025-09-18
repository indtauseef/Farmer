import streamlit as st
import random

# --- Title & Description ---
st.set_page_config(page_title="AI Crop Recommender", page_icon="🌾")
st.title("🌾 AI Crop Recommendation for Farmers")
st.write("Get the best crop recommendation based on your region, resources, and past crop.")

# --- Input Fields ---
region = st.selectbox("Select Region (State)", [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
])

season = st.selectbox("Select Season", ["Kharif", "Rabi", "Zaid"])
water = st.selectbox("Water Availability", ["Low", "Medium", "High"])
land_size = st.selectbox("Land Size", ["Small", "Medium", "Large"])
budget = st.selectbox("Budget", ["Low", "Medium", "High"])
previous_crop = st.selectbox("Previous Crop", [
    "Wheat", "Rice", "Maize", "Sugarcane", "Cotton",
    "Barley", "Pulses", "Millets", "Mustard", "Groundnut"
])

# --- Crop Images (replace with your own local images or online links) ---
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
def recommend_crop(region, season, water, land_size, budget, previous_crop):
    if region == "Bihar" and season == "Kharif":
        if water == "Medium" and land_size == "Small" and budget == "Low" and previous_crop == "Wheat":
            return random.choice(["Rice", "Maize", "Pulses"])
        elif water == "High":
            return "Rice"
        else:
            return random.choice(["Maize", "Pulses"])
    elif region == "Punjab" and season == "Rabi":
        return random.choice(["Wheat", "Barley", "Mustard"])
    elif region == "Tamil Nadu" and season == "Kharif":
        return random.choice(["Rice", "Cotton", "Groundnut"])
    else:
        return random.choice(["Rice", "Wheat", "Maize"])  # Default

# --- Prediction Button ---
if st.button("🔍 Get Recommendation"):
    crop = recommend_crop(region, season, water, land_size, budget, previous_crop)

    st.success(f"✅ Recommended Crop for {region} ({season}): **{crop}**")
    if crop in crop_images:
        st.image(crop_images[crop], caption=f"{crop} Field", use_column_width=True)
