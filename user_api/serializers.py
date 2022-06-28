from rest_framework import serializers
from .models import *
 
 
class UserTableSerializer(serializers.ModelSerializer):   

    class Meta:
        model = UserTable
        fields = ('__all__')
 

class UserDetailsTableSerializer(serializers.ModelSerializer):   

    class Meta:
        model = UserDetailsTable
        fields = ('__all__')
 