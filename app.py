import streamlit as st
from PIL import Image

# Set page config to set the layout and initial settings
st.set_page_config(page_title="Flight Passenger Time Series Analysis", layout="centered")

# Custom CSS to match the Flask webpage styling with updated heading colors and width
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;
        }
        .main {
            background-color: #f0f4f8;
            color: #333;
            font-family: Arial, sans-serif;
        }
        h1 {
            background-color: #212b4a;
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 2.3rem;
            max-width: 100%;  /* Adjust width of the main heading */
            margin: 0 auto;  /* Center the main heading */
        }
        .project-description {
            margin-bottom: 40px;
            text-align: center;
            color: #333;
        }
        .section-header h2 {
            color: black;  /* Make the section headers black */
            text-align: center;
            margin-top: 20px;
            font-size: 1.5rem;
        }
        .footer {
            text-align: center;
            padding: 20px;
            background-color: #212b4a;
            color: white;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the page
st.markdown('<h1>Flight Passenger Time Series Analysis</h1>', unsafe_allow_html=True)

st.markdown("   ")

# Description of the project
st.markdown("""
<div class="project-description">
    This project focuses on forecasting airline passenger traffic using time series analysis.
    By analyzing monthly passenger data from 1949 to 1960, I employed ARIMA and SARIMAX models
    to predict future trends. The SARIMAX model, in particular, effectively captures seasonal
    patterns, providing valuable insights into future passenger numbers, helping airlines optimize
    operations and plan for future demand.
</div>
""", unsafe_allow_html=True)

# Section to upload the final prediction image
st.markdown('<div class="section-header"><h2>Future Prediction</h2></div>', unsafe_allow_html=True)
##uploaded_file = st.file_uploader("Upload the final prediction graph", type="png")

##if uploaded_file is not None:
    # Display the uploaded image
    ##image = Image.open(uploaded_file)
    ##st.image(image, caption='Uploaded Future Prediction Graph', use_column_width=True)
##else:
    # Placeholder for the image if not uploaded
st.image("static/final.png", caption="Future Prediction")

# Display other images as per the original layout
st.markdown('<div class="section-header"><h2>Arima Correlation Analysis</h2></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.image("static/arima_pacf.png", caption="ARIMA Partial Autocorrelation")
with col2:
    st.image("static/arima_acf.png", caption="ARIMA Autocorrelation")


st.markdown('<div class="section-header"><h2>SARIMAX Correlation Analysis</h2></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.image("static/sar1.png", caption="SARIMAX Partial Autocorrelation")
with col2:
    st.image("static/sar2.png", caption="SARIMAX Autocorrelation")

st.markdown('<div class="section-header"><h2>Rolling Mean and Standard Deviation</h2></div>', unsafe_allow_html=True)
st.image("static/rolling_mean_std.png", caption="Rolling Mean and Std")

# Footer
st.markdown('<div class="footer"><p>Created by Avani Choudhary</p></div>', unsafe_allow_html=True)
