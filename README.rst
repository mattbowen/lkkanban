LKKanban: LeanKitKanban's API for Python
========================================

LKKanban aspires to make it easy to interact with LeanKitKanban via python.
Unlike other python LeanKit libraries, it is permissively licenses (it uses
ISC). Although it aspires to provide a pythonic API, right now it is just a
simple wrapper around the HTTP API, using Kenneth Reitz's excellent
`Requests <http://docs.python-requests.org/en/latest/index.html>`_. In fact,
it currently only gets some data -- it cannot update a board. That should
change soon though. See lkkanban.http_api.HttpApi for which endpoints are
currently wrapped, until they all are (at which point this sentence will
go away).

Using the HTTP API wrapper looks like this.

::
    >>> from lkkanban.httpapi import HttpApi
    >>> api = HttpApi('account', 'user@example.com', 'password')
    >>> api.get_boards()
    {u'ReplyText': u'Board(s) successfully retrieved.', u'ReplyCode': 200,
    u'ReplyData': [[{u'BreakoutBoards': None, u'Description': u'', u'Title':
    u'Our Board', u'DrillThroughBoards': [], u'IsBreakoutBoard': False,
    u'ParentId': 0, u'IsArchived': False, u'CreationDate': u'20/01/2012',
    'Id': 10000000}]]

API method names follow the `Lean Kit docs
<http://support.leankitkanban.com/forums/20153741-api>`_, but with the
CamelCase method names converted to PEP8 compliant names (so
AddCardWithWipOverride becomes add_card_with_wip_override).

All methods return JSON.

Any method that should post takes a dictionary with the request body, with all
names following LeanKit's docs.

Developed by `Matt Bowen <http://www.mattbowen.net>`_.