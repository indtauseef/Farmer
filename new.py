import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="AI Crop Recommender", page_icon="🌾", layout="centered")

# Custom CSS for black background & white text
st.markdown(
    """
    <style>
        .stApp {
            background-color: black;
            color: white;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #00FF7F;
        }
        .stSelectbox label, .stRadio label, .stButton button {
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title & Description ---
st.title("🌾 AI Crop Recommendation for Farmers")
st.write("Get the best crop recommendation based on your state, region, resources, and past crop.")

# --- Input Fields ---
state = st.selectbox("Select State", ["Uttar Pradesh", "Jharkhand"])

if state == "Uttar Pradesh":
    region = st.selectbox("Select Region", ["North UP", "South UP", "East UP", "West UP", "Central UP"])
elif state == "Jharkhand":
    region = st.selectbox("Select Region", ["North Jharkhand", "South Jharkhand", "East Jharkhand", "West Jharkhand", "Central Jharkhand"])
else:
    region = "General"

season = st.selectbox("Select Season", ["Kharif", "Rabi", "Zaid"])
soiltype = st.selectbox("Select Season",["alluvial soil","loamy soil","clayey soil","black soil","Sandy soil"])
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
    # Uttar Pradesh
    if state == "Uttar Pradesh":
        if region == "West UP" and season == "Kharif":
            if water == "High" and budget != "Low":
                return "Sugarcane"
            elif water == "Medium":
                return "Rice"
            else:
                return "Maize"
            
        
        elif region == "East UP" and season == "Rabi":
            if water == "low" and soiltype == "loamy soil":
                return "Mustard"
            elif water == "Medium":
                return "Wheat"
            else:
                return "Pulses"
        
        elif region == "North UP" and season == "Rabi":
            return "Wheat" if water != "Low" else "Barley"
        
        elif region == "South UP" and season == "Kharif":
            return "Rice" if water == "High" else "Cotton"
        
        elif region == "Central UP":
            return "Rice" if season == "Kharif" else "Wheat"

    # Jharkhand
    elif state == "Jharkhand":
        if region == "North Jharkhand" and season == "Kharif":
            return "Rice" if water == "High" else "Maize"
        
        elif region == "South Jharkhand" and season == "Rabi":
            return "Wheat" if water != "Low" else "Mustard"
        
        elif region == "East Jharkhand":
            return "Rice" if water == "High" else "Pulses"
        
        elif region == "West Jharkhand":
            return "Groundnut" if water == "Low" else "Maize"
        
        elif region == "Central Jharkhand":
            return "Rice" if season == "Kharif" else "Wheat"
    
    # Default
    return "Rice"

# --- Prediction Button ---
if st.button("🔍 Get Recommendation"):
    crop = recommend_crop(state, region, season, water, land_size, budget, previous_crop)

    st.success(f"✅ Recommended Crop for *{region}, {state} ({season} season): **{crop}*")
    
    if crop in crop_images:
        st.image(crop_images[crop], caption=f"{crop} grown in {region}, {state}", use_container_width=True)
