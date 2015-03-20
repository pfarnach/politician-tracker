from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from jsonfield import JSONField
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
POL_IMG_DIR = os.path.join(BASE_DIR, 'static/images/congress_portraits/225x275/')


# Create your models here.
class Politician(models.Model):

	# bio
	first_name = models.CharField(max_length = 500, unique = False, blank=False)
	last_name = models.CharField(max_length = 500, unique = False, blank=False)
	official_full_name = models.CharField(max_length = 500, unique = False, blank=True)
	birthday = models.CharField(max_length = 500, unique = False, default = None, null=True)
	gender = models.CharField(max_length = 500, unique = False, default = None, null=True)
	religion = models.CharField(max_length = 500, unique = False, default = None, null=True)
	address = models.CharField(max_length = 500, unique = False, default = None, null=True)
	office = models.CharField(max_length = 500, unique = False, default = None, null=True)
	contact_form = models.URLField(max_length = 5000, unique = False, default = None, null=True)
	phone = models.CharField(max_length = 500, unique = False, default = None, null=True)
	url = models.URLField(max_length=1000, unique = False, default = None, blank=True)
	rss_url = models.URLField(max_length=1000, unique = False, default=None, blank=True, null=True)
	
	# IDs
	id_bioguide = models.CharField(max_length = 500, unique = False, blank=False)
	id_govtrack = models.IntegerField(max_length = 500, unique = True, default = None, blank=True, null=True)
	id_opensecrets = models.CharField(max_length = 500, unique = True, default = None, blank=True, null=True)
	id_lis = models.CharField(max_length = 500, unique = True, default = None, blank=True, null=True)
	id_thomas = models.CharField(max_length = 500, unique = True, default = None, blank=True, null=True)
	id_maplight = models.IntegerField(max_length = 500, unique = True, default = None, blank=True, null=True)
	id_votesmart = models.IntegerField(max_length = 500, unique = True, default = None, blank=True, null=True)
	id_fec = models.CharField(max_length = 500, unique = True, default = None, blank=True, null=True)

	# congress
	party = models.CharField(max_length = 500, unique = False, default=None, blank=True)
	state = models.CharField(max_length = 500, unique = False, default=None, blank=True)
	chamber = models.CharField(max_length = 500, unique = False, default=None, blank=True)
	rep_district = models.CharField(max_length = 500, null=True, unique = False, default=None, blank=True)
	sen_class = models.CharField(max_length = 500, null=True, unique = False, default=None, blank=True)
	first_elected = models.DateField(null=True, unique = False, default = None, blank=True)
	term_end = models.DateField(null=True, unique = False, default = None, blank=True)
	role = models.CharField(max_length = 500, unique = False, default=None, blank=True, null=True)
	role_start = models.DateField(max_length = 500, unique = False, default=None, blank=True, null=True)
	notes = models.CharField(max_length = 500, unique = False, default=None, null=True, blank=True)

	# social media
	youtube_id = models.CharField(max_length = 500, null=True, unique = False, default=None, blank=True)
	twitter_id = models.CharField(max_length = 500, null=True, unique = False, default=None, blank=True)
	facebook_id = models.CharField(max_length = 500, null=True, unique = False, default=None, blank=True)

	# slug
	slug = models.SlugField(max_length = 500, unique=True)
	

	def __unicode__(self):
		return self.official_full_name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.official_full_name)
		super(Politician, self).save(*args, **kwargs)

	# meant to determine if file with bioguide_id exists -- if not, return false and use default prof pic
	def getImageURL(self):
		self.imagePath = POL_IMG_DIR + self.id_bioguide + ".jpg"
		return os.path.isfile(self.imagePath)

class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance
	user = models.OneToOneField(User)

	zipcode = models.IntegerField(max_length = 50, unique = False, default = None, blank=False, null=False)
	last_login = models.DateTimeField(null=True, unique = False, default = None, blank=True)
	created_on = models.DateTimeField(null=True, unique = False, blank=False)
	email_pref = models.CharField(max_length = 500, unique = False, default=None, blank=True, null=True)
	# Store UUID link
	avatar = models.CharField(max_length = 1000, unique = True, default=None, blank=True, null=True)

	# Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.user.username

class UserSubscription(models.Model):
	user = models.ForeignKey(User)
	politician = models.ForeignKey(Politician)
	timestamp = models.DateTimeField(null=True, unique = False, blank=False)

class CachedOpenSecrets(models.Model):
	politician = models.ForeignKey(Politician)
	timestamp = models.DateTimeField(null=True, unique = False, blank=False)

	# will store JSON
	top_contributor = JSONField(max_length = 5000, unique = False, default=None, blank=True, null=True)
	top_industry = JSONField(max_length = 5000, unique = False, default=None, blank=True, null=True)

	# from memPFDprofile
	net_low = models.IntegerField(max_length = 50, unique = False, default = None, blank=True, null=True)
	net_high = models.IntegerField(max_length = 50, unique = False, default = None, blank=True, null=True)

class Article(models.Model):
	politician = models.ForeignKey(Politician)
	user = models.ForeignKey(User)
	timestamp = models.DateTimeField(unique = False, null=True, blank=False)
	title = models.CharField(max_length = 100, unique = False, null=False, blank=False)
	url = models.URLField(max_length=500, unique = False, null=False, blank=False)
	tags = models.CharField(max_length = 250, unique = False, default=None, blank=True, null=True)

	def __unicode__(self):
		return self.title

class ArticleVote(models.Model):
	user = models.ForeignKey(User)
	article = models.ForeignKey(Article)
	timestamp = models.DateTimeField(unique = False, default=None, null=False, blank=False)
	vote = models.CharField(max_length = 50, unique = False, default = None, null=True, blank=True)

	def __unicode__(self):
		return self.vote



