from operator import itemgetter
import json

def open_json():
   with open("operations.json", encoding="utf-8") as f:
      data = json.load(f)
   return data

data = open_json()

def return_data(data):
   data_list = []

   for item in data:
      if "from" in item:
         data_list.append(item)

   data_one_second = sorted(data_list, key=itemgetter('date'), reverse=True)
   data_sorted = sorted(data_one_second, key=itemgetter('state'), reverse=True)
   return data_sorted

data_sorted = return_data(data)

def description(data_sorted, y):
   text = []
   text += data_sorted[y]["date"][0:10], data_sorted[y]["description"]
   print(data_sorted[y]["date"][0:10], data_sorted[y]["description"])
   return text
      
def screen(data_sorted,y):
   text = []
   if data_sorted[y]["description"] != "Открытие вклада":
         from_ = data_sorted[y]["from"].split(" ")
         to_ = data_sorted[y]["to"].split(" ")
         text += from_[-2] , from_[-1][0:4] , f"{from_[-1][4:6]}**" , "****" , from_[-1][-4:] , "-->" , to_[-2] , f"**{to_[-1][16:]}"
         print(from_[-2] , from_[-1][0:4] , f"{from_[-1][4:6]}**" , "****" , from_[-1][-4:] , "-->" , to_[-2] , f"**{to_[-1][16:]}")
   return text

def amount(data_sorted,y):
   text = []
   text += data_sorted[y]["operationAmount"]["amount"] , data_sorted[y]["operationAmount"]["currency"]["name"]
   print(data_sorted[y]["operationAmount"]["amount"] , data_sorted[y]["operationAmount"]["currency"]["name"])
   return text

def space():
   text = []
   text += ""
   print("")
   return text

def view_screem(data_sorted):
   text = []
   y = 0
   while True:
      text += description(data_sorted,y)
      
      text += screen(data_sorted,y)

      text += amount(data_sorted,y)

      text += space()
      y += 1
      
      if y == 5:
         break
   return text


