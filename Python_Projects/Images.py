from PIL import Image

def resize_image(input_path, output_path, new_width):

	try:

		with Image.open(input_path) as img:
			#get original dimensions
			width,height = img.size
			print(f"Orignal size: {width} X {height}")

			# Aspect ratio is height / width.
			# We know the new_width, so can use the
			# aspect ratio to figure the new width.
			aspect_ratio = height / width
			new_height = int(new_width * aspect_ratio)

			resized_image = img.resize((new_width, new_height))

			resized_image.save(output_path)

			print(f"Image resized and saved in {output_path}. New Size is {new_width} x {new_height}.")

	except IOError:
		print("Error")
		print(f"Input path is {input_path})")
		print(f"Output path is {output_path})")
		print(f"Unable to open or save the image. Please check the file paths.")

def image_resizer():
	input_path = input("Enter the path of the image to resize: ")
	output_path = input("Enter the output path for the resized image: ")
	new_width = int(input("Enter the new width for the resized image: "))
	resize_image(input_path, output_path, new_width)


image_resizer()
