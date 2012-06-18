from django.http import HttpResponse
from django.utils import simplejson as json


class LazyJSONEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            iterable = iter(o)
        except TypeError:
            pass
        else:
            return list(iterable)
        try:
            from django.db.models.base import ModelBase
            isinstance(o.__class__, ModelBase)
        except Exception:
            pass
        else:
            from django.utils.encoding import force_unicode
            return force_unicode(o)
        return super(LazyJSONEncoder, self).default(o)


class JsonResponse(HttpResponse):
    def __init__(self, content=None, mimetype="application/json", *args, **kwargs):
        data = json.dumps(content or {}, cls=kwargs.pop('cls', LazyJSONEncoder))
        super(JsonResponse, self).__init__(data, mimetype, *args, **kwargs)
