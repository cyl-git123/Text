from django.urls import path

from chimingsiapp import views

urlpatterns = [
    path("chimingsi/",views.class_emp),
]