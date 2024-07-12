# puddleext/convert.py
from PIL import Image
from . import logger

def convert_file(input_file):
    if input_file.lower().endswith('.png'):
        return convert_png_to_puddle(input_file)
    elif input_file.lower().endswith('.puddle'):
        return convert_puddle_to_png(input_file)
    else:
        logger.error(f"{input_file} is not a PNG or PUDDLE file.")
        return

def convert_png_to_puddle(input_file):
    try:
        with Image.open(input_file) as img:
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            width, height = img.size
            img_array = list(img.getdata())

            width_bin = format(width, '016b')
            height_bin = format(height, '016b')
            pixels_bin = ''.join(format(value, '08b') for pixel in img_array for value in pixel)

            binary_data = width_bin + height_bin + pixels_bin
            
            logger.info(f"Converted {input_file} to binary format.")
            logger.debug(f"Binary data: {binary_data}")

            byte_data = int(binary_data, 2).to_bytes((len(binary_data) + 7) // 8, byteorder='big')

            logger.info(f"Converted {input_file} to byte format.")
            logger.debug(f"Byte data: {byte_data}")

            with open(input_file.replace('.png', '.puddle'), 'wb') as f:
                f.write(byte_data)
            
            return byte_data, binary_data

    except Exception as e:
        logger.error(f"Error processing {input_file}: {e}")
        return None, None
    
def convert_puddle_to_png(input_file):
    try:
        with open(input_file, 'rb') as f:
            byte_data = f.read()

        binary_data = reverse_to_binary(byte_data)

        logger.info(f"Converted {input_file} to binary format.")
        logger.debug(f"Original byte data: {byte_data}")
        logger.debug(f"Binary data: {binary_data}")

        width = int(binary_data[:16], 2)
        height = int(binary_data[16:32], 2)
        pixels_bin = binary_data[32:]
        pixels = [
            tuple(int(pixels_bin[i:i+8], 2) for i in range(j, j + 32, 8))
            for j in range(0, len(pixels_bin), 32)
        ]

        pixel_array = [(width, height)] + pixels

        logger.info(f"Converted binary to RGBA arrat.")
        logger.debug(f"Array data: {pixel_array}")

        img = Image.new('RGBA', (width, height))
        img.putdata(pixels)

        png_file = input_file.replace('.puddle', '.png')
        img.save(png_file)

        logger.info(f"Converted {input_file} to {png_file}.")
        return pixel_array

    except Exception as e:
        logger.error(f"Error processing {input_file}: {e}")
        return None

def reverse_to_binary(byte_data):
    binary_string = bin(int.from_bytes(byte_data, byteorder='big'))[2:]
    # Pad the binary string to make sure it's of the correct length
    padding_length = (len(byte_data) * 8) - len(binary_string)
    binary_string = '0' * padding_length + binary_string
    return binary_string