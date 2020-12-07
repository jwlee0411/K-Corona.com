from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Blog
from .form import BlogUpdate

from bs4 import BeautifulSoup
import requests


# Create your views here.


def home(request):
    return render(request, 'home.html')


def korea(request):
    corona_K_list = list()
    # 한국
    r = requests.get('https://www.worldometers.info/coronavirus/country/south-korea/')
    html = r.text

    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.select('.maincounter-number > span')

    for title in titles:
        corona_K_list.append(title.text)

    totalCase = corona_K_list[0]
    return render(request, 'FrameKorea.html', {'totalCase': totalCase})


def main(request):
    return render(request, 'FrameMain.html')


def protect(request):
    return render(request, 'FrameProtect.html')


def site(request):
    return render(request, 'FrameSite.html')


def world(request):
    # msg = "Hello World!"
    #
    # html = requests.get('https://www.worldometers.info/coronavirus/').text
    # html_soup = BeautifulSoup(html, 'html.parser')
    # rows = html_soup.find_all('tr')
    #
    # def extract_text(row, tag):
    #     element = BeautifulSoup(row, 'html.parser').find_all(tag)
    #     text = [col.get_text() for col in element]
    #     return text
    #
    # corona_list = []
    # for row in rows:
    #     test_data = extract_text(str(row), 'td')[1:9]
    #     corona_list.append(test_data)
    #
    #
    #
    # msg = str(corona_list)

    # debug_01 = str(requests.get('https://www.worldometers.info/coronavirus/'))

    # 전세계
    r = requests.get('https://www.worldometers.info/coronavirus/')
    html = r.content

    soup = BeautifulSoup(html, 'html.parser')
    # titles = soup.select('.post-content > h4 > a')
    titles = soup.select('.maincounter-number > span')

    corona_world_list = list()

    print(titles)
    for title in titles:
        corona_world_list.append(title.text)

    totalCase = str(corona_world_list[0])
    deathCase = str(corona_world_list[1])
    recoveredCase = str(corona_world_list[2])

    # return render(request, 'FrameWorld.html', {'totalCase': totalCase}, {'deathCase': deathCase}, {'recoveredCase': recoveredCase})
    return render(request, 'FrameWorld.html', {'totalCase': totalCase})
    # return render(request, 'FrameWorld.html', {'corona_world_list' : corona_world_list})
    # return render(request, 'FrameWorld.html', {'titles':titles})


def Iframe(request):
    return render(request, 'Iframe.html')


def board(request):
    blogs = Blog.objects.order_by('-id')
    return render(request, 'BulletinBoard.html', {'blogs': blogs})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'BoardDetail.html', {'blog': blog_detail})


def write(request):
    return render(request, 'BoardWrite.html')


def postboard(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/kcovidapp/BoardDetail/' + str(blog.id))


def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method == 'POST':
        form = BlogUpdate(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.pub_date = timezone.now()
            blog.save()
            return redirect('/kcovidapp/BoardDetail/' + str(blog.id))
    else:
        form = BlogUpdate(instance=blog)

        return render(request, 'update.html', {'form': form})


def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/kcovidapp/BulletinBoard/')


def search(request):
    blogs = Blog.objects.all().order_by('-id')

    q = request.POST.get('q', "")

    if q:
        blogs = blogs.filter(title__icontains=q)
        return render(request, 'search.html', {'blogs': blogs, 'q': q})

    else:
        return render(request, 'search.html')
