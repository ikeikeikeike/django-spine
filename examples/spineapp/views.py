# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext


def app(request):
    return render_to_response("spineapp/app.html",
            RequestContext(request, {}))
