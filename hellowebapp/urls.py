from django.conf.urls import url, patterns, include
from django.contrib import admin
from collection import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name="contact"),
    url(r'^reviews/(?P<slug>[-\w]+)/$', views.review_detail, name='review_detail'),
    url(r'^reviews/(?P<slug>[-\w]+)/edit/$', views.edit_review, name='edit_review'),
    url(r'^admin/', include(admin.site.urls)),
]
