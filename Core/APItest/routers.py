from rest_framework.routers import DefaultRouter
from APItest.views import PersonViewSet

routers = DefaultRouter()
routers.register(r'persons' , PersonViewSet , basename='persons')