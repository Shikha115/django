# convert model instances into JSON

# campaign/serializers.py
from rest_framework import serializers
from .models import Agent, Campaign, CampaignResult

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'agent_name', 'language', 'voice_id', 'updated']
        # fields = '__all__'

class CampaignSerializer(serializers.ModelSerializer):
    agent = serializers.PrimaryKeyRelatedField(queryset=Agent.objects.all())  

    class Meta:
        model = Campaign
        fields = ['id', 'campaign_name', 'campaign_type', 'phone_number', 'status', 'agent']

class CampaignResultSerializer(serializers.ModelSerializer):
    campaign = serializers.PrimaryKeyRelatedField(queryset=Campaign.objects.all())

    class Meta:
        model = CampaignResult
        fields = ['id', 'name', 'result_type', 'phone', 'cost', 'outcome', 'call_duration', 'recording', 'summary', 'transcription', 'campaign']
