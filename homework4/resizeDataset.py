import cv2
import os
import logging
from tqdm import tqdm
import sys


def resizeDataset(path,width,height,output):
        if  os.path.isdir(output) == False:
            os.makedirs(output)
        logging.basicConfig(filename=os.path.join(output,'resizeDataset.log') , level=logging.INFO)
        Classes = map( lambda s: s+'/', os.listdir(path=path))
        for Class in Classes:
            if os.path.isdir(os.path.join(path, Class)) == False :
                continue
            count = 0;
            images = os.listdir(path=os.path.join(path,Class))
            if os.path.isdir(os.path.join(output, Class)) == False:
                os.makedirs(os.path.join(output, Class))
            for imageName in tqdm(images):
                try:
                    img = cv2.imread(os.path.join(path,Class,imageName))
                    resized = cv2.resize(img, (width, height))
                    cv2.imwrite(os.path.join(output,Class,imageName), resized)
                    count += 1
                except:
                    logging.warning('Failed resize for ' + path + Class + imageName)
            logging.info('successful execution for class - '+Class+'. Image resize: ' + str(count))
        logging.shutdown()



if __name__ == '__main__':
    print(sys.argv )
    resizeDataset("./dataset/image/",200,200,"C:/project/ML_PSU/PSU/homework4/resizeDataset/")
    #resizeDataset(path=sys.argv[1], width=int(sys.argv[2]), height=int(sys.argv[3]), output=sys.argv[4])


