from django.urls import path
from .views import CreateOrderView,OrderListView,OrderDetailView
urlpatterns = [
    path("create/",CreateOrderView.as_view(),name="create_order"),
    path("list/",OrderListView.as_view(),name="order_list"),
    path("detail/",CreateOrderView.as_view(),name="order_details"),
    
]