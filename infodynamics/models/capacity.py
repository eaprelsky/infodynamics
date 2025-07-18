"""Information Capacity Model (C_info) - placeholder"""

def calculate_c_info(agent_profile, context=None):
    """Calculate information capacity (knowledge accumulation)."""
    # Simple version based on working memory and expertise
    wm = agent_profile.get("working_memory", 7.0) / 10.0
    expertise = agent_profile.get("expertise", 0.5)
    motivation = agent_profile.get("motivation", 0.7)
    return 3.0 * wm + 2.0 * expertise + 1.0 * motivation 