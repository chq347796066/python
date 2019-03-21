from json import JSONEncoder

from django.http import HttpResponse
from django.http import JsonResponse
from HelloWorld.bean_demo import Student
import json

class MyEncoder(JSONEncoder):
    def default(self,o):
        return o.__dict__



def hello(request):
    return HttpResponse("Hello world !")

def get_student(request):
    print("method:%s"%request.method)
    username=request.GET.get('username')
    print("username: %s"%username)

    print("get student")
    list = []
    encode=MyEncoder()
    for index in range(10):
        st = Student("zhangsan" + str(index), 28 + index)
        st_en = encode.encode(st)
        list.append(st_en)
    json_str=json.dumps(list,ensure_ascii=False)
    return JsonResponse(json_str,safe=False)


