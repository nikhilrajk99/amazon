from . import views
from django.urls import path
app_name='amazonapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('electronic',views.electronic,name='electronic'),
    path('fashion',views.fashion,name='fashion'),
    path('jewellery',views.jewellery,name='jewellery')
]