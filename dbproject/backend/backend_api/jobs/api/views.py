from main.static_functions import get_token_from_get_request, auth_permission_authorized_only, json_succ, json_err
from database_app.database_interface import Database
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def get_all_jobs_view(request):
  try:
    token = get_token_from_get_request(request)

    if auth_permission_authorized_only(token):
      db = Database()
      jobs = db.get_jobs()
      return JsonResponse({"jobs": jobs}, status='200')
    else:
      err = json_err('AUTHORIZATION_REQUIRED', 'User is not logged in', 'Redirect user to login page then get them to retry')
      return JsonResponse({"errors": [err]})
  except Exception as e:
    errOne = json_err("UNKNOWN_SERVER_ERROR", str(e), "Retry API endpoint")
    return JsonResponse({"errors": [errOne]}, status='500')


@require_http_methods(["GET"])
def get_all_available_jobs_view(request):
  try:
    token = get_token_from_get_request(request)

    if auth_permission_authorized_only(token):
      db = Database()
      return JsonResponse({"jobs": db.get_jobs_available()}, status='200')
    else:
      err = json_err('AUTHORIZATION_REQUIRED', 'User is not logged in', 'Redirect user to login page then get them to retry')
      return JsonResponse({"errors": [err]})
  except Exception as e:
    errOne = json_err("UNKNOWN_SERVER_ERROR", str(e), "Retry API endpoint")
    return JsonResponse({"errors": [errOne]}, status='500')


@require_http_methods(["GET"])
def get_all_not_available_jobs_view(request):
  try:
    token = get_token_from_get_request(request)

    if auth_permission_authorized_only(token):
      db = Database()
      return JsonResponse({"jobs": db.get_jobs_not_available()}, status='200')
    else:
      err = json_err('AUTHORIZATION_REQUIRED', 'User is not logged in',
                     'Redirect user to login page then get them to retry')
      return JsonResponse({"errors": [err]})
  except Exception as e:
    errOne = json_err("UNKNOWN_SERVER_ERROR", str(e), "Retry API endpoint")
    return JsonResponse({"errors": [errOne]}, status='500')
