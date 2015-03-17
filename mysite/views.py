
__author__ = 'Owner'
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
def my_site(request, template_name):

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))