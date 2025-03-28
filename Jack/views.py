from django.shortcuts import render
from .models import CV

def cv_view(request):
    cv = CV.objects.first()  # Fetch the first entry
    return render(request, 'cv.html', {'cv': cv})
