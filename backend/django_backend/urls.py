"""django_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.staticfiles.views import serve
from django.views.generic import RedirectView

from rest_framework import routers

from api import views
from blog import views as BlogViews

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'case-studies', views.CaseStudyViewSet)
router.register(r'highlighted-case-studies', views.HighlightedCaseStudyViewSet)

urlpatterns = [
    url(r'^admin-cool/', include(admin.site.urls)),
    url(r'^django-health-check/$', BlogViews.HealthCheckView.as_view(), name='django-health-check'),
    url(r'^fail-test/$', BlogViews.FailView.as_view(), name='fail-test'),

    url(r'^report', BlogViews.EmailView.as_view(), name='report'),
    url(r'^recaptcha/$', BlogViews.ContactMeView.as_view(), name='recaptcha'),

    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^api/uploads/', views.FileUploadView.as_view()),
    
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), # for the browsable API login URLs
    url(r'^api/token-auth/', obtain_jwt_token), # for the browsable API login URLs
    url(r'^api/token-refresh/', refresh_jwt_token), # for the browsable API login URLs
    url(r'^api/', include(router.urls)),

    # handling static file request (icons/js/css)
    url(r'^ngsw-worker.js$', serve, kwargs={'path': 'ngsw-worker.js'}),
    url(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',
        RedirectView.as_view(url='/static/%(path)s', permanent=False)), # alter static access url

    # let front end handle the rest of all routings
    # url(r'^.*$', serve, kwargs={'path': 'index.html'}), # use static to serve templates
    url(r'^(?P<path>.*)$', RedirectView.as_view(url='/static/%(path)s')) # change for k8 production
]
