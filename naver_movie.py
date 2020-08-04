import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
movie_list = soup.select('#content > div.article > div.obj_section > div.lst_wrap > ul > li')

movie_data = []

for movie in movie_list :
    a_tag  = movie.select_one('dl.lst_dsc > dt.tit > a')
            
    movie_title = a_tag.text
    movie_link = a_tag['href']
    code_idx = movie_link.find("code=") + len("code=")

    data = {
        "title" : movie_title, 
        "code" : movie_link[code_idx:]
    }
    movie_data.append(data)

print(movie_data)
