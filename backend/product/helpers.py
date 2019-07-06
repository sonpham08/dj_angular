def format_desc(desc="", available_values=[]):
    """
    """
    output_str = ""
    output_str += desc
    if len(available_values) == 0:
        return output_str
    output_str += "\nExplain the meaning of the parameter:"
    
    for a_value in available_values:
        meaning, value = a_value
        output_str += "\n- {0}: {1}".format(value, meaning)
    
    return output_str