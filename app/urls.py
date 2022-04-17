from django.urls import path
from rest_framework.routers import DefaultRouter
from app.views import UserViewSet, get_user_list, CreateShipArea, start_game, FindGame, get_current_area
from . import views
router = DefaultRouter()

router.register('api/v1/user_reg', UserViewSet, basename='reg_users')
router.register('api/v1/create_area/', CreateShipArea, basename='create_area')

urlpatterns = [
    path('api/v1/get_area_list/', views.ListAreView.as_view(), name='get_area_list'),
    path('api/v1/get_game_list/', views.ListGameView.as_view(), name='get_game_list'),
    path('api/v1/get_user_list/', get_user_list, name='get_user_list'),
    path('api/v1/start_game/', start_game, name='start_game'),
    path('api/v1/find_game/', FindGame.as_view(), name='find_game'),
    path('api/v1/get_current_area', get_current_area, name='get_current_area'),
]

urlpatterns += router.urls
