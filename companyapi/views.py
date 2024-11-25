from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("Home page request")
    friends = [
        {"name": "John", "age": 25},
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 35},
    ]
    return JsonResponse(friends, safe=False) 
    # return HttpResponse("<h1>Home page response</h1>") # can we normal text or html here