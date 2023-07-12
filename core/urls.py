from django.urls import path  # noqa

from core import views
app_name = 'core'

urlpatterns = [
    path('customers/', views.CustomerAPIView.as_view(), name='customers'),
    path('deal_file_upload', views.DealFileUploadAPIView.as_view(), name='deals_file'),
]
