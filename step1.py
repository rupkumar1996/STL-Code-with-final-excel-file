import xlrd 
import os
import re
import shutil 
from bs4 import BeautifulSoup
from scraping import ReadAsin
import timeit
import csv
from openpyxl import Workbook


start = timeit.default_timer()

output_folder = 'C:/Users/rupkumar.saha/Desktop/Ama_Files'
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
  
# Give the location of the file 
loc = ('data.xlsx') 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
ncols = sheet.ncols

with open('C:/Users/rupkumar.saha/Desktop/Ama_Files/final.csv', 'w', newline='', encoding="utf-8") as csvfile:
    fieldnames = ['SL No.', 'NAME', 'SALE_PRICE', 'ORIGINAL_PRICE', 'URL', 'IMAGE', 'MERCHANT NAME']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# print("Sheet name is " + sheet_name)

start = int(input ("Enter starting row index:  "))
end = int(input ("Enter end row index:  "))

for i in range(start, end+1):
    x = i
    index_name = sheet.cell_value(i-1,1)
    # print(index_name)
    folder_name = index_name.replace(' ', '-')
    folder_name = re.sub('[^a-zA-Z0-9//-]+', '', folder_name)
    folder_name = folder_name.lower()

    path_folder =output_folder + '/'+folder_name
    if not os.path.exists(path_folder):
        os.mkdir(path_folder) 
    if not os.path.exists(path_folder+'/css'):
        shutil.copytree('css', path_folder+'/css')
    if not os.path.exists(path_folder+'/js'):
        shutil.copytree('js', path_folder+'/js')
    if not os.path.exists(path_folder+'/index.html'):
        shutil.copy('index.html', path_folder+'/index.html')
    if not os.path.exists(path_folder + '/images'):
        os.mkdir(path_folder + '/images')
    

    trello_folder_path = os.getcwd() + '/trello-images/'
   
    if os.listdir(trello_folder_path):
        files = os.listdir(trello_folder_path)
        for name in files:
            if name == folder_name:
                shutil.copyfile(trello_folder_path + '/' + name + '/group1.webp', path_folder + '/images' + '/group1.webp') 
    
        
    
    
    with open(path_folder + '/index.html') as fp:
        soup = BeautifulSoup(fp, 'lxml')

    tag = soup.title
    tag.string = index_name

    with open(path_folder + "/index.html", "w", encoding="utf-8") as file:
        file.write(str(soup))

    url_array = []
    j=5
    for j in range(5, ncols):
        if sheet.cell_value(i-1,j):
            url_array.append(sheet.cell_value(i-1,j))
            if j < ncols:
                j=j+1

        
    print("\n" + folder_name)
    ReadAsin(url_array, path_folder, x, folder_name)

stop = timeit.default_timer()
wb = Workbook()
ws = wb.active

with open('C:/Users/rupkumar.saha/Desktop/Ama_Files/final.csv', 'r', encoding="utf-8") as f:
    for row in csv.reader(f):
        ws.append(row)
wb.save('C:/Users/rupkumar.saha/Desktop/Ama_Files/final.xlsx')

print('Time: ', stop - start)  

