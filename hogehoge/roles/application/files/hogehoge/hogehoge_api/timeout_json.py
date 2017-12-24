# -*- coding:utf-8 -*-
import json
from django.views.decorators.cache import cache_control
from django.http import HttpResponse

########################################
# Timeout Error
########################################
@cache_control(no_cache=True, no_store=True, must_revalidate=True, proxy_revalidate=True, private=True)
def index(request):
    # Format error message as JSON
    error_msg = {"Error": True, "timeout": 1, "error_msg": 'Session timeout. Please log in again.'}
    j = json.dumps(error_msg, ensure_ascii=False)
    return HttpResponse(j, status=401, content_type="application/json; charset=utf-8")

