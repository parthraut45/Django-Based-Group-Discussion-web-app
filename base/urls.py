
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/' , views.loginPage , name="log"),
    path('logout/' , views.logoutUser , name="logout"),
    path('register/' , views.registerUser , name="register"),
    path('',views.home , name = "home"), #we gave the path to fuction we gonna call when user ask for
    path('room/<str:prime>/',views.rooms , name = "room"),
    path('profile/<str:prime>/',views.userProfile , name = "user-profile"),
    path('create-room/' , views.createRoom,name="create-room"),
    path('update-room/<str:prime>/' , views.updateRoom,name="update-room"),
    path('delete-room/<str:prime>/' , views.deleteRoom,name="delete-room"),
    path('delete-message/<str:prime>/' , views.deleteMessage,name="delete-message"),
    path('update-user/' , views.updateUser,name="update-user"),
    path('topics/' , views.topicsPage,name="topics"),
    path('activity/' , views.activityPage,name="activity"),
]