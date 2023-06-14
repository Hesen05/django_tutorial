from home.models import Category,Strories
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from home.api.serializers import CategorySerial,StroriesSerial,CategoryCreateSerial2
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# @api_view(['GET'])
# def category_api(request):
#     categories = Category.objects.all()
#     serial = CategorySerial(categories, many = True, context = {'request':request})
#     return Response(data=serial.data)
# @api_view(['GET'])
# def category_api_slug(request, slug):
#     if request.method == 'POST':
#         pass

#     categories = Category.objects.get(slug = slug )
#     serial = CategorySerial(categories)
#     return Response(data=serial.data)
class CategoryView(APIView):
    def get(self,request):
        datas = Category.objects.all()
        serial = CategorySerial(datas, many = True)
        return Response(data = serial.data)
    def post(self,request):
        data = request.data
        serial = CategorySerial(data = data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors)
        

class CategoryViewSlug(APIView):
    def get(self,request,slug):
        data = get_object_or_404(Category, slug = slug)
        # category = Category.objects.get(slug = slug)
        serial = CategorySerial(data)
        return Response(data=serial.data)
    def post(self,request,slug):
        data = Category.objects.get(slug = slug)
        serial = CategoryCreateSerial2(data, data =request.data)
        if serial.is_valid():
            serial.save()
        return Response(data=serial.data)

class StroriesView(APIView):
    def get(self,request,*args,**kwargs):
        strories = Strories.objects.all()
        serial = StroriesSerial(strories, many = True, context = {'request':request})
        return Response(data = serial.data)

    def post():
        pass