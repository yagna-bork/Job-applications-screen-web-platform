import json
from django.http import JsonResponse
import hashlib
from database_app.database_interface import Database

def get_json_data(request):
  return json.loads(request.body.decode("utf-8"))

def json_err(status, message, hint):
  return {"error_status": status, "error_message": message, "error_hint": hint}

def json_succ(msg):
  return JsonResponse({"message": msg}, status='200')

def generate_token(email):
  return hashlib.md5(email.encode()).hexdigest()

def auth_permission_authorized_only(token):
  db = Database()
  return db.does_token_exist(token)

def auth_permission_authorized_and_admin_only(token):
  db = Database()
  return auth_permission_authorized_only(token) and db.is_admin(token)
  
def get_token_from_get_request(request):
  return request.META.get('HTTP_AUTH_TOKEN')
