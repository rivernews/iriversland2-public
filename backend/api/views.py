from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from blog.models import (
    Post,
    CaseStudy, HighlightedCaseStudy
)

from rest_framework import viewsets
from .serializers import (
    UserSerializer, GroupSerializer,
    PostSerializer,
    CaseStudySerializer, HighlightedCaseStudySerializer,
)

from rest_framework import permissions
from .permissions import (
    AllowOptionsIsAdminUser,
    AllowOptionsIsAdminUserOrReadOnly,
)

from rest_framework.response import Response
from rest_framework import status
# Status Code
# http://www.django-rest-framework.org/api-guide/status-codes/
#

from rest_framework.views import APIView

# usage of default_storage
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#cloudfront
# from django.core.files.storage import default_storage
from django_backend.custom_storages import MediaStorage
import os
from django.conf import settings

from datetime import datetime

from django.db.models import Q

from rest_framework import serializers

from django.views.generic.base import TemplateView

class APIIndexView(TemplateView):
    template_name = "api/index.html"

class FileUploadView(APIView):
    permission_classes = (AllowOptionsIsAdminUser,)
    
    def post(self, requests, ** kwargs):
        file_obj = requests.FILES.get('file', '')
        work_type = requests.POST.get('workType', 'other-work-type')
        created_time_js_string = requests.POST.get('createdTime', '')
        work_id = requests.POST.get('id', '')

        if created_time_js_string == '' or work_id == '' or file_obj == '':
            return Response({
                'message': 'Meta or file data not given',
            }, status=status.HTTP_417_EXPECTATION_FAILED)

        # Prepare date for file directory organizarion
        work_created_datetime = datetime.strptime(created_time_js_string, '%Y-%m-%dT%H:%M:%S.%fZ')
        work_created_date = work_created_datetime.date()

        # Determine directory
        file_path_with_directory = os.path.join(
            settings.CKEDITOR_UPLOAD_PATH,
            work_type,
            '{}-{}'.format(work_created_date, work_id),
            file_obj.name
        )

        # Avoid overwriting existing file
        media_storage = MediaStorage()

        # if not default_storage.exists(file_path_with_directory):
        #     default_storage.save(file_path_with_directory, file_obj)
        #     file_url = default_storage.url(file_path_with_directory)

        #     return Response({
        #         'message': 'OK',
        #         'fileUrl': file_url,
        #     })
        if not media_storage.exists(file_path_with_directory):
            media_storage.save(file_path_with_directory, file_obj)
            file_url = media_storage.url(file_path_with_directory)
            print('\nfile url is ', file_url)

            return Response({
                'message': 'OK',
                'fileUrl': file_url,
            })
        else:
            return Response({
                'message': 'Filename already exists, please change a filename or try a different file.',
            }, status=status.HTTP_409_CONFLICT)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (AllowOptionsIsAdminUser,)

    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (AllowOptionsIsAdminUser,)

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FilterByAuthorMixin(object):
    def get_queryset_filtered_by_author(self, original_model):
        queryset = self.filter_queryset(original_model.objects.all())  # Apply any filter backends

        request_user = self.request.user
        if request_user.is_superuser:
            return queryset # user is suepr user --> return all
        elif request_user.is_authenticated:
            return queryset.filter(Q(is_public=True) | Q(user=request_user)) # user is author --> return all is_public + is author but !is_public
        else:
            return queryset.filter(is_public=True) # user is anonymus --> return is_public


class PostViewSet(FilterByAuthorMixin, viewsets.ModelViewSet):
    permission_classes = (AllowOptionsIsAdminUserOrReadOnly,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # setup user upon creation, see https://stackoverflow.com/questions/32509815/django-rest-framework-get-data-from-foreign-key-relation
    user = serializers.PrimaryKeyRelatedField(
        # set it to read_only as we're handling the writing part ourselves
        read_only=True,
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.get_queryset_filtered_by_author(Post)


class CaseStudyViewSet(FilterByAuthorMixin, viewsets.ModelViewSet):
    permission_classes = (AllowOptionsIsAdminUserOrReadOnly,)

    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer

    # setup user upon creation, see https://stackoverflow.com/questions/32509815/django-rest-framework-get-data-from-foreign-key-relation
    user = serializers.PrimaryKeyRelatedField(
        # set it to read_only as we're handling the writing part ourselves
        read_only=True,
    )
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.get_queryset_filtered_by_author(CaseStudy)


class HighlightedCaseStudyViewSet(FilterByAuthorMixin, viewsets.ModelViewSet):
    permission_classes = (AllowOptionsIsAdminUserOrReadOnly,)

    queryset = HighlightedCaseStudy.objects.all()
    serializer_class = HighlightedCaseStudySerializer

    def get_queryset(self):
        return self.get_queryset_filtered_by_author(HighlightedCaseStudy) 