#Top100UkrainianFilms
import requests
from bs4 import BeautifulSoup

URL='https://dovzhenkocentre.org/top-100-all/'
page=requests.get(URL)

# print(page.status_code)
films=[]
allData=[]

soup=BeautifulSoup(page.text, 'html.parser')
allData=soup.find_all('h3')
# films = allData[2:]
# for i in range(2,len(allData) ):
#     films.append(allData[i].text)

def writingFile():
    with open('film.txt', 'w') as file:
        for film in allData:
            file.write(film.text + '\n')
writingFile()

 

