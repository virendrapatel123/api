from rest_framework import serializers
from app.models import Product

def alphanumeric(value):
    if not str(value).isalpha():
        raise serializers.ValidationError('number must be alphanumeric')

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name=serializers.CharField(validators=[alphanumeric])
    description=serializers.CharField()
    price=serializers.IntegerField()
    
    def create(self, validated_data):
        
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.description=validated_data.get('description', instance.description)
        instance.price=validated_data.get('price', instance.price)
        instance.save()
        return instance
    
    def validate_price(self, value):
        if value < 1000:
            raise serializers.ValidationError("price not less than 1000")
        return value
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description is not same")
        return data



