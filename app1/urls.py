from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from app1.views import CustomLoginView

urlpatterns = [
    path('', views.home, name='process_input'),
    path('find_donors/', views.find_donors_view, name='find_donors'),
    path('donate_blood/', views.donate_blood, name='donate_blood'),
    #path('request_blood/', views.request_blood, name='request_blood'),
    path('donate_blood_success/', views.donate_blood_success, name='donate_blood_success'),
    path('request_blood_success/', views.request_blood_success, name='request_blood_success'), 
    path('parking/', views.parking, name='parking'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('request_blood/', views.request_blood, name='request_blood'),  # Existing view for the "Request Blood" form
    path('login/', CustomLoginView.as_view(), name='login'),
    path('parking_videos/', views.parking_videos, name='video_page'),
    path('request_blood/', login_required(views.request_blood), name='request_blood'),
    path('logout/', views.logout_view, name='logout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
