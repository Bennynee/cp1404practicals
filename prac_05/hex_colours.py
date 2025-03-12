COLOR_TO_HEX = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AQUAMARINE": "#7FFFD4",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF"
}

color_name = input("Enter color name: ").strip().upper()

while color_name != "":
    if color_name in COLOR_TO_HEX:
        print(f"{color_name.title()} is {COLOR_TO_HEX[color_name]}")
    else:
        print("Invalid color name")
    color_name = input("Enter color name: ").strip().upper()
