
from django.urls import path , include
from home.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')

urlpatterns = [
    path('router/', include(router.urls)),
    path('index/',index , name="index" ),
    path('student/', StudentView , name="student"),
    path('login/', login , name="login"),
    path('student_api', StudentAPIView.as_view() , name="student_api"),
    path('register_user/', RegisterUser.as_view() , name="register_user"),
    path('login_user/', LoginView.as_view() , name="login_user"),
]
