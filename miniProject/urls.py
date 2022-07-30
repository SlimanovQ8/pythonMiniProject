"""miniProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from event_planner.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("event/add/", AddEventApiView.as_view(), ),
    path("test/", EventListPagination.as_view(), ),
    path("event-lists/", EventListAPIView.as_view(), ),
    path("event/search/", EventsSearchListAPIView.as_view(), ),
    path("full/", FullyBookedEvents.as_view(), ),
    path("date/", EventListAfterCertainDateAPIView.as_view(), ),
    path("event/<organizer_name>/", EventAPIView.as_view(), ),
    path("event/<organizer_name>/update", EventObjAPIUpdateView.as_view()),
    path("event/<organizer_name>/delete", EventDeleteAPIView.as_view()),

]
