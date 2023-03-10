
""" Resistor Color Codes """
rc = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

def colors() -> list[str]:
    return rc

def color_code(color: str) -> int:
    return colors().index(color)
