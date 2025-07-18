"""
Information Dynamics: Mathematical modeling of information flows in cognitive systems

This package provides mathematical models and tools for analyzing information 
flow through cognitive agents using electrical circuit analogies.

Main components:
- G_info: Information conductivity (attention, working memory)
- R_info: Information resistance (cognitive load, barriers)  
- L_info: Information inductance (processing delays, inertia)
- C_info: Information capacity (knowledge accumulation)
- U_info: Information voltage (content quality, influence)

Based on the Information Dynamics theory developed in 2025.
"""

__version__ = "1.0.0-alpha"
__author__ = "Information Dynamics Research Team"
__license__ = "MIT"

# Import main models
from .models.conductivity import calculate_g_info
from .models.resistance import calculate_r_info  
from .models.inductance import calculate_l_info
from .models.capacity import calculate_c_info
from .models.voltage import calculate_u_info
from .models.ohms_law import calculate_flow_rate, calculate_impedance

# Import utilities
from .utils.validators import validate_input_ranges
from .utils.converters import normalize_scores, denormalize_scores

__all__ = [
    # Core models
    'calculate_g_info',
    'calculate_r_info', 
    'calculate_l_info',
    'calculate_c_info',
    'calculate_u_info',
    
    # Ohm's law
    'calculate_flow_rate',
    'calculate_impedance',
    
    # Utilities
    'validate_input_ranges',
    'normalize_scores',
    'denormalize_scores',
]

# Package metadata
__doc__ = """
Information Dynamics Package

Mathematical models for information flow through cognitive systems.

Example usage:
    >>> import infodynamics as id
    >>> 
    >>> # Calculate user's information conductivity
    >>> user = {"working_memory": 7.2, "attention": 0.8, "motivation": 0.9}
    >>> G = id.calculate_g_info(user)
    >>> 
    >>> # Calculate content's information voltage  
    >>> content = {"factual_density": 0.8, "credibility": 0.9}
    >>> U = id.calculate_u_info(content)
    >>> 
    >>> # Predict information flow rate
    >>> flow = id.calculate_flow_rate(U, G)
    >>> print(f"Information flow rate: {flow:.2f}")
""" 