from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Post, Comment, CaseStudy, HighlightedCaseStudy


class PostViewAdmin(admin.ModelAdmin):
	# list_display = [ field.name for field in Post._meta.fields ]
	list_display = [
        'title', 'cover_image',
        'user', 'tags', 'preview_content', 'modified_at', 'is_public', 'order'
    ]

admin.site.register(Post, PostViewAdmin)


class CommentViewAdmin(admin.ModelAdmin):
	list_display = [ field.name for field in Comment._meta.fields ]

admin.site.register(Comment, CommentViewAdmin)


class CaseStudyViewAdmin(admin.ModelAdmin):
	list_display = [
        'title', 'cover_image',
        'roles', 'demonstrated_skills', 'project_type', 'client_type', 'time_spent', 'is_public', 'order'
    ]

admin.site.register(CaseStudy, CaseStudyViewAdmin)


class HighlightedCaseStudyViewAdmin(admin.ModelAdmin):
	list_display = [
        'case_study', 'highlighted_abstract', 
        'highlighted_image', 'highlighted_image_css_position', 'highlighted_image_css_position_mobile',
        'leader_action', 'is_public'
    ]

admin.site.register(HighlightedCaseStudy, HighlightedCaseStudyViewAdmin)