from trello import TrelloClient
import requests
import re
import os
import timeit
from PIL import Image
import xlsxwriter

start = timeit.default_timer()

client = TrelloClient(
    api_key='f0f3c926292bcce056db551471e95247',
    api_secret='3aa90a9a950fec265b7629381e4f9f5d9e432f8a79365ea93f2e027a6b5fb1e5',
    token='c6c08bb22bf251ecf4c978ac63a41e896b4c6cde75f48b4b8a36cfb2e83637f1'
)

board = client.list_boards()[13]
# print(board)
# for list in 
# print(board.open_lists())


list_id = board.open_lists()[0].id
my_list = board.get_list(list_id)

cards = my_list.list_cards()
print(len(cards))

workbook = xlsxwriter.Workbook('Trello Cards.xlsx')
worksheet = workbook.add_worksheet()
row=0
column=0
print(cards)
attachments = []
k=0
for card in cards:
    # print(card.name)
    for i in range(0,4):
        attachment_name = card.get_attachments()[i].name
        if attachment_name:
            if "jpg" in attachment_name:
                if not "YYY" in attachment_name:
                    k = k+1
                    url=attachment_name
                    worksheet.write(row, column, card.name)
                    row=row+1
                    folder_name = card.name.replace(' ', '-')
                    folder_name = re.sub('[^a-zA-Z0-9//-]+', '', folder_name)
                    folder_name = folder_name.lower()
                    path_folder = os.getcwd() + '/trello-images/' + folder_name
                    if not os.path.exists(path_folder):
                        os.mkdir(path_folder) 
                    print(str(k) + " " + url )
                    r = requests.get(card.get_attachments()[i].url, allow_redirects=True)
                    open(os.getcwd() + '/trello-images/'+ folder_name + '/group1.jpg','wb').write(r.content)
                    foo = Image.open(os.getcwd() + '/trello-images/'+ folder_name + '/group1.jpg')
                    foo.save(os.getcwd() + '/trello-images/'+ folder_name + '/group1.webp',optimize=True,quality=10)
                    os.remove(os.getcwd() + '/trello-images/'+ folder_name + '/group1.jpg')


                    break

workbook.close()

stop = timeit.default_timer()

print('Time: ', stop - start)  