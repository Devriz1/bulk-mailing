from django.contrib import admin
from django.urls import path
from mailing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.upload_csv, name='upload_csv'),
]