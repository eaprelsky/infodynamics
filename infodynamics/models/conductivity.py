"""
Information Conductivity Model (G_info)

Mathematical model for calculating how well a cognitive agent can receive 
and process information, based on selective attention research.

Based on:
- Broadbent's Filter Model
- Treisman's Attenuation Theory  
- Cognitive Load Theory (Sweller)
- Working Memory Model (Baddeley)
"""

import numpy as np
from typing import Dict, Union, Optional


def calculate_g_info(
    agent_profile: Dict[str, float],
    context: Optional[Dict[str, float]] = None,
    weights: Optional[Dict[str, float]] = None
) -> float:
    """
    Calculate Information Conductivity (G_info) for a cognitive agent.
    
    Args:
        agent_profile: Dictionary with agent characteristics:
            - working_memory: Working memory capacity (0-10 scale, typical 7±2)
            - attention_selectivity: Selective attention ability (0-1 scale)
            - motivation: Motivation/interest level (0-1 scale) 
            - expertise: Domain expertise level (0-1 scale)
            - processing_speed: Information processing speed (0-1 scale)
            
        context: Optional contextual factors:
            - distraction_level: Environmental distractions (0-1, higher = more)
            - time_pressure: Time constraints (0-1, higher = more pressure)
            - fatigue: Cognitive fatigue level (0-1, higher = more tired)
            
        weights: Optional component weights (defaults provided)
    
    Returns:
        G_info: Information conductivity value (0-10 scale)
        
    Example:
        >>> profile = {
        ...     "working_memory": 7.2,
        ...     "attention_selectivity": 0.8,
        ...     "motivation": 0.9,
        ...     "expertise": 0.6,
        ...     "processing_speed": 0.7
        ... }
        >>> G = calculate_g_info(profile)
        >>> print(f"G_info = {G:.2f}")
    """
    
    # Default weights based on literature review
    if weights is None:
        weights = {
            "working_memory": 0.30,      # Strongest predictor
            "attention_selectivity": 0.25,
            "motivation": 0.20,
            "expertise": 0.15,
            "processing_speed": 0.10
        }
    
    # Extract agent characteristics with defaults
    wm = agent_profile.get("working_memory", 7.0)  # Miller's 7±2
    attention = agent_profile.get("attention_selectivity", 0.7)
    motivation = agent_profile.get("motivation", 0.7)
    expertise = agent_profile.get("expertise", 0.5)
    speed = agent_profile.get("processing_speed", 0.7)
    
    # Normalize working memory to 0-1 scale
    wm_normalized = min(1.0, max(0.0, wm / 10.0))
    
    # Calculate base conductivity
    G_base = (
        weights["working_memory"] * wm_normalized +
        weights["attention_selectivity"] * attention +
        weights["motivation"] * motivation +
        weights["expertise"] * expertise +
        weights["processing_speed"] * speed
    )
    
    # Apply contextual modifiers if provided
    if context:
        distraction = context.get("distraction_level", 0.0)
        time_pressure = context.get("time_pressure", 0.0) 
        fatigue = context.get("fatigue", 0.0)
        
        # Context reduces conductivity
        context_penalty = (
            0.3 * distraction +
            0.2 * time_pressure +
            0.5 * fatigue
        )
        
        G_modified = G_base * (1.0 - 0.5 * context_penalty)
    else:
        G_modified = G_base
    
    # Apply nonlinear scaling (sigmoid-like curve)
    # High conductivity is harder to achieve
    G_scaled = 10.0 * (1.0 / (1.0 + np.exp(-6.0 * (G_modified - 0.5))))
    
    return max(0.1, min(10.0, G_scaled))


def calculate_g_info_social(
    agent_profile: Dict[str, float],
    social_context: Dict[str, float],
    weights: Optional[Dict[str, float]] = None
) -> float:
    """
    Calculate Information Conductivity for social media contexts.
    
    Args:
        agent_profile: Individual characteristics
        social_context: Social factors:
            - echo_chamber_strength: How much in echo chamber (0-1)
            - social_proof: Social validation level (0-1)
            - network_diversity: Diversity of information sources (0-1)
            
    Returns:
        G_info_social: Social information conductivity
    """
    
    # Calculate base individual conductivity
    G_individual = calculate_g_info(agent_profile)
    
    # Social modifiers
    echo_chamber = social_context.get("echo_chamber_strength", 0.0)
    social_proof = social_context.get("social_proof", 0.5)
    diversity = social_context.get("network_diversity", 0.7)
    
    # Echo chambers reduce conductivity to new information
    # But increase conductivity to confirming information
    echo_penalty = 0.3 * echo_chamber * (1.0 - diversity)
    social_boost = 0.2 * social_proof
    
    G_social = G_individual * (1.0 - echo_penalty + social_boost)
    
    return max(0.1, min(10.0, G_social))


def validate_agent_profile(profile: Dict[str, float]) -> bool:
    """Validate agent profile parameters are in correct ranges."""
    
    required_keys = ["working_memory", "attention_selectivity", "motivation", "expertise"]
    
    for key in required_keys:
        if key not in profile:
            raise ValueError(f"Missing required parameter: {key}")
    
    # Validate ranges
    if not (0 <= profile["working_memory"] <= 10):
        raise ValueError("working_memory must be 0-10")
        
    for key in ["attention_selectivity", "motivation", "expertise"]:
        if not (0 <= profile[key] <= 1):
            raise ValueError(f"{key} must be 0-1")
    
    return True


# Preset profiles for common user types
PRESET_PROFILES = {
    "expert": {
        "working_memory": 8.5,
        "attention_selectivity": 0.9,
        "motivation": 0.9,
        "expertise": 0.95,
        "processing_speed": 0.8
    },
    
    "student": {
        "working_memory": 6.5,
        "attention_selectivity": 0.6,
        "motivation": 0.7,
        "expertise": 0.3,
        "processing_speed": 0.7
    },
    
    "casual_user": {
        "working_memory": 7.0,
        "attention_selectivity": 0.5,
        "motivation": 0.5,
        "expertise": 0.4,
        "processing_speed": 0.6
    },
    
    "overloaded": {
        "working_memory": 5.0,
        "attention_selectivity": 0.3,
        "motivation": 0.4,
        "expertise": 0.5,
        "processing_speed": 0.4
    }
} 