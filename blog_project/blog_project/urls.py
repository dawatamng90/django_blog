"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'), # Read all posts
    path('post_detail/<int:post_id>/',views.post_detail, name='post_detail'), # Read single posts
    path('add/',views.add_post,name='add_post'), # Create post
    path('update_post/<int:post_id>/',views.update_post, name='update_post'), # Update post
    path('delete_post/<int:post_id>/',views.delete_post, name='delete_post'), # Delete post
]

