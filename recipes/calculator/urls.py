from calculator import views
from django.urls import path, re_path


urlpatterns = [
    path("<str:dish>", views.receipt)
]
