import streamlit as st

# Title
st.title("🌾 AI Crop Recommendation System")

# Input fields
region = st.selectbox("Region", ["Jharkhand", "Bihar", "Uttar Pradesh"])
season = st.selectbox("Season", ["Kharif", "Rabi", "Zaid"])
water = st.selectbox("Water Availability", ["Low", "Medium", "High"])
land_size = st.selectbox("Land Size", ["Small", "Medium", "Large"])
budget = st.selectbox("Budget", ["Low", "Medium", "High"])
previous_crop = st.selectbox("Previous Crop", ["Wheat", "Rice", "Maize"])

# Recommendation logic (simple rules)
def recommend_crop(region, season, water, land_size, budget, previous_crop):
    if season == "Kharif" and water == "Medium" and land_size == "Small" and budget == "Low" and previous_crop == "Wheat":
        return "Maize"
    elif season == "Kharif" and water == "Medium":
        return "Rice"
    else:
        return "Wheat"

# Button to get recommendation
if st.button("Get Crop Recommendation"):
    crop = recommend_crop(region, season, water, land_size, budget, previous_crop)
    st.success(f"Recommended Crop: {crop}")
