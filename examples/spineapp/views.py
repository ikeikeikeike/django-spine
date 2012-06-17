from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import (
    Example,
    ExampleMapper
)
from subcommand.utils import JsonResponse


def index(request):

    if request.is_ajax():
        return JsonResponse(map(lambda obj: ExampleMapper(obj).as_dict(), Example.objects.all()))
    else:
        return render_to_response("spineapp/app.html", RequestContext(request, {}))
