import requests
from bs4 import BeautifulSoup

web_data =  requests.get(url="https://news.ycombinator.com/news")
web_page = web_data.text

soup = BeautifulSoup(web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)


subtexts = soup.find_all(class_="subtext")
article_upvotes = [int(line.span.span.getText().strip(" points")) if line.span.span else 0 for line in subtexts]
print(article_upvotes)
largest_number = max(article_upvotes)
print(largest_number)

largest_number_index = article_upvotes.index(largest_number)

print(
    f"Most upvoted article: {article_texts[largest_number_index]}\n"
    f"Number of upvotes: {article_upvotes[largest_number_index]} points\n"
    f"Available at: {article_links[largest_number_index]}."
)