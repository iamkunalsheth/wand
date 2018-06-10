import os
import urllib.request as ulib
import csv
import xml.etree.cElementTree as ET
from PIL import Image

csv_BB = open('TV_in_Television_Vali_BB.csv','r')
csvreader = csv.reader(csv_BB, delimiter=',', quotechar='|')

def save_images(links):
    directory = 'TV_in_Television_Vali'
    if not os.path.isdir(directory):
        os.mkdir(directory)

    for i, link in enumerate(links):
        file_name = '{:06}.png'.format(i+1418)
        print (file_name)
        savepath = os.path.join(directory, file_name)
        ulib.urlretrieve(link, savepath)

        img = Image.open('TV_in_Television_Vali/' + file_name)
        widht, height = img.size
    
        annotation = ET.Element("annotation")
        folder = ET.SubElement(annotation, "folder").text = 'images'
        filename = ET.SubElement(annotation, "filename").text = file_name
        segmented = ET.SubElement(annotation, "segmented").text = '0'
        size = ET.SubElement(annotation, "size")
        width = ET.SubElement(size, "width").text = str(widht)
        height = ET.SubElement(size, "height").text = str(height)
        depth = ET.SubElement(size, "depth").text = '3'
        for j in range(0,int(len(coords[i])),4):
            print (coords[i])
            obj = ET.SubElement(annotation, "object")
            name = ET.SubElement(obj, "name").text = 'TV'
            pose = ET.SubElement(obj, "pose").text = 'Unspecified'
            truncated = ET.SubElement(obj, "truncated").text = '0'
            difficult = ET.SubElement(obj, "difficult").text = '0'
            bndbox = ET.SubElement(obj, "bndbox")
            xmin = ET.SubElement(bndbox, "xmin").text = str(int(round(float(coords[i][j])*int(widht))))
            ymin = ET.SubElement(bndbox, "ymin").text = str(int(round(float(coords[i][j+1])*int(height))))
            xmax = ET.SubElement(bndbox, "xmax").text = str(int(round(float(coords[i][j+2])*int(widht))))
            ymax = ET.SubElement(bndbox, "ymax").text = str(int(round(float(coords[i][j+3])*int(height))))
        tree = ET.ElementTree(annotation)
        tree.write("TV_in_Television_Vali_xml/" + file_name.replace('.png','.xml'))
    

links = []
coords = []
for row in csvreader:
    links.append(row[1])
    coords_temp = []
    for i in range(2,len(row)):
        if row[i] != '':
            coords_temp.append(row[i])
    coords.append(coords_temp)
    print (len(links))

save_images(links)