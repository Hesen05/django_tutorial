from typing import Optional
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import User



# class BlockIp(MiddlewareMixin):
#     blockUser = [User.objects.get(username ='eli' )]
#     def __call__(self, request: HttpRequest) -> HttpResponse:
        
#         return super().__call__(request)