text = []
for char in str:
    if char == "0":
        text.append("#")
    if char == "1":
        text.append("*")
return "".join(text)