from rest_framework import serializers

from main.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'image', 'price')


class DiscountSerializer(serializers.ModelSerializer):
        discounted_price = serializers.SerializerMethodField()

        class Meta:
            model = Product
            fields = ('id', 'name', 'discount', 'image', 'discounted_price')

        def get_discounted_price(self, obj):
            discounted_price, original_price = obj.discount_calculation()
            return {
                'discounted_price': discounted_price,
                'original_price': original_price,
            }


class FilterSerializer(serializers.ModelSerializer):
    pr_name = serializers.CharField(required=False)




class Sellerss(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'sizes')
