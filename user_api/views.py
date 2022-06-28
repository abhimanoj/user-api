from rest_framework import viewsets
from .models import *
from .serializers import *
from django.core import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

 
class UserTableClassView(viewsets.ModelViewSet):
    serializer_class = UserTableSerializer
    queryset = UserTable.objects.all()


    # Apply Filter..
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    filterset_fields = ("id", "first_name")
    # Apply Sorting..
    ordering_fields = ["created_at"]
    # Serchalble Fields..
    search_fields = ["first_name"]



class UserDetailsTableClassView(viewsets.ModelViewSet):
    serializer_class = UserDetailsTableSerializer



    def get_queryset(self):
        
        data = UserDetailsTable.objects.raw('SELECT id FROM user_api_userdetailstable')

        for row in data:
            print(serializers.serialize('json',data),'-----')

        queryset = UserDetailsTable.objects.all()

        return queryset


    # Apply Filter..
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    filterset_fields = ("id", "email", "user_table__first_name")
    # Apply Sorting..
    ordering_fields = ["created_at"]
    # Serchalble Fields..
    search_fields = ["email"]






