#__author__ = 'zhoumeidong'
from django.conf.urls import patterns,url

# noinspection PyUnresolvedReferences
urlpatterns=patterns('',
                     url(r'^$', "mynote.views.index", name="index"),
                    url(r'^test','mynote.views.test',name="test"),
                     )

