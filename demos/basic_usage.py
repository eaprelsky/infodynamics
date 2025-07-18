#!/usr/bin/env python3
"""
Information Dynamics - Basic Usage Demo

This demo shows how to use the Information Dynamics library to:
1. Calculate user's information conductivity  
2. Calculate content's information voltage
3. Predict information flow rate
4. Analyze complete information circuits
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import infodynamics as id
from infodynamics.models.conductivity import PRESET_PROFILES
from infodynamics.models.ohms_law import PRESET_CIRCUITS, analyze_information_circuit


def demo_basic_calculations():
    """Demonstrate basic Information Dynamics calculations."""
    
    print("🧠 Information Dynamics - Basic Demo")
    print("=" * 50)
    
    # 1. Define a user profile
    user_profile = {
        "working_memory": 7.2,
        "attention_selectivity": 0.8,
        "motivation": 0.9,
        "expertise": 0.6,
        "processing_speed": 0.7
    }
    
    print("👤 User Profile:")
    for key, value in user_profile.items():
        print(f"   {key.replace('_', ' ').title()}: {value}")
    
    # 2. Calculate information conductivity
    G_info = id.calculate_g_info(user_profile)
    print(f"\n⚡ Information Conductivity: G_info = {G_info:.2f}")
    
    # 3. Define content characteristics
    content_profile = {
        "factual_density": 0.8,
        "credibility": 0.9,
        "semantic_quality": 0.85,
        "timeliness": 0.7
    }
    
    print("\n📄 Content Profile:")
    for key, value in content_profile.items():
        print(f"   {key.replace('_', ' ').title()}: {value}")
    
    # 4. Calculate information voltage
    U_info = id.calculate_u_info(content_profile)
    print(f"\n🔋 Information Voltage: U_info = {U_info:.2f}")
    
    # 5. Calculate information flow rate
    flow_rate = id.calculate_flow_rate(U_info, G_info)
    print(f"\n🌊 Information Flow Rate: V_info = {flow_rate:.2f}")
    
    # 6. Interpretation
    print(f"\n💡 Interpretation:")
    if flow_rate > 50:
        print(f"   🚀 Excellent match! Information will flow very efficiently.")
    elif flow_rate > 25:
        print(f"   ✅ Good match! Information will be well-received.")
    elif flow_rate > 10:
        print(f"   ⚠️  Moderate match. Consider optimizing content or user state.")
    else:
        print(f"   ❌ Poor match. Significant barriers to information flow.")
    
    return G_info, U_info, flow_rate


def demo_preset_profiles():
    """Demonstrate analysis with preset user profiles."""
    
    print("\n\n🎭 Preset User Profiles Analysis")
    print("=" * 50)
    
    for profile_name, profile_data in PRESET_PROFILES.items():
        print(f"\n👤 {profile_name.replace('_', ' ').title()} Profile:")
        
        G_info = id.calculate_g_info(profile_data)
        R_info = id.calculate_r_info(profile_data)  
        L_info = id.calculate_l_info(profile_data)
        C_info = id.calculate_c_info(profile_data)
        
        print(f"   G_info (Conductivity): {G_info:.2f}")
        print(f"   R_info (Resistance):   {R_info:.2f}")
        print(f"   L_info (Inductance):   {L_info:.2f}")
        print(f"   C_info (Capacity):     {C_info:.2f}")


def demo_circuit_analysis():
    """Demonstrate complete circuit analysis."""
    
    print("\n\n🔌 Complete Circuit Analysis")
    print("=" * 50)
    
    # Use high performance circuit
    circuit = PRESET_CIRCUITS["high_performance"]
    voltage = 8.0  # High quality content
    
    print(f"🎛️  Circuit: {circuit['description']}")
    print(f"   R_info = {circuit['resistance']:.2f}")
    print(f"   L_info = {circuit['inductance']:.2f}")
    print(f"   C_info = {circuit['capacity']:.2f}")
    print(f"   U_info = {voltage:.2f}")
    
    # Perform complete analysis
    analysis = analyze_information_circuit(
        voltage, 
        circuit['resistance'],
        circuit['inductance'], 
        circuit['capacity']
    )
    
    print(f"\n📊 Analysis Results:")
    print(f"   Resonant Frequency:    {analysis['resonant_frequency']:.3f} Hz")
    print(f"   Resonant Flow Rate:    {analysis['resonant_flow_rate']:.2f}")
    print(f"   DC Flow Rate:          {analysis['dc_flow_rate']:.2f}")
    print(f"   Minimum Impedance:     {analysis['min_impedance']:.2f}")
    print(f"   Circuit Quality:       {analysis['circuit_quality']:.2f}")
    
    print(f"\n💡 Optimization Insights:")
    if analysis['resonant_frequency'] > 2.0:
        print(f"   🔄 Fast adaptation - good for dynamic content")
    else:
        print(f"   🐌 Slow adaptation - better for stable content")
        
    if analysis['circuit_quality'] > 4.0:
        print(f"   🎯 High selectivity - excellent for expert content")
    else:
        print(f"   📖 Broad acceptance - good for general content")


def demo_optimization():
    """Demonstrate content optimization for different users."""
    
    print("\n\n🎯 Content Optimization Demo")
    print("=" * 50)
    
    # Target different user types
    users = ["expert", "student", "casual_user"]
    
    # Original content
    original_content = {
        "factual_density": 0.9,    # Very factual
        "credibility": 0.95,       # Highly credible
        "semantic_quality": 0.8,   # Good quality
        "timeliness": 0.6          # Moderate urgency
    }
    
    print("📄 Original Content Profile:")
    for key, value in original_content.items():
        print(f"   {key.replace('_', ' ').title()}: {value}")
    
    original_voltage = id.calculate_u_info(original_content)
    print(f"\n🔋 Original Voltage: {original_voltage:.2f}")
    
    print(f"\n📊 Flow Rates by User Type:")
    for user_type in users:
        profile = PRESET_PROFILES[user_type]
        G_info = id.calculate_g_info(profile)
        flow_rate = id.calculate_flow_rate(original_voltage, G_info)
        
        print(f"   {user_type.replace('_', ' ').title():12}: {flow_rate:5.1f} "
              f"(G_info={G_info:.1f})")
    
    # Optimize for casual user
    print(f"\n🔧 Optimizing for Casual User:")
    casual_G = id.calculate_g_info(PRESET_PROFILES["casual_user"])
    target_flow = 25.0  # Good flow rate
    optimal_voltage = target_flow / casual_G
    
    print(f"   Target flow rate: {target_flow:.1f}")
    print(f"   Required voltage: {optimal_voltage:.1f}")
    print(f"   Recommendation: {'Simplify content' if optimal_voltage < original_voltage else 'Enhance content'}")


def main():
    """Run all demos."""
    
    try:
        # Basic calculations
        demo_basic_calculations()
        
        # Preset profiles
        demo_preset_profiles()
        
        # Circuit analysis
        demo_circuit_analysis()
        
        # Optimization
        demo_optimization()
        
        print(f"\n\n🎉 Demo completed successfully!")
        print(f"💡 Try the CLI tool: python tools/cli.py --help")
        print(f"📚 See docs/ for more detailed documentation")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print(f"💡 Make sure to install dependencies: pip install -r requirements.txt")
        return 1
        
    except Exception as e:
        print(f"❌ Error during demo: {e}")
        return 1
        
    return 0


if __name__ == '__main__':
    sys.exit(main()) 