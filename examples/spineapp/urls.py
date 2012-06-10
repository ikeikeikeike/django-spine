from django.conf.urls import (
    patterns,
    url,
    # include
)

import views

urlpatterns = patterns('',
    url(r"", views.app, name="spineapp_app"),
)
