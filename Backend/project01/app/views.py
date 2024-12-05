from django.shortcuts import render

# Create your views here.

def index(request):
    # Define the list of subjects and total
    subjects = ['Tamil', 'English', 'Maths', 'Science']

    Tamil = 50
    English = 65
    Maths = 75

    total = Tamil + English + Maths
    
    # Pass the values to the template through context
    return render(request, 'index.html', {'subjects': subjects, 'total': total})