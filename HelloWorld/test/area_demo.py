x=100
globals()
locals()
def test_area():
    global x
    print(x)
    x=123
    print(x)



if __name__=="__main__":
    y=1000
    print(globals())