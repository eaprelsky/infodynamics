"""Score conversion utilities"""

def normalize_scores(scores, scale_from=(0, 10), scale_to=(0, 1)):
    """Normalize scores from one scale to another."""
    old_min, old_max = scale_from
    new_min, new_max = scale_to
    
    normalized = {}
    for key, value in scores.items():
        # Normalize to 0-1 first
        norm_01 = (value - old_min) / (old_max - old_min)
        # Scale to target range
        normalized[key] = new_min + norm_01 * (new_max - new_min)
    
    return normalized

def denormalize_scores(scores, scale_from=(0, 1), scale_to=(0, 10)):
    """Convert normalized scores back to original scale."""
    return normalize_scores(scores, scale_from, scale_to) 