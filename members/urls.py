from django.conf.urls import *

urlpatterns = patterns('members.views',
	(r'^$', 'home'),
	(r'^all/$', 'all_members'),
	(r'^here_today/$', 'here_today'),
	(r'^profile/$', 'profile_redirect'),
	(r'^tags/$', 'tags'),
	(r'^ticker/$', 'ticker'),
	(r'^t/(?P<tag>[^/]+)/$', 'tag'),
	(r'^u/(?P<username>[^/]+)/$', 'user'),
	(r'^u/(?P<username>[^/]+)/tags/$', 'user_tags'),
	(r'^u/(?P<username>[^/]+)/deltag/(?P<tag>[^/]+)$', 'delete_tag'),
	(r'^u/(?P<username>[^/]+)/mail/$', 'mail'),
	(r'^u/(?P<username>[^/]+)/edit/$', 'edit_profile'),
	(r'^u/(?P<username>[^/]+)/r/(?P<id>\d+)/$', 'receipt'),
	(r'^help/(?P<slug>[^/]+)/$', 'help_topic'),

)

# Copyright 2010 Office Nomads LLC (http://www.officenomads.com/) Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
