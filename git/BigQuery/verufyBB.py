import os
import csv

csv_img = open('TV_in_Television_Vali.csv','r')
csvreader = csv.reader(csv_img)

imgID = []
imglink =[]
for row in csvreader:
    imgID.append(row[0])
    imglink.append(row[1])
csv_img.close()
print (len(imgID))


csv_ann = open('/home/kunal/Documents/codes/image_classifier/darkflow-master/BigQuery/Bouding Box Annotations/validation/annotations-human-bbox.csv', 'r')
csvreader = csv.reader(csv_ann, delimiter=',', quotechar='|')

csv_BB = open('TV_in_Television_Vali_BB.csv','w')
csvwriter = csv.writer(csv_BB)

last_row = 'abc86960879d2e09'
coords_list = []
n = 1
for row in csvreader:
    if row[0] in imgID and row[2] == '/m/07c52':
        print (n)
        if row[0] != last_row:
            n += 1
            print row[0]
            index = imgID.index(last_row)
            csvwriter.writerow([imgID[index],imglink[index]] + coords_list)
            last_row = row[0]
            coords_list = [row[4],row[6],row[5],row[7]]
        else:
            coords_list += [row[4],row[6],row[5],row[7]]

csv_ann.close()
csv_BB.close()

