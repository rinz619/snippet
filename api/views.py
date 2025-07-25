from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


from api.models import *

class login(APIView):
    def post(self,request):
        data = {}
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = User.objects.create(email=email)
            
        refresh_token = RefreshToken.for_user(user)
        access_token = refresh_token.access_token

        data['access_token'] = str(access_token)
        data['refresh_token'] = str(refresh_token)
        
        status_code = status.HTTP_200_OK
        tmp = {
                "status": True,
                "data":data,
                "message": "Success",
                "status_code": status_code,
            }
        return Response(tmp)
    
class tagslist(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        data = {}
        data['tags'] = list(Tags.objects.all().values('id','title'))
        status_code = status.HTTP_200_OK
        tmp = {
                "status": True,
                "data":data,
                "message": "Success",
                "status_code": status_code,
            }
        return Response(tmp)
        
            
class snippetlist(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        data = {}
        data['total_snippets'] = Snippets.objects.all().count()
        data['snippets'] = list(Snippets.objects.all().values('id','title'))
        status_code = status.HTTP_200_OK
        tmp = {
                "status": True,
                "data":data,
                "message": "Success",
                "status_code": status_code,
            }
        return Response(tmp)
    
    def post(self,request):
        
        title = request.POST.get('title')
        try:
            tag = Tags.objects.get(title=title)
        except:
            tag = Tags.objects.create(title=title)
        data = Snippets()
        data.title = title
        data.note = request.POST.get('note')
        data.user = request.user
        data.tags = tag
        data.save()
        status_code = status.HTTP_200_OK
        tmp = {
                "status": True,
                "message": "Success",
                "status_code": status_code,
            }
        return Response(tmp)
        
        
        
class snippetdetails(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        data = {}
        id = request.GET.get('id')
        snippet = Snippets.objects.get(id=id,user=request.user.id)
        data['detail'] = {
            'id':snippet.id,
            'title':snippet.title,
            'note':snippet.note,
            'datetime':snippet.created_at,
        }
        status_code = status.HTTP_200_OK
        tmp = {
                "status": True,
                "data":data,
                "message": "Success",
                "status_code": status_code,
            }
        return Response(tmp)
    
    def post(self,request):
        data = {}
        id = request.POST.get('id')
        snippet = Snippets.objects.get(id=id,user=request.user.id)
        title = request.POST.get('title')
        try:
            tag = Tags.objects.get(title=title)
        except:
            tag = Tags.objects.create(title=title)
        snippet.title = title
        snippet.note = request.POST.get('note')
        snippet.user = request.user
        snippet.tags = tag
        snippet.save()
        
        snippet = Snippets.objects.get(id=id,user=request.user.id)
        
        data['detail'] = {
            'id':snippet.id,
            'title':snippet.title,
            'note':snippet.note,
            'datetime':snippet.created_at,
        }
        status_code = status.HTTP_200_OK
        tmp = {
                "status": True,
                "data":data,
                "message": "Success",
                "status_code": status_code,
            }
        return Response(tmp)
        
        
       
            
class snippetdelete(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        data = {}
        id = request.GET.get('id')
        Snippets.objects.filter(id=id,user=request.user.id).delete()
        data['snippets'] = list(Snippets.objects.all().values('id','title'))
        status_code = status.HTTP_200_OK
        tmp = {
                "status": True,
                "data":data,
                "message": "Success",
                "status_code": status_code,
            }
        return Response(tmp)