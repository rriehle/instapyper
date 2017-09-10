# encoding: utf-8

import requests
from requests_oauthlib import OAuth1


class Instapyper:

    # Not sure this dict is necessary or even useful
    status_codes = {
        200: "Ok",
        201: "URL successfully added",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Invalid username or password",
        405: "Method not allowed",
        500: "Service error, try again later",
        504: "Gateway timeout",
    }

    # Likewise unsure of the utility of this dict
    urls = {
        'add': "https://www.instapaper.com/api/add",
        'auth': "https://www.instapaper.com/api/authenticate",
        'bookmarks_list': "https://www.instapaper.com/api/1/bookmarks/list",
        'folders_list': "https://www.instapaper.com/api/1/folders/list",
        'oauth_access_token': "https://www.instapaper.com/api/1/oauth/access_token",
    }

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def add(self, url, title=None, selection=None, redirect=None, jsonp=None):

        parameters = {
            'username': self.user,
            'password': self.password,
            'url': url,
        }

        if title:
            parameters['title'] = title

        if selection:
            parameters['selection'] = selection

        if redirect:
            parameters['redirect'] = redirect

        if jsonp:
            parameters['jsonp'] = jsonp

        try:
            self.response = requests.post(
                Instapyper.urls['add'],
                data=parameters,
            )
        except Exception as e:
            print(e)

        return self.response

    def bookmarks_list(self):
        pass

    def oauth(self, jsonp=None):
        '''
        http://docs.python-requests.org/en/master/user/authentication/#oauth-1-authentication
        '''

        auth = OAuth1(
            'APP_KEY',
            'APP_SECRET',
            'USER_OAUTH_TOKEN',
            'USER_OAUTH_TOKEN_SECRET',
        )

        try:
            self.response = requests.get(
                Instapyper.urls['oauth_access_token'],
                auth=auth,
            )
        except Exception as e:
            print(e)

        return self.response
