import classdemo
f=open("te/text.txt","a")
f.write("python向文件中写入"+"\n")
f.close()
fr=open("te/text.txt","r")
str = fr.read()
print(str)
fr.close()

t=(1,"chenhaiquan")
print(type(t))

try:
    a=1/0
except Exception as e:
    print(format(e))


