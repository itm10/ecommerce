from django.urls import path

from main.views import OverallAPIView, UpdateAPIView, ByCategoryAPIView, DiscountAPIView

urlpatterns = [
    path('', OverallAPIView.as_view(), name=''),
    path('update/<int:pk>', UpdateAPIView.as_view(), name='update'),
    path('bycategory/<str:name>', ByCategoryAPIView.as_view(), name='bycategory'),
    path('discount', DiscountAPIView.as_view(), name='discount'),
    path('filters/<str:obj>', PizzaAndSubcategoriesAPIView.as_view(), name='filters'),
    path('sell/<int:pk>', Sellers.as_view(), name='sell')
]
