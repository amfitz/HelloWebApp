from django.conf.urls import url, patterns, include
from django.contrib import admin
from collection import views
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name="contact"),
    url(r'^reviews/(?P<slug>[-\w]+)/$', views.review_detail, name='review_detail'),
    url(r'^reviews/(?P<slug>[-\w]+)/edit/$', views.edit_review, name='edit_review'),

    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^accounts/password/reset/$', password_reset, {'template_name':'registration/password_reset_form.html'}, name='password_reset'),
    url(r'^accounts/password/reset/done/$', password_reset_done, {'template_name':'registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-a]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name':'registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^accounts/password/done/$', password_reset_complete, {'template_name':'registration/password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^admin/', include(admin.site.urls)),
]
