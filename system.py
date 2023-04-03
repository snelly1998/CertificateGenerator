from PIL import Image, ImageDraw, ImageFont
import csv
import os

number_of_certificates = 0

font = ImageFont.truetype('arial.ttf', 60)

with open('data.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

unique_values = []

for i, name in enumerate(data):
    if name[2] not in unique_values:
        unique_values.append(name[2])

for value in unique_values:
    os.makedirs(f"./certs/{value}/", exist_ok=True)

for i, name in enumerate(data):
    image = Image.open('cert.png')
    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textsize(name[0], font)

    # Center the Name horizontally
    x = (image.width - text_width) / 2 

    # Center the Name vertically 
    y = (image.height - text_height) / 2 

    #Name
    draw.text((x, y), name[0], font=font, fill=(0, 0, 0))
    #Completion Date
    draw.text((1250, 1000), name[1], font=font, fill=(0, 0, 0))
    #Company Name
    draw.text((300, 1000), name[2], font=font, fill=(0, 0, 0))

    image.save(f'./certs/{name[2]}/{name[0]} - {name[1]} - {name[2]}.jpg')

    number_of_certificates += 1