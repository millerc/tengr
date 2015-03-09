import json
from PIL import ImageOps

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib import messages

from tgr.models import Region, Community, Feedback, Attribute
from tgr.forms import FeedbackForm

# Create your views here.

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def region(request, slug):
    region = get_object_or_404(Region, slug=slug)
    path = json.loads(region.border.simplify(0.001).json)['coordinates']
    if request.GET.get('attrs'):
        attributes = request.GET.get('attrs').split(',')
        range1 = region.community_set.filter(attributes__slug__in=attributes)
        ranges = [range1]
        range_labels = [(1,999999)]
#     if request.GET.get('lower'):
#         lower = request.GET.get('lower')
#         upper = request.GET.get('upper')
#         try:
#            range1 = region.community_set.filter(population__range=(lower,upper))
#            ranges = [range1]
#            range_labels = [(lower,upper)]
#         except:
#            pass 
    else:       
        range1 = region.community_set.filter(population__range=(1000,4999))
        range2 = region.community_set.filter(population__range=(5000,9999))
        range3 = region.community_set.filter(population__range=(10000,19999))
        rangex = region.community_set.filter(population__gte=20000)
        ranges = [range1,range2,range3,rangex]
        range_labels = [(1000,4999),(5000,9999),(10000,19999),(20000,)]
    return render_to_response("tgr/region.html", {
        "attrs": Attribute.objects.all(),
        "region": region,
        "path": path,
        "ranges": ranges,
        "range_labels": range_labels,
    }, context_instance=RequestContext(request))        

def region_markers(request, slug, attrs=None):
    region = Region.objects.defer("border").get(slug=slug)
    #region = get_object_or_404(Region, slug=slug)
    markergroup = Community.objects.filter(region=region)
    if attrs:
        markergroup = markergroup.filter(attributes__in=attrs.split('_')).distinct()
    return render_to_response("tgr/markergroup.js", {
        "markergroup": markergroup,
        "region": region,
    }, context_instance=RequestContext(request), content_type="text/javascript")
    
def community(request, region, slug):
    community = get_object_or_404(Community, slug=slug, region__slug=region)
    return render_to_response("tgr/community.html", {
        "community": community,
    }, context_instance=RequestContext(request))        

def community_modal(request, region, slug):
    community = Community.objects.get(slug=slug)
    nearby = Community.objects.filter(publish=True).exclude(id=community.id).distance(community.point).order_by('distance')[:5]
    form = FeedbackForm
    return render_to_response("tgr/community-modal.html", {
        "community": community,
        "nearby": nearby,
        "form": form,
    }, context_instance=RequestContext(request))        

def feedback(request, region, slug):
    community = Community.objects.get(slug=slug,region__slug=region)
    new_feedback = Feedback(community=community)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=new_feedback)
        if form.is_valid():
            form.save()
            messages.add_message(
              request, messages.SUCCESS, 
              ('Thank you for your feedback, %s!' % form.cleaned_data['name'])
            )
            return redirect(community.region)            

def marker_image(request, hex):
    rgb = hex_to_rgb(hex)
    return HttpResponse(image_data, mimetype='image/png')



#from django.contrib.gis.db.models import Extent, Union
#counties = County.objects.filter(id__in=[2696,2349,1703,2396,2146,2751,2362,2778,2959,2395,2134,2400,2785,2138,2745,2760,2147,2855,2748,2718,1707,2388,2704,1730,1710,2356,2707,2131,2364,2698,2348,2789,2142,2703,2750,2403,1702,1715,2141,2709,2386,2708,2172,1719,2173,2709,2360,2382]).aggregate(Union('geom')) 
