# coding: UTF-8
from django.utils.translation import ugettext as _


class Consts:
    # Django Logger Name (in settings.py)
    LOGGER = 'ars_log'
    LOGMSG_API_ERROR = u'API Error \t{msg}'
    LOGMSG_EXCEPT = '"Exception raised: File "%s", line %s , in %s : %s'

    @staticmethod
    def get_msg_err():
        msg_err = {}
        # Message Common Function
        msg_err['MSG_ERR_0001'] = _('Unexpected error, please contact your system administrator.')
        
        return msg_err
