# with open('DataFile', 'r') as reader:
#     content = reader.readlines()
#     content1 = reversed(content)
#     print(content)

File = open('DataFile')
Line= File.readline()
while Line != "":
     print(Line)
     Line = File.readline()
with open('dataFile','w') as writer:
     for i in reversed(Line):
        print(i)
        # .



