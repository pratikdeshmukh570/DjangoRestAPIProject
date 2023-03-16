from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import CompanyViewSet, EmployeeViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'User', UserViewSet)
urlpatterns = [
    path('', include(router.urls))
]

