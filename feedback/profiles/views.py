from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import UserProfile


class CreateProfileView(CreateView):
    template_name = 'profiles/create_profile.html'
    fields = '__all__'
    model = UserProfile
    success_url = '/profile'


class ProfilesView(ListView):
    model = UserProfile
    template_name = 'profiles/user_profiles.html'
    context_object_name = 'profiles'
#
# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             'form': form
#         })
#
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#
#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES['user_image'])
#             profile.save()
#             return HttpResponseRedirect('/profile')
#         return render(request, "profiles/create_profile.html")
