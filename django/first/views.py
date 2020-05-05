from django.shortcuts import render

from django.views import View
from .models import Book
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication



# def first_funct(request):
#     books=Book.objects.all()

#     return render(request,'index.html',{'books':books})

class BookViewSet(viewsets.ModelViewSet):
    serializer_class=BookSerializer
    queryset=Book.objects.all()
    authentication_classes=(TokenAuthentication,)

