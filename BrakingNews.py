from tkinter import *
import requests
import json

# url
url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=4dbad97afb1f467b88320f20c20a6019"
news = requests.get(url).text
news_dict = json.loads(news)
arts = news_dict['articles']

root = Tk()
root.title("News Reader")
root.geometry("900x600")
for article in arts:
    ls = (article['title'])
    # print(ls)
text_label = Label(text=ls)
text_label.pack(anchor="center",padx=100, pady=100) 
root.mainloop()
