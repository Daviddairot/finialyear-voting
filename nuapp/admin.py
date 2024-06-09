from django.contrib import admin
from .models import (
    Most_Influential,
    UserProfile,
    Social_Media_Content_Creator,
    Sportsman_of_the_Year,
    Sportswoman_of_the_Year,
    Most_Popular_Male,
    Most_Popular_Female,
    Entrepreneur_of_the_Year_Male,
    Entrepreneur_of_the_Year_Female,
    Clique_of_the_Year,
    Most_Social,
    Most_Fashionable_Male,
    Most_Fashionable_Female,
    UserVote
)

@admin.register(Most_Influential)
class Most_InfluentialAdmin(admin.ModelAdmin):
    list_display = ('name', 'votes')
    search_fields = ('name',)

@admin.register(Social_Media_Content_Creator)
class Social_Media_Content_CreatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'votes')
    search_fields = ('name',)

@admin.register(Sportsman_of_the_Year)
class Sportsman_of_the_YearAdmin(admin.ModelAdmin):
    list_display = ('name', 'votes')
    search_fields = ('name',)

@admin.register(Sportswoman_of_the_Year)
class Sportswoman_of_the_YearAdmin(admin.ModelAdmin):
    list_display = ('name', 'votes')
    search_fields = ('name',)

@admin.register(Most_Popular_Male)
class Most_Popular_MaleAdmin(admin.ModelAdmin):
    list_display = ('name', 'votes')
    search_fields = ('name',)

@admin.register(Most_Popular_Female)
class Most_Popular_FemaleAdmin(admin.ModelAdmin):
    list_display = ('name', 'votes')
    search_fields = ('name',)

@admin.register(Entrepreneur_of_the_Year_Male)
class Entrepreneur_of_the_Year_MaleAdmin(admin.ModelAdmin):
    list_display = ('name', 'votes')
    search_fields = ('name',)

@admin.register(Entrepreneur_of_the_Year_Female)
class Entrepreneur_of_the_Year_FemaleAdmin(admin.ModelAdmin):
    list_display = ('name', 'votes')
    search_fields = ('name',)

@admin.register(Clique_of_the_Year)
class Clique_of_the_YearAdmin(admin.ModelAdmin):
    list_display = ('name', 'votes')
    search_fields = ('name',)

@admin.register(Most_Social)
class Most_SocialAdmin(admin.ModelAdmin):
    list_display = ('name', 'votes')
    search_fields = ('name',)

@admin.register(Most_Fashionable_Male)
class Most_Fashionable_MaleAdmin(admin.ModelAdmin):
    list_display = ('name', 'votes')
    search_fields = ('name',)

@admin.register(Most_Fashionable_Female)
class Most_Fashionable_FemaleAdmin(admin.ModelAdmin):
    list_display = ('name', 'votes')
    search_fields = ('name',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'has_voted')
    search_fields = ('name',)

@admin.register(UserVote)
class UserVoteAdmin(admin.ModelAdmin):
    list_display = [
        'user_profile', 'Most_Influential_voted', 'Social_Media_Content_Creator_voted', 'Sportsman_of_the_Year_voted', 
        'Sportswoman_of_the_Year_voted', 'Most_Popular_Male_voted', 'Most_Popular_Female_voted',
        'Entrepreneur_of_the_Year_Male_voted', 'Entrepreneur_of_the_Year_Female_voted', 'Clique_of_the_Year_voted',
        'Most_Social_voted', 'Most_Fashionable_Male_voted', 'Most_Fashionable_Female_voted'
    ]
    list_filter = [
        'Most_Influential_voted', 'Social_Media_Content_Creator_voted', 'Sportsman_of_the_Year_voted', 
        'Sportswoman_of_the_Year_voted', 'Most_Popular_Male_voted', 'Most_Popular_Female_voted',
        'Entrepreneur_of_the_Year_Male_voted', 'Entrepreneur_of_the_Year_Female_voted', 'Clique_of_the_Year_voted',
        'Most_Social_voted', 'Most_Fashionable_Male_voted', 'Most_Fashionable_Female_voted'
    ]
