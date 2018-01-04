from django.conf.urls import include, url
from . import views
# hola	 
urlpatterns = [
    url(r'^$', views.post_list),
]