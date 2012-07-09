import requests


class HttpApi(object):
    """A minimal wrapper around the LeanKitKanban HTTP API.
       Methods take dictionaries for POST data, returns JSON
    """
    def __init__(self, account_name, username, password, _service_base=None):
        self.account_name = account_name
        self.session = requests.session(auth=(username, password))
        self._service_base = _service_base

    def _get_endpoint(self, name, board_id=''):
        """All LeanKit endpoints include the account name, so this will
        take an endpoint name and construct a leankit endpoint URL with
        the account name included"""
        url_template = \
            ("http://%(account)s.leankitkanban.com/Kanban/"
             "Api/%(board_id)s$%(name)s")
        if name == 'Boards':
            url_template = url_template.replace(
                '%(board_id)s$%(name)s', '%(name)s$%(board_id)s')
        elif board_id != '':
            board_id = ''.join(('Board/', str(board_id)))
        if board_id == '':
            url_template = url_template.replace('$', '')
        else:
            url_template = url_template.replace('$', '/')
        return url_template % \
            {'account': self.account_name, 'name': name, 'board_id': board_id}

    def get_boards(self):
        """Wraps LeanKits' GetBoards method
        See http://support.leankitkanban.com/entries/20264797-get-boards
        """
        endpoint = self._get_endpoint('Boards')
        r = self.session.get(endpoint)
        return r.json

    def get_board_identifiers(self, board_id):
        """Wraps LeanKit's GetBoardIdentifiers
        See http://support.leankitkanban.com/entries/20267921-getboardidentifiers
        """
        endpoint = self._get_endpoint('GetBoardIdentifiers', board_id)
        r = self.session.get(endpoint)
        return r.json

    def get_board(self, board_id):
        """Wraps LeanKit's GetBoard
        See http://support.leankitkanban.com/entries/20267956-get-board
        """
        endpoint = self._get_endpoint('Boards', board_id)
        r = self.session.get(endpoint)
        return r.json

    def get_newer_if_exists(self, board_id, board_version):
        """Wraps LeanKit's GetNewerIfExists
        See http://support.leankitkanban.com/entries/20267966-getnewerifexists
        """
        base_endpoint = self._get_endpoint('BoardVersion', board_id)
        endpoint = '/'.join((
            base_endpoint,
            str(board_version),
            'GetNewerIfExists'))
        r = self.session.get(endpoint)
        return r.json

    def get_board_history_since(self, board_id, board_version):
        """Wraps LeanKit's GetBoardHistorySince
        See http://support.leankitkanban.com/entries/20267971-getboardhistorysince
        """
        base_endpoint = self._get_endpoint('BoardVersion', board_id)
        endpoint = '/'.join((
            base_endpoint,
            str(board_version),
            'GetBoardHistorySince'))
        r = self.session.get(endpoint)
        return r.json

    def get_card(self, board_id, card_id):
        """Wraps LeanKit's GetCard
        See http://support.leankitkanban.com/entries/20267991-getcard
        """
        base_endpoint = self._get_endpoint('GetCard', board_id)
        endpoint = '/'.join((base_endpoint, str(card_id)))
        r = self.session.get(endpoint)
        return r.json
