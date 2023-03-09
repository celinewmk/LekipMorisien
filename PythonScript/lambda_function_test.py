from lambda_function import get_middle_pixel_RGB, get_closest_color, get_exact_color
from get_test_params import get_test_params
import unittest

class TestImageProcessing(unittest.TestCase):
  
  def setUp(self):
    ((image_dict, error_images), pixel_colors) = get_test_params()
    self.image_dict = image_dict
    self.error_images = error_images
    self.pixel_colors = pixel_colors
    
  def test_get_middle_pixel_RGB(self):
    for base64_encoded_image, rgb in self.image_dict.items():
      v = get_middle_pixel_RGB(base64_encoded_image) == rgb
      self.assertTrue(v.all())
  
  def test_error_get_middle_pixel_RGB(self):
    for base64_encoded_image in self.error_images:
      with self.assertRaises(Exception):
        get_middle_pixel_RGB(base64_encoded_image)
        
  def test_get_closest_color(self):
    for middle_pixel, (_, expected) in self.pixel_colors.items():
      self.assertEqual(get_closest_color(middle_pixel), expected)
      
  def test_get_exact_color(self):
    for middle_pixel, (expected, _) in self.pixel_colors.items():
      self.assertEqual(get_exact_color(middle_pixel), expected)

if __name__ == '__main__':
  unittest.main()