from django.urls import path
from . import views
from django.contrib import admin

from .views import activate_voice_assistant


urlpatterns = [
  
     path("admin/", admin.site.urls),
    path('', views.index, name='index'),
   path('predictor', views.predictor, name='predictor'),
   path('courses', views.courses, name='courses'),
   path('team', views.team, name='team'),
   path('testimonial', views.testimonial, name='testimonial'),
    path('four', views.four, name='four'),
    path('predict_career',views.predict_career, name='predict_career'),
    path('activate_assistant/', activate_voice_assistant, name='activate_assistant'),
     path('future', views.future, name='future'),
     path('doctor', views.doctor, name='doctor'),
     path('engineer', views.engineer, name='engineer'),
      path('sports', views.sports, name='sports'),
     path('courses', views.courses, name='courses'),
     path('login/', views.login, name='login'),
    path('my_view/', views.my_view, name='my_view'),
     path('chatbot/', views.chatbot, name='chatbot'),
    # Other URL patterns

   
     
]

