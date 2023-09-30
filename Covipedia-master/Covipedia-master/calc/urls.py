from django.urls import path
from . import views
from .views import home,addresources
urlpatterns=[
    path('',views.home,name='home'),
    path('addresources/',views.addresources,name='addresources'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('like/<int:pk>/', views.like, name='post-like'),
    path('dislike/<int:pk>', views.dislike, name='post-dislike')
]