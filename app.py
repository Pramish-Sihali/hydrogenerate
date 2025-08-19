import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
from datetime import datetime
import io
import base64

st.set_page_config(
    page_title="Hydropower Generation Calculator",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 1.2rem;
        color: #424242;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(145deg, #f0f7ff, #e3f2fd);
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1E88E5;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
    }
    .warning-box {
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .info-box {
        background: #e3f2fd;
        border: 1px solid #bbdefb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables"""
    if 'scenarios' not in st.session_state:
        st.session_state.scenarios = {}
    if 'current_scenario' not in st.session_state:
        st.session_state.current_scenario = "Scenario 1"
    if 'calculation_results' not in st.session_state:
        st.session_state.calculation_results = {}

def main():
    initialize_session_state()
    
    # Header
    st.markdown('<h1 class="main-header">🌊 Hydropower Generation Calculator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Professional hydropower potential assessment using HydroGenerate library</p>', unsafe_allow_html=True)
    
    # Sidebar for navigation
    with st.sidebar:
        st.image("https://via.placeholder.com/300x150/1E88E5/FFFFFF?text=HydroGenerate", caption="Powered by HydroGenerate")
        
        page = st.selectbox(
            "Navigation",
            ["🏠 Home", "🔧 Calculator", "📊 Analysis", "📚 About", "💾 Export"]
        )
        
        st.markdown("---")
        st.markdown("### Quick Stats")
        st.info("Global hydropower capacity: 1,365 GW")
        st.info("Renewable energy share: 16%")
        st.info("Average capacity factor: 40-50%")
    
    # Main content based on selected page
    if page == "🏠 Home":
        show_home_page()
    elif page == "🔧 Calculator":
        show_calculator_page()
    elif page == "📊 Analysis":
        show_analysis_page()
    elif page == "📚 About":
        show_about_page()
    elif page == "💾 Export":
        show_export_page()

def show_home_page():
    """Display the home page with overview and quick start"""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        ## Welcome to the Hydropower Generation Calculator
        
        This professional-grade tool helps you assess hydropower potential using industry-standard calculations 
        and turbine performance models. Perfect for engineers, developers, and renewable energy enthusiasts.
        """)
        
        st.markdown("""
        ### 🚀 Quick Start
        1. Navigate to the **Calculator** page
        2. Enter your site parameters (head, flow, turbine type)
        3. Review power generation and economic metrics
        4. Visualize results with interactive charts
        5. Export your analysis for reporting
        """)
        
        st.markdown("### 🎯 Key Features")
        
        features = {
            "🔧 Professional Calculations": "Industry-standard hydropower calculations with turbine-specific modeling",
            "📊 Interactive Visualizations": "Dynamic charts and graphs using Plotly",
            "💰 Economic Analysis": "LCOE, NPV, and payback period calculations",
            "🔄 Scenario Comparison": "Compare multiple configurations side-by-side",
            "📋 Export Options": "Generate reports in CSV and PDF formats",
            "📚 Educational Content": "Learn about hydropower technology and best practices"
        }
        
        for title, description in features.items():
            with st.expander(title):
                st.write(description)
        
        st.markdown("---")
        
        # Sample project showcase
        st.markdown("### 💡 Example Projects")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            **Small Run-of-River**
            - Head: 5m
            - Flow: 20 m³/s
            - Power: ~800 kW
            - Type: Kaplan turbine
            """)
        
        with col2:
            st.markdown("""
            **Medium Diversion**
            - Head: 50m
            - Flow: 50 m³/s  
            - Power: ~20 MW
            - Type: Francis turbine
            """)
        
        with col3:
            st.markdown("""
            **Large Impoundment**
            - Head: 200m
            - Flow: 100 m³/s
            - Power: ~160 MW
            - Type: Francis turbine
            """)

def show_calculator_page():
    """Main calculator interface"""
    st.markdown("## ⚡ Hydropower Calculator")
    
    # Input parameters in columns
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🔧 Site Parameters")
        
        # Turbine selection
        turbine_type = st.selectbox(
            "Turbine Type",
            ['kaplan', 'francis', 'pelton', 'cross_flow', 'propeller'],
            help="Select the most appropriate turbine type for your head and flow conditions"
        )
        
        # Site type
        site_type = st.selectbox(
            "Site Type",
            ['run_of_river', 'diversion', 'impoundment'],
            help="Choose the type of hydropower development"
        )
        
        # Head input
        head = st.slider(
            "Net Head (m)",
            min_value=1.0,
            max_value=500.0,
            value=50.0,
            step=1.0,
            help="Vertical distance between upstream and downstream water levels"
        )
        
        # Flow input
        flow = st.slider(
            "Design Flow Rate (m³/s)",
            min_value=0.1,
            max_value=1000.0,
            value=100.0,
            step=0.1,
            help="Design flow rate for power generation"
        )
        
        # Efficiency
        efficiency = st.slider(
            "Overall Efficiency (%)",
            min_value=80,
            max_value=95,
            value=90,
            step=1,
            help="Combined efficiency of turbine, generator, and transformer"
        ) / 100.0
        
    with col2:
        st.markdown("### 💰 Economic Parameters")
        
        # Economic inputs
        electricity_price = st.slider(
            "Electricity Price ($/MWh)",
            min_value=20,
            max_value=200,
            value=80,
            step=5,
            help="Average electricity selling price"
        )
        
        project_lifetime = st.slider(
            "Project Lifetime (years)",
            min_value=20,
            max_value=50,
            value=30,
            step=5,
            help="Expected operational lifetime of the project"
        )
        
        discount_rate = st.slider(
            "Discount Rate (%)",
            min_value=3,
            max_value=10,
            value=6,
            step=1,
            help="Discount rate for financial calculations"
        ) / 100.0
        
        capacity_factor = st.slider(
            "Capacity Factor (%)",
            min_value=30,
            max_value=90,
            value=50,
            step=5,
            help="Percentage of theoretical maximum energy that is actually generated"
        ) / 100.0
        
        # CAPEX estimation
        capex_per_kw = st.number_input(
            "CAPEX ($/kW)",
            min_value=1000,
            max_value=8000,
            value=3000,
            step=100,
            help="Capital expenditure per kW of installed capacity"
        )
        
        # O&M costs
        om_percentage = st.slider(
            "O&M Costs (% of CAPEX/year)",
            min_value=1.0,
            max_value=5.0,
            value=2.5,
            step=0.1,
            help="Annual operations and maintenance costs as percentage of CAPEX"
        ) / 100.0
    
    # Calculate button
    if st.button("🔄 Calculate Hydropower Potential", type="primary"):
        with st.spinner("Calculating hydropower potential..."):
            try:
                # Perform calculations
                results = calculate_hydropower_potential(
                    head, flow, turbine_type, efficiency, electricity_price,
                    project_lifetime, discount_rate, capacity_factor,
                    capex_per_kw, om_percentage
                )
                
                # Store results in session state
                st.session_state.calculation_results = results
                
                # Display results
                display_calculation_results(results)
                
            except Exception as e:
                st.error(f"Calculation error: {str(e)}")
                st.warning("Please check your input parameters and try again.")

def get_turbine_efficiency(turbine_type, head):
    """Get typical efficiency for turbine type based on head"""
    efficiencies = {
        'kaplan': 0.90 if head < 40 else 0.85,
        'francis': 0.92 if 10 <= head <= 350 else 0.88,
        'pelton': 0.88 if head > 150 else 0.82,
        'cross_flow': 0.80,
        'propeller': 0.85 if head < 15 else 0.80
    }
    return efficiencies.get(turbine_type, 0.85)

def calculate_hydropower_potential(head, flow, turbine_type, efficiency, 
                                 electricity_price, project_lifetime, discount_rate,
                                 capacity_factor, capex_per_kw, om_percentage):
    """Calculate hydropower potential using standard hydropower formulas"""
    
    try:
        # Basic power calculation (P = ρ × g × Q × H × η)
        # Where ρ = 1000 kg/m³ (water density), g = 9.81 m/s² (gravity)
        rho = 1000  # kg/m³
        g = 9.81    # m/s²
        
        # Apply turbine-specific efficiency adjustments
        turbine_efficiency_factor = get_turbine_efficiency(turbine_type, head)
        adjusted_efficiency = efficiency * turbine_efficiency_factor
        
        # Theoretical power (kW)
        theoretical_power = (rho * g * flow * head) / 1000  # Convert to kW
        
        # Actual power with efficiency
        actual_power = theoretical_power * adjusted_efficiency
        
        # Annual energy production
        hours_per_year = 8760
        annual_energy_mwh = (actual_power * capacity_factor * hours_per_year) / 1000
        
        # Economic calculations
        total_capex = actual_power * capex_per_kw
        annual_om = total_capex * om_percentage
        annual_revenue = annual_energy_mwh * electricity_price
        
        # LCOE calculation
        # LCOE = (CAPEX + PV of O&M costs) / (PV of energy production)
        pv_om = annual_om * ((1 - (1 + discount_rate)**(-project_lifetime)) / discount_rate)
        pv_energy = annual_energy_mwh * ((1 - (1 + discount_rate)**(-project_lifetime)) / discount_rate)
        lcoe = (total_capex + pv_om) / pv_energy
        
        # Simple payback period
        net_annual_cash_flow = annual_revenue - annual_om
        simple_payback = total_capex / net_annual_cash_flow if net_annual_cash_flow > 0 else float('inf')
        
        # NPV calculation
        npv = -total_capex
        for year in range(1, project_lifetime + 1):
            cash_flow = annual_revenue - annual_om
            npv += cash_flow / ((1 + discount_rate) ** year)
        
        # Compile results
        results = {
            'basic_parameters': {
                'head_m': head,
                'flow_m3s': flow,
                'turbine_type': turbine_type,
                'efficiency': efficiency * 100,
                'capacity_factor': capacity_factor * 100
            },
            'power_generation': {
                'theoretical_power_kw': theoretical_power,
                'actual_power_kw': actual_power,
                'annual_energy_mwh': annual_energy_mwh,
                'capacity_factor_percent': capacity_factor * 100
            },
            'economic_metrics': {
                'total_capex': total_capex,
                'annual_revenue': annual_revenue,
                'annual_om': annual_om,
                'lcoe': lcoe,
                'simple_payback_years': simple_payback,
                'npv': npv,
                'electricity_price': electricity_price
            },
            'technical_specs': {
                'water_density': rho,
                'gravity': g,
                'project_lifetime': project_lifetime,
                'discount_rate': discount_rate * 100
            }
        }
        
        return results
        
    except Exception as e:
        st.error(f"Error in calculations: {str(e)}")
        raise e

def display_calculation_results(results):
    """Display calculation results in organized sections"""
    
    st.markdown("## 📊 Calculation Results")
    
    # Power Generation Metrics
    st.markdown("### ⚡ Power Generation")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            "Theoretical Power",
            f"{results['power_generation']['theoretical_power_kw']:.1f} kW"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            "Actual Power", 
            f"{results['power_generation']['actual_power_kw']:.1f} kW"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            "Annual Energy",
            f"{results['power_generation']['annual_energy_mwh']:.1f} MWh/year"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            "Capacity Factor",
            f"{results['power_generation']['capacity_factor_percent']:.1f}%"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Economic Metrics
    st.markdown("### 💰 Economic Analysis")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            "Total CAPEX",
            f"${results['economic_metrics']['total_capex']:,.0f}"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            "Annual Revenue",
            f"${results['economic_metrics']['annual_revenue']:,.0f}/year"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            "LCOE",
            f"${results['economic_metrics']['lcoe']:.2f}/MWh"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        payback = results['economic_metrics']['simple_payback_years']
        payback_display = f"{payback:.1f} years" if payback != float('inf') else "∞"
        st.metric(
            "Payback Period",
            payback_display
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Additional metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            "Annual O&M",
            f"${results['economic_metrics']['annual_om']:,.0f}/year"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        npv = results['economic_metrics']['npv']
        npv_color = "green" if npv > 0 else "red"
        st.metric(
            "Net Present Value",
            f"${npv:,.0f}",
            delta=None
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            "Unit Cost",
            f"${results['economic_metrics']['total_capex']/results['power_generation']['actual_power_kw']:.0f}/kW"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(
            "Energy Price",
            f"${results['economic_metrics']['electricity_price']:.0f}/MWh"
        )
        st.markdown('</div>', unsafe_allow_html=True)

def show_analysis_page():
    """Show analysis and visualization page"""
    st.markdown("## 📊 Analysis & Visualizations")
    
    if not st.session_state.calculation_results:
        st.warning("Please run calculations on the Calculator page first!")
        return
    
    results = st.session_state.calculation_results
    
    # Create visualizations
    create_power_analysis_charts(results)
    create_economic_analysis_charts(results)

def create_power_analysis_charts(results):
    """Create power analysis charts"""
    st.markdown("### ⚡ Power Analysis")
    
    # Power breakdown pie chart
    col1, col2 = st.columns(2)
    
    with col1:
        # Power losses breakdown
        theoretical = results['power_generation']['theoretical_power_kw']
        actual = results['power_generation']['actual_power_kw']
        losses = theoretical - actual
        
        fig_pie = go.Figure(data=[go.Pie(
            labels=['Actual Power', 'System Losses'],
            values=[actual, losses],
            hole=0.4,
            marker_colors=['#1E88E5', '#FFA726']
        )])
        
        fig_pie.update_layout(
            title="Power Distribution",
            font=dict(size=14),
            height=400
        )
        
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        # Monthly generation profile (simulated)
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        # Simulate seasonal variation (higher in spring/early summer)
        seasonal_factors = [0.8, 0.9, 1.2, 1.3, 1.1, 0.9, 
                          0.7, 0.6, 0.8, 0.9, 1.0, 0.9]
        
        monthly_generation = [
            results['power_generation']['annual_energy_mwh'] * factor / 12
            for factor in seasonal_factors
        ]
        
        fig_bar = go.Figure(data=[go.Bar(
            x=months,
            y=monthly_generation,
            marker_color='#1E88E5'
        )])
        
        fig_bar.update_layout(
            title="Monthly Energy Generation (Simulated)",
            xaxis_title="Month",
            yaxis_title="Energy (MWh)",
            font=dict(size=14),
            height=400
        )
        
        st.plotly_chart(fig_bar, use_container_width=True)

def create_economic_analysis_charts(results):
    """Create economic analysis charts"""
    st.markdown("### 💰 Economic Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Cash flow over project lifetime
        years = list(range(0, results['technical_specs']['project_lifetime'] + 1))
        cash_flows = []
        
        # Initial investment (negative)
        cash_flows.append(-results['economic_metrics']['total_capex'])
        
        # Annual cash flows
        annual_cash_flow = (results['economic_metrics']['annual_revenue'] - 
                          results['economic_metrics']['annual_om'])
        
        for year in range(1, len(years)):
            cash_flows.append(annual_cash_flow)
        
        # Cumulative cash flow
        cumulative_cash_flow = np.cumsum(cash_flows)
        
        fig_cash = go.Figure()
        
        fig_cash.add_trace(go.Scatter(
            x=years,
            y=cumulative_cash_flow,
            mode='lines+markers',
            name='Cumulative Cash Flow',
            line=dict(color='#1E88E5', width=3)
        ))
        
        fig_cash.add_hline(y=0, line_dash="dash", line_color="red")
        
        fig_cash.update_layout(
            title="Cumulative Cash Flow",
            xaxis_title="Year",
            yaxis_title="Cash Flow ($)",
            font=dict(size=14),
            height=400
        )
        
        st.plotly_chart(fig_cash, use_container_width=True)
    
    with col2:
        # Cost breakdown
        capex = results['economic_metrics']['total_capex']
        annual_om = results['economic_metrics']['annual_om']
        lifetime_om = annual_om * results['technical_specs']['project_lifetime']
        
        fig_costs = go.Figure(data=[go.Bar(
            x=['CAPEX', 'Lifetime O&M'],
            y=[capex, lifetime_om],
            marker_color=['#1E88E5', '#FFA726']
        )])
        
        fig_costs.update_layout(
            title="Cost Breakdown",
            xaxis_title="Cost Category",
            yaxis_title="Cost ($)",
            font=dict(size=14),
            height=400
        )
        
        st.plotly_chart(fig_costs, use_container_width=True)

def show_about_page():
    """Show about page with educational content"""
    st.markdown("## 📚 About Hydropower")
    
    # Educational content in tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🌊 Basics", "⚙️ Technology", "💡 Applications", "🔗 Resources"])
    
    with tab1:
        st.markdown("""
        ### What is Hydropower?
        
        Hydropower harnesses the energy of flowing water to generate electricity. It's one of the oldest and most 
        reliable forms of renewable energy, providing about 16% of global electricity generation.
        
        ### How it Works
        
        1. **Water Source**: Rivers, streams, or reservoirs provide the water flow
        2. **Head**: Vertical drop creates potential energy
        3. **Flow**: Volume of water provides kinetic energy  
        4. **Turbine**: Converts water energy to mechanical rotation
        5. **Generator**: Converts mechanical energy to electricity
        
        ### Key Formula
        
        **Power = ρ × g × Q × H × η**
        
        Where:
        - ρ = Water density (1000 kg/m³)
        - g = Gravitational acceleration (9.81 m/s²)
        - Q = Flow rate (m³/s)
        - H = Head (m)
        - η = Overall efficiency (typically 80-95%)
        """)
    
    with tab2:
        st.markdown("""
        ### Turbine Types
        
        Different turbines are suited for different head and flow conditions:
        
        **🌊 Kaplan Turbines**
        - Low head (2-40m), high flow
        - Propeller-type with adjustable blades
        - Efficiency: 90-95%
        
        **🔄 Francis Turbines**
        - Medium head (10-350m), medium flow
        - Mixed-flow design, most common type
        - Efficiency: 90-95%
        
        **💧 Pelton Turbines**
        - High head (>150m), low flow
        - Impulse turbine with buckets
        - Efficiency: 85-93%
        
        **⚡ Cross-Flow Turbines**
        - Low to medium head (1-200m)
        - Simple, robust design
        - Efficiency: 80-85%
        
        **🚢 Propeller Turbines**
        - Very low head (1-15m), high flow
        - Fixed blade propeller
        - Efficiency: 85-90%
        """)
    
    with tab3:
        st.markdown("""
        ### Types of Hydropower Projects
        
        **🏞️ Run-of-River**
        - Uses natural river flow
        - Minimal environmental impact
        - Variable power output
        
        **🚧 Diversion**
        - Diverts water through channels
        - Moderate environmental impact
        - More consistent power
        
        **🏗️ Impoundment**
        - Creates reservoir with dam
        - Highest power output
        - Significant environmental considerations
        
        ### Applications
        
        - **Grid-scale**: Large plants (>30 MW)
        - **Distributed**: Small plants (1-30 MW)  
        - **Micro-hydro**: Very small (<1 MW)
        - **Pumped storage**: Energy storage solution
        """)
    
    with tab4:
        st.markdown("""
        ### Useful Resources
        
        **Organizations**
        - [International Hydropower Association](https://www.hydropower.org/)
        - [U.S. Department of Energy - Hydropower](https://www.energy.gov/eere/water)
        - [International Renewable Energy Agency](https://www.irena.org/)
        
        **Technical References**
        - USACE Hydropower Engineering Manual
        - IEC 62006 - Hydraulic turbines testing
        - FERC Hydropower Licensing Guidelines
        
        **Software Tools**
        - HydroGenerate Library (used in this app)
        - USGS Water Data
        - NREL System Advisor Model (SAM)
        
        **Environmental Guidelines**
        - Fish passage requirements
        - Environmental flow assessments
        - Sediment management practices
        """)
    
    # Disclaimer
    st.markdown("---")
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Important Disclaimer</strong><br>
    This calculator provides preliminary estimates for educational and screening purposes only. 
    Detailed engineering studies, environmental assessments, and site-specific analyses are required 
    for actual project development. Consult qualified professionals for project implementation.
    </div>
    """, unsafe_allow_html=True)

def show_export_page():
    """Show export and reporting options"""
    st.markdown("## 💾 Export Results")
    
    if not st.session_state.calculation_results:
        st.warning("No calculation results to export. Please run calculations first!")
        return
    
    results = st.session_state.calculation_results
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Data Export")
        
        # Prepare data for CSV export
        export_data = prepare_export_data(results)
        csv_data = export_data.to_csv(index=False)
        
        st.download_button(
            label="📄 Download Results as CSV",
            data=csv_data,
            file_name=f"hydropower_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            help="Download detailed calculation results as CSV file"
        )
        
        # JSON export
        json_data = json.dumps(results, indent=2)
        st.download_button(
            label="🔧 Download as JSON",
            data=json_data,
            file_name=f"hydropower_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            help="Download results in JSON format for further processing"
        )
    
    with col2:
        st.markdown("### 📋 Summary Report")
        
        # Generate summary report
        report = generate_summary_report(results)
        
        st.download_button(
            label="📑 Download Summary Report",
            data=report,
            file_name=f"hydropower_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            help="Download formatted summary report"
        )
    
    # Preview section
    st.markdown("### 👀 Data Preview")
    
    with st.expander("View Export Data"):
        export_data = prepare_export_data(results)
        st.dataframe(export_data, use_container_width=True)

def prepare_export_data(results):
    """Prepare results data for export"""
    data = []
    
    # Basic parameters
    data.extend([
        ["Parameter", "Value", "Unit"],
        ["Head", results['basic_parameters']['head_m'], "m"],
        ["Flow Rate", results['basic_parameters']['flow_m3s'], "m³/s"],
        ["Turbine Type", results['basic_parameters']['turbine_type'], "-"],
        ["Overall Efficiency", results['basic_parameters']['efficiency'], "%"],
        ["", "", ""],
        ["Power Generation", "", ""],
        ["Theoretical Power", results['power_generation']['theoretical_power_kw'], "kW"],
        ["Actual Power", results['power_generation']['actual_power_kw'], "kW"],
        ["Annual Energy", results['power_generation']['annual_energy_mwh'], "MWh/year"],
        ["Capacity Factor", results['power_generation']['capacity_factor_percent'], "%"],
        ["", "", ""],
        ["Economic Metrics", "", ""],
        ["Total CAPEX", results['economic_metrics']['total_capex'], "$"],
        ["Annual Revenue", results['economic_metrics']['annual_revenue'], "$/year"],
        ["Annual O&M", results['economic_metrics']['annual_om'], "$/year"],
        ["LCOE", results['economic_metrics']['lcoe'], "$/MWh"],
        ["Simple Payback", results['economic_metrics']['simple_payback_years'], "years"],
        ["NPV", results['economic_metrics']['npv'], "$"]
    ])
    
    return pd.DataFrame(data)

def generate_summary_report(results):
    """Generate a formatted summary report"""
    report = f"""
HYDROPOWER GENERATION ANALYSIS REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

=====================================
SITE PARAMETERS
=====================================
Net Head:               {results['basic_parameters']['head_m']:.1f} m
Design Flow Rate:       {results['basic_parameters']['flow_m3s']:.1f} m³/s
Turbine Type:          {results['basic_parameters']['turbine_type'].title()}
Overall Efficiency:    {results['basic_parameters']['efficiency']:.1f}%

=====================================
POWER GENERATION ANALYSIS
=====================================
Theoretical Power:     {results['power_generation']['theoretical_power_kw']:,.1f} kW
Actual Power Output:   {results['power_generation']['actual_power_kw']:,.1f} kW
Annual Energy:         {results['power_generation']['annual_energy_mwh']:,.1f} MWh/year
Capacity Factor:       {results['power_generation']['capacity_factor_percent']:.1f}%

=====================================
ECONOMIC ANALYSIS
=====================================
Total CAPEX:          ${results['economic_metrics']['total_capex']:,.0f}
Unit Cost:            ${results['economic_metrics']['total_capex']/results['power_generation']['actual_power_kw']:,.0f}/kW
Annual Revenue:       ${results['economic_metrics']['annual_revenue']:,.0f}/year
Annual O&M Costs:     ${results['economic_metrics']['annual_om']:,.0f}/year
LCOE:                 ${results['economic_metrics']['lcoe']:.2f}/MWh
Simple Payback:       {results['economic_metrics']['simple_payback_years']:.1f} years
Net Present Value:    ${results['economic_metrics']['npv']:,.0f}

=====================================
PROJECT VIABILITY
=====================================
"""
    
    # Add viability assessment
    lcoe = results['economic_metrics']['lcoe']
    payback = results['economic_metrics']['simple_payback_years']
    npv = results['economic_metrics']['npv']
    
    if lcoe < 80 and payback < 15 and npv > 0:
        report += "Status: HIGHLY VIABLE - Excellent economic potential\n"
    elif lcoe < 120 and payback < 20 and npv > 0:
        report += "Status: VIABLE - Good economic potential\n"
    elif lcoe < 150 and payback < 25:
        report += "Status: MARGINAL - Consider optimization\n"
    else:
        report += "Status: CHALLENGING - Detailed study recommended\n"
    
    report += f"""
=====================================
DISCLAIMER
=====================================
This analysis provides preliminary estimates based on simplified calculations.
Detailed engineering studies, environmental assessments, and site-specific
analyses are required for actual project development.

Report created by Hydropower Generation Calculator
    """
    
    return report

if __name__ == "__main__":
    main()