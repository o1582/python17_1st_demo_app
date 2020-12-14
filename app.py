import requests
import re
import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():

    response = requests.get('https://www.google.com/search?q=%E7%8C%AB%E3%80%80%E7%94%BB%E5%83%8F&hl=ja&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiFjJ6Dnc3tAhUYZt4KHcVABnwQ_AUoAXoECBIQAw&biw=1287&bih=666')
    soup = BeautifulSoup(response.text,'lxml')
    links = soup.findAll('img')

    src_list = []
    for link in links:
        src_list.append(link.get('src'))

    return render_template("index.html", img_url_list=src_list)

if __name__ == "__main__":
    app.run(debug=True, port=5003)
