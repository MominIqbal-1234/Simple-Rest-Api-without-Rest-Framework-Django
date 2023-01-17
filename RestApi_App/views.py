from django.http import HttpResponse

from RestApi_App.models import MyTableName
from django.core.serializers import serialize
from django.views import View

# Function Base Api
def home(request):
    name = MyTableName.objects.all()
    result = serialize('json',name,fields=('name'))
    return HttpResponse(result,content_type='application/json')

# Class Base Api
class Home(View):
    def get(self,request):
        name = MyTableName.objects.all()
        result = serialize('json',name,fields=('name'))
        return HttpResponse(result,content_type='application/json')