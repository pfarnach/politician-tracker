from django.shortcuts import render
from django.http import HttpResponse
from profiles.models import Politician, UserSubscription, UserProfile, CachedOpenSecrets, Article, ArticleVote
# from profiles.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required # for decorator
from django.core import serializers # for AJAX response

from django.utils import timezone
import datetime
import math
import us
import json

import apikeys
import requests
import urllib2
import xml.etree.ElementTree as ET

#
# URL-called functions
#

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

# gets list of subscriptions for current user
@login_required
def view_subscriptions(request):
    context_dict = {}
    user_id = request.user.id

    # get subscriptions based on current user
    subscriptions = UserSubscription.objects.filter(user_id=user_id)

    pols = []

    # build list of politicians that user is subscribed to
    for subscription in subscriptions:
        pols.append(Politician.objects.get(id=subscription.politician_id))

    context_dict['pols'] = pols

    return render(request, 'profiles/view_subscriptions.html', context_dict)

# AJAX request to get cached OpenSecrets data -- if it doesn't already exist or is expired, fetch it
def get_money_info(request):

    pol = None

    if request.method == "GET":
        pol_id = request.GET['pol_id']

    # see if politcian by ID exists
    try:
        pol = Politician.objects.get(id=pol_id)
    except Politician.DoesNotExist:
        HttpResponse('Politician does not exist')

    # see if cache exists for politician, if not, go get it and return it
    try:
        cached = CachedOpenSecrets.objects.get(politician_id=pol_id)
    except CachedOpenSecrets.DoesNotExist:
        cached = cache_opensecrets(pol_id, pol)
        serialized_data = serializers.serialize("json", [cached])
        return HttpResponse(serialized_data, content_type='application/json')

    # if cache exists, check to see if it's expired (every 1 day)
    if cached and pol:
        time_cached = cached.timestamp
        time_now = timezone.now()
        time_diff = time_now - time_cached

        if time_diff > datetime.timedelta(days=1):
            # print "cache expired"
            old_cached = cached

            # get new cache
            cached = cache_opensecrets(pol_id, pol)
            serialized_data = serializers.serialize("json", [cached])

            # delete old cache
            old_cached.delete()
            return HttpResponse(serialized_data, content_type='application/json')
        else:
            # print "cache still good"
            serialized_data = serializers.serialize("json", [cached])
            return HttpResponse(serialized_data, content_type='application/json')

def get_articles(request):

    context_dict = {}
    context_dict['is_authenticated'] = request.user.is_authenticated()
    pol = None

    if request.method == "GET":
        pol_id = request.GET['pol_id']

    try:
        articles = Article.objects.get(politician=pol_id)
    except Article.DoesNotExist:
        context_dict['articles'] = 'None'
        return HttpResponse(json.dumps(context_dict))
    

#
# Helper functions
#

# queries Opensecrets API
def cache_opensecrets(pol_id, pol): 

    # OpenSecrets API parameters
    apikey = apikeys.opensecrets
    method1 = 'memPFDprofile'
    method2 = 'candContrib'
    method3 = 'candIndustry'
    year = '2014'
    cycle = '2014'
    cid = pol.id_opensecrets
    output1 = 'json'
    output2 = 'xml'

    ### Call to get indiv contributor info
    base_url = "http://www.opensecrets.org/api/?method=%s&cycle=%s&cid=%s&output=%s&apikey=%s" % (method2, cycle, cid, output1, apikey)
    request = requests.get(base_url).json()
    request_root = request['response']['contributors']['contributor']

    top_contributor = []

    for i in range(len(request_root)):
        top_contributor.append([])
        top_contributor[i] = {}
        top_contributor[i]['org_name'] = request_root[i]['@attributes']['org_name']
        top_contributor[i]['total'] = request_root[i]['@attributes']['total']
        top_contributor[i]['pacs'] = request_root[i]['@attributes']['pacs']
        top_contributor[i]['indivs'] = request_root[i]['@attributes']['indivs']

    ### Call to get industry contributor info
    base_url = "http://www.opensecrets.org/api/?method=%s&cycle=%s&cid=%s&output=%s&apikey=%s" % (method3, cycle, cid, output1, apikey)
    request = requests.get(base_url).json()
    request_root = request['response']['industries']['industry']

    top_industry = []

    for i in range(len(request_root)):
        top_industry.append([])
        top_industry[i] = {}
        top_industry[i]['total'] = request_root[i]['@attributes']['total']
        top_industry[i]['pacs'] = request_root[i]['@attributes']['pacs']
        top_industry[i]['indivs'] = request_root[i]['@attributes']['indivs']
        top_industry[i]['industry_code'] = request_root[i]['@attributes']['industry_code']
        top_industry[i]['industry_name'] = request_root[i]['@attributes']['industry_name']

    ### Call to get net worth (high and low)
    base_url = "http://www.opensecrets.org/api/?method=%s&year=%s&cid=%s&output=%s&apikey=%s" % (method1, year, cid, output2, apikey)
    request = urllib2.urlopen(base_url).read()
    request_xml = ET.fromstring(request)

    # some politicians won't have net value info
    try:
        net_low = int(request_xml[0].attrib['net_low'])
        net_high = int(request_xml[0].attrib['net_high'])
    except:
        net_low = None
        net_high = None

    # Create new instance with timestamp that will 'expire' in a week
    cached = CachedOpenSecrets(politician=pol, timestamp=timezone.now(), top_contributor=top_contributor, top_industry=top_industry, net_low=net_low, net_high=net_high)
    cached.save()
    return cached



