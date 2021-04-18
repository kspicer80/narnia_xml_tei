file = "/Volumes/GoogleDrive/My Drive/DHStuff/Projects/narnia/data/narnia/pc.txt"

with open(file, "r", encoding="utf-8") as f:
    text = f.read()

chapters = text.split("_Chapter ")[1:]
print (chapters[0][0:300])

data = []
for chapter in chapters:
    paras = []
    paragraphs = chapter.split("\n\n")
    for paragraph in paragraphs:
        if paragraph != "":
            paragraph = paragraph.replace("\n", " ")
            paras.append(paragraph)
            data.append(paras)

print(len(data))
