from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import modelformset_factory
from django.template import RequestContext

from celebrity.models import Celebrity, CelebrityForm
from penvelopekravitz.settings import CELEBS_TO_SEND, ROUND_TIME

import random

def home(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def play(request):
    total = Celebrity.objects.count()
    names = []
    tries = 0
    while len(names) < CELEBS_TO_SEND and tries < 5:
        try:
            rand = random.randrange(1, total+1)
            celeb = Celebrity.objects.get(pk=rand)
            if celeb not in names:
                names.append(celeb)
        except (ObjectDoesNotExist, ValueError):
            tries += 1
            pass
    return render_to_response('play.html', {'celebs':names, 'max_celebs' : CELEBS_TO_SEND, 'max_time' : ROUND_TIME}, context_instance=RequestContext(request))

def add_celeb(request):
    cf = modelformset_factory(Celebrity, CelebrityForm, max_num=10, extra=10)
    if request.method == 'POST':
        formset = cf(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('add_celeb'))
        else:
            render_to_response('add.html', 
            {"formset": formset,
            'error_message': "Invalid celebrity name"},
            context_instance=RequestContext(request))
            
    else:
        formset = cf(queryset=Celebrity.objects.none())
    return render_to_response('add.html', {"formset": formset}, context_instance=RequestContext(request))