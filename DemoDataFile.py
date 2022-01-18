File = open('DataFile')

#print(File.read())

#Line = File.readline()

# while Line != "":
#     print(Line)
#     Line = File.readline()

d=[]
for i in File.readlines():
   if i != "":
     d.append(i)

print(d)


#print(File.readline())