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
    corona_K_list = list()  # 빈 리스트 생성
    r = requests.get('https://www.worldometers.info/coronavirus/country/south-korea/')
    html = r.text # 지정한 링크에서 html 소스코드를 가져옴

    soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup

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

#게시판 메인
def board(request):
    #id를 역순으로 정렬함
    blogs = Blog.objects.order_by('-id')
    return render(request, 'BulletinBoard.html', {'blogs': blogs})

#게시판 세부
def detail(request, blog_id):
    # get_object_or_404에 사용할 모델인 Blog와 검색 조건인 blog_id, blog_id는 장고가 부여하는 고유번호, 조건에 맞는게 없으면 http404 익셉션
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'BoardDetail.html', {'blog': blog_detail})


def write(request):
    return render(request, 'BoardWrite.html')

#글 저장
def postboard(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()#글쓴 시간 자동저장
    blog.save()
    return redirect('/kcovidapp/BoardDetail/' + str(blog.id)) #쓴 글 페이지로 바로 이동

#글 수정
def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method == 'POST': #POST방식이면 데이터를 받아 검증하고 성공시 저장, get방식이면 update.html로 이동
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

#삭제
def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/kcovidapp/BulletinBoard/')

#게시물 검색
def search(request):
    blogs = Blog.objects.all().order_by('-id') #모든객체를 역순으로 담음

    s = request.POST.get('s', "") #s에 s의이름으로 넘어온것을 담음

    if site:
        blogs = blogs.filter(title__icontains=s) #s와 비교 
        return render(request, 'search.html', {'blogs': blogs, 's': s}) #같으면 search.html에 blogs와 s를 넘겨줌

    else:
        return render(request, 'search.html') #아니면 search.html 리턴
