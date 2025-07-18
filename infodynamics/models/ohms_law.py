"""
Ohm's Law for Information

Core equations for information flow using electrical circuit analogies:
- V_info = U_info / Z_info (information flow rate)
- Z_info = R_info + jωL_info + 1/(jωC_info) (information impedance)

Where:
- V_info: Information flow rate (how fast info spreads)
- U_info: Information voltage (content quality/influence)  
- Z_info: Information impedance (total resistance to flow)
- R_info: Information resistance (cognitive barriers)
- L_info: Information inductance (processing delays)
- C_info: Information capacity (knowledge accumulation)
"""

import math
import cmath
from typing import Dict, Union, Optional, Tuple


def calculate_flow_rate(
    voltage: float,
    conductivity: float,
    resistance: Optional[float] = None
) -> float:
    """
    Calculate information flow rate using simplified Ohm's law.
    
    V_info = U_info * G_info  (DC case)
    or 
    V_info = U_info / R_info  (if resistance provided)
    
    Args:
        voltage: Information voltage (U_info, 0-10)
        conductivity: Information conductivity (G_info, 0-10)
        resistance: Optional resistance (1/G_info if not provided)
        
    Returns:
        flow_rate: Information flow rate (0-100 scale)
    """
    
    if resistance is None:
        # Use conductivity: V = U * G
        flow_rate = voltage * conductivity
    else:
        # Use resistance: V = U / R  
        if resistance < 0.01:
            resistance = 0.01  # Prevent division by zero
        flow_rate = voltage / resistance
    
    return max(0.0, min(100.0, flow_rate))


def calculate_impedance(
    resistance: float,
    inductance: float,
    capacity: float,
    frequency: float = 1.0
) -> Tuple[float, float]:
    """
    Calculate complex information impedance.
    
    Z_info = R_info + jωL_info + 1/(jωC_info)
    
    Args:
        resistance: Information resistance (R_info)
        inductance: Information inductance (L_info) 
        capacity: Information capacity (C_info)
        frequency: Information frequency (ω, changes per time unit)
        
    Returns:
        Tuple of (magnitude, phase) of complex impedance
    """
    
    if frequency == 0:
        frequency = 0.01  # Prevent division by zero
    
    # Inductive reactance: ωL
    X_L = 2 * math.pi * frequency * inductance
    
    # Capacitive reactance: 1/(ωC)  
    if capacity == 0:
        capacity = 0.01
    X_C = 1.0 / (2 * math.pi * frequency * capacity)
    
    # Total reactance
    X_total = X_L - X_C
    
    # Complex impedance
    Z_complex = complex(resistance, X_total)
    
    # Magnitude and phase
    magnitude = abs(Z_complex)
    phase = cmath.phase(Z_complex)
    
    return magnitude, phase


def calculate_ac_flow_rate(
    voltage: float,
    impedance_magnitude: float,
    impedance_phase: float = 0.0
) -> float:
    """
    Calculate AC information flow rate with phase considerations.
    
    |V_info| = |U_info| / |Z_info|
    
    Args:
        voltage: RMS information voltage
        impedance_magnitude: Impedance magnitude  
        impedance_phase: Phase shift (radians)
        
    Returns:
        rms_flow_rate: RMS information flow rate
    """
    
    if impedance_magnitude < 0.01:
        impedance_magnitude = 0.01
    
    # RMS flow rate
    rms_flow = voltage / impedance_magnitude
    
    # Phase affects effective flow (power factor)
    power_factor = math.cos(impedance_phase)
    effective_flow = rms_flow * abs(power_factor)
    
    return max(0.0, min(100.0, effective_flow))


def calculate_resonant_frequency(inductance: float, capacity: float) -> float:
    """
    Calculate resonant frequency where X_L = X_C.
    
    f_res = 1 / (2π√(LC))
    
    At resonance, impedance is minimized (only resistance remains).
    This represents optimal information flow frequency.
    
    Args:
        inductance: Information inductance (L_info)
        capacity: Information capacity (C_info)
        
    Returns:
        resonant_frequency: Optimal information update frequency
    """
    
    if inductance == 0 or capacity == 0:
        return 0.0
    
    f_res = 1.0 / (2 * math.pi * math.sqrt(inductance * capacity))
    return f_res


def analyze_information_circuit(
    voltage: float,
    resistance: float, 
    inductance: float,
    capacity: float,
    frequency_range: Optional[Tuple[float, float]] = None
) -> Dict[str, Union[float, list]]:
    """
    Complete analysis of information circuit behavior.
    
    Args:
        voltage: Information voltage (U_info)
        resistance: Information resistance (R_info)
        inductance: Information inductance (L_info)  
        capacity: Information capacity (C_info)
        frequency_range: (min_freq, max_freq) for analysis
        
    Returns:
        Dictionary with circuit analysis results
    """
    
    if frequency_range is None:
        frequency_range = (0.1, 10.0)
    
    # Calculate resonant frequency
    f_resonant = calculate_resonant_frequency(inductance, capacity)
    
    # Analyze at resonance
    Z_res_mag, Z_res_phase = calculate_impedance(
        resistance, inductance, capacity, f_resonant
    )
    flow_res = calculate_ac_flow_rate(voltage, Z_res_mag, Z_res_phase)
    
    # Frequency response
    frequencies = []
    impedances = []
    flows = []
    
    f_min, f_max = frequency_range
    for i in range(20):  # 20 points
        f = f_min + (f_max - f_min) * i / 19
        Z_mag, Z_phase = calculate_impedance(resistance, inductance, capacity, f)
        flow = calculate_ac_flow_rate(voltage, Z_mag, Z_phase)
        
        frequencies.append(f)
        impedances.append(Z_mag)
        flows.append(flow)
    
    return {
        "resonant_frequency": f_resonant,
        "resonant_flow_rate": flow_res,
        "min_impedance": Z_res_mag,
        "frequencies": frequencies,
        "impedances": impedances,
        "flow_rates": flows,
        "dc_flow_rate": calculate_flow_rate(voltage, 1/resistance if resistance > 0 else 10),
        "circuit_quality": capacity / resistance if resistance > 0 else float('inf')
    }


# Preset circuit configurations
PRESET_CIRCUITS = {
    "high_performance": {
        "resistance": 0.5,     # Low resistance
        "inductance": 0.2,     # Low inductance  
        "capacity": 2.0,       # High capacity
        "description": "Expert user with optimal conditions"
    },
    
    "average_user": {
        "resistance": 2.0,
        "inductance": 1.0,
        "capacity": 1.0, 
        "description": "Typical user performance"
    },
    
    "overloaded": {
        "resistance": 5.0,     # High resistance
        "inductance": 3.0,     # High inductance
        "capacity": 0.3,       # Low capacity
        "description": "Cognitively overloaded user"
    },
    
    "learning_mode": {
        "resistance": 1.5,
        "inductance": 2.0,     # Higher inductance (slower initial response)
        "capacity": 3.0,       # Higher capacity (better retention)
        "description": "Student in active learning"
    }
} 