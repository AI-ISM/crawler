import requests
import json
from openpyxl import Workbook

url ="https://leetcode.com//api/problems/all/"
response = requests.get(url)
# print(response.json())
# Writing JSON data
with open('problemSet.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f)
# print(response['data']['translations'])