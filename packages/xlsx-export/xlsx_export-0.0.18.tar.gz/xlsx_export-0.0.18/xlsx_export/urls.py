from django.urls import path
from .views import upload_file, success_view

app_name = 'xlsx_export'

urlpatterns = [
    path('upload/', upload_file, name='upload'),
    path('success/', success_view, name='success'),
]
