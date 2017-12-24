# -*- coding:utf-8 -*-
import json
import logging
import traceback
import sys
from django.http import HttpResponse
from ncom_ars.common.consts import Consts

########################################
# JSON Exception class
########################################
class ApiException(Exception):
    logger = None
    _message = ''
    
    ########################################
    # Constructor
    ########################################
    def __init__(self, m):
        Exception.__init__(self, m.encode("utf8"))
        self.logger = logging.getLogger(Consts.LOGGER)
        self.logger.info("API Error")
        self._message = m

    ########################################
    # Show Error message as JSON
    ########################################
    def showError(self, request):
        # Format error message as JSON
        error_msg = {"Error": True, "error_msg": self._message}
        j = json.dumps(error_msg, ensure_ascii=False)
        # Put traceback to log
        #tb = traceback.format_exc(sys.exc_info()[2]).decode('utf-8')
        tb = traceback.format_exc()
        self.logger.info(tb)
        # Return
        return HttpResponse(j, status=400, content_type="application/json; charset=utf-8")

