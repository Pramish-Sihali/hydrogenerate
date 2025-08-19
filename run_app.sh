#!/bin/bash

# Activate virtual environment and run Streamlit app
echo "🌊 Starting Hydropower Generation Calculator..."
echo "Activating virtual environment..."

source venv/bin/activate

echo "Checking if required packages are installed..."
python -c "import streamlit, plotly, pandas, numpy; print('✅ All packages installed successfully')"

echo "Starting Streamlit app..."
echo "🚀 App will open in your browser at http://localhost:8501"
echo "Press Ctrl+C to stop the application"

streamlit run app.py