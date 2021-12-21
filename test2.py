import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions/54106071/how-can-i-set-up-a-virtual-environment-for-python-in-visual-studio-code'

response = requests.get(url).text
soup = BeautifulSoup(response,'html.parser')

div = soup.find(class_='d-flex sm:fd-column')
heading = div.h1.a
print(heading['href'])