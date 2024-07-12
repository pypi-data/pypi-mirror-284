# tests/test_convert.py
import unittest
from puddleext.convert import convert_file, reverse_to_binary
from unittest.mock import patch, MagicMock
import logging
import io
import os

class TestConvertFile(unittest.TestCase):

    def setUp(self):
        # Set up the log capture
        self.log_stream = io.StringIO()
        self.handler = logging.StreamHandler(self.log_stream)
        logger = logging.getLogger('puddle')
        logger.addHandler(self.handler)
        logger.setLevel(logging.DEBUG)

    def tearDown(self):
        # Clean up the log capture
        logger = logging.getLogger('puddle')
        logger.removeHandler(self.handler)
        self.log_stream.close()

    @patch('puddle.convert.Image.open')
    def test_convert_file(self, mock_open):
        # Mock image and image data
        mock_image = mock_open.return_value.__enter__.return_value
        mock_image.mode = 'RGBA'
        mock_image.getdata.return_value = [(242, 92, 98, 255), (238, 48, 56, 255), (238, 48, 56, 255), (237, 28, 36, 255)]
        mock_image.size = (2, 2)
        
        byte_data, binary_data = convert_file('test.png')

        # Get log output
        self.handler.flush()

        # Check if the logs contain specific messages
        self.assertEqual(binary_data, '0000000000000010000000000000001011110010010111000110001011111111111011100011000000111000111111111110111000110000001110001111111111101101000111000010010011111111')
        self.assertEqual(byte_data, b'\x00\x02\x00\x02\xf2\\b\xff\xee08\xff\xee08\xff\xed\x1c$\xff')
        self.assertEqual(binary_data, reverse_to_binary(byte_data))

        pixel_array = convert_file('test.puddle')

        self.assertEqual(pixel_array, [(2, 2), (242, 92, 98, 255), (238, 48, 56, 255), (238, 48, 56, 255), (237, 28, 36, 255)])

        os.remove('test.puddle')
        os.remove('test.png')
    
    def test_convert_file_not_png(self):
        convert_file('test.txt')

        # Get log output
        self.handler.flush()
        log_contents = self.log_stream.getvalue()

        # Check if the logs contain specific messages
        self.assertIn('test.txt is not a PNG or PUDDLE file.', log_contents)

if __name__ == '__main__':
    unittest.main()
