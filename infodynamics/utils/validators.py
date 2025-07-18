"""Input validation utilities"""

def validate_input_ranges(values, ranges):
    """Validate that values are within specified ranges."""
    for key, value in values.items():
        if key in ranges:
            min_val, max_val = ranges[key]
            if not (min_val <= value <= max_val):
                raise ValueError(f"{key} = {value} not in range [{min_val}, {max_val}]")
    return True 