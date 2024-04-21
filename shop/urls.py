from django.urls import path, include
from rest_framework import routers
from shop import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('all-products/', include(router.urls)),
    path('all-profiles/', views.UserProfileListCreateView.as_view(), name='all-profiles'),
    path('profile/<int:pk>', views.UserProfileDetailView.as_view(), name='profile'),
]
