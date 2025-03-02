from django.urls import path
from . import views
from .views import coursedashboard, index, math_problem_view, quiz_view,ai,cys,blockchain, login_view, register_view,profile_view,puzzle,story,video  # Import individual views

urlpatterns = [
    path('', index, name='index'),                       # Homepage
    path('math/', math_problem_view, name='math_problem'),  # Math problem page
    path('quiz/', quiz_view, name='quiz'),
    path('course-dashboard/', coursedashboard, name='coursedashboard'),
    path('ai/', ai, name='ai'),
    path('cys/', cys, name='cys'),
    path('blockchain/', blockchain, name='blockchain'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view,name='profile'),
    path('video/', video,name='video'),
    path('story/', story,name='story'),
    path('puzzle/', puzzle,name='puzzle'),
    path('video/puzzle/', puzzle, name='puzzle'),     
    path('profile/update/', views.update_profile, name='update_profile'),                    # Quiz page
    path('chat/', views.chatbot_view, name='chat'),
   

]




 

