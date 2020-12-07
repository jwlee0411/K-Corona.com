from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('FrameKorea/',views.korea, name='korea'),
    path('FrameMain/',views.main, name='main'),
    path('FrameProtect/',views.protect,name='protect'),
    path('FrameSite/', views.site, name='site'),
    path('FrameWorld/', views.world,name='world'),
    path('BulletinBoard/',views.board,name='board'),
    path('BoardDetail/<int:blog_id>', views.detail, name='detail'),
    path('write/',views.write, name='write'),
    path('postboard/',views.postboard, name='postboard'),
    path('update/<int:blog_id>/', views.update, name='update'),
    path('delete/<int:blog_id>/', views.delete, name='delete'),
    path('search', views.search, name='search'),

]