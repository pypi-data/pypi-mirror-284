# puddleext/view.py
from PIL import Image
import os
from . import logger
from puddle_ext.convert import reverse_to_binary

def view_file(input_file):
    if not input_file.lower().endswith('.puddle'):
        logger.error("Error: The input file is not a PUDDLE file.")
        return

    try:
        with open(input_file, 'rb') as file:
            
            byte_data = file.read()
            binary_data = reverse_to_binary(byte_data)
            
            width = int(binary_data[:16], 2)
            height = int(binary_data[16:32], 2)
            pixels_bin = binary_data[32:]
            pixels = [
                tuple(int(pixels_bin[i:i+8], 2) for i in range(j, j+32, 8))
                for j in range(0, len(pixels_bin), 32)
            ]

            img = Image.new('RGBA', (width, height))
            img.putdata(pixels)
            img.show()

    except Exception as e:
        logger.error(f"Error processing the image: {e}")
