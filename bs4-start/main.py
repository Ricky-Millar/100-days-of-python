from bs4 import BeautifulSoup
import requests
with open("website.html", encoding='utf-8') as website:
    code = website.read()
line = "#--------------------------------------------------------------------#"
banana_soup = BeautifulSoup(code, 'html.parser')

#the soup object represents the whole HTML code, you can then pull stuff from that
print(line)

print(banana_soup.title)
print(banana_soup.title.string)
print(banana_soup.find_all(name="p")) #prints all paragraph tags

print(line)

for paragraph in banana_soup.find_all(name="p"):
    words = paragraph.get_text()
    print(words)

for anchors in banana_soup.find_all(name="a"):
    # for more deeper digging, you can specify the specific atribute
    link = anchors.get('href')
    print(link)
print(line)
#Find a specific tagged thing, so out of the h12 headings find the one with the id 'name'
print(banana_soup.find(name='h1', id='name'))
#to find a class you use "class_" as "class" is a term used in python.
print('#')
print(banana_soup.find(name='h3', class_="heading"))

print(line)
print('#Searching for attributes')
heading = banana_soup.find(name='h3', class_="heading")
print(heading.get("class"))
print(line)
print('#For really digging down')
#ths one is strange, the selector is based of the css code, it looks for a A within a P
link_in_paragraph = banana_soup.select_one(selector="p a")
print(link_in_paragraph)
things_with_class_heading = banana_soup.select(".heading")
print(things_with_class_heading)

print(f"{line}\n{line}\n{line}\n######WEB SCRAPER#########\n{line}\n{line}\n{line}\n")

response = requests.get('https://news.ycombinator.com/')

yc_webpage = response.text

miso_soup = BeautifulSoup(yc_webpage, "html.parser")

print (miso_soup.title)
artical_tag = miso_soup.find_all(name='a', class_="storylink")
artical_text = []
artical_links = []


for tag in artical_tag:
    artical_text.append(tag.getText())
    artical_links.append(tag.get("href"))
artical_scores = []
scores = miso_soup.find_all(name= "span", class_="score")
print(scores)
artical_scores = [int(score.getText().split()[0]) for score in scores]

max_score = max(artical_scores)
max_index = artical_scores.index(max_score)

print(artical_scores[max_index])
print(artical_text[max_index])
print(artical_links[max_index])

print(f"{line}\n{line}\n{line}\n######TOP MOVIES#########\n{line}\n{line}\n{line}\n")

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')

movie_webpage = response.text

carrot_soup = BeautifulSoup(movie_webpage, "html.parser")
string_list = carrot_soup.find_all(name= "img", class_="jsx-4015086601")
print(string_list)