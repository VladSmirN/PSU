import unittest
import cv2
import os
from resizeDataset import resizeDataset
import shutil
class resizeDatasetTest(unittest.TestCase):
   def setUp(self):
       self.folder_output = "./output/"
       self.folder_dataset = "./datasetTest/"
   def test_small_image(self):
       resizeDataset(path=self.folder_dataset,width=10,height=20,output=self.folder_output)
       Classes = os.listdir(path=self.folder_output)
       self.assertEqual(Classes, ["1", "2", "3",'resizeDataset.log'])
       for Class in Classes:
           if Class == 'resizeDataset.log' :
               continue
           else:
               Class = Class+'/'
           imageNames = os.listdir(path= os.path.join(self.folder_output, Class))
           self.assertEqual(imageNames, [ "2.jpg", "3.jpg"] )
           for imageName in imageNames:
               img = cv2.imread( os.path.join(self.folder_output, Class,imageName))
               self.assertEqual(img.shape, (20, 10, 3))
       shutil.rmtree(self.folder_output)
if __name__ == "__main__":
   unittest.main()


