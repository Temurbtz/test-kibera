from rest_framework import serializers
from  .models  import New


class NewSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username')
    class Meta:
        model = New
        fields = ('name','text','owner','date_created')
    


   

class  NewCreateSerializer(serializers.ModelSerializer):
     class Meta:
        model = New
        fields = ('name','text')
 