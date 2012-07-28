from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext

from celebrity.models import Celebrity
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
    return render_to_response('add.html', context_instance=RequestContext(request))