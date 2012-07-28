from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext

from celebrity.models import Celebrity

import random

def home(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def play(request):
    total = Celebrity.objects.count()
    names = []
    tries = 0
    while len(names) < 20 and tries < 5:
        try:
            rand = random.randrange(1, total+1)
            celeb = Celebrity.objects.get(pk=rand)
            if celeb not in names:
                names.append(celeb)
        except ObjectDoesNotExist:
            tries += 1
            pass
    return render_to_response('play.html', {'celebs':names}, context_instance=RequestContext(request))

def add_celeb(request):
    return render_to_response('add.html', context_instance=RequestContext(request))