file = "tmn.txt"

with open(file, "r", encoding="utf-8") as f:
    text = f.read()

para = []
paragraphs =  text.split("\n\n")

for paragraph in paragraphs:
    paragraph = paragraph.replace(paragraph, "<p>"+paragraph+"</p>")
    para.append(paragraph)

#print(para)
#with open('test_file_with_tags.txt', 'w') as output:
    #output.write(str(para))

listToStr = ' '.join([str(elem) for elem in para])
#print(listToStr)

with open('tmn_with_tags.txt', 'w') as output:
    output.write(listToStr)

#def add_p_tags(text):
    #paragra
    #text = text.split("\n\n")
    #text = "<p>"+
