from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from blog.models import Post, CaseStudy, HighlightedCaseStudy
from rest_framework import serializers

def get_field_name_list(model_object):
    return [ field_obj.name for field_obj in model_object._meta.fields ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = get_user_model()
        fields = get_field_name_list(get_user_model())


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Group
        fields = get_field_name_list(Group)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    # see https://stackoverflow.com/questions/32509815/django-rest-framework-get-data-from-foreign-key-relation
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CaseStudySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = CaseStudy
        fields = (
            'id', 'user', 'username', 
            'title', 'cover_image', 'content',
            'is_public', 'order', 'created_at',
            'roles', 'time_spent', 'project_type', 'client_type', 'demonstrated_skills'
        )



class HighlightedCaseStudySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    # case study info
    case_study_id = serializers.CharField(source='case_study.id', read_only=True)
    case_study_title = serializers.CharField(source='case_study.title', read_only=True)
    case_study_cover_image = serializers.URLField(source='case_study.cover_image', read_only=True)
    case_study_demo_skills = serializers.CharField(source='case_study.demonstrated_skills', read_only=True)
    case_study_roles = serializers.CharField(source='case_study.roles', read_only=True)

    class Meta:
        model = HighlightedCaseStudy
        fields = (
            'id',
            'url',

            'case_study',
            'case_study_id',
            'case_study_title',
            'case_study_cover_image',
            'case_study_demo_skills',
            'case_study_roles',

            'highlighted_abstract',
            'highlighted_image',
            'highlighted_image_css_position',
            'highlighted_image_css_position_mobile',

            'leader_words',
            'leader_action',
            'is_public',
        )
        # depth = 1 # for list out all fields in foreign key to case study