import json
import requests
from openpyxl import Workbook


url = "https://leetcode-cn.com/graphql"
response = requests.get(url)
headers = response.headers
cookie = response.cookies.get_dict()
token = response.cookies.get_dict()['csrftoken']
Cookie = "csrftoken="+token
with open('payload.json', 'r') as f:
    data = json.load(f)
headers = {
    "accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": "238",
    "Cookie": Cookie,
    "content-type": "application/json",
    "csrftoken": token,
    "Host": "leetcode-cn.com",
    "Origin": "https://leetcode-cn.com",
    "Referer": "https://leetcode-cn.com/problemset/all/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "X-CSRFToken": token,
}

jsonRes = requests.post(url, json=data, headers=headers).json()
# Writing JSON data
# with open('problemSet.json', 'w', encoding='utf-8') as f:
#     json.dump(postRes.json(), f)
# print(jsonRes['data']['translations'])
items = jsonRes['data']['translations']
excel = Workbook()
sheet1 = excel.create_sheet('sheet1', index=0)

for item in items:
    # print(item)
    row = ['title', item['title'], 'questionId', item['question']['questionId']]
    print(row)
    sheet1.append(row)
excel.save(r'problemSet.xlsx')