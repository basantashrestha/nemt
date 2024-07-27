from django.urls import path
from .views import ItemList, ItemDetail
urlpatterns = [
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view())
]