import datetime

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.pagination import  PageNumberPagination


from .models import Event
from django.db.models import F
from .serializers import CreateSerializer, ListSerializer, UpdateSerializer, DetailSerializer, EventAfterCertainDateSerialzer
from django.db.models.functions import Lower
from rest_framework import filters, generics

class ResultsSetPagination(PageNumberPagination):
    page_size = 2 # add 10 objects or make the page size equal 1 to see the pages list
    page_size_query_param = 'page_size'

class EventListPagination(ListAPIView):
    pagination_class = ResultsSetPagination
    queryset = Event.objects.all()
    serializer_class = ListSerializer

class EventsSearchListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = ListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class AddEventApiView(CreateAPIView):
    serializer_class = CreateSerializer


class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = ListSerializer


class EventListAfterCertainDateAPIView(ListAPIView):
    serializer_class = EventAfterCertainDateSerialzer

    def get_queryset(self):
        return Event.objects.filter(start_date__gt=datetime.date(2022, 8, 7)).order_by("start_date", Lower("name"))



class FullyBookedEvents(ListAPIView):
    queryset = Event.objects.filter(booked_seats=F('num_of_seats'))
    serializer_class = ListSerializer



class EventAPIView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'organizer'
    lookup_url_kwarg = 'organizer_name'


class EventObjAPIUpdateView(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = UpdateSerializer
    lookup_field = 'organizer'
    lookup_url_kwarg = 'organizer_name'


class EventDeleteAPIView(DestroyAPIView):
    queryset = Event.objects.all()
    lookup_field = 'organizer'
    lookup_url_kwarg = 'organizer_name'
