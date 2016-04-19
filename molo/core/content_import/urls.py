from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^api-auth/', include(
        'rest_framework.urls', namespace='rest_framework')),
    url(
        r'^repos/$',
        'molo.core.content_import.views.get_repos',
        name='get_repos'
    ),
    url(
        r'^repos/(?P<name>[\w-]+)/$',
        'molo.core.content_import.views.get_repo_languages',
        name='get_repo_languages'
    ),
    url(
        r'^repos/(?P<name>[\w-]+)/import/',
        'molo.core.content_import.views.import_content',
        name='import_content'
    ),
    url(
        r'^repos/(?P<name>[\w-]+)/validate/',
        'molo.core.content_import.views.import_validate',
        name='import_validate'
    ),
)
