from django.urls import path
from .views import CreateProductView,ListProductView,DetailProductView
urlpatterns = [
    path("create/",CreateProductView.as_view(),name="create_product"),
    path("list/",ListProductView.as_view(),name="product_list"),
    path("detail/<str:slug>/",DetailProductView.as_view(),name="product_detail"),
]