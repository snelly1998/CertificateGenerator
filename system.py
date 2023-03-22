from PIL import Image, ImageDraw, ImageFont
import csv

number_of_certificates = 0

font = ImageFont.truetype('arial.ttf', 60)

with open('data.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

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
    draw.text((335, 1000), name[2], font=font, fill=(0, 0, 0))

    print(f'./images/{name[0]} - {name[1]} - {name[2]}.jpg')

    image.save(f'./images/{name[0]} - {name[1]} - {name[2]}.jpg')

    number_of_certificates += 1

    #Splitting the certificates into different folders. 

    # if name[2] == 'Harnois':

    #     image.save(f'./images/Harnois/{name[0]} - {name[1]} - {name[2]}.jpg')

    #     number_of_certificates += 1
    # else:

    #     print(f'./images/{name[0]} - {name[1]} - {name[2]}.jpg')

    #     image.save(f'./images/{name[0]} - {name[1]} - {name[2]}.jpg')

    #     number_of_certificates += 1

print(number_of_certificates)