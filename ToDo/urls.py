from django.urls import path
from .views import (
    ItemCreateView,
    ItemDeleteView,
    ItemListView,
    ItemUpdateView,
)

app_name = 'todo'
urlpatterns = [
    path("", ItemListView.as_view(), name="index"),
    path("create/", ItemCreateView.as_view(), name="item-create"),
    path("<int:pk>/update/", ItemUpdateView.as_view(), name="item-update"),
    path("<int:pk>/delete/", ItemDeleteView.as_view(), name="item-delete"),
]