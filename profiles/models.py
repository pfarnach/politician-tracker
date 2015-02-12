from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Politician(models.Model):
	name = models.CharField(max_length = 50, unique = False)
	party = models.CharField(max_length = 50, unique = False, default=None)
	district = models.CharField(max_length = 50, unique = False, default=None)
	chamber = models.CharField(max_length = 50, unique = False, default=None)
	notes = models.CharField(max_length = 50, unique = False, default=None)
	rank = models.CharField(max_length = 50, unique = False, default=None) # or class in the case of Senators
	profile_pic_url = models.URLField(max_length=1000, blank=True)
	wiki_url = models.URLField(max_length=1000, default=None, blank=True)
	slug = models.SlugField(unique=True)
	

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Politician, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = "Politicians"