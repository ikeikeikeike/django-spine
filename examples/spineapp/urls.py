from django.conf.urls import (
    patterns,
    url,
    # include
)

import views

urlpatterns = patterns('',
    url(r"^examples", views.index, name="spineapp_index"),
#    url(r"", views.index, name="spineapp_index"),
)
