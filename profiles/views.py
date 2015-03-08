from django.shortcuts import render
from django.http import HttpResponse
from profiles.models import Politician
# from profiles.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required # for decorator
from django.core import serializers # for AJAX response

def index(request):
    politician_list_house = Politician.objects.filter(chamber="rep")
    politician_list_senate = Politician.objects.filter(chamber="sen")
    context_dict = {"pols_house": politician_list_house, "pols_senate": politician_list_senate}
    return render(request, 'profiles/index.html', context_dict)

def politician_profile(request, politician_name_slug):
    context_dict = {}

    try:
        # try to get politician by slug name -- if doesn't exit, we'll handle non-existance in template
        politician = Politician.objects.get(slug=politician_name_slug)
        context_dict['politician'] = politician
    except Politician.DoesNotExist:
        pass

    # Go render the response and return it to the client.
    return render(request, 'profiles/politician_profile.html', context_dict)

# AJAX request -- sends back JSON data of all politicians in database
def search_list(request):

    if request.method == "GET":
        politicians = Politician.objects.all()
        serialized_data = serializers.serialize("json", politicians)        

    return HttpResponse(serialized_data, content_type='application/json')







