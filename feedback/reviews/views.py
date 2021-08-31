# Create your views here.
from django.shortcuts import render


def review(request):
    return render(request, 'reviews/review.html')
