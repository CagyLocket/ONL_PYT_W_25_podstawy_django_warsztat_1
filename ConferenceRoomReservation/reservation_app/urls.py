from django.urls import path
from . import views as reservation_views

app_name = 'reservation_app'

urlpatterns = [
    path('', reservation_views.home_view, name="home"),

]
