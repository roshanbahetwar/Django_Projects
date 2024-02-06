from django.http import HttpResponse

class TempW(object):
    def __init__(self,response):
        self.response = response

    def __call__(self,request):
        print("before request")
        response = self.response(request)
        print("after execution")
        return response