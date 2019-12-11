from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'obiadekchan'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ThreadView.as_view(), name='thread'),
    path('mode/', views.ModeratorView.as_view(), name='mode'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('banned/', views.banned, name='banned')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)