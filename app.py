import streamlit as st

def convert_units(category, from_unit, to_unit, value):
    formulas = ""
    result = None
    
    conversions = {
        "Length": {
            ("Meters", "Kilometers"): (value / 1000, "value / 1000"),
            ("Kilometers", "Meters"): (value * 1000, "value * 1000"),
            ("Feet", "Meters"): (value * 0.3048, "value * 0.3048"),
            ("Meters", "Feet"): (value / 0.3048, "value / 0.3048"),
            ("Inches", "Centimeters"): (value * 2.54, "value * 2.54"),
            ("Centimeters", "Inches"): (value / 2.54, "value / 2.54"),
            ("Yards", "Meters"): (value * 0.9144, "value * 0.9144"),
            ("Meters", "Yards"): (value / 0.9144, "value / 0.9144"),
        },
        "Weight": {
            ("Kilograms", "Grams"): (value * 1000, "value * 1000"),
            ("Grams", "Kilograms"): (value / 1000, "value / 1000"),
            ("Pounds", "Kilograms"): (value * 0.453592, "value * 0.453592"),
            ("Kilograms", "Pounds"): (value / 0.453592, "value / 0.453592"),
        },
        "Temperature": {
            ("Celsius", "Fahrenheit"): (value * 9/5 + 32, "(value * 9/5) + 32"),
            ("Fahrenheit", "Celsius"): ((value - 32) * 5/9, "(value - 32) * 5/9"),
            ("Celsius", "Kelvin"): (value + 273.15, "value + 273.15"),
        },
        "Speed": {
            ("Km/h", "Miles/h"): (value * 0.621371, "value * 0.621371"),
            ("Miles/h", "Km/h"): (value / 0.621371, "value / 0.621371"),
        },
        "Volume": {
            ("Liters", "Milliliters"): (value * 1000, "value * 1000"),
            ("Milliliters", "Liters"): (value / 1000, "value / 1000"),
        },
        "Time": {
            ("Hours", "Minutes"): (value * 60, "value * 60"),
            ("Minutes", "Seconds"): (value * 60, "value * 60"),
        }
    }
    
    if category in conversions and (from_unit, to_unit) in conversions[category]:
        result, formulas = conversions[category][(from_unit, to_unit)]
    return result, formulas

st.set_page_config(page_title="Smart Unit Converter", layout="centered")

st.markdown(
    """
     <style>
        /* Full-page background */
        body {
            background-color: #FBE9E7; /* Pastel Yellowish-Pink */
        }

        /* Left Sidebar Background */
        div[data-testid="stSidebar"] {
            background-color: #FBE9E7 !important; /* Pastel Yellowish-Pink */
            color: black;
        }

        /* Make sure sidebar elements get the background */
        div[data-testid="stSidebar"] * {
            background-color: #FBE9E7 !important; /* Ensures inner elements match the sidebar */
            color: black !important;
        }

        /* Ensuring radio button options also follow the background color */
        div[data-testid="stRadio"] label {
            color: black !important;
            font-weight: bold;
            padding-top: 0.5em;
            font-size: 2em
        }

        /* Sidebar title */
        div[data-testid="stSidebar"] h1, 
        div[data-testid="stSidebar"] h2, 
        div[data-testid="stSidebar"] h3 {
            color: black;
        }

        /* Styling Buttons */
        .stButton > button {
            border-radius: 10px;
            background-color: #FFAB91; /* Soft orange-pink */
            color: white;
            font-size: 16px;
            font-weight: bold;
        }

        /* Styling Input Fields */
        .stTextInput, .stSelectbox, .stNumberInput {
            background-color: lightgreen;
            color: white;
            font-size: large;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("🔄 Smart Unit Converter")
category = st.sidebar.radio("Select Category", ["Length", "Weight", "Temperature", "Speed", "Volume", "Time"])

unit_options = {
    "Length": ["Meters", "Kilometers", "Feet", "Inches", "Centimeters", "Yards"],
    "Weight": ["Kilograms", "Grams", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Speed": ["Km/h", "Miles/h"],
    "Volume": ["Liters", "Milliliters"],
    "Time": ["Hours", "Minutes", "Seconds"],
}

st.markdown("## ⚖️ 🌡️ ⏳  Smart Unit Convertor App")
st.info("Select a category and enter values to convert units instantly.")

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        from_unit = st.selectbox("From Unit", unit_options[category])
        value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    
    with col2:
        to_unit = st.selectbox("To Unit", unit_options[category])
        st.write("")
        convert_btn = st.button("Convert", use_container_width=True)

if convert_btn:
    converted_value, formula = convert_units(category, from_unit, to_unit, value)
    if converted_value is not None:
        st.success(f"### ✅ Conversion Formula: {formula}")
        st.info(f"### 🎯 Converted Value: {converted_value:.2f} {to_unit}")
    else:
        st.error("❌ Invalid Conversion")

st.markdown("### 📌 Example Conversions:")
st.markdown("- 1 Meter = 100 Centimeters")
st.markdown("- 1 Kilogram = 1000 Grams")
st.markdown("- 1 Hour = 60 Minutes")
