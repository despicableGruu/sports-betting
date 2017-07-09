"""NewBet URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from betapp.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^competitions/', CompetitionsView.as_view(), name="competitions"),
    url(r'^competition/(?P<id>[\d]+)', CompetitionView.as_view(),
        name="competition"),
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^logout/', LogoutView.as_view(), name="logout"),
    url(r'^register/', RegisterView.as_view(), name="register"),
    url(r'^bet_fixture/(?P<id>[\d]+)', BetFixtureView.as_view(),
        name="bet-fixture"),
    url(r'^account_details/', AccountDetailsView.as_view(),
        name="account-details"),
    url(r'^show_team/(?P<team_id>[\d]+)', ShowTeamView.as_view(),
        name="show-team"),
    url(r'^add_competitions/(?P<season>[\d]+)', AddCompetitionsView.as_view(),
        name="add-competitions"),
]

