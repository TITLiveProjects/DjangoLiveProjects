from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    # Set example
    fruits = {"apple", "banana", "cherry", "date"}
    
    # Dictionary example
    student_data = {
        "name": "John Doe",
        "age": 21,
        "subjects": ["Math", "Science", "History"],
    }

    view_user=[
        {"name":"selva","age":23},
        {"name":"sri","age":17},
        {"name":"selva","age":27},
        {"name":"selva","age":12},
    ]
    
    context = {
        "fruits": fruits,
        "student": student_data,
        "users": view_user
    }
    return render(request, 'index.html', context)
