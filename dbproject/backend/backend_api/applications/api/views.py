import sys
sys.path.append('../../../MachineLearning')

from django.shortcuts import render
from django.http import JsonResponse
from main.static_functions import get_json_data, json_err, auth_permission_authorized_and_admin_only, auth_permission_authorized_only, json_succ, get_token_from_get_request
import json
import mysql
from mysql.connector import Error
# from MachineLearning.NeutralNetworkPackage.NetworkClass import NeutralNetwork
from machine_learning.neutral_network.NetworkClass import NeutralNetwork
from database_app.database_interface import Database #TODO
from django.views.decorators.http import require_http_methods

# def test_view(request):
#   return JsonResponse({"SuccessMessage": "Urls works"}, status='200')

example_submit_new_application_json = {
  "Name": "Jaunita Adell", 
  "DegreeQualification": "Physics, MPhys", 
  "DegreeLevel": "2:1", 
  "UniversityAttended": "Princeton University", 
  "ALevelQualifications": [
    {"Subject": "Mathematics", "Grade": "A"}, 
    {"Subject": "Japanese ", "Grade": "A"}, 
    {"Subject": "English Language and Literature ", "Grade": "A"}, 
    {"Subject": "Irish ", "Grade": "A"}
  ], 
  "LanguagesKnown": [
    {"Language": "Visual Basic .NET", "Expertise": 9}, 
    {"Language": "Ruby", "Expertise": 9}, 
    {"Language": "C++", "Expertise": 4}, 
    {"Language": "HTML", "Expertise": 6}, 
    {"Language": "Ruby-on-rails", "Expertise": 6}, 
    {"Language": "Executable UML", "Expertise": 8}, 
    {"Language": "UNITY", "Expertise": 4}, 
    {"Language": "TeX", "Expertise": 6}, 
    {"Language": "LaTeX", "Expertise": 6}, 
    {"Language": "High Level Assembly", "Expertise": 9}, 
    {"Language": "Visual Basic", "Expertise": 5}, 
    {"Language": "PostScript", "Expertise": 5}, 
    {"Language": "BASIC", "Expertise": 4}, 
    {"Language": "SQL", "Expertise": 6}, 
    {"Language": "Assembly", "Expertise": 8}, 
    {"Language": "Mathematica", "Expertise": 10}, 
    {"Language": "Perl", "Expertise": 4}, 
    {"Language": "R", "Expertise": 9}
  ], 
  "PreviousEmployment": [
    {"Company": "Dunder Mifflin", "Position": "Senior Architect", "LengthOfEmployment": "3 years 4 months"}
  ], 
  "Skills": [
    {"Skill": "Data Entry", "Expertise": 6}, 
    {"Skill": "Maya", "Expertise": 10}
  ], 
  "Hobbies": [
    {"Name": "Glass blowing", "Interest": 10}
  ],
  "auth_token": "sdaoskdoasjdoajsdojas",
  "job_id": "1"
}

@require_http_methods(["POST"])
def submit_new_application_view(request):
  #getting data + validation of json call
  try:
    data = get_json_data(request)
    name = data['Name']
    deg_qual = data['DegreeQualification']
    deg_lvl = data['DegreeLevel']
    uni_attended = data['UniversityAttended']
    a_lvl_qual = data['ALevelQualifications']
    langs_known = data['LanguagesKnown']
    prev_emp = data['PreviousEmployment']
    skills = data['Skills']
    hobbies = data['Hobbies']
    auth_token = data['auth_token']
    job_id = data['job_id']
  except KeyError as e:
    err = json_err('BAD_API_CALL',
                   'JSON field: {0} missing'.format(str(e)), '')
    return JsonResponse({"errors": [err]}, status='400')
  except json.decoder.JSONDecodeError as e:
    print(str(e))
    err = json_err('INVALID_JSON_SYNTAX', str(e),
                   'Change JSON syntax then retry API call')
    return JsonResponse({"errors": [err]}, status='400')
  
  #processing data
  try:
    if auth_permission_authorized_only(auth_token):
      model = NeutralNetwork()
      db = Database()

      data = json.dumps(data)
      print(data)
      user_id = db.get_user_id_from_token(auth_token)
      job_id = job_id
      response = int((model.create_scores(data, user_id, job_id))[0])
      print("model response: {0}".format(response)) #TODO: only for testing remove
      return json_succ("Model succesfully evaluated application. Reponse stored in database")
    else:
      print("authentication error")
      err = json_err('AUTHORIZATION_REQUIRED', 'User is not logged in', 'Redirect user to login page then get them to retry')
      return JsonResponse({"errors": [err]})
  except mysql.connector.Error as e:
    print("database error")
    err = json_err('UNEXPECTED_DATABASE_ERROR', str(e), 'Retry API call')
    return JsonResponse({"errors": [err]}, status='500')
  except Exception as e:
    print(str(e))
    print("unknown error")
    errOne = json_err("UNKNOWN_SERVER_ERROR", str(e), "Retry API endpoint")
    return JsonResponse({"errors": [errOne]}, status='500')
  
@require_http_methods(["POST"])
def db_submit_feedback_view(request):
  try:
    data = get_json_data(request)
    job_id = data['job_id']
    application_id = data['application_id']
    feedback_given = data['feedback_given'] #TODO: find out if this string or becomes dictionary too
    auth_token = data['auth_token']
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

  #retrain model
  try:
    if auth_permission_authorized_only(auth_token):
      model = NeutralNetwork()
      new_feedback = json.dumps(feedback_given)
      model.retrain_neutral_network(new_feedback, job_id, application_id)
      return json_succ("Model succesfully retrained with new feedback")
    else:
      err = json_err('AUTHORIZATION_REQUIRED', 'User is not logged in', 'Redirect user to login page then get them to retry')
      return JsonResponse({"errors": [err]})
  except mysql.connector.Error as e:
    err = json_err('UNEXPECTED_DATABASE_ERROR', str(e), 'Retry API call')
    return JsonResponse({"errors": [err]}, status='500')
  except Exception as e:
    errOne = json_err("UNKNOWN_SERVER_ERROR", str(e), "Retry API endpoint")
    return JsonResponse({"errors": [errOne]}, status='500')


@require_http_methods(["GET"])
def get_feedback_to_review_view(request):
  try:
    token = get_token_from_get_request(request)  # TODO: test when its not there
    if auth_permission_authorized_and_admin_only(token):
      db = Database()
      applications = db.get_new_interviews_json()
      print(applications)
      
      #filter all applications to ones with given job_id
      # valid_applications = []
      # for app in applications:
      #   if app['user_id'] == job_id:
      #     valid_applications.append(app)
      
      return JsonResponse({"Applications": applications})
    else:
      err = json_err('AUTHORIZATION_OR_ADMIN_AUTHORIZATION_REQUIRED', 'User is not logged in or is not an admin',
                    'Redirect to admin login page then get them to retry')
      return JsonResponse({"errors": [err]})
  except mysql.connector.Error as e:
    err = json_err('UNEXPECTED_DATABASE_ERROR', str(e), 'Retry API call')
    return JsonResponse({"errors": [err]}, status='500')
  # except Exception as e:
  #   errOne = json_err("UNKNOWN_SERVER_ERROR", str(e), "Retry API endpoint")
  #   return JsonResponse({"errors": [errOne]}, status='500')

@require_http_methods(["GET"])
def get_db_application_feedback_user_view(request):
  try:
    token = get_token_from_get_request(request)
    if auth_permission_authorized_only(token):
      db = Database()
      user_id = db.get_user_id_from_token(token)
      print(json.loads(db.get_applications(user_id)))
      return JsonResponse({"applications": json.loads(db.get_applications(user_id))}, status='200')
    else:
      err = json_err('AUTHORIZATION_OR_ADMIN_AUTHORIZATION_REQUIRED', 'User is not logged in or is not an admin',
                     'Redirect to admin login page then get them to retry')
      return JsonResponse({"errors": [err]})
  except mysql.connector.Error as e:
    err = json_err('UNEXPECTED_DATABASE_ERROR', str(e), 'Retry API call')
    return JsonResponse({"errors": [err]}, status='500')
  except Exception as e:
    errOne = json_err("UNKNOWN_SERVER_ERROR", str(e), "Retry API endpoint")
    return JsonResponse({"errors": [errOne]}, status='500')

