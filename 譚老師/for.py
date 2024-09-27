import scrapy
from bs4 import BeautifulSoup
import requests

n = 5
for i in range(n):  # 控制行數
    for j in range(i + 1):  # 控制每行的星數
        print("*", end=" ")
    print()  # 換行
