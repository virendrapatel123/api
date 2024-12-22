from rest_framework import serializers
from app.models import Product,Showroom


class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Showroom
        fields="__all__"

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
       model = Product
       fields ='__all__'
    #    exclude=['name']
       
    
    
    
    def validate_price(self, value):
        if value < 1000:
            raise serializers.ValidationError("price not less than 1000")
        return value
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description is not same")
        return data



