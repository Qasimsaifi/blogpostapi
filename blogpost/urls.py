from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('posts', views.BlogPostViewSet)

urlpatterns = [
    # ...
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
