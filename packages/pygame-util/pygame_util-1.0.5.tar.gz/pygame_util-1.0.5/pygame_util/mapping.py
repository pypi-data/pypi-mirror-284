def map_values(value: int, input_start: int, input_end: int, output_start: int, output_end: int) -> int:
    """Maps a value from one range to another."""

    input_range = input_end - input_start
    output_range = output_end - output_start
    value_scaled = (value - input_start) / input_range

    mapped_value = output_start + (value_scaled * output_range)

    return mapped_value
