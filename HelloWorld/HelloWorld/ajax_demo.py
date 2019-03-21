from django.http import JsonResponse

from bean_demo import Student


def get_student(request):
    list=[]
    for index in range(10):
        st=Student("zhangsan"+str(index),28+index)
        list.append(st)
    return JsonResponse(list)