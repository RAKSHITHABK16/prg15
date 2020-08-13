from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
  
    path('img/',views.img_upld,name="img"),
]