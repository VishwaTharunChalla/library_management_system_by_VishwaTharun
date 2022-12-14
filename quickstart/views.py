# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from quickstart.models import Category,Book,User,Publisher,Author,Book
from rest_framework import viewsets
from quickstart.serializers import UserSerializer,CategorySerializer,PublisherSerializer,AuthorSerializer,BookSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import signup_required
from django.shortcuts import get_object_or_404
from quickstart.models import User
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
# Create your views here.
@login_required
def index(request):
	categories = Category.objects.all()
	return render(request,"index.html",{"categories":categories})

@login_required
def category(request,category_id):
	books = Book.objects.filter(categories__id=category_id)
	return render(request,"category.html",{"books":books})	

@login_required
def book(request,book_id):
	book = Book.objects.get(id=book_id)
	return render(request,"book.html",{"book":book})
@signup_required
def index(request):
	categories = Category.objects.all()
	return render(request,"index.html",{"categories":categories})

@signup_required
def category(request,category_id):
	books = Book.objects.filter(categories__id=category_id)
	return render(request,"category.html",{"books":books})	

@signup_required
def book(request,book_id):
	book = Book.objects.get(id=book_id)
	return render(request,"book.html",{"book":book})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registerlibrarian.html'

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response({'serializer': serializer, 'user': user})

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'user': user})
        serializer.save()
        return redirect('profile-list')
    def update(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'user': user})
        serializer.save()
        return redirect('profile-list')
    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response({'serializer': serializer, 'user': user})





