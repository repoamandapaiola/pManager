from django.urls import path
from .views import IndexView, MeeiroView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('meeiro', MeeiroView.as_view(), name='meeiro')
]
