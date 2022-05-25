from bs4 import BeautifulSoup
import requests
import lxml

url = "http://upload.itcollege.ee/~aleksei/test.xml"
xml_content = requests.get(url).content
soup = BeautifulSoup(xml_content,'xml')

# your code here
