from django.shortcuts import render
from .models import Profile
from .forms import EditInformation
# Create your views here.


def my_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        form = EditInformation(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = EditInformation(instance=profile)
    return render(request, "my_profile.html", {"profile": profile, 'form': form})
