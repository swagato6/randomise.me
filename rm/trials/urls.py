from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from rm.trials.views import (MyTrials,
                             TrialDetail,
                             TrialCreate, N1TrialCreate,
                             TrialReport, JoinTrial,
                             EditTrial, TrialQuestion, StopTrial,
                             LeaveTrial, PeekTrial, InviteTrial,
                             ReproduceTrial, TrialAsCsv,
                             AllTrials, FeaturedTrialsList)


urlpatterns = patterns(
    '',
    url(r'my-trials$', MyTrials.as_view(), name='mytrials'),
    url(r'new$', TemplateView.as_view(template_name='trials/new.html'),
        name='trial-create'),

    url(r'create$', TrialCreate.as_view(), name='rm-trial-create'),

    url(r'create-n1$', N1TrialCreate.as_view(), name='n1-trial-create'),
    url(r'(?P<pk>\d+)$', TrialDetail.as_view(), name='trial-detail'),
    url(r'(?P<pk>\d+)/report', TrialReport.as_view(), name='trial-report'),
    url(r'(?P<pk>\d+)/question', TrialQuestion.as_view(), name='trial-question'),
    url(r'(?P<pk>\d+)/edit$', EditTrial.as_view(), name='edit-trial'),
    url(r'(?P<pk>\d+)/join$', JoinTrial.as_view(), name='join-trial'),
    url(r'(?P<pk>\d+)/stop$', StopTrial.as_view(), name='stop-trial'),
    url(r'(?P<pk>\d+)/invite$', InviteTrial.as_view(), name='trial-invite'),
    url(r'(?P<pk>\d+)/peek$', PeekTrial.as_view(), name='trial-peek'),
    url(r'(?P<pk>\d+)/leave$', LeaveTrial.as_view(), name='leave-trial'),
    url(r'(?P<pk>\d+)/reproduce$', ReproduceTrial.as_view(),
        name='reproduce-trial'),
    url(r'(?P<pk>\d+)/as-csv$', TrialAsCsv.as_view(), name='trial-as-csv'),

    # Multiple ways to see lists of trials
    url(r'featured$', FeaturedTrialsList.as_view(), name='featured'),
    url(r'$', AllTrials.as_view(), name='trials'),

)