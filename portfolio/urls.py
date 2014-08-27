from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','brochure.views.home',name='home'),
    url(r'^hello/$', 'brochure.views.hello'),
    url(r'^name/$','brochure.views.name'),


    url(r'^hello/(?P<name>\w+)/(?P<color>\w+)/$', 'brochure.views.hello'),

    url(r'^aboutme/$','brochure.views.aboutme'),
    url(r'^projects/$','brochure.views.projects'),
    url(r'^contact/$','brochure.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects/professional/$','brochure.views.professional'),



    url(r'^fizzbuzz/(?P<num1>\w+)/(?P<num2>\w+)/$', 'brochure.views.fizzbuzz'),
)
