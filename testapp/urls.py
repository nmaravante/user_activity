from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Profile_Activity,name="ProfileActivity"),

# ---------------------- class based url ----###
    path('activity/', views.ActivityList.as_view()),

]