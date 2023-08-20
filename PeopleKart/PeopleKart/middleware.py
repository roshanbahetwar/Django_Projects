from django.http import HttpResponse
"""this is for middleware...
1. create middleware.py module at project level, write code
2. go settings.py module, register in middleware, write 'PeopleKart.middleware.Temp'
where 'PeopleKart' is project name(for project level), where 'middleware' is module name
which are create in project level and 'Temp' is class inside middleware.py module
"""

class Temp(object):
    def __init__(self,response):
        self.response = response

    def __call__(self,request):
        return HttpResponse('<h1><center>Site Is In Under Maintenance...</center></h1>')