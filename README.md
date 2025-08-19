# 🌊 Hydropower Generation Calculator

A comprehensive Streamlit web application that uses industry-standard hydropower calculations to assess hydropower potential. This production-ready app provides professional-grade hydropower assessments with interactive visualizations and detailed economic analysis.

## 🚀 Features

### Core Functionality
- **Professional Calculations**: Industry-standard hydropower calculations with turbine-specific performance modeling
- **Interactive Interface**: User-friendly Streamlit interface with sliders, dropdowns, and input controls
- **Real-time Results**: Instant calculation updates with parameter changes
- **Comprehensive Analysis**: Power generation, economic metrics, and viability assessments

### Technical Capabilities
- **Multiple Turbine Types**: Kaplan, Francis, Pelton, Cross-flow, and Propeller turbines
- **Site Type Analysis**: Run-of-river, diversion, and impoundment projects
- **Economic Modeling**: LCOE, NPV, payback period, and cash flow analysis
- **Interactive Visualizations**: Plotly charts for power and economic analysis

### Advanced Features
- **Export Options**: CSV, JSON, and formatted text reports
- **Educational Content**: Comprehensive hydropower technology information
- **Professional Styling**: Clean, responsive design optimized for presentation
- **Error Handling**: Robust validation and error management

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Setup

1. **Clone or download this repository**
```bash
cd hydro-generate
```

2. **Create virtual environment**
```bash
python3 -m venv venv
```

3. **Activate virtual environment**
```bash
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Run the application**
```bash
# Using the provided script:
./run_app.sh

# Or directly:
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 🎯 Usage Guide

### 1. Home Page
- Overview of application features
- Quick start guide
- Sample project examples

### 2. Calculator Page
- **Site Parameters**: Enter head, flow rate, turbine type, and efficiency
- **Economic Parameters**: Set electricity prices, project lifetime, costs
- **Calculate**: Click the calculate button to generate results
- **Results Display**: View power generation and economic metrics

### 3. Analysis Page
- **Power Analysis**: Interactive charts showing power distribution and seasonal variations
- **Economic Analysis**: Cash flow projections and cost breakdowns
- **Visualizations**: Professional-grade Plotly charts

### 4. About Page
- **Educational Content**: Learn about hydropower technology
- **Turbine Types**: Detailed information about different turbine technologies
- **Applications**: Understanding different project types
- **Resources**: Links to additional information and tools

### 5. Export Page
- **Data Export**: Download results as CSV or JSON
- **Summary Reports**: Generate formatted text reports
- **Data Preview**: Review export data before downloading

## 🔧 Technical Details

### Calculations
The app performs industry-standard hydropower calculations:

```
Power (kW) = ρ × g × Q × H × η
```

Where:
- ρ = Water density (1000 kg/m³)
- g = Gravitational acceleration (9.81 m/s²)
- Q = Flow rate (m³/s)
- H = Net head (m)
- η = Overall efficiency (decimal)

### Economic Analysis
- **LCOE**: Levelized Cost of Energy calculation
- **NPV**: Net Present Value analysis
- **Payback Period**: Simple payback calculation
- **Cash Flow**: Annual revenue and O&M costs

### Libraries Used
- **Streamlit**: Web application framework
- **Plotly**: Interactive visualizations
- **Pandas**: Data manipulation
- **NumPy**: Numerical calculations
- **SciPy**: Scientific computing functions

## 📊 Input Parameters

### Site Parameters
- **Net Head**: 1-500m (vertical drop)
- **Flow Rate**: 0.1-1000 m³/s (design flow)
- **Turbine Type**: Kaplan, Francis, Pelton, Cross-flow, Propeller
- **Efficiency**: 80-95% (overall system efficiency)
- **Site Type**: Run-of-river, Diversion, Impoundment

### Economic Parameters
- **Electricity Price**: $20-200/MWh
- **Project Lifetime**: 20-50 years
- **Discount Rate**: 3-10%
- **Capacity Factor**: 30-90%
- **CAPEX**: $1000-8000/kW
- **O&M Costs**: 1-5% of CAPEX annually

## 🎨 Customization

### Styling
The app includes custom CSS for professional appearance:
- Gradient backgrounds
- Custom metric cards
- Responsive design
- Professional color scheme

### Adding Features
The modular design allows easy addition of:
- New turbine types
- Additional economic calculations
- More visualization options
- Enhanced export formats

## 🌐 Deployment

### Streamlit Cloud
1. Push code to GitHub repository
2. Connect to Streamlit Cloud
3. Deploy with `requirements.txt`

### Local Network
```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

### Docker (Optional)
Create a Dockerfile for containerized deployment:
```dockerfile
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## ⚠️ Important Notes

### Disclaimers
- This calculator provides preliminary estimates for educational and screening purposes
- Detailed engineering studies are required for actual project development
- Environmental assessments and site-specific analyses are necessary
- Consult qualified professionals for project implementation

### Limitations
- Simplified hydraulic calculations
- Generic turbine performance curves
- Approximate economic modeling
- No environmental impact assessment
- No detailed hydraulic analysis

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is open source. Please cite the HydroGenerate library when using this application.

## 📞 Support

For issues or questions:
- Check the About page for educational content
- Review the technical documentation
- Consult hydropower engineering resources

---

**Built with ❤️ using industry-standard hydropower calculations and Streamlit**

*Professional hydropower assessment made accessible*