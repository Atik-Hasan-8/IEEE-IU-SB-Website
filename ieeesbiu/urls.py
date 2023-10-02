"""ieeesbiu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from  team import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home_view, name='home'),
    path('event/', views.events_view, name='events'),
    path('about/', views.about_view, name='about'),
    path('teams/', views.team_view, name='teams'),
    path('blog/', views.blog_view, name='blog'),
    path('contact/', views.contact_view, name='contact'),
    path('event/event2/',views.event2_view,name='event2'),
    path('event/event-description-1/',views.events_single_1_view,name='event-single-1'),
    path('event/event-description-2/',views.events_single_2_view,name='event-single-2'),
    path('event/event-description-3/',views.events_single_3_view,name='event-single-3'),
    path('event/event-description-4/', views.events_single_4_view,name='event-single-4'),
    path('event/event-description-5/',views.events_single_5_view,name='event-single-5'),
    path('event/event-description-6/',views.events_single_view,name='event-single'),
    path('event/event-description-7',views.events_single_2_1_view,name='event-single-21'),
    path('event/event-description-8/',views.events_single_2_2_view,name='event-single-22'),
    path('event/event-description-9/',views.events_single_2_3_view,name='event-single-23'),
    path('event/event-description-10/',views.events_single_2_4_view,name='event-single-24'),
    path('event/event-description-11/',views.events_single_2_5_view,name='event-single-25'),
    path('event/event-description-12/',views.events_single_2_6_view,name='event-single-26'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
