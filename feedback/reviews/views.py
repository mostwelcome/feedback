# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.base import TemplateView

from .forms import ReviewForm
from .models import Review


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    # def get(self, request):
    #     form = ReviewForm()
    #
    #     return render(request, 'reviews/review.html', {
    #         'form': form
    #     })
    #
    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/thank-you')
    #     return render(request, 'reviews/review.html', {
    #         'form': form
    #     })


class ThanksYouView(TemplateView):
    # def get(self, request):
    #     return render(request, 'reviews/thank_you.html')
    template_name = 'reviews/thank_you.html'

    # To pass fields in your template
    def get_context_data(self, **kwargs):
        context = super(ThanksYouView, self).get_context_data(**kwargs)
        context['message'] = 'This works!'
        return context


class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews_list'

    '''Custom query set'''
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=3)
    #     return data


class ReviewDetailsView(DetailView):
    template_name = 'reviews/review_details.html'
    model = Review
    context_object_name = 'review_details'

