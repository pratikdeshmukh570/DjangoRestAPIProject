from django.http import JsonResponse


def home_page(request):
    print("home page requested")
    friends = [
        'rahul',
        'kunal',
        'satvik',
        'shubham',
        'rohit'
    ]
    return JsonResponse(friends, safe=False)
