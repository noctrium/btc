from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('freebtc123.views',
    url(r'^$', 'fav', name='fav'),
    url(r'^index$', 'fav', name='fav'),
    url(r'^home$', 'fav', name='fav'),
    url(r'^freebtc$', 'freebtc', name='freebtc'),
    url(r'^altcoin$', 'altcoin', name='altcoin'),
    url(r'^btcforum$', 'btcforum', name='btcforum'),
    url(r'^btcwiki$', 'btcwiki', name='btcwiki'),
    url(r'^submitsite$', 'submitsite', name='submitsite'),
    url(r'^visit/(?P<siteid>\d+)/$', 'visit', name='visit'),
    url(r'^evaluate/(?P<siteid>\d+)/$', 'evaluate', name='evaluate'),
    url(r'^like$', 'like', name='like'),
    url(r'^favorite$', 'favorite', name='favorite'),

    url(r'^login$', 'login', name='login'),
    url(r'^signup$', 'signup', name='signup'),
    url(r'^logout$', 'logout', name='logout'),
    url(r'^usercheck$', 'usercheck', name='usercheck'),
)