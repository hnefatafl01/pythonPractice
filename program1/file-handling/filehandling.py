file=open("./files/example.txt",'r')
# print(type(file))
content=file.read()
content=file.readlines()
# print(content)
file.seek(0)
content1=[i.rstrip("\n") for i in content]
print(content1)
file.close()
