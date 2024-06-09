from django.conf import settings
from django.shortcuts import render, redirect
from .models import Most_Influential, UserProfile, Social_Media_Content_Creator, Sportsman_of_the_Year, Sportswoman_of_the_Year, Most_Popular_Male, Most_Popular_Female, Entrepreneur_of_the_Year_Male, Entrepreneur_of_the_Year_Female, Most_Social, Most_Fashionable_Male, Most_Fashionable_Female,  UserVote, Clique_of_the_Year
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import re  # Import regular expression module
import csv
import os




def index(request):
    return render(request, 'index.html')

def close(request):
    return render(request, 'close.html')

def next_page(request):
    return render(request, 'next_page.html')


def election_results(request):
    Most_Influential_votes = Most_Influential.objects.values_list('name', 'votes')
    Social_Media_Content_Creator_votes = Social_Media_Content_Creator.objects.values_list('name', 'votes')
    Sportsman_of_the_Year_votes = Sportsman_of_the_Year.objects.values_list('name', 'votes')
    Sportswoman_of_the_Year_votes = Sportswoman_of_the_Year.objects.values_list('name', 'votes')
    Most_Popular_Male_votes = Most_Popular_Male.objects.values_list('name', 'votes')
    Most_Popular_Female_votes = Most_Popular_Female.objects.values_list('name', 'votes')
    Entrepreneur_of_the_Year_Male_votes = Entrepreneur_of_the_Year_Male.objects.values_list('name', 'votes')
    Entrepreneur_of_the_Year_Female_votes = Entrepreneur_of_the_Year_Female.objects.values_list('name', 'votes')
    Most_Social_votes = Most_Social.objects.values_list('name', 'votes')
    Most_Fashionable_Male_votes = Most_Fashionable_Male.objects.values_list('name', 'votes')
    Most_Fashionable_Female_votes = Most_Fashionable_Female.objects.values_list('name', 'votes')
    Clique_of_the_Year_votes = Clique_of_the_Year.objects.values_list('name', 'votes')


    # Prepare data for the pie charts
    labels = [candidate[0] for candidate in Most_Influential_votes]
    votes = [candidate[1] for candidate in Most_Influential_votes]

    colabels = [candidate[0] for candidate in Clique_of_the_Year_votes]
    covotes = [candidate[1] for candidate in Clique_of_the_Year_votes]

    vlabels = [candidate[0] for candidate in Social_Media_Content_Creator_votes]
    vvotes = [candidate[1] for candidate in Social_Media_Content_Creator_votes]

    gs_labels = [candidate[0] for candidate in Sportsman_of_the_Year_votes]
    gs_votes = [candidate[1] for candidate in Sportsman_of_the_Year_votes]

    fs_labels = [candidate[0] for candidate in Sportswoman_of_the_Year_votes]
    fs_votes = [candidate[1] for candidate in Sportswoman_of_the_Year_votes]

    sd_labels = [candidate[0] for candidate in Most_Popular_Male_votes]
    sd_votes = [candidate[1] for candidate in Most_Popular_Male_votes]

    td_labels = [candidate[0] for candidate in Most_Popular_Female_votes]
    td_votes = [candidate[1] for candidate in Most_Popular_Female_votes]

    sp_labels = [candidate[0] for candidate in Entrepreneur_of_the_Year_Male_votes]
    sp_votes = [candidate[1] for candidate in Entrepreneur_of_the_Year_Male_votes]

    pro_labels = [candidate[0] for candidate in Entrepreneur_of_the_Year_Female_votes]
    pro_votes = [candidate[1] for candidate in Entrepreneur_of_the_Year_Female_votes]

    t_labels = [candidate[0] for candidate in Most_Social_votes]
    t_votes = [candidate[1] for candidate in Most_Social_votes]

    wd_labels = [candidate[0] for candidate in Most_Fashionable_Male_votes]
    wd_votes = [candidate[1] for candidate in Most_Fashionable_Male_votes]

    as_labels = [candidate[0] for candidate in Most_Fashionable_Female_votes]
    as_votes = [candidate[1] for candidate in Most_Fashionable_Female_votes]


    context = {
        'labels': labels,
        'votes': votes,
        'vlabels': vlabels,
        'vvotes': vvotes,
        'gs_labels': gs_labels,
        'gs_votes': gs_votes,
        'fs_labels': fs_labels,
        'fs_votes': fs_votes,
        'sd_labels': sd_labels,
        'sd_votes': sd_votes,
        'td_labels': td_labels,
        'td_votes': td_votes,
        'sp_labels': sp_labels,
        'sp_votes': sp_votes,
        'pro_labels': pro_labels,
        'pro_votes': pro_votes,
        't_labels': t_labels,
        't_votes': t_votes,
        'wd_labels': wd_labels,
        'wd_votes': wd_votes,
        'as_labels': as_labels,
        'as_votes': as_votes,
        'colabels ':colabels ,
        'covotes':covotes,
    }
    return render(request, 'election_results.html', context)

def vote(request):
    most_influential_candidates = Most_Influential.objects.all()
    social_media_content_creators = Social_Media_Content_Creator.objects.all()
    sportsmen_of_the_year = Sportsman_of_the_Year.objects.all()
    most_fashionable_male_candidates = Most_Fashionable_Male.objects.all()
    sportswomen_of_the_year = Sportswoman_of_the_Year.objects.all()
    most_popular_male_candidates = Most_Popular_Male.objects.all()
    most_popular_female_candidates = Most_Popular_Female.objects.all()
    entrepreneur_of_the_year_male_candidates = Entrepreneur_of_the_Year_Male.objects.all()
    entrepreneur_of_the_year_female_candidates = Entrepreneur_of_the_Year_Female.objects.all()
    most_social_candidates = Most_Social.objects.all()
    most_fashionable_female_candidates = Most_Fashionable_Female.objects.all()
    Clique_of_the_Year_candidates =  Clique_of_the_Year.objects.all()

    context = {
        'most_influential_candidates': most_influential_candidates,
        'social_media_content_creators': social_media_content_creators,
        'sportsmen_of_the_year': sportsmen_of_the_year,
        'most_fashionable_male_candidates': most_fashionable_male_candidates,
        'sportswomen_of_the_year': sportswomen_of_the_year,
        'most_popular_male_candidates': most_popular_male_candidates,
        'most_popular_female_candidates': most_popular_female_candidates,
        'entrepreneur_of_the_year_male_candidates': entrepreneur_of_the_year_male_candidates,
        'entrepreneur_of_the_year_female_candidates': entrepreneur_of_the_year_female_candidates,
        'most_social_candidates': most_social_candidates,
        'most_fashionable_female_candidates': most_fashionable_female_candidates,
        'Clique_of_the_Year_candidates':Clique_of_the_Year_candidates,
    }

    return render(request, 'vote.html', context)



def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip().lower()  # Convert to lowercase

        # Debugging: Print the name
        print("Name:", name)

        # Path to the CSV file
        csv_file_path = os.path.join(settings.BASE_DIR, 'user.csv')

        # Validate name by checking it in the CSV file
        name_exists = False
        try:
            with open(csv_file_path, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0].strip().lower() == name:
                        name_exists = True
                        break
        except FileNotFoundError:
            feedback_message = "User CSV file not found."
            return render(request, 'next_page.html', {'feedback_message': feedback_message})

        if not name_exists:
            feedback_message = "Name not found."
            return render(request, 'next_page.html', {'feedback_message': feedback_message})

        # Set the name in the session
        request.session['name'] = name

        # Save the name to the UserProfile model
        user_profile, created = UserProfile.objects.get_or_create(name=name, defaults={'has_voted': False})

        # Check if the user has already voted
        if user_profile.has_voted:
            return redirect('close')  # Redirect to the end page if the user has already voted

        # Redirect to the voting page
        return redirect('vote')

    return render(request, 'next_page.html')





def vote_submit(request):
    if request.method == 'POST':
        # Get the selected candidates' IDs from the submitted form
        Most_Influential_id = request.POST.get('Most_Influential')
        Social_Media_Content_Creator_id = request.POST.get('Social_Media_Content_Creator')
        Sportsman_of_the_Year_id = request.POST.get('general_secretaries')
        Most_Fashionable_Male_id = request.POST.get('Most_Fashionable_Male')
        Sportswoman_of_the_Year_id = request.POST.get('Sportswoman_of_the_Year')
        Most_Popular_Male_id = request.POST.get('Most_Popular_Male')
        Most_Popular_Female_id = request.POST.get('Most_Popular_Female')
        Entrepreneur_of_the_Year_Male_id = request.POST.get('Entrepreneur_of_the_Year_Male')
        Entrepreneur_of_the_Year_Female_id = request.POST.get('Entrepreneur_of_the_Year_Female')
        Most_Social_id = request.POST.get('Most_Social')
        Most_Fashionable_Female_id = request.POST.get('Most_Fashionable_Female')
        Clique_of_the_Year_id = request.POST.get('Clique_of_the_Year')

        # Check if any position was left unvoted
        if not Most_Influential_id or not Social_Media_Content_Creator_id or not Sportsman_of_the_Year_id \
                or not Most_Fashionable_Male_id or not Sportswoman_of_the_Year_id \
                or not Most_Popular_Male_id or not Most_Popular_Female_id \
                or not Entrepreneur_of_the_Year_Male_id or not Entrepreneur_of_the_Year_Female_id \
                or not Most_Social_id or not Most_Fashionable_Female_id:
            return redirect('vote')

        # Get the actual model instances
        most_influential = Most_Influential.objects.get(pk=Most_Influential_id)
        social_media_content_creator = Social_Media_Content_Creator.objects.get(pk=Social_Media_Content_Creator_id)
        sportsman_of_the_year = Sportsman_of_the_Year.objects.get(pk=Sportsman_of_the_Year_id)
        most_fashionable_male = Most_Fashionable_Male.objects.get(pk=Most_Fashionable_Male_id)
        sportswoman_of_the_year = Sportswoman_of_the_Year.objects.get(pk=Sportswoman_of_the_Year_id)
        most_popular_male = Most_Popular_Male.objects.get(pk=Most_Popular_Male_id)
        most_popular_female = Most_Popular_Female.objects.get(pk=Most_Popular_Female_id)
        entrepreneur_of_the_year_male = Entrepreneur_of_the_Year_Male.objects.get(pk=Entrepreneur_of_the_Year_Male_id)
        entrepreneur_of_the_year_female = Entrepreneur_of_the_Year_Female.objects.get(pk=Entrepreneur_of_the_Year_Female_id)
        most_social = Most_Social.objects.get(pk=Most_Social_id)
        most_fashionable_female = Most_Fashionable_Female.objects.get(pk=Most_Fashionable_Female_id)
        clique_of_the_year = Clique_of_the_Year.objects.get(pk = Clique_of_the_Year_id)

        # Increment the vote count for each candidate
        clique_of_the_year.votes += 1
        clique_of_the_year.save()
        most_influential.votes += 1
        most_influential.save()
        social_media_content_creator.votes += 1
        social_media_content_creator.save()
        sportsman_of_the_year.votes += 1
        sportsman_of_the_year.save()
        most_fashionable_male.votes += 1
        most_fashionable_male.save()
        sportswoman_of_the_year.votes += 1
        sportswoman_of_the_year.save()
        most_popular_male.votes += 1
        most_popular_male.save()
        most_popular_female.votes += 1
        most_popular_female.save()
        entrepreneur_of_the_year_male.votes += 1
        entrepreneur_of_the_year_male.save()
        entrepreneur_of_the_year_female.votes += 1
        entrepreneur_of_the_year_female.save()
        most_social.votes += 1
        most_social.save()
        most_fashionable_female.votes += 1
        most_fashionable_female.save()

        # Get the user profile using the session data (assuming 'name' is unique)
        user_name = request.session.get('name')
        user_profile = UserProfile.objects.get(name=user_name)
        
        # Create a UserVote instance
        UserVote.objects.create(
            user_profile=user_profile,
            Most_Influential_voted=most_influential,
            Social_Media_Content_Creator_voted=social_media_content_creator,
            Sportsman_of_the_Year_voted=sportsman_of_the_year,
            Sportswoman_of_the_Year_voted=sportswoman_of_the_year,
            Most_Popular_Male_voted=most_popular_male,
            Most_Popular_Female_voted=most_popular_female,
            Entrepreneur_of_the_Year_Male_voted=entrepreneur_of_the_year_male,
            Entrepreneur_of_the_Year_Female_voted=entrepreneur_of_the_year_female,
            Most_Social_voted=most_social,
            Most_Fashionable_Male_voted=most_fashionable_male,
            Most_Fashionable_Female_voted=most_fashionable_female,
        )

        # Mark the user profile as having voted
        user_profile.has_voted = True
        user_profile.save()
    
        # Render the closing page
        return render(request, 'close.html')

    return redirect('vote')


        # Mark the user as voted in the UserProfile
        #Most_Influential_candidates = Most_Influential.objects.values('name', 'votes')
        #Social_Media_Content_Creator_candidates = Social_Media_Content_Creator.objects.values('name', 'votes')
        #Sportsman_of_the_Year_candidates = Sportsman_of_the_Year.objects.values('name', 'votes')
        #Most_Fashionable_Male_candidates = Most_Fashionable_Male.objects.values('name', 'votes')
        #Sportswoman_of_the_Year_candidates = Sportswoman_of_the_Year.objects.values('name', 'votes')
        #Most_Popular_Male_candidates = Most_Popular_Male.objects.values('name', 'votes')
        #Most_Popular_Female_candidates = Most_Popular_Female.objects.values('name', 'votes')
        #Entrepreneur_of_the_Year_Male_candidates = Entrepreneur_of_the_Year_Male.objects.values('name', 'votes')
        #Entrepreneur_of_the_Year_Female_candidates = Entrepreneur_of_the_Year_Female.objects.values('name', 'votes')
        #Most_Social_candidates = Most_Social.objects.values('name', 'votes')
        #Most_Fashionable_Female_candidates = Most_Fashionable_Female.objects.values('name', 'votes')

        #return render(request, 'end.html', {
        #   'Most_Influential_candidates': Most_Influential_candidates,
        #    'Social_Media_Content_Creator_candidates': Social_Media_Content_Creator_candidates,
        #    'Sportsman_of_the_Year_candidates': Sportsman_of_the_Year_candidates,
        #    'Most_Fashionable_Male_candidates': Most_Fashionable_Male_candidates,
        #    'Sportswoman_of_the_Year_candidates': Sportswoman_of_the_Year_candidates,
        #    'Most_Popular_Male_candidates': Most_Popular_Male_candidates,
        #    'Most_Popular_Female_candidates': Most_Popular_Female_candidates,
        #    'Entrepreneur_of_the_Year_Male_candidates': Entrepreneur_of_the_Year_Male_candidates,
        #    'Entrepreneur_of_the_Year_Female_candidates': Entrepreneur_of_the_Year_Female_candidates,
        #    'Most_Social_candidates': Most_Social_candidates,
        #    'Most_Fashionable_Female_candidates': Most_Fashionable_Female_candidates,

        #})
    
        
    # If the request method is not POST, handle it accordingly (redirect or render a different page)
    return redirect('close')  

def end(request):
        Most_Influential_candidates = Most_Influential.objects.values('name', 'votes')
        Social_Media_Content_Creator_candidates = Social_Media_Content_Creator.objects.values('name', 'votes')
        Sportsman_of_the_Year_candidates = Sportsman_of_the_Year.objects.values('name', 'votes')
        Most_Fashionable_Male_candidates = Most_Fashionable_Male.objects.values('name', 'votes')
        Sportswoman_of_the_Year_candidates = Sportswoman_of_the_Year.objects.values('name', 'votes')
        Most_Popular_Male_candidates = Most_Popular_Male.objects.values('name', 'votes')
        Most_Popular_Female_candidates = Most_Popular_Female.objects.values('name', 'votes')
        Entrepreneur_of_the_Year_Male_candidates = Entrepreneur_of_the_Year_Male.objects.values('name', 'votes')
        Entrepreneur_of_the_Year_Female_candidates = Entrepreneur_of_the_Year_Female.objects.values('name', 'votes')
        Most_Social_candidates = Most_Social.objects.values('name', 'votes')
        Most_Fashionable_Female_candidates = Most_Fashionable_Female.objects.values('name', 'votes')


        return render(request, 'end.html', {
            'Most_Influential_candidates': Most_Influential_candidates,
            'Social_Media_Content_Creator_candidates': Social_Media_Content_Creator_candidates,
            'Sportsman_of_the_Year_candidates': Sportsman_of_the_Year_candidates,
            'Most_Fashionable_Male_candidates': Most_Fashionable_Male_candidates,
            'Sportswoman_of_the_Year_candidates': Sportswoman_of_the_Year_candidates,
            'Most_Popular_Male_candidates': Most_Popular_Male_candidates,
            'Most_Popular_Female_candidates': Most_Popular_Female_candidates,
            'Entrepreneur_of_the_Year_Male_candidates': Entrepreneur_of_the_Year_Male_candidates,
            'Entrepreneur_of_the_Year_Female_candidates': Entrepreneur_of_the_Year_Female_candidates,
            'Most_Social_candidates': Most_Social_candidates,
            'Most_Fashionable_Female_candidates': Most_Fashionable_Female_candidates,
        })







def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')
