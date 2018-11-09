from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated, AllowAny, BasePermission, SAFE_METHODS

from blog.views import EmailReportMixin

class LogPermissionStatusMixin(EmailReportMixin, object):
    def LogPermissionStatus(self, request, view):
        if not request.user.is_superuser and not 'localhost' in request.get_host() :        
            self.send_feedback_notice_email(request)
        # print('============ {}: {}'.format(request.method, request.build_absolute_uri()))
        # print('header  --%s--' % request.META.get('HTTP_AUTHORIZATION'))
        # print('AllowAny:', AllowAny.has_permission(self, request, view))
        # print('IsAuthenticatedOrReadOnly:', IsAuthenticatedOrReadOnly.has_permission(self, request, view))
        # print('IsAuthenticated:', IsAuthenticated.has_permission(self, request, view))
        # print('IsAdminUser:', IsAdminUser.has_permission(self, request, view))
        # print('request.user', request.user)
        # print('request user is auth', request.user.is_authenticated)
        # print('request user is staff', request.user.is_staff)
        # print('request user is super', request.user.is_superuser)


class AllowOptionsIsAuthenticatedOrReadOnly(LogPermissionStatusMixin, IsAuthenticatedOrReadOnly):
    def has_permission(self, request, view):
        self.LogPermissionStatus(request, view)
        if request.method == 'OPTIONS':
            return True
        return super(AllowOptionsIsAuthenticatedOrReadOnly, self).has_permission(request, view)


class AllowOptionsIsAdminUserOrReadOnly(LogPermissionStatusMixin, BasePermission):
    def has_permission(self, request, view):
        self.LogPermissionStatus(request, view)
        if request.method == 'OPTIONS':
            return True
        elif request.method in SAFE_METHODS:
            return True
        else:
            return request.user and request.user.is_superuser


class AllowOptionsIsSatffUser(LogPermissionStatusMixin, IsAdminUser):
    def has_permission(self, request, view):
        self.LogPermissionStatus(request, view)
        if request.method == 'OPTIONS':
            return True
        return super(AllowOptionsIsSatffUser, self).has_permission(request, view)


class AllowOptionsIsAdminUser(LogPermissionStatusMixin, BasePermission):
    def has_permission(self, request, view):
        self.LogPermissionStatus(request, view)
        if request.method == 'OPTIONS':
            return True
        return request.user and request.user.is_superuser


