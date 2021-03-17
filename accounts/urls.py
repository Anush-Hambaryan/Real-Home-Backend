from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginView
from knox import views as knox_views


router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view()),
    path('logout/', knox_views.LogoutView.as_view()),
]
