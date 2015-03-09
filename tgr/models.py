import os
from django.contrib.gis.db import models
from django.core.urlresolvers import reverse
from localflavor.us.models import USStateField, PhoneNumberField
from colorfield.fields import ColorField
from census_places.models import PlaceBoundary

# Upload path functions
def get_community_logo_upload_path(instance, filename):
    return os.path.join(instance.region.slug, 'community-logos', filename)

def get_community_title_upload_path(instance, filename):
    return os.path.join(instance.region.slug, 'community-titles', filename)

def get_community_marker_upload_path(instance, filename):
    return os.path.join(instance.region.slug, 'community-markers', filename)
    
def get_reason_image_upload_path(instance, filename):
    return os.path.join(instance.community.region.slug, instance.community.slug, 'reason-images', filename)

def get_sponsor_image_upload_path(instance, filename):
    return os.path.join(instance.reason.community.region.slug, instance.reason.community.slug, 'sponsor-images', filename)

def get_attraction_image_upload_path(instance, filename):
    return os.path.join(instance.region.slug, 'attractions', filename)

class Region(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    border = models.MultiPolygonField()
    objects = models.GeoManager()
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tgr.views.region', args=[self.slug])


class Attribute(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name    

class Community(models.Model):
    region = models.ForeignKey(Region)
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    state = USStateField()
    place = models.OneToOneField(PlaceBoundary, blank=True, null=True)
    color = ColorField()
    publish = models.BooleanField(default=False)
    population = models.IntegerField()
    median_home_value = models.IntegerField(blank=True, null=True)
    median_household_income = models.IntegerField(blank=True, null=True)
    retail_sales = models.IntegerField(blank=True, null=True)
    attributes = models.ManyToManyField(Attribute,blank=True)
    video_id = models.CharField(max_length=16,blank=True)
    title_image = models.ImageField(upload_to=get_community_title_upload_path,blank=True,null=True)
    marker = models.ImageField(upload_to=get_community_marker_upload_path)
    point = models.PointField()
    objects = models.GeoManager()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'communities'
        unique_together = (('name', 'region'),)
        
    def __str__(self):
        return self.name
        
    def reason_set_random(self):
        return self.reason_set.all().order_by('?')
    
    def get_reasons_with_sponsor_modals(self):
        return self.reason_set.exclude(sponsor__modal=u'')
      
    def get_absolute_url(self):
        return reverse('tgr.views.community', args=[self.region.slug,self.slug])


class Reason(models.Model):
    community = models.ForeignKey(Community)
    headline = models.CharField(max_length=128)
    content = models.TextField()
    image = models.ImageField(upload_to=get_reason_image_upload_path)
    caption = models.TextField()
    
    class Meta:
        order_with_respect_to = 'community'

    def __str__(self):
        return ' | '.join([self.community.name, str(self.number()), self.headline])
        
    def number(self):
        return self._order + 1
        
class Sponsor(models.Model):
    reason = models.OneToOneField(Reason)
    name = models.CharField(max_length=128)
    url = models.URLField()
    image = models.ImageField(upload_to=get_sponsor_image_upload_path)
    modal = models.TextField(blank=True,null=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Attraction(models.Model):
    region = models.ForeignKey(Region)
    name = models.CharField(max_length=128)
    phone = PhoneNumberField()
    website = models.URLField()
    image = models.ImageField(upload_to=get_attraction_image_upload_path,blank=True,null=True)
    point = models.PointField()
    objects = models.GeoManager()
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        

class Feedback(models.Model):
    community = models.ForeignKey(Community)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    message = models.TextField(blank=True,null=True)
    notify = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Feedback'

    def __str__(self):
        return ' | '.join([self.community.name, self.name])