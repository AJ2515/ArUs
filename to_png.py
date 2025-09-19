import os
from PIL import Image
from pillow_heif import register_heif_opener

def convert_folder_to_png(input_folder, output_folder):
    """
    Converts all supported image files in a folder to PNG format
    and saves them to a specified output folder.
    """
    # Register HEIF opener to support .heif files
    register_heif_opener()

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Check if it's a file and a recognized image format
        if os.path.isfile(input_path):
            try:
                img = Image.open(input_path).convert("RGB")
                base_name = os.path.splitext(filename)[0]
                output_path = os.path.join(output_folder, base_name + ".png")
                img.save(output_path, "PNG")
                print(f"Converted '{filename}' to '{os.path.basename(output_path)}'")
            except Image.UnidentifiedImageError:
                print(f"Skipping '{filename}': Not a recognized image file.")
            except Exception as e:
                print(f"Error converting '{filename}': {e}")

# Example usage
if __name__ == "__main__":
    input_folder = "C:/Users/Ankit/Desktop/190020006/AR/target_pic"
    output_folder = "C:/Users/Ankit/Desktop/190020006/AR/target_pic_png"

    # Create dummy image files for testing
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print(f"Created dummy input folder: {input_folder}")
        # Create a dummy JPEG
        Image.new('RGB', (60, 30), color = 'red').save(os.path.join(input_folder, 'test_image_1.jpg'))
        # Create a dummy PNG
        Image.new('RGB', (60, 30), color = 'green').save(os.path.join(input_folder, 'test_image_2.png'))
        # Note: Creating a dummy HEIF is more complex and usually requires an actual image.
        # For demonstration, assume a '.heif' file might exist here.
        with open(os.path.join(input_folder, 'test_image_3.heif'), 'w') as f:
            f.write("This is a placeholder for a HEIF file.")
        print("Created dummy image files for testing in the input folder.")

    convert_folder_to_png(input_folder, output_folder)