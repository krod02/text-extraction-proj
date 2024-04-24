from PIL import Image
from pytesseract import pytesseract

# Defining path to tesseract executable
path_to_tesseract = r"/opt/homebrew/bin/tesseract"

# Providing the tesseract executable location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

# List of image paths
image_paths = ["test-image.png", "test-image2.png", "test-image3.png", "test-image4.png", "test-image5.png"]

# Loop through the list of image files
for image_path in image_paths:
    # Opening the image & storing it in an image object
    img = Image.open(image_path)

    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(img)

    # Displaying the extracted text
    print(f"Text from {image_path}:")
    print(text[:-1])  # Display extracted text
    print("-" * 40)  # Print a divider for readability between images
