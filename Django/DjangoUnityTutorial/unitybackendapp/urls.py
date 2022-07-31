# Copyright (c) 2015 Eamon Woortman
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import home_view
from unitybackendapp.api import ScoreAPI, UserAPI, GetAuthToken, SavegameAPI

app_name = 'api'

urlpatterns = [#'unitybackendapp.views',
	path('', home_view, name='home_view'),
    
    #apis
    path('score', ScoreAPI.as_view(), name='score'),
    path('user/<int:pk>', UserAPI.as_view(), name='user-detail'),
    path('user', UserAPI.as_view(), name='user-list'),
    path('getauthtoken', GetAuthToken.as_view()),
    path('savegame/<int:pk>', SavegameAPI.as_view(), name='savegame-detail'),
    path('savegame', SavegameAPI.as_view(), name='savegame-list'),
    path('savegames/<int:pk>', SavegameAPI.as_view(), name='savegames-detail'),
    # path('api/score', ScoreAPI.as_view(), name='score'),
    # path('api/user/<int:pk>', UserAPI.as_view(), name='user-detail'),
    # path('api/user', UserAPI.as_view(), name='user-list'),
    # path('api/getauthtoken', GetAuthToken.as_view()),
    # path('api/savegame/<int:pk>', SavegameAPI.as_view(), name='savegame-detail'),
    # path('api/savegame', SavegameAPI.as_view(), name='savegame-list'),
    # path('api/savegames/<int:pk>', SavegameAPI.as_view(), name='savegames-detail'),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
