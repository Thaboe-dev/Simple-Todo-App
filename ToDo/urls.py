from django.urls import path
from .views import (
    ItemCreateView,
    ItemDeleteView,
    ItemListView,
    ItemUpdateView,
)

app_name = 'todo'
urlpatterns = [
    path("", ItemListView.as_view(), name="home"),
    path("create/", ItemCreateView, name="item-create"),
    path("<int:id>/update/", ItemUpdateView, name="item-update"),
    path("<int:pk>/delete/", ItemDeleteView.as_view(), name="item-delete"),
]