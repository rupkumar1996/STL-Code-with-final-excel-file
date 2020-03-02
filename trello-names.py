from trello import TrelloClient
import requests
import re
import os
import timeit
from lxml import html
import csv
import os
import requests
from time import sleep
from random import randint
import xlrd
import urllib3
import random
#from jsWriteFile import jsWriter
from openpyxl import Workbook
from PIL import Image  
import aggdraw
from bs4 import BeautifulSoup
import re
from lxml.html import fromstring
from itertools import cycle
import random
import time
import bottlenose
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from PIL import Image

start = timeit.default_timer()

client = TrelloClient(
    api_key='f0f3c926292bcce056db551471e95247',
    api_secret='3aa90a9a950fec265b7629381e4f9f5d9e432f8a79365ea93f2e027a6b5fb1e5',
    token='c6c08bb22bf251ecf4c978ac63a41e896b4c6cde75f48b4b8a36cfb2e83637f1'
)

board = client.list_boards()[12]
# print(board)
# for list in 
# print(board.open_lists())


list_id = board.open_lists()[0].id
my_list = board.get_list(list_id)

names = my_list.list_cards()
print(len(names))

print(names)

with open('C:/Users/rupkumar.saha/Desktop/names.csv', 'w', newline='', encoding="utf-8") as csvfile:
    fieldnames = ['names']
    
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
   # writer.writeheader()    
    # print(extracted_data)
    for data in names:
        writer.writerow(data) 

    wb = Workbook()
    ws = wb.active
    with open('C:/Users/rupkumar.saha/Desktop/names.csv','r', encoding="utf-8") as f:
        for row in csv.reader(f):
            ws.append(row)
    wb.save('C:/Users/rupkumar.saha/Desktop/names.xlsx')

stop = timeit.default_timer()

print('Time: ', stop - start)  