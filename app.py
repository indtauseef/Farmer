import streamlit as st

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

# --- Rule-Based Simple Recommendation ---
def recommend_crop(region, season, water, land_size, budget, previous_crop):
    # Basic sample rules (you can replace with ML model later)
    if region == "Bihar" and season == "Kharif":
        if water == "Medium" and land_size == "Small" and budget == "Low" and previous_crop == "Wheat":
            return ["Rice", "Maize", "Pulses"]
        elif water == "High":
            return ["Rice", "Sugarcane"]
        else:
            return ["Maize", "Pulses"]
    elif region == "Punjab" and season == "Rabi":
        return ["Wheat", "Barley", "Mustard"]
    elif region == "Tamil Nadu" and season == "Kharif":
        return ["Rice", "Cotton", "Groundnut"]
    else:
        return ["Rice", "Wheat", "Maize"]  # Default recommendation

# --- Prediction Button ---
if st.button("🔍 Get Recommendation"):
    crops = recommend_crop(region, season, water, land_size, budget, previous_crop)
    st.success(f"✅ Recommended Crops for {region} ({season}):")
    for crop in crops:
        st.write(f"- 🌱 {crop}")

