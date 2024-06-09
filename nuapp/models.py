from django.db import models
import re  # Import regular expression module




class Most_Influential(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Social_Media_Content_Creator(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.name
    
class Sportsman_of_the_Year(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.name
    
class Sportswoman_of_the_Year(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Most_Popular_Male(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Most_Popular_Female(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Entrepreneur_of_the_Year_Male(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Entrepreneur_of_the_Year_Female(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Clique_of_the_Year(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Most_Social(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Most_Fashionable_Male(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Most_Fashionable_Female(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True,)  # Assuming name is unique and used as username
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class UserVote(models.Model):
    user_profile = models.OneToOneField('UserProfile', on_delete=models.CASCADE)
    Most_Fashionable_Female_voted = models.ForeignKey(Most_Fashionable_Female, related_name='Most_Fashionable_Female', on_delete=models.CASCADE, blank=True, null=True)
    Most_Influential_voted = models.ForeignKey(Most_Influential, related_name='Most_Influential', on_delete=models.CASCADE, blank=True, null=True)
    Social_Media_Content_Creator_voted = models.ForeignKey(Social_Media_Content_Creator, related_name='Social_Media_Content_Creator', on_delete=models.CASCADE, blank=True, null=True)
    Sportsman_of_the_Year_voted = models.ForeignKey(Sportsman_of_the_Year, related_name='votes_for_Sportsman_of_the_Year', on_delete=models.CASCADE, blank=True, null=True)
    Sportswoman_of_the_Year_voted = models.ForeignKey(Sportswoman_of_the_Year, related_name='votes_for_Sportswoman_of_the_Year', on_delete=models.CASCADE, blank=True, null=True)
    Most_Popular_Male_voted = models.ForeignKey(Most_Popular_Male, related_name='votes_for_Most_Popular_Male', on_delete=models.CASCADE, blank=True, null=True)
    Most_Popular_Female_voted = models.ForeignKey(Most_Popular_Female, related_name='votes_for_Most_Popular_Female', on_delete=models.CASCADE, blank=True, null=True)
    Entrepreneur_of_the_Year_Male_voted = models.ForeignKey(Entrepreneur_of_the_Year_Male, related_name='votes_for_public_relations_officer', on_delete=models.CASCADE, blank=True, null=True)
    Entrepreneur_of_the_Year_Female_voted = models.ForeignKey(Entrepreneur_of_the_Year_Female, related_name='Entrepreneur_of_the_Year_Female', on_delete=models.CASCADE, blank=True, null=True)
    Clique_of_the_Year_voted = models.ForeignKey(Clique_of_the_Year, related_name='votes_for_Clique_of_the_Year', on_delete=models.CASCADE, blank=True, null=True)
    Most_Social_voted = models.ForeignKey(Most_Social, related_name='votes_for_Most_Social', on_delete=models.CASCADE, blank=True, null=True)
    Most_Fashionable_Male_voted = models.ForeignKey(Most_Fashionable_Male, related_name='votes_for_Most_Fashionable_Male', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.user_profile.name} voted for candidates"