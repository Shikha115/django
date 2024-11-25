from django.db import models

# Create your models/schema here.

class Agent(models.Model):
    agent_name = models.CharField(max_length=255)
    language = models.CharField(max_length=100)
    voice_id = models.CharField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.agent_name
    

class Campaign(models.Model):
    CAMPAIGN_TYPE_CHOICES = [
        ('Inbound', 'Inbound'),
        ('Outbound', 'Outbound'),
    ]
    

    CAMPAIGN_STATUS_CHOICES = [
        ('Running', 'Running'),
        ('Paused', 'Paused'),
        ('Completed', 'Completed'),
    ]

    campaign_name = models.CharField(max_length=255)
    campaign_type = models.CharField(max_length=10, choices=CAMPAIGN_TYPE_CHOICES)
    phone_number = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=CAMPAIGN_STATUS_CHOICES)
    agent = models.ForeignKey(Agent, related_name='campaigns', on_delete=models.CASCADE)

    def __str__(self):
        return self.campaign_name


class CampaignResult(models.Model):

    CAMPAIGN_OUTCOME_CHOICES = [
        ('Success', 'Success'),
        ('Failure', 'Failure'),
    ]

    name = models.CharField(max_length=255)
    result_type = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    cost = models.FloatField()
    outcome = models.CharField(max_length=10, choices=CAMPAIGN_OUTCOME_CHOICES)
    call_duration = models.FloatField()  # Duration in seconds
    recording = models.URLField()
    summary = models.TextField()
    transcription = models.TextField()

    campaign = models.ForeignKey(Campaign, related_name='results', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

