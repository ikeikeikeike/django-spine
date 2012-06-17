from django.conf.urls import (
    patterns,
    url,
    # include
)

import views

urlpatterns = patterns('',
    url(r"^examples", views.index, name="spineapp_index"),
    url(r"^examples/new", views.new, name="spineapp_new"),
    url(r"^examples/edit", views.edit, name="spineapp_edit"),
    url(r"^examples/show", views.show, name="spineapp_show"),
)
