from bs4 import BeautifulSoup
import requests

result = requests.get("https://en.wikipedia.org/wiki/Special:Random")
result.raise_for_status()

wikiped = BeautifulSoup(result.text, "html.parser")

file_pointer = open("Article.txt", "w+", encoding='utf-8')

heading = wikiped.find("h1").text

file_pointer.write(heading + "\n")
for i in wikiped.select("p"):
    file_pointer.write(i.getText())

file_pointer.close()
print("File Saved as Article.txt")