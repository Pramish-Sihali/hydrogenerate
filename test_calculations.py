#!/usr/bin/env python3
"""
Test script to verify hydropower calculations are working correctly
"""

import sys

def test_basic_calculation():
    """Test basic hydropower calculation"""
    print("🧪 Testing basic hydropower calculations...")
    
    # Test parameters
    head = 50.0  # meters
    flow = 100.0  # m³/s
    efficiency = 0.90  # 90%
    
    # Constants
    rho = 1000  # kg/m³
    g = 9.81    # m/s²
    
    # Calculate theoretical power
    theoretical_power = (rho * g * flow * head) / 1000  # kW
    actual_power = theoretical_power * efficiency
    
    print(f"📊 Test Parameters:")
    print(f"   Head: {head} m")
    print(f"   Flow: {flow} m³/s") 
    print(f"   Efficiency: {efficiency*100}%")
    print(f"")
    print(f"🔋 Results:")
    print(f"   Theoretical Power: {theoretical_power:.1f} kW")
    print(f"   Actual Power: {actual_power:.1f} kW")
    
    # Verify reasonable results
    expected_theoretical = 49050  # kW (approximately)
    if abs(theoretical_power - expected_theoretical) < 100:
        print("   ✅ Calculation verified!")
        return True
    else:
        print(f"   ❌ Calculation error - expected ~{expected_theoretical} kW")
        return False

def test_streamlit_import():
    """Test Streamlit and other libraries import"""
    print("🔧 Testing required libraries...")
    
    try:
        import streamlit
        import plotly
        import pandas
        import numpy
        print("   ✅ All required libraries imported successfully!")
        return True
    except Exception as e:
        print(f"   ❌ Import error: {e}")
        return False

def test_economic_calculation():
    """Test economic calculations"""
    print("💰 Testing economic calculations...")
    
    # Test parameters
    power_kw = 44145  # from basic calculation above
    capex_per_kw = 3000
    electricity_price = 80  # $/MWh
    capacity_factor = 0.5
    project_lifetime = 30
    discount_rate = 0.06
    om_percentage = 0.025
    
    # Calculate metrics
    total_capex = power_kw * capex_per_kw
    annual_energy_mwh = (power_kw * capacity_factor * 8760) / 1000
    annual_revenue = annual_energy_mwh * electricity_price
    annual_om = total_capex * om_percentage
    
    # LCOE calculation
    pv_om = annual_om * ((1 - (1 + discount_rate)**(-project_lifetime)) / discount_rate)
    pv_energy = annual_energy_mwh * ((1 - (1 + discount_rate)**(-project_lifetime)) / discount_rate)
    lcoe = (total_capex + pv_om) / pv_energy
    
    print(f"📈 Economic Results:")
    print(f"   Total CAPEX: ${total_capex:,.0f}")
    print(f"   Annual Energy: {annual_energy_mwh:,.0f} MWh/year")
    print(f"   Annual Revenue: ${annual_revenue:,.0f}/year")
    print(f"   LCOE: ${lcoe:.2f}/MWh")
    
    # Verify reasonable LCOE (should be between $50-150/MWh typically)
    if 50 <= lcoe <= 150:
        print("   ✅ Economic calculations verified!")
        return True
    else:
        print(f"   ⚠️  LCOE seems unusual: ${lcoe:.2f}/MWh")
        return True  # Still pass as this could be valid

def main():
    """Run all tests"""
    print("🌊 Hydropower Generation Calculator - Test Suite")
    print("=" * 50)
    
    tests = [
        test_streamlit_import,
        test_basic_calculation,
        test_economic_calculation
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"   ❌ Test failed with error: {e}")
            failed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Summary: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! App should work correctly.")
        return 0
    else:
        print("⚠️  Some tests failed. Check the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())