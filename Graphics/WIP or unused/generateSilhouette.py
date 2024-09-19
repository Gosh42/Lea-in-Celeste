from os import listdir
from os import makedirs
from os.path import isfile, join, exists
from PIL import Image


# The script to generate silhouette sprites from images in a folder.
# Requires python and pillow library installed - install python from the official website
#   and type "pip install pillow" in command line without quotes


# Input path with your images. Replace text in quotes with the file path
path = r"C:\MyImageFolder"

# Output path where silhouette images will be saved
output_folder = r"C:\MyImageFolder\Silhouettes"

if not exists(output_folder):
    makedirs(output_folder)

files = [f for f in listdir(path) if isfile(join(path, f))]

# The RGB values of the outline colours to replace with solid black
# Useful if your character has coloured outlines - if not, just keep it as [(0,0,0,255)]
# Keep last number as 255, it's the alpha channel
colours = [
    (0, 0, 0, 255),
    (66, 4, 19, 255),
    (63, 4, 18, 255),
    (0, 17, 85, 255),
    (33, 30, 36, 255)
]

for file in files:
    file_path = join(path, file)
    img = Image.open(file_path)

    w, h = img.size
    data = img.load()

    for y in range(h):
        for x in range(w):
            if data[x, y] in colours:
                data[x, y] = (0, 0, 0, 255)
            elif data[x, y][3] == 255:
                data[x, y] = (255, 255, 255, 255)

    img.save(join(output_folder, file), "PNG")

print("done.")