number=9
guess=-1
# while guess!=number:
#     guess=int(input("请输入一个数字:"))
#     if guess==number:
#         print("苶喜你答对了")
#     elif guess<number:
#         print("太小了")
#     else:
#         print("太大了")

class MyNumber:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        if self.a<20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration

myclass=MyNumber()
it = iter(myclass)
for x in it:
    print(x)



str='chenhaiquan'
for letter in str:
    if letter=='h':
        break
    print(letter)

print("==============================")
for letter in str:
    if letter=='h':
        continue
    print(letter)


list=list(range(10))
print(list)
it = iter(list)
while next(it):
    print(next(it))

for item in list:
    print("item:",item)


def changNum(a):
    print(a)
    a=10

b=2
changNum(b)
print(b)