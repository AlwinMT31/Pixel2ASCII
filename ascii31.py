INPUT_FILE = "image.bmp"
OUTPUT_FILE = "neymar_ascii.txt"

ASCII = "@%#*+=-:. "
NEW_WIDTH = 100
VERTICAL_SCALE = 2

with open(INPUT_FILE, "rb") as f:
    bmp = bytearray(f.read())

data_offset = int.from_bytes(bmp[10:14], "little")
width = int.from_bytes(bmp[18:22], "little", signed=True)
height = int.from_bytes(bmp[22:26], "little", signed=True)

abs_w = abs(width)
abs_h = abs(height)

bytes_per_pixel = 3
row_size = (abs_w * bytes_per_pixel + 3) & ~3

scale = NEW_WIDTH / abs_w
NEW_HEIGHT = int(abs_h * scale)

ascii_output = []

y = 0
while y < NEW_HEIGHT:
    src_y = int(y / scale)
    row = ""
    x = 0

    while x < NEW_WIDTH:
        src_x = int(x / scale)
        i = data_offset + src_y * row_size + src_x * bytes_per_pixel

        b = bmp[i]
        g = bmp[i + 1]
        r = bmp[i + 2]

        gray = (b * 11 + g * 59 + r * 30) // 100
        idx = gray * (len(ASCII) - 1) // 255

        if idx < 0:
            idx = 0
        if idx >= len(ASCII):
            idx = len(ASCII) - 1

        row = row + ASCII[idx]
        x = x + 1

    if y % VERTICAL_SCALE == 0:
        ascii_output.append(row)

    y = y + 1

if height > 0:
    ascii_output.reverse()

# Print to terminal
for line in ascii_output:
    print(line)

# Save to text file
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for line in ascii_output:
        f.write(line + "\n")
