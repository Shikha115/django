from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AgentSerializer, CampaignSerializer, CampaignResultSerializer
from .models import Agent, Campaign, CampaignResult

# Create your views here.
class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all() # Get all agents
    serializer_class = AgentSerializer



class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class CampaignResultViewSet(viewsets.ModelViewSet):
    queryset = CampaignResult.objects.all()
    serializer_class = CampaignResultSerializer