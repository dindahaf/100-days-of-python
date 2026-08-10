from bs4 import BeautifulSoup

with open ("website.html", "r") as file:
    content = file.read()


soup = BeautifulSoup(content, "html.parser")
# print(soup.title.string)
# print(soup.p)

# print(soup.find_all("p"))

all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.get_text())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)
print(heading.get_text())

section_heading = soup.find_all(name="h3", class_="heading")
print(section_heading)
for tag in section_heading:
    print(tag.get_text())


name = soup.select_one(selector="#name")
print(name)

name2 = soup.select_one(selector=".heading")
print(name2)
print(name2.get_text())

name3 = soup.select_one(selector="p a")
print(name3)
print(name3.get("href"))

name4 = soup.select(selector="p a")
print([name_value.get("href") for name_value in name4 ])