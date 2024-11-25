# Backend Development Assignment

## Overview
This is a Django project created for the backend development assignment by **Prio Chatterjee** company, Delhi. The project implements a backend API for handling agents, campaigns, and campaign results using **Django REST Framework**.
It allows you to perform CRUD (Create, Read, Update, Delete) operations on these entities via RESTful endpoints.

## GitHub Repository
To clone the project, use the following command:
```bash
git clone https://github.com/Shikha115/django.git
```


## Setting Up the Project

### 1. Create a Django Project
To create the Django project, run the following command:

```bash
django-admin startproject companyapi .
```

### 2. Run the Django Project
To run the project locally, use the following command:

```bash
python manage.py runserver
```


### 3. Apply Migrations
If you make any changes to the models, you can apply the migrations using the following commands:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

## Available Endpoints

### Agents API
- **GET /api/agents**: Get a list of agents.
- **POST /api/agents**: Create a new agent.
- **GET /api/agents/{id}/**: Get details of a specific agent.
- **PATCH /api/agents/{id}/**: Update details of a specific agent.
- **DELETE /api/agents/{id}/**: Delete a specific agent.

### Campaigns API
- **GET /api/campaigns**: Get a list of campaigns.
- **POST /api/campaigns**: Create a new campaign.
- **GET /api/campaigns/{id}/**: Get details of a specific campaign.
- **PATCH /api/campaigns/{id}/**: Update details of a specific campaign.
- **DELETE /api/campaigns/{id}/**: Delete a specific campaign.

### Campaign Results API
- **GET /api/campaign-results**: Get a list of campaign results.
- **POST /api/campaign-results**: Create a new campaign result.
- **GET /api/campaign-results/{id}/**: Get details of a specific campaign result.
- **PATCH /api/campaign-results/{id}/**: Update details of a specific campaign result.
- **DELETE /api/campaign-results/{id}/**: Delete a specific campaign result.


## Extra Information

### 1. Default Database
By default, Django uses SQLite as the database for development. The database file is located at:

```bash
db.sqlite3
```

### 2. python3 manage.py startapp anyName
To create a new API, run the following command:

```bash
python3 manage.py startapp anyName
```

This will create a new app with preconfigured folders for models, views, and more.

### 3. Dummy Data

#### Agents
[
  {
    "agent_name": "Jose Alinson",
    "language": "English",
    "voice_id": "voice-1234-xyz",
    "updated": "2024-11-25T12:00:00Z"
  },
  {
    "agent_name": "Maria Fernandez",
    "language": "Spanish",
    "voice_id": "voice-5678-abc",
    "updated": "2024-11-25T12:30:00Z"
  },
  {
    "agent_name": "John Doe",
    "language": "English",
    "voice_id": "voice-9876-pqr",
    "updated": "2024-11-25T13:00:00Z"
  },
  {
    "agent_name": "Lily Tran",
    "language": "Vietnamese",
    "voice_id": "voice-1122-stu",
    "updated": "2024-11-25T14:00:00Z"
  },
  {
    "agent_name": "David Kim",
    "language": "Korean",
    "voice_id": "voice-3344-vwx",
    "updated": "2024-11-25T15:00:00Z"
  }
]

#### Campaigns

[
  {
    "campaign_name": "Campaign Alpha",
    "campaign_type": "Outbound",
    "phone_number": "123-456-7890",
    "status": "Running",
    "agent": 1
  },
  {
    "campaign_name": "Campaign Beta",
    "campaign_type": "Inbound",
    "phone_number": "098-765-4321",
    "status": "Paused",
    "agent": 2
  },
  {
    "campaign_name": "Campaign Gamma",
    "campaign_type": "Outbound",
    "phone_number": "555-123-4567",
    "status": "Completed",
    "agent": 3
  },
  {
    "campaign_name": "Campaign Delta",
    "campaign_type": "Inbound",
    "phone_number": "555-765-4321",
    "status": "Running",
    "agent": 4
  },
  {
    "campaign_name": "Campaign Epsilon",
    "campaign_type": "Outbound",
    "phone_number": "777-111-2222",
    "status": "Paused",
    "agent": 5
  }
]

#### Campaign Results
[
  {
    "name": "Result 1",
    "result_type": "Successful Call",
    "phone": "123-456-7890",
    "cost": 50.75,
    "outcome": "Success",
    "call_duration": 120.5,
    "recording": "http://example.com/recording/1.mp3",
    "summary": "The call went well, the customer was interested in the offer.",
    "transcription": "Hello, this is Jose from Campaign Alpha. We have an exciting offer for you. Do you have a minute to talk?",
    "campaign": "1"
  },
  {
    "name": "Result 2",
    "result_type": "Failed Call",
    "phone": "098-765-4321",
    "cost": 30.25,
    "outcome": "Failure",
    "call_duration": 45.0,
    "recording": "http://example.com/recording/2.mp3",
    "summary": "The call failed, the customer didn't answer.",
    "transcription": "Hello, this is Maria from Campaign Beta. Sorry we missed you. Please call back later.",
    "campaign": "2"
  },
  {
    "name": "Result 3",
    "result_type": "Successful Call",
    "phone": "555-123-4567",
    "cost": 65.50,
    "outcome": "Success",
    "call_duration": 180.0,
    "recording": "http://example.com/recording/3.mp3",
    "summary": "The customer expressed interest, and we scheduled a follow-up call.",
    "transcription": "Hi, this is John from Campaign Gamma. Thanks for your time today. We'd love to follow up on the details we discussed.",
    "campaign": "3"
  },
  {
    "name": "Result 4",
    "result_type": "Failed Call",
    "phone": "555-765-4321",
    "cost": 25.50,
    "outcome": "Failure",
    "call_duration": 30.0,
    "recording": "http://example.com/recording/4.mp3",
    "summary": "Customer was unavailable during the call.",
    "transcription": "Hello, this is Lily from Campaign Delta. Sorry we missed you. We'll try calling again soon.",
    "campaign": "4"
  },
  {
    "name": "Result 5",
    "result_type": "Successful Call",
    "phone": "777-111-2222",
    "cost": 40.00,
    "outcome": "Success",
    "call_duration": 150.0,
    "recording": "http://example.com/recording/5.mp3",
    "summary": "The customer was interested in the product and requested a demo.",
    "transcription": "Hi, this is David from Campaign Epsilon. We'd love to show you more about our product. When would be a good time for a demo?",
    "campaign": "5"
  }
]



