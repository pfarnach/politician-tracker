from django.shortcuts import render
from django.http import HttpResponse
from profiles.models import Politician, UserSubscription, UserProfile
# from profiles.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required # for decorator
from django.core import serializers # for AJAX response

import datetime, math, us

# index of politicians
def politician_index(request):
    politician_list_house = Politician.objects.filter(chamber="rep")
    politician_list_senate = Politician.objects.filter(chamber="sen")
    context_dict = {"pols_house": politician_list_house, "pols_senate": politician_list_senate}
    return render(request, 'profiles/index.html', context_dict)

# individual politician's profile page
def politician_profile(request, politician_name_slug):
    context_dict = {}

    try:
        # try to get politician by slug name -- if doesn't exit, we'll handle non-existance in template
        politician = Politician.objects.get(slug=politician_name_slug)

        # format dates and calculate age   
        politician.birthday = datetime.datetime.strptime(politician.birthday, '%Y-%m-%d')
        age = politician.birthday - datetime.datetime.now()
        politician.age = int(math.floor(abs((age.days) / 365.25)))

        politician.address = politician.address.replace(';','</br>')

        politician.state = us.states.lookup(politician.state).name

        if not politician.getImageURL() and politician.gender == "M":
            context_dict['alt_profile_pic'] = "male"
        elif not politician.getImageURL() and politician.gender == "F":
            context_dict['alt_profile_pic'] = "female"

        try:
            if UserSubscription.objects.get(politician=politician, user=request.user):
                context_dict['can_subscribe'] = False
        except:
            context_dict['can_subscribe'] = True

        context_dict['politician'] = politician

    except Politician.DoesNotExist:
        # if Politician slug doesn't exist, we take care of that in template
        pass

    # Go render the response and return it to the client.
    return render(request, 'profiles/politician_profile.html', context_dict)

# AJAX request -- sends back JSON data of all politicians in database
def search_list(request):

    if request.method == "GET":
        politicians = Politician.objects.all()
        serialized_data = serializers.serialize("json", politicians)        

    return HttpResponse(serialized_data, content_type='application/json')

# AJAX request to subscribe to politician
@login_required
def subscribe_to_pol(request):
    
    pol_id = None

    # get politician ID that is going to be subscribed/unsubscribed to
    if request.method == "GET":
        pol_id = request.GET['pol_id']

    # fetch politician object if 
    if pol_id:
        pol = Politician.objects.get(id=int(pol_id))

    # see if it can be deleted (unsubscribed) to. If not, created a new subscription for user/politican
    try:
        UserSubscription.objects.get(politician=pol, user=request.user).delete()
        return HttpResponse('unsubscribed')

    except Exception as e:
        # no subscription? Created a new one for specific user/politician and save
        subscription = UserSubscription(politician=pol, user=request.user, timestamp=datetime.datetime.now())
        subscription.save()
        return HttpResponse('subscribed')

    # total_subscriptions = len(UserSubscription.objects.filter(politician=pol))

    return HttpResponse('neither subscribed nor unsubscribed')




