from rest_framework.views import APIView, Response
from rest_framework.generics import GenericAPIView
from .serializers import ProductSerializer, Sellerss, DiscountSerializer, FilterSerializer

from .models import Product, Category, PizzaSize
from drf_yasg.utils import swagger_auto_schema


class OverallAPIView(GenericAPIView):
    serializer_class = ProductSerializer

    def get(self, request):
        product = Product.objects.all()
        product_serializer = ProductSerializer(product, many=True)
        return Response(product_serializer.data)


class UpdateAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = ProductSerializer

    def put(self, request, pk):
        name = request.data.get('name')
        description = request.data.get('description')
        price = request.data.get('price')
        product = Product.objects.get(pk=pk)
        product.name = name
        product.description = description
        product.price = price
        product.save()
        product_serializer = ProductSerializer(product)
        return Response(product_serializer.data)

    def patch(self, request, pk):
        name = request.data.get('name', None)
        description = request.data.get('description', None)
        price = request.data.get('price', None)
        discount = request.data.get('discount', None)
        product = Product.objects.get(pk=pk)
        if name:
            product.name = name

        if description:
            product.description = description

        if price:
            product.price = price

        if discount:
            product.discount = discount

        product.save()
        product_serializer = ProductSerializer(product)
        return Response(product_serializer.data)

    def delete(self, request, pk):
        Product.objects.get(pk=pk).delete()
        return Response(status=204)


class ByCategoryAPIView(GenericAPIView):

    def get(self, request, name):
        category = Category.objects.get(name=name)
        category_ids = category.id
        product = Product.objects.filter(category_id=category_ids)
        product_serializer = ProductSerializer(product, many=True)
        return Response(product_serializer.data)


class DiscountAPIView(APIView):
    def get(self, request):
        products_with_discount = Product.objects.filter(discount__gt=0)

        data = []
        for product in products_with_discount:
            serialized_data = DiscountSerializer(product).data
            data.append(serialized_data)

        return Response(data)


class Sellers(GenericAPIView):
    serializer_class = Sellerss

    def post(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)

        selected_size_id = request.data.get('sizes')
        selected_size = None

        if selected_size_id:
            try:
                selected_size = PizzaSize.objects.get(id=selected_size_id)
                total_price = product.price

                if selected_size:
                    final = selected_size.get_price()
                    total_price += final
                    return Response({'total_price': total_price})

            except PizzaSize.DoesNotExist:
                return Response({'error': 'Invalid size ID'}, status=400)














