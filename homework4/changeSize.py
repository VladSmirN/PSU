import cv2
import os
import logging
from tqdm import tqdm
import sys

logging.basicConfig(filename='changeSize.log', level=logging.INFO)

def changeSize(path,width, height,output):
    try:
        os.mkdir(output)
        logging.info( 'create folder - ' +output )
    except OSError:
        logging.info( 'folder ' +output+' already exist')

    images = os.listdir(path=path)
    c = 0
    for imageName in tqdm(images):
        try:
            img = cv2.imread(path + imageName)
            resized = cv2.resize(img, (width, height))
            cv2.imwrite(output + imageName, resized)
            c+=1
        except:
            logging.warning('Failed resize for ' + path+imageName)
    logging.info('successful execution. Image resize: ' +str(c))


if __name__ == '__main__':
    print(sys.argv )
    changeSize(path=sys.argv[1], width=int(sys.argv[2]), height=int(sys.argv[3]), output=sys.argv[4])
    #changeSize(path="./dataset/image/Anime/",width=200,height=200,output="C:/project/ML_PSU/PSU/homework4/output/")
    #python changeSize.py ./dataset/image/Anime/ 200 200 C:/project/ML_PSU/PSU/homework4/output/

