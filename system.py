from PIL import Image, ImageDraw, ImageFont
import csv
import os
import zipfile

# TODO: Rewrite the certificate.png so that we can add a Course Name rather than it being static. 
# TODO: Maybe check a database of some sort that see when the last time the script was run? Maybe not important though. 

#Global Vars
folder_path = './certs/'
font = ImageFont.truetype('arial.ttf', 60)
unique_values = []

with open('data.csv', encoding="utf8", errors='ignore') as f:
    reader = csv.reader(f)
    data = list(reader)

# Loops over the store names and adds each unique name into a list. 
for i, name in enumerate(data):
    if name[15] not in unique_values:
        unique_values.append(name[15])

# Loops over the list and creates a folder for each of the unique store names in the ./certs/ folder. 
for value in unique_values:
    os.makedirs(f"./certs/{value}/", exist_ok=True)

for i, name in enumerate(data):
    # Grab the information for each of the students and store them in a variable. 
    student = name[1]
    complete_date = name[8].split("T")[0]
    store_name = name[15]
    score = name[3]
    
    # Checks to see if the date on the certificate is on or after the date provided by the user
    # This ensures that the certificates being generated are only the ones that are required.     
    if complete_date >= "2023-01-05" and score == "100.0":
        print(student, complete_date, store_name, score)
        # Grabs the image and draws it
        image = Image.open('cert.png')
        draw = ImageDraw.Draw(image)
        text_width, text_height = draw.textsize(student, font)

        # Gets the center of the page so that we can write the students name in the middle. 
        x = (image.width - text_width) / 2 
        y = (image.height - text_height) / 2 
        draw.text((x, y), student, font=font, fill=(0, 0, 0))
        
        # Writes the Date
        draw.text((1250, 1000), complete_date, font=font, fill=(0, 0, 0))
        
        #Writes the Store Name
        draw.text((300, 1000), store_name, font=font, fill=(0, 0, 0))

        # Saves the image to the certs folder. 
        image.save(f'./certs/{store_name}/{student} - {complete_date} - {store_name}.jpg')
        
for folder_name in os.listdir(folder_path):
    # Construct the full path to the folder
    folder_path_full = os.path.join(folder_path, folder_name)
     # Make sure the item is a directory, not a file
    if os.path.isdir(folder_path_full):
        # Check if the folder contains any files
        if len(os.listdir(folder_path_full)) > 0:
            # Create a zip file for the folder
            zip_path = f"{folder_path_full}.zip"
            with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
                # Iterate over the files in the folder and add them to the zip file
                for file_name in os.listdir(folder_path_full):
                    file_path_full = os.path.join(folder_path_full, file_name)
                    if os.path.isfile(file_path_full):
                        zip_file.write(file_path_full, file_name)