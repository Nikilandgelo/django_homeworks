from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductPositionSerializer(serializers.ModelSerializer):
    product_title = serializers.CharField(source='product.title', read_only=True)
    product_description = serializers.CharField(source='product.description', read_only=True)
    
    class Meta:
        model = StockProduct
        fields = ['product', 'product_title', 'product_description', 'quantity', 'price']

class StockSerializer(serializers.ModelSerializer):
    
    positions = ProductPositionSerializer(many=True)
    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data:dict) -> Stock:
        position:list[dict] = validated_data.pop('positions')
        stock = Stock.objects.create(**validated_data)
        for pos in position:
            StockProduct.objects.create(stock = stock, **pos)
        return stock

    def update(self, instance:Stock, validated_data:dict) -> Stock:
        position:list[dict] = validated_data.pop('positions')
        if validated_data:
            Stock.objects.filter(id = instance.id).update(**validated_data)
        stock_product_datas = StockProduct.objects.filter(stock = instance)
        for index, data in enumerate(stock_product_datas):
            try:
                for key, value in position[index].items():
                    setattr(data, key, value)
                data.save()
            except IndexError:
                break
        return instance