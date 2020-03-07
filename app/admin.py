from django.contrib import admin
from .models import Member, Field, Topic, Curriculum, Bit, Comment, Upvote, Subscription, Subject, Teach, ChangeLog

# Register your models here.

class UpvoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'curriculum', 'bit','changelog')

admin.site.register(Upvote, UpvoteAdmin)

class ChangeLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_on', 'member', 'description', 'curriculum', 'bit', 'subject', 'operation')

admin.site.register(ChangeLog, ChangeLogAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_on', 'last_modified', 'member', 'curriculum', 'bit', 'comment', 'changelog',)

admin.site.register(Comment, CommentAdmin)

class BitAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_on', 'last_modified', 'bit_type', 'title', 'description', 'curriculum', 'file', 'text')

admin.site.register(Bit, BitAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'subject', 'curriculum')

admin.site.register(Subscription, SubscriptionAdmin)

class TeachAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'curriculum')

admin.site.register(Teach, TeachAdmin)

class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_on', 'last_modified', 'posted_by','subject', 'title', 'description')

admin.site.register(Curriculum, CurriculumAdmin)

class MemberInline(admin.ModelAdmin):
    list_display = ('u_id','created_on', 'username', 'full_name', 'email', 'institution', 'designation', 'image')

admin.site.register(Member, MemberInline)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'title')

admin.site.register(Subject, SubjectAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'field', 'title')

admin.site.register(Topic, TopicAdmin)

class FieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Field, FieldAdmin)