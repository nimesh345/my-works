from django.urls import path
from home import views
urlpatterns = [
   
    path('',views.index,name="nmr"),
    path('about/',views.about,name="about")

]
