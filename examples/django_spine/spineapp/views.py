from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import (
#    require_GET,
    require_POST,
    require_safe
)
from spine.utils import (
    JsonResponse,
    json,
)
from .models import (
    Example,
    ExampleMapper
)


def index(request):
    if request.method == 'GET':
        if request.is_ajax():
            return JsonResponse(map(lambda obj: ExampleMapper(obj).as_dict(), Example.objects.all()))
        else:
            return render_to_response("spineapp/app.html", RequestContext(request, {}))
    try:
        data = json.loads(request.body)
        data.pop("id")
        post = Example(**data)
        post.save()
        return JsonResponse(ExampleMapper(post).as_dict())
    except Exception, err:
        return JsonResponse({"err": err.message})


@require_POST
def show(request):
    pass


@require_safe
def new(request):
    pass


@require_safe
def edit(request):
    pass


@require_POST
def update(request):
    pass


@require_POST
def destroy(request):
    pass
