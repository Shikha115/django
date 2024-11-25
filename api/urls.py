from django.contrib import admin
from django.urls import path, include
from .views import AgentViewSet, CampaignViewSet, CampaignResultViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'agents', AgentViewSet)
router.register(r'campaigns', CampaignViewSet)
router.register(r'campaign-results', CampaignResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
