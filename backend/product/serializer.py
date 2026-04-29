from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = [
            'current_price', 'views', 'purchased', 'created_at', 'updated_at',
        ]

    def validate(self, data):
        base_price = data.get('base_price')
        stock = data.get('stock')

        if base_price is not None and base_price < 0:
            raise serializers.ValidationError("base price cannot be negative ")
        
        if stock is not None and stock < 0:
            raise serializers.ValidationError("stock cannot be negative")

        return data