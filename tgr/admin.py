from django.contrib.gis import admin
from tgr.models import Region, Community, Reason, Sponsor, Attraction, Feedback, Attribute
# Register your models here.

class MapAdmin(admin.OSMGeoAdmin):
    default_lon = -10973837
    default_lat = 4841007
    map_width = 720
    map_height = 420
    default_zoom = 4

class AttributeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class RegionAdmin(MapAdmin):
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True

class ReasonInline(admin.StackedInline):
    model = Reason
    extra = 10
    max_num = 10
    
class SponsorInline(admin.StackedInline):
    model = Sponsor
    extra = 1
    max_num = 1
    
class CommunityAdmin(MapAdmin):
    list_display = ['name','slug','state','population','color','publish']
    list_filter = ['publish','region']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['attributes']
    inlines = [ ReasonInline, ]
    save_on_top = True
    
class ReasonAdmin(admin.ModelAdmin):
    list_filter = ['community__region','community',]
    search_fields = ['headline', 'content', 'caption', ]
    inlines = [ SponsorInline, ]
    save_on_top = True
    
class AttractionAdmin(MapAdmin):
    list_display = ['name','phone','website']
    list_filter = ['region']
    save_on_top = True

class FeedbackAdmin(admin.ModelAdmin):
    list_filter = ['notify', 'community']
    list_display = ['name', 'community', 'email', 'timestamp', 'notify']
    save_on_top = True

admin.site.site_header = "10GR Admin"
admin.site.site_title = admin.site.site_header

admin.site.register(Region, RegionAdmin)
admin.site.register(Community, CommunityAdmin)
admin.site.register(Reason, ReasonAdmin)
admin.site.register(Sponsor)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Attraction, AttractionAdmin)
admin.site.register(Feedback, FeedbackAdmin)