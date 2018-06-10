import os
import urllib.request as ulib
import csv
import xml.etree.cElementTree as ET
from PIL import Image

csv_img = open('TV_in_Television_Test.csv','r')
csvreader = csv.reader(csv_img, delimiter=',', quotechar='|')

csv_ann = open('/home/kunal/Documents/codes/image_classifier/darkflow-master/BigQuery/Bouding Box Annotations/test/annotations-human-bbox.csv', 'r')
csvreader_ann = csv.reader(csv_ann, delimiter=',', quotechar='|')

def save_images(links):
    directory = 'TV_in_Television_Raw'
    if not os.path.isdir(directory):
        os.mkdir(directory)

    for i, link in enumerate(links):
        file_name = '{:06}.png'.format(i+1483)
        print (file_name)
        savepath = os.path.join(directory, file_name)
        ulib.urlretrieve(link, savepath)
    

links = []
imgID = []
imgTag = []
for row in csvreader_ann:
    imgID.append(row[0])
    imgTag.append(row[2])

for row in csvreader:
    n = 0
    if row[0] not in imgID:
        links.append(row[1])
    else:
        ind = imgID.index(row[0])
        while imgID[ind] == row[0]:
            if imgTag[ind] == '/m/07c52':
                n = 1
            ind += 1
        if n==0:
            links.append(row[1])

print (len(links))
save_images(links)