from django.shortcuts import render
from django.views.generic import CreateView
from django.http import JsonResponse
from main.static_functions import get_json_data, json_err, json_succ, generate_token
from database_app.database_interface import Database
from django.views.decorators.http import require_http_methods
import json
from django.http import HttpResponse

@require_http_methods(["POST"])
def login_view(request):
  try:
    data = get_json_data(request)
    email = data['email']
    password = data['password']
  except KeyError as e:
    err = json_err('BAD_API_CALL',
                   'JSON field: {0} missing'.format(str(e)), '')
    return JsonResponse({"errors": [err]}, status='400')
  except json.decoder.JSONDecodeError as e:
    err = json_err('INVALID_JSON_SYNTAX', str(e),
                   'Change JSON syntax then retry API call')
    return JsonResponse({"errors": [err]}, status='400')
  except Exception as e:
    errOne = json_err("UNKNOWN_SERVER_ERROR", str(e), "Retry API endpoint")
    return JsonResponse({"errors": [errOne]}, status='500')

  try:
    db = Database()
    if db.loginVerification(email, password):
      token = db.get_token(email, False)
      # response_data = {
      #     "auth_token": token
      # }
      # response = HttpResponse(json.dumps(response_data), status=200, content_type="application/json")
      # response["Access-Control-Allow-Origin": "*"]
      # return response

      # response = JsonResponse({
      #   "auth_token": token
      # }, status='200')
      # response["Access-Control-Allow-Origin"] = "*"
      # response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
      # response["Access-Control-Max-Age"] = "1000"
      # response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
      # return response
      
      return JsonResponse({
        "auth_token": token
      }, status='200')
    else:
      err = json_err('LOGIN_DETAILS_INVALID', '', '')
      return JsonResponse({"errors" : [err]}, status='400')
  except:
    errOne = json_err("UNKNOWN_SERVER_ERROR", "Database connection caused this error", "Retry API endpoint") #TODO: set status
    return JsonResponse({"errors": [errOne]}, status='500')

@require_http_methods(["POST"])
def register_view(request):
  try:
    data = get_json_data(request)
    firstname = data['firstname']
    lastname = data['lastname']
    email = data['email']
    password = data['password']
  except KeyError as e:
    err = json_err('BAD_API_CALL',
                   'JSON field: {0} missing'.format(str(e)), '')
    return JsonResponse({"errors": [err]}, status='400')
  except json.decoder.JSONDecodeError:
    err = json_err('INVALID_JSON_SYNTAX', '', 'Change JSON syntax then retry API call')
    return JsonResponse({"errors": [err]}, status='400')
    
  #TODO: valid data

  try:
    db = Database()
    db.createUser(firstname, lastname, email, password)
    token = generate_token(email)
    db.insert_into_tokens(email, token, False)
    return json_succ('User successfully registered')
  except KeyError as e:
    err = json_err('BAD_API_CALL',
                   'JSON field: {0} missing'.format(str(e)), '')
    return JsonResponse({"errors": [err]}, status='400')
  except Exception as e:
    err = json_err('UNEXPECTED_SERVER_ERROR', str(e), 'Retry API call')
    return JsonResponse({"errors": [err]}, status='500')

@require_http_methods(["POST"])
def register_admin_view(request):
  #getting data from request
  try:
    data = get_json_data(request)
    email = data['email']
    password = data['password']
    key = int(data['key'])
  except KeyError as e:
    err = json_err('BAD_API_CALL',
                   'JSON field: {0} missing'.format(str(e)), '')
    return JsonResponse({"errors": [err]}, status='400')
  except json.decoder.JSONDecodeError:
    err = json_err('INVALID_JSON_SYNTAX', '',
                   'Change JSON syntax then retry API call')
    return JsonResponse({"errors": [err]}, status='400')
  

  #processing request
  try:
    db = Database()
    if db.check_key(key):
      db = Database()
      if db.create_admin(email, password):
        token = generate_token(email)
        db.insert_into_tokens(email, token, True)
        return json_succ('Admin successfully registered')
      else:
        err = json_err(
            'INVALID_ADMIN_REGISTER_DETAILS', 'Email already used or invalid data types for field', 'Retry register with differnet values')
        return JsonResponse({"errors": [err]}, status='400')
    else:
      err = json_err('INVALID_KEY', 'Key entered is an invalid value', 'Retry with a different key')
      return JsonResponse({"errors": [err]}, status='400')
  except Exception as e:
    err = json_err('UNEXPECTED_SERVER_ERROR', str(e), 'Retry API call')
    return JsonResponse({"errors": [err]}, status='500')

@require_http_methods(["POST"])
def login_admin_view(request):
  #getting data from request
  try:
    data = get_json_data(request)
    email = data['email']
    password = data['password']
  except KeyError as e:
    err = json_err('BAD_API_CALL',
                   'JSON field: {0} missing'.format(str(e)), '')
    return JsonResponse({"errors": [err]}, status='400')
  except json.decoder.JSONDecodeError:
    err = json_err('INVALID_JSON_SYNTAX', '',
                   'Change JSON syntax then retry API call')
    return JsonResponse({"errors": [err]}, status='400')
  except Exception as e:
    errOne = json_err("UNKNOWN_SERVER_ERROR", str(e), "Retry API endpoint")
    return JsonResponse({"errors": [errOne]}, status='500')

  #processing request
  try:
    db = Database()
    if db.validate_admin(email, password):
      token = db.get_token(email, True)
      return JsonResponse({"auth_token": token}, status='200')
    else:
      err = json_err('ADMIN_DETAILS_INVALID', 'Details entered are invalid for an admin account', 'Retry login or login as a normal user')
      return JsonResponse({"errors": [err]}, status='400')
  except Exception:
    err = json_err('UNEXPECTED_SERVER_ERROR',
                   'Internal database error', 'Retry API call')
    return JsonResponse({"errors": [err]}, status='500')

