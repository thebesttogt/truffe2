# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.utils.encoding import smart_str
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db import connections
from django.core.paginator import InvalidPage, EmptyPage, Paginator, PageNotAnInteger
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

from django.db.models import Q


def ecrans(request):
    """View to display the ecran page"""

    return render_to_response('communication/ecrans.html', {}, context_instance=RequestContext(request))


def random_slide(request):
    """Return the URL to a random slide"""

    from communication.models import AgepSlide

    slide = AgepSlide.objects.filter(status='2_online').filter(Q(start_date=None) | Q(start_date__lt=now())).filter(Q(end_date=None) | Q(end_date__gt=now())).order_by('?').all()[0]

    return HttpResponse(slide.picture.url)