import streamlit as st
import requests
import json

# Configuration
# When running locally, we point to localhost. 
# When deployed, we will update this URL.
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="OpenOA Dashboard", layout="wide")

# Header
st.title("OpenOA: Wind Plant Analysis Platform")
st.markdown("### Powered by NREL's OpenOA Library")

# Sidebar for inputs
with st.sidebar:
    st.header("Configuration")
    site_name = st.text_input("Site Name", "La Haute Borne")
    capacity = st.number_input("Capacity (MW)", min_value=1.0, value=12.5)
    
    if st.button("Run Analysis"):
        with st.spinner("Connecting to OpenOA API..."):
            try:
                # This calls your FastAPI backend
                payload = {"site_name": site_name, "capacity_mw": capacity}
                response = requests.post(f"{API_URL}/simulate_analysis", json=payload)
                
                if response.status_code == 200:
                    st.session_state['results'] = response.json()
                    st.success("Analysis Complete!")
                else:
                    st.error(f"API Error: {response.status_code}")
            except requests.exceptions.ConnectionError:
                st.error("Could not connect to Backend. Is the FastAPI server running?")

# Main Display Area
if 'results' in st.session_state:
    data = st.session_state['results']
    
    # metrics row
    col1, col2, col3 = st.columns(3)
    col1.metric("Site Name", data['site'])
    col2.metric("Plant Capacity", f"{data['capacity']} MW")
    col3.metric("Predicted AEP", f"{data['predicted_aep_gwh']:.2f} GWh")
    
    st.json(data)
else:
    st.info("Enter parameters in the sidebar and click 'Run Analysis' to start.")