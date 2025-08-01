from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("documents/", views.view_documents, name="view_documents")
]
