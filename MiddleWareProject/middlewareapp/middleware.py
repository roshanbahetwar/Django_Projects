from django.http import HttpResponse

class Temp(object):
    def __init__(self,response):
        self.response = response

    def __call__(self,request):
        return HttpResponse('<h1><center>Site is Under Maintenance...</center></h1>')  # it is return from middleware
        # print('before request')
        # response = self.response(request)
        # print('after execution')
        # return response