from django.http import HttpResponse

class GTemp(object):
    def __init__(self,response):
        self.response = response

    def __call__(self,requset):
        return HttpResponse("<h1><center>Site Under maintenance....</center></h1>")