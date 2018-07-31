import bs4
import expanddouban
import time
# 参数tags可以包含多个以逗号分隔的标签
base_type_douban_url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影{}"

"""task1: getMovieUrl() function
return a string corresponding to the URL of douban movie lists given category and location.
"""


def get_movie_url(category, location=""):
    url = None
    tags = ""
    if location == "":
        tags = "," + category
    else:
        tags = "," + category + "," + location
    url = base_type_douban_url.format(tags)
    print(url)
    return url

# task2: getHtml(url)


def getHtml(url):
    html = expanddouban.getHtml(url, True)
    return html


"""task3: define movie class, add constructor 
"""


class Movie:
    def __init__(self, name, rate, location, category, info_link, cover_link): # 构造函数
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link


"""task4:
return a list of Movie objects with the given category and location.
"""


def get_movies(category, location):
    movies = []
    url = get_movie_url(category, location)
    html = expanddouban.getHtml(url, True)

    soup = bs4.BeautifulSoup(html, "html.parser")
    content_div = soup.find(class_="list-wp")

    for movie in content_div.find_all(class_="item", recursive=False):
        name = movie.find(class_="title").string
        rate = movie.find(class_="rate").string
        info_link = movie['href']
        cover_link = movie.img['src']
        movies.append(Movie(str(name), str(rate), str(location), str(category), str(info_link), str(cover_link)))

    # for i in range(len(movies)):
    #     print(movies[i].__dict__)

    return movies

# task 5 选择3个喜欢的电影类型，获取所有的地区，遍历所有类型和地区获取电影列表
# 从网页上选取你最爱的三个电影类型


my_favorite_tags = ["喜剧", "爱情", "历史"]

# 获取所有地区
locations = []
html_movie = expanddouban.getHtml(base_type_douban_url)

soup = bs4.BeautifulSoup(html_movie, "html.parser")
tags_div = soup.find(class_="tags")
for tags_location in tags_div.contents[2].find_all("li"):
    location = tags_location.span.string
    locations.append(location)
locations.pop(0)
print(locations)

# 获取三个类型、所有地区
movies_all_favorite = []
for i in range(len(my_favorite_tags)):
    for j in range(len(locations)):
        movies = get_movies(my_favorite_tags[i], locations[j])
        for m in movies:
            movies_all_favorite.append(m)
        time.sleep(5)

# 将列表输出到文件 movies.csv
with open('movies.csv', 'w') as f:
    for i in range(len(movies_all_favorite)):
        movie = movies_all_favorite[i]
        f.write(",".join([movie.name, movie.rate, movie.location, movie.category, movie.info_link,
                          movie.cover_link]) + "\n")

# task 6
# 统计每个类别的电影个数
category_1_movies = []
category_2_movies = []
category_3_movies = []

for i in range(len(movies_all_favorite)):
    movie = movies_all_favorite[i]
    if movie.category == my_favorite_tags[0]:
        category_1_movies.append(movie)
    elif movie.category == my_favorite_tags[1]:
        category_2_movies.append(movie)
    else:
        category_3_movies.append(movie)

category_1_movies_nums = len(category_1_movies)
category_2_movies_nums = len(category_2_movies)
category_3_movies_nums = len(category_3_movies)

# 统计每个类别中每个地区的电影个数
dic_1_movies = {}
dic_2_movies = {}
dic_3_movies = {}


def set_movie(dic_movies, key):
    counts = dic_movies.get(key, 0)
    dic_movies[key] = counts + 1
    return dic_movies


for i in range(len(category_1_movies)):
    movie = category_1_movies[i]
    location = movie.location
    dic_1_movies = set_movie(dic_1_movies, location)

for i in range(len(category_2_movies)):
    movie = category_2_movies[i]
    location = movie.location
    dic_2_movies = set_movie(dic_2_movies, location)

for i in range(len(category_3_movies)):
    movie = category_3_movies[i]
    location = movie.location
    dic_3_movies = set_movie(dic_3_movies, location)

# 每个电影类别中，数量排名前三的地区

zip_1 = zip(dic_1_movies.values(), dic_1_movies.keys())
list_1 = sorted(list(zip_1), reverse=True)
nums_1, locations_1 = zip(*list_1)

zip_2 = zip(dic_2_movies.values(), dic_2_movies.keys())
list_2 = sorted(list(zip_2), reverse=True)
nums_2, locations_2 = zip(*list_2)

zip_3 = zip(dic_3_movies.values(), dic_3_movies.keys())
list_3 = sorted(list(zip_3), reverse=True)
nums_3, locations_3 = zip(*list_3)

# 分别占此类别电影总数的百分比

# my_favorite_tags[0]
locations_1_1 = locations_1[0]
percents_1 = []
percent_1_1 = '%.2f%%'%((nums_1[0]/category_1_movies_nums)*100)
percents_1.append(percent_1_1)
locations_1_2 = locations_1[1]
percent_1_2 = '%.2f%%'%((nums_1[1]/category_1_movies_nums)*100)
percents_1.append(percent_1_2)
locations_1_3 = locations_1[2]
percent_1_3 = '%.2f%%'%((nums_1[2]/category_1_movies_nums)*100)
percents_1.append(percent_1_3)

# my_favorite_tags[1]
locations_2_1 = locations_2[0]
percents_2 = []
percent_2_1 = '%.2f%%'%((nums_2[0]/category_2_movies_nums)*100)
percents_2.append(percent_2_1)
locations_2_2 = locations_2[1]
percent_2_2 = '%.2f%%'%((nums_2[1]/category_2_movies_nums)*100)
percents_2.append(percent_2_2)
locations_2_3 = locations_2[2]
percent_2_3 = '%.2f%%'%((nums_2[2]/category_2_movies_nums)*100)
percents_2.append(percent_2_3)

# my_favorite_tags[2]
locations_3_1 = locations_3[0]
percents_3 = []
percent_3_1 = '%.2f%%'%((nums_3[0]/category_3_movies_nums)*100)
percents_3.append(percent_3_1)
locations_3_2 = locations_3[1]
percent_3_2 = '%.2f%%'%((nums_3[1]/category_3_movies_nums)*100)
percents_3.append(percent_3_2)
locations_3_3 = locations_3[2]
percent_3_3 = '%.2f%%'%((nums_3[2]/category_3_movies_nums)*100)
percents_3.append(percent_3_3)
# 将列表输出到文件 output.txt
with open('output.txt', 'w') as f:
    for i in range(len(my_favorite_tags)):
        f.write(my_favorite_tags[i] + ": \n")
        for j in range(3):
            if i == 0:
                f.write(locations_1[j] + ":" + percents_1[j] + "\n")
            elif i == 1:
                f.write(locations_2[j] + ":" + percents_2[j] + "\n")
            else:
                f.write(locations_3[j] + ":" + percents_3[j] + "\n")

