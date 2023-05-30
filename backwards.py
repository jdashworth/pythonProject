text = input("Write text here : ")
textlist = list(text)
backward = textlist[::-1]
newtext = ''.join(backward)
print(newtext)
