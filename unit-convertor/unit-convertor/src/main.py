import streamlit as st
from length_converter import LengthConverter
from time_converter import TimeConverter
from mass_converter import MassConverter

# Set page configuration
st.set_page_config(
    page_title="Unit Converter",
    page_icon="🔄",
    layout="wide"
)


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .stButton>button {
        background-color: #FF8C00 !important;
        color: white !important;
        border-radius: 5px;
        font-size: 16px;
    }

    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.title("🔄 Unit Converter")
    
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Length Converter", "Time Converter", "Mass Converter"])

    if page == "Length Converter":
        st.header("📏 Length Converter")
        length_converter = LengthConverter()
        length_units = ["Meters", "Kilometers", "Miles", "Feet"]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            length_from = st.selectbox("Convert from:", length_units)
        with col2:
            length_to = st.selectbox("Convert to:", length_units)
        with col3:
            length_value = st.number_input("Value:", min_value=0.0)
        
        if st.button("Convert Length"):
            result = length_converter.convert(length_value, length_from, length_to)
            st.success(f"{length_value} {length_from} = {result} {length_to}")

    elif page == "Time Converter":
        st.header("⏰ Time Converter")
        time_converter = TimeConverter()
        time_units = ["Seconds", "Minutes", "Hours"]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            time_from = st.selectbox("Convert from:", time_units, key="time_from")
        with col2:
            time_to = st.selectbox("Convert to:", time_units, key="time_to")
        with col3:
            time_value = st.number_input("Value:", min_value=0.0, key="time_value")
        
        if st.button("Convert Time"):
            result = time_converter.convert(time_value, time_from, time_to)
            st.success(f"{time_value} {time_from} = {result} {time_to}")

    elif page == "Mass Converter":
        st.header("⚖️ Mass Converter")
        mass_converter = MassConverter()
        mass_units = ["Grams", "Kilograms", "Pounds"]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            mass_from = st.selectbox("Convert from:", mass_units, key="mass_from")
        with col2:
            mass_to = st.selectbox("Convert to:", mass_units, key="mass_to")
        with col3:
            mass_value = st.number_input("Value:", min_value=0.0, key="mass_value")
        
        if st.button("Convert Mass"):
            result = mass_converter.convert(mass_value, mass_from, mass_to)
            st.success(f"{mass_value} {mass_from} = {result} {mass_to}")

if __name__ == "__main__":
    main()
