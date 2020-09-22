import json
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

def create_diagram():
	file_path = 'D:/Study/Telegram History Chat Export/json 2/chat_history.json'
	with open(file_path, encoding='utf-8') as data_file:
	    data = json.load(data_file)

	day_arr = []
	messages_amount_arr = []

	j = 0
	k = 0
	messages_arr = data["chats"]["list"][0]["messages"]
	amount_of_messages = len(data["chats"]["list"][0]["messages"])
	unique_days = 0
	for i in range(amount_of_messages - 1):
	    if (messages_arr[i]["date"][0:10] != messages_arr[i + 1]["date"][0:10]):
	        unique_days += 1
	date_arr = []

	for message in messages_arr:
	    date_arr.append(message["date"][0:10])

	c = Counter(date_arr)
	df = pd.DataFrame.from_dict(c, orient='index').reset_index()
	plt.rcParams['figure.figsize'] = [800, 100]
	plt.bar(c.keys(), c.values())
	plt.savefig("graphic.png")

	df.to_excel("D:/Study/Telegram History Chat Export/output.xlsx")

if __name__ == "__main__":
	create_diagram()




