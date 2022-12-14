from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings

app_name = 'blog'

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),

]
