import os
import platform
import re
import code128
from PIL import Image, ImageDraw, ImageFont

# Define the font size
font_size = 120
# Load the font based on the operating system
if platform.system() == 'Darwin':
	# macOS
	font = ImageFont.truetype("/Library/Fonts/Arial.ttf", font_size)
elif platform.system() == 'Windows':
	# Windows
	font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", font_size)
else:
	# Unsupported operating system
	raise OSError('Unsupported operating system')

# User input the location zone (alphabet), location number digits (number) and the location number (number)
location_zone = input("Enter the location zone (e.g., N): ").strip().upper()
while True:
	num_digits = input("Enter the number of digits for location number (e.g., 4): ").strip()
	if re.fullmatch(r'\d', num_digits):
		break
	else:
		print("Invalid input. Please enter a single-digit number.")
# Define the regex pattern for the specified number of digits
pattern = rf'^\d{{{num_digits}}}$'
# Get the start location number
while True:
	location_number_start = input("Enter the start of location number: ").strip()
	if re.fullmatch(pattern, location_number_start):
		location_number_start = int(location_number_start)
		break
	else:
		print(f"Invalid input. Please enter a number with exactly {num_digits} digits.")
# Get the end location number
while True:
	location_number_end = input("Enter the end of location number: ").strip()
	if re.fullmatch(pattern, location_number_end):
		location_number_end = int(location_number_end)
		break
	else:
		print(f"Invalid input. Please enter a number with exactly {num_digits} digits.")
# Loop through the location number range, concatenate the location zone and each location number
for location_number in range(location_number_start, location_number_end + 1):
	# Concatenate the location zone and location number
	barcode_param = f'{location_zone}{location_number:0{num_digits}d}'
	# Set barcode text to the same value as the barcode parameter
	barcode_text = barcode_param
	# Original barcode image
	barcode_image = code128.image(barcode_param, height=100)
	# Retrieve the size of the barcode image
	width, height = barcode_image.size
	# Define the margin to add to the image
	margin = 80
	# Define new width
	new_width = width + (2 * margin)
	# Define new height
	new_height = height + (2 * margin)
	# Create a new image with the new size
	new_image = Image.new('RGB', (new_width, new_height + margin), (255, 255, 255))
	# Calculate the x-position to center the barcode
	barcode_x_position = (new_image.width - width) // 2
	# Put barcode on new image
	new_image.paste(barcode_image, (barcode_x_position, margin))
	# Object to draw text
	draw = ImageDraw.Draw(new_image)
	# Calculate the bounding box of the text
	bbox = draw.textbbox((0, 0), barcode_text, font=font)
	text_width = bbox[2] - bbox[0]
	text_height = bbox[3] - bbox[1]
	# Calculate the position to center the text
	x_position = (new_image.width - text_width) // 2
	y_position = margin + height + margin // 2
	# Draw the text with the new position and font
	draw.text((x_position, y_position), barcode_text, fill=(0, 0, 0), font=font)
	# output files folder
	output_folder = 'output_files'
	# Create the folder if it does not exist
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)
	# Save the new image
	new_image.save(f'{output_folder}/{barcode_text}.png')
