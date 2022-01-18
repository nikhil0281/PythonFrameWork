# with open('DataFile', 'r') as reader:
#     content = reader.readlines()
#     content1 = reversed(content)
#     print(content)

try:
    File = open('DataFile12')
    content1 = File.readlines()
    for i in content1:
        assert(i != "")
        print(i)
    try:
        with open('DataFile','w') as writer:

            for j in reversed(content1):
                print(j)
                if j =="":
                    raise Exception("String is blank")
                writer.write(j)
    except:
        print("Write file doesn't exist")

except Exception as e :
    print(e)

finally:
    print("Finally block is executing")




