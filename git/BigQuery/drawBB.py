from PIL import Image
import cv2
import os
import xml.etree.cElementTree as ET

for image_file in os.scandir('TV_in_Television_Vali'):
    im = cv2.imread(image_file.path)
    img = Image.open(image_file.path)
    coords = []
    tree = ET.parse('TV_in_Television_Vali_xml/' + image_file.name.replace('png','xml'))
    root = tree.getroot()
    for j in range(len(root)-4):
        coords.append(int(root[j+4][4][0].text))
        coords.append(int(root[j+4][4][1].text))
        coords.append(int(root[j+4][4][2].text))
        coords.append(int(root[j+4][4][3].text))

    for i in range(0,len(coords),4):
        cv2.rectangle(im,(coords[i],coords[i+1]),(coords[i+2],coords[i+3]),(0,255,0),2)
    cv2.imwrite('TV_in_Television_Vali_BB/' + image_file.name,im)