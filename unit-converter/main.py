# import streamlit as st  

# def convert_units(value, unit_from, unit_to):

#     conversions={
#         "Meters_Kilometers": 0.001,
#         "Kilometers_Meters": 1000,
#         "Grams_Kilograms":0.001,
#         "Kilograms_Grams": 1000,
#         "Meters_Foots": 3.28084,
#         "Foots_Meters": 0.3048

#     } 

#     key = f"{unit_from}_{unit_to}"

#     if key in conversions:
#         conversion = conversions[key]
#         return value * conversion
#     else:
#         return "Conversion failed"     
    
# st.title("Unit Converter") 
# value = st.number_input("Enter the value:", min_value=1.0, step=1.0)

# unit_from = st.selectbox("Convert from:" , ["Meters","Kilometers","Grams","Kilograms","Foot"])
# unit_to = st.selectbox("Convert to:", ["Meters", "Kilometers","Grams","Kilograms","Foot"]) 

# if st.button("Convert"):
#     result = convert_units(value, unit_from,unit_to)
#     st.write(f"Converted Value:{result}")




import streamlit as st  
st.markdown("""
    <style>
    /* Increase font size for title */
    .css-1g1j9g4 {
        font-size: 40px !important;
    }
    /* Increase font size for the number input field */
    .stNumberInput input {
        font-size: 25px !important;
    }
    /* Increase font size for the select box */
    .stSelectbox select {
        font-size: 20px !important;
    }
    /* Increase font size for the button */
    .stButton button {
        font-size: 25px !important;
        padding: 10px 20px !important;
    }
    /* Increase font size for the result text */
    .stMarkdown {
        font-size: 30px !important;
    }
    </style>
""", unsafe_allow_html=True)

def convert_units(value, unit_from, unit_to):
    # Defining the conversions dictionary with more units
    conversions = {
        # Length 
        "Meters_Kilometers": 0.001,
        "Kilometers_Meters": 1000,
        "Meters_Feet": 3.28084,
        "Feet_Meters": 0.3048,
        "Meters_Inches": 39.3701,
        "Inches_Meters": 0.0254,

        # Weight 
        "Grams_Kilograms": 0.001,
        "Kilograms_Grams": 1000,
        "Grams_Ounces": 0.035274,
        "Ounces_Grams": 28.3495,
        "Kilograms_Pounds": 2.20462,
        "Pounds_Kilograms": 0.453592,

        # Temperature 
        "Celsius_Fahrenheit": lambda x: (x * 9/5) + 32,
        "Fahrenheit_Celsius": lambda x: (x - 32) * 5/9,
        "Celsius_Kelvin": lambda x: x + 273.15,
        "Kelvin_Celsius": lambda x: x - 273.15,
        "Fahrenheit_Kelvin": lambda x: (x - 32) * 5/9 + 273.15,
        "Kelvin_Fahrenheit": lambda x: (x - 273.15) * 9/5 + 32,
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        if callable(conversion):  # Handle temperature conversion (which is a function)
            return conversion(value)
        else: 
            return value * conversion
    else:
        return "Conversion not available for these units"

# Streamlit UI setup
st.title("🌍 Unit Converter")

# Input for value to convert
value = st.number_input("Enter the value ⏳:", min_value=1.0, step=1.0)

# Category selection for conversion
category = st.selectbox("Select Category 🤸‍♀️:", ["Length", "Weight", "Temperature"])

# Unit selection based on category
if category == "Length":
    unit_from = st.selectbox("Convert from ⚖️:", ["Meters", "Kilometers", "Feet", "Inches"])
    unit_to = st.selectbox("Convert to 📏:", ["Meters", "Kilometers", "Feet", "Inches"])
elif category == "Weight":
    unit_from = st.selectbox("Convert from ⚖️:", ["Grams", "Kilograms", "Ounces", "Pounds"])
    unit_to = st.selectbox("Convert to 📏:", ["Grams", "Kilograms", "Ounces", "Pounds"])
else:  # Temperature
    unit_from = st.selectbox("Convert from ⚖️:", ["Celsius", "Fahrenheit", "Kelvin"])
    unit_to = st.selectbox("Convert to 📏:", ["Celsius", "Fahrenheit", "Kelvin"])

# When convert button is pressed
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted Value: {result} {unit_to}")
