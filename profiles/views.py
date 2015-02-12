from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from profiles.models import Politician
# from profiles.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required # for decorator

from django.core import serializers # for AJAX response

from bs4 import BeautifulSoup
import wikipedia, requests

def index(request):
    politician_list_house = Politician.objects.filter(chamber="U.S. House of Representatives")
    politician_list_senate = Politician.objects.filter(chamber="U.S. Senate")
    context_dict = {"pols_house": politician_list_house, "pols_senate": politician_list_senate}
    return render(request, 'profiles/index.html', context_dict)


def politician_profile(request, politician_name_slug):
	# Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}
    context_dict['slug'] = politician_name_slug

    try:
        # Can we find a politician name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        politician = Politician.objects.get(slug=politician_name_slug)

        # Adds our results list to the template context under name pages.
        # context_dict['pages'] = pages
        # We also add the politician object from the database to the context dictionary.
        # We'll use this in the template to verify that the politician exists.
        context_dict['politician'] = politician

        # We check to see if wiki profile url exists -- if not, fetch it from wikipedia
        if not politician.wiki_url:
            
            # fetches html from list of US Congressmen and soupifies it
            if politician.chamber == "U.S. House of Representatives":
                raw_data = requests.get('https://en.wikipedia.org/wiki/List_of_current_members_of_the_United_States_House_of_Representatives_by_seniority')
            elif politician.chamber == "U.S. Senate":
                raw_data = requests.get('https://en.wikipedia.org/wiki/List_of_current_United_States_Senators')

            soup = BeautifulSoup(raw_data.text)

            for row in soup.table.find_all('tr'):
                # runs into exception with the header which doesn't contain same information as body of table
                try:
                    if row.contents[3].contents[0].string == politician.name:
                        politician.wiki_url = 'https://en.wikipedia.org' + str(row.contents[3].contents[0]['href'])
                        politician.save(commit=False)
                except (AttributeError, IndexError, TypeError):
                    pass

        # now check to see if there's already an image -- if not, grab image url from wikipedia based on wiki_url
        if not politician.profile_pic_url:

            raw_html = requests.get(politician.wiki_url)
            soup = BeautifulSoup(raw_html.text)
            
            all_a_tags = soup.find_all('a')
            for tag in all_a_tags:
                try:
                    if tag['class'] == ["image"]:
                        politician.profile_pic_url = "http://" + str(tag.contents[0]['src'])[2:]
                        politician.save()
                        context_dict['profile_pic'] = politician.profile_pic_url
                        break
                except KeyError: # because some a tags don't have classes
                    pass
        else:
            context_dict['profile_pic'] = politician.profile_pic_url
            print context_dict['profile_pic']

    except Politician.DoesNotExist:
        # We get here if we didn't find the specified politician.
        # Don't do anything - the template displays the "no politician" message for us.
        pass


    

    # Go render the response and return it to the client.
    return render(request, 'profiles/politician_profile.html', context_dict)

# AJAX request -- sends back JSON data of all politicians in database
def search_list(request):

    if request.method == "GET":
        politicians = Politician.objects.all()
        serialized_data = serializers.serialize("json", politicians)        

    return HttpResponse(serialized_data, content_type='application/json')







