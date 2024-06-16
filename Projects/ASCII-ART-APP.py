import ascii_magic as art
output = art.from_image('/Users/skmirajulislam/Documents/Ascii.jpeg')
print(dir(art))
display = art.AsciiArt
display.to_terminal(output)

