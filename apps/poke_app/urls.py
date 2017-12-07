from django.conf.urls import url
from . import views           # This line is new!

app_name = "poke_app"
urlpatterns = [
    url(r'^$', views.index, name="index"),
     url(r'^create_poke/(?P<number>\d+)$', views.create_poke, name = "create_poke"),
    
  	 url(r'^clear$', views.clear, name="clear"),
   
    ]