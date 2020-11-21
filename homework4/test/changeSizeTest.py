import unittest
import cv2
import os
from changeSize import changeSize
import shutil
class changeSizeTest(unittest.TestCase):
   def setUp(self):
       self.folder_output = "./output/"
       self.folder_dataset = "./image/"
   def test_small_image(self):
       changeSize(path=self.folder_dataset,width=10,height=20,output=self.folder_output)
       images = os.listdir(path=self.folder_output)
       self.assertEqual(images, ["1.jpg", "2.jpg", "3.jpg", "4.jpg"])
       for imageName in images:
               img = cv2.imread(self.folder_output + imageName)
               self.assertEqual(img.shape, (20, 10, 3))
       shutil.rmtree(self.folder_output)
   def test_large_image(self):
       changeSize(path=self.folder_dataset,width=1000,height=1000,output=self.folder_output)
       images = os.listdir(path=self.folder_output)
       self.assertEqual(images, ["1.jpg", "2.jpg", "3.jpg", "4.jpg"])
       for imageName in images:
               img = cv2.imread(self.folder_output + imageName)
               self.assertEqual(img.shape, (1000, 1000, 3))
       shutil.rmtree(self.folder_output)
   def test_void_folder(self):
       changeSize(path='./',width=1000,height=1000,output=self.folder_output)
       images = os.listdir(path=self.folder_output)
       self.assertEqual(images, [])
       shutil.rmtree(self.folder_output)

if __name__ == "__main__":
   unittest.main()


