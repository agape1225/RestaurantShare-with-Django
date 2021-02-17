from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


# Create your views here.

def index(request):
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    content = {'categories':categories, 'restaurants':restaurants}
    return render(request, 'shareRes/index.html', content)
    #return HttpResponse("index")

def restaurantDetail(request, res_id):
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'restaurant':restaurant}
    return render(request, 'shareRes/restaurantDetail.html', content)

def restaurantCreate(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'shareRes/restaurantCreate.html', content)

def Update_restaurant(request):
    resId = request.POST['resId']
    resCategory = request.POST['resCategory']
    category = Category.objects.get(id = resCategory)
    restaurant = Restaurant.objects.get(id = resId)
    resTitle = request.POST['resTitle']
    resLink = request.POST['resLink']
    resContent = request.POST['resContent']
    resLoc = request.POST['resLoc']

    restaurant.category = category
    restaurant.restaurant_name = resTitle
    restaurant.restaurant_link = resLink
    restaurant.restaurant_content = resContent
    restaurant.restaurant_keyword = resLoc
    restaurant.save()

    return HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id' : resId}))

def restaurantDelete(request, res_id):
    restaurant = Restaurant.objects.get(id = res_id)
    restaurant.delete()
    return HttpResponseRedirect(reverse('index'))

def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'shareRes/categoryCreate.html', content)

def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))

def Delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category.objects.get(id = category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))

def Create_restaurant(request):
    resCategory = request.POST['resCategory']
    category = Category.objects.get(id = resCategory)
    resTitle = request.POST['resTitle']
    resLink = request.POST['resLink']
    resContent = request.POST['resContent']
    resLoc = request.POST['resLoc']

    new_res = Restaurant(category = category, restaurant_name = resTitle,
                         restaurant_link = resLink, restaurant_content = resContent,
                         restaurant_keyword = resLoc)

    new_res.save()
    return HttpResponseRedirect(reverse('index'))

def restaurantUpdate(request, res_id):
    categories = Category.objects.all()
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'categories' : categories, 'restaurant' : restaurant}
    return render(request,'shareRes/restaurantUpdate.html',content)