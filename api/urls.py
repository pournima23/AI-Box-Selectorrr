from django.urls import path
from .views import home, recommend_box, order_recommendation

urlpatterns = [
    path('', home, name='home'),
    path('recommend/<int:product_id>/', recommend_box, name='recommend_box'),
    path('order-recommend/<int:order_id>/', order_recommendation, name='order_recommendation'),
]