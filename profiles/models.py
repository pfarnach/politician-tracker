from django.db import models
from django.template.defaultfilters import slugify

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

	# congress
	party = models.CharField(max_length = 500, unique = False, default=None, blank=True)
	state = models.CharField(max_length = 500, unique = False, default=None, blank=True)
	chamber = models.CharField(max_length = 500, unique = False, default=None, blank=True)
	rep_district = models.CharField(max_length = 500, null=True, unique = False, default=None, blank=True)
	sen_class = models.CharField(max_length = 500, null=True, unique = False, default=None, blank=True)
	term_end = models.DateField(null=True, unique = False, default = None, blank=True)
	role = models.CharField(max_length = 500, unique = False, default=None, blank=True, null=True)
	role_start = models.DateField(max_length = 500, unique = False, default=None, blank=True, null=True)
	notes = models.CharField(max_length = 500, unique = False, default=None, null=True, blank=True)

	# slug
	slug = models.SlugField(max_length = 500, unique=True)
	

	def __unicode__(self):
		return self.official_full_name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.official_full_name)
		super(Politician, self).save(*args, **kwargs)