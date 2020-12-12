from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponsePermanentRedirect


def index(request):
    # return HttpResponsePermanentRedirect(reverse('blog_app:blog_list'
    return HttpResponse('I am Index page')

