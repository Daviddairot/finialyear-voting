from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('then', views.index, name="index"),
    path('next_pag/', views.next_page, name='next_page'),
    path('next/', views.login_view, name='next'),  # 'next' is the login page
    path('vot/', views.vote, name='vote'),
    path('res/', views.end, name='end'),
    path('vote_submit/', views.vote_submit, name='vote_submit'),
    path('close/', views.close, name='close'),
    path('election_results/', views.election_results, name = 'election_results'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
