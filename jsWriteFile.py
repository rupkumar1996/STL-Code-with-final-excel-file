
import xlrd
from string import Template
import os
import shutil 




def jsWriter(folder_name, small_folder_name):
    if os.path.exists(folder_name +'/js'):
        shutil.rmtree(folder_name +'/js')
        shutil.copytree(os.getcwd() + '/js', folder_name+'/js')
    with open(folder_name+'/js/externalFile.js', "a") as fp:
        wb = xlrd.open_workbook('C:/Users/rupkumar.saha/Desktop/Ama_Files/final.xlsx')
        sheet = wb.sheet_by_index(0)
        nrows = sheet.nrows
#        print(nrows)

        l=0
        for j in range(nrows-1):
            if (sheet.cell_value(j+1,0) == small_folder_name) :
                fp.writelines("\n{")
                fp.writelines(Template("id: \"$i\",\n").substitute(i=l + 1))
                fp.writelines(Template("image: \"images/$k.webp\",\n").substitute(k=l + 1))
                fp.writelines(Template("price: \"Rs. $price\",\n").substitute(
                    price=int(float((str(sheet.cell_value(j + 1, 2)).strip()).replace(",", "")))))
                fp.writelines(Template("name: \"$name\",\n").substitute(name=sheet.cell_value(j + 1, 1)))

                fp.writelines(
                    Template("merchantName: \"$merchant\",\n").substitute(merchant=sheet.cell_value(j + 1, 6)))

                fp.writelines(Template("viewproductUrl: \"$url\"\n").substitute(url=sheet.cell_value(j + 1, 4)))
                fp.writelines("},")
                l=l+1




    fp.close()
    with open(folder_name+'/js/externalFile.js', 'rb+') as f:
        f.seek(0,2)                 
        size=f.tell()
        f.truncate(size-1)
    f.close()


    with open(folder_name+'/js/externalFile.js', "a") as fp:
        fp.writelines('\n\n]')

    fp.close()

rootdir = 'C:/Users/rupkumar.saha/Desktop/Ama_Files/'
for folders in os.listdir(rootdir):
    if folders == '.DS_Store' or folders == 'final.csv' or folders == 'final.xlsx' or folders == '~$final.xlsx':
        continue
    wb = xlrd.open_workbook('C:/Users/rupkumar.saha/Desktop/Ama_Files/final.xlsx')
    sheet = wb.sheet_by_index(0)

    nrows = sheet.nrows
    #        print(nrows)
    for j in range(nrows - 1):
        if (sheet.cell_value(j + 1, 0) == folders):
            print(folders)
            jsWriter(rootdir + folders, folders)
