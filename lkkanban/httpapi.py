import requests


class HttpApi(object):
    """A minimal wrapper around the LeanKitKanban HTTP API."""
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
