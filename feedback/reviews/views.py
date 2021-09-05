# Create your views here.
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)


class ThanksYouView(TemplateView):
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get('favorite_review')
        context['is_favorite'] = favorite_id == str(loaded_review.id)
        return context


class AddFavorite(View):
    def post(self, request):
        review_id = request.POST['review_id']
        # fav_review = Review.objects.get(pk=review_id)
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect('/reviews/' + review_id)
