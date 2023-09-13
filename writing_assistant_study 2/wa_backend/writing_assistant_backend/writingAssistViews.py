"""
 @file: writingAssistViews.py
 @Time    : 2023/7/12
 @Author  : Peinuan qin
 """

import json
import os

import openai
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Login, User, TaskOrder, Training, Time, ExperienceAndAttitude
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import random
import time  
from gspread.exceptions import APIError


single_root = os.path.join(
    settings.BASE_DIR, 'writing_assistant_backend/single')

auth_json_path = os.path.join(os.path.abspath(
    os.getcwd()), 'writing_assistant_backend/authenticweb-ec067e1b5436.json')


credentials = ServiceAccountCredentials.from_json_keyfile_name(
        auth_json_path, gss_scopes)
gss_client = gspread.authorize(credentials)

@csrf_exempt
def writing_assistant(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get('prompt')
        model = data.get('model')
        user = data.get('user')
        post = data.get('post')
        retry_count = 0
        while retry_count < 10: 
            retry_count+=1
            try:
                openai.api_key = ''  # openai key
                print("prompt", prompt)
                response = openai.ChatCompletion.create(
                    model=f"{model}",
                    messages=[
                        {"role": "user", "content": f"{prompt}"},
                    ],
                    request_timeout=90,
                    temperature=0.01,
                )
                response_content = response.choices[0].message.content
                uploadGoogleSheetMimicTask(user,response_content,post)
                # print("content", response_content)
                return JsonResponse({
                    "content": response_content
                })
            except openai.error.Timeout as e:
            #Handle timeout error, e.g. retry or log
                print(f"OpenAI API request timed out: {e}")
                pass
            except openai.error.APIError as e:
            #Handle API error, e.g. retry or log
                print(f"OpenAI API returned an API Error: {e}")
                pass
            except openai.error.APIConnectionError as e:
            #Handle connection error, e.g. check network or log
                print(f"OpenAI API request failed to connect: {e}")
                pass
            except openai.error.InvalidRequestError as e:
            #Handle invalid request error, e.g. validate parameters or log
                print(f"OpenAI API request was invalid: {e}")
                pass
            except openai.error.AuthenticationError as e:
            #Handle authentication error, e.g. check credentials or log
                print(f"OpenAI API request was not authorized: {e}")
                pass
            except openai.error.PermissionError as e:
            #Handle permission error, e.g. check scope or log
                print(f"OpenAI API request was not permitted: {e}")
                pass
            except openai.error.RateLimitError as e:
            #Handle rate limit error, e.g. wait or log
                print(f"OpenAI API request exceeded rate limit: {e}")
                pass
        else:
            return JsonResponse({
                'content': "error"
            })




@csrf_exempt
def writing_regeneration(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get('prompt')
        model = data.get('model')
        retry_count = 0
        while retry_count < 10: 
            retry_count+=1
            try:
                openai.api_key = ''  # openai gpt key
                print("backend", prompt)
                response = openai.ChatCompletion.create(
                    model=f"{model}",
                    messages=[
                        {"role": "user", "content": f"{prompt}"},
                    ],
                    request_timeout=90,
                    temperature=0.001,
                )
                response_content = response.choices[0].message.content
                print(response_content)
                return JsonResponse({
                    "content": response_content
                })
            except openai.error.Timeout as e:
            #Handle timeout error, e.g. retry or log
                print(f"OpenAI API request timed out: {e}")
                pass
            except openai.error.APIError as e:
            #Handle API error, e.g. retry or log
                print(f"OpenAI API returned an API Error: {e}")
                pass
            except openai.error.APIConnectionError as e:
            #Handle connection error, e.g. check network or log
                print(f"OpenAI API request failed to connect: {e}")
                pass
            except openai.error.InvalidRequestError as e:
            #Handle invalid request error, e.g. validate parameters or log
                print(f"OpenAI API request was invalid: {e}")
                pass
            except openai.error.AuthenticationError as e:
            #Handle authentication error, e.g. check credentials or log
                print(f"OpenAI API request was not authorized: {e}")
                pass
            except openai.error.PermissionError as e:
            #Handle permission error, e.g. check scope or log
                print(f"OpenAI API request was not permitted: {e}")
                pass
            except openai.error.RateLimitError as e:
            #Handle rate limit error, e.g. wait or log
                print(f"OpenAI API request exceeded rate limit: {e}")
                pass
    else:
        return JsonResponse({
            'content': "error"
        })



@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        target_prolific_id = data.get('name')
        condition = data.get('condition')
    
        print("signup",data)

    
        print("received name", target_prolific_id)
        

        
        taskOrder = [1, 2, 3]
        random.shuffle(taskOrder)
        
        # condition = User.objects.count()%2+2
        # condition = 6
        User.objects.create(ProlificID=target_prolific_id,condition = condition)
        TaskOrder.objects.create(ProlificID=target_prolific_id,current="0", order1 = taskOrder[0],order2 = taskOrder[1],order3 = taskOrder[2])
        Training.objects.create(ProlificID=target_prolific_id)
        ExperienceAndAttitude.objects.create(ProlificID=target_prolific_id)
    
        return JsonResponse({'success': 'success','condition':condition,'order1': taskOrder[0],'order2': taskOrder[1],'order3': taskOrder[2]})
    else:
        return JsonResponse({'error': 'error'})

@csrf_exempt
def ensure_dir_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
        print("successfully create path:", dir_path)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        # pwd = data.get('pwd')

        print("received name", name)
        # print('received pwd', pwd)

        new_user = Login.objects.create(name=name)
        print('login', new_user)
        Login.objects.all()
        if new_user:
            return JsonResponse({'success': 'success'})
    else:
        return JsonResponse({'error': 'error'})


@csrf_exempt
def text(request):
    if request.method == 'POST':
        return JsonResponse({'success': 'success'})
    else:
        return JsonResponse({'error2': 'error2'})



@csrf_exempt
def uploadGoogleSheetMimicTask(Pid, data, post):
    
    try:
        record = User.objects.get(ProlificID=Pid)
    except User.DoesNotExist:
        print("uploadGoogleSheetMimicTask user not existed")
    print("uploadGoogleSheetMimicTask:", data)
    print("uploadGoogleSheetMimicTask", post)
    if post == "1":
        if not record.main_task_1:
            record.main_task_1 = data
            record.save()
    if post == "2":
        if not record.main_task_2:
            record.main_task_2 = data
            record.save()
    if post == "3":
        if not record.main_task_3:
            record.main_task_3 = data
            record.save()



@csrf_exempt
def get_google_sheet_mimic_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        target_prolific_id = data.get('pid')
        post=data.get('post')
        print("get_google_sheet_mimic_task",data)
        if post == "1":
            try:
                record = User.objects.get(ProlificID=target_prolific_id)
            except User.DoesNotExist:
                print("get_google_sheet_mimic_task not find pid")
            mimic_output = record.main_task_1

        if post == "2":
            try:
                record = User.objects.get(ProlificID=target_prolific_id)
            except User.DoesNotExist:
                print("get_google_sheet_mimic_task not find pid")
            mimic_output = record.main_task_2
        
        if post == "3":
            try:
                record = User.objects.get(ProlificID=target_prolific_id)
            except User.DoesNotExist:
                print("get_google_sheet_mimic_task not find pid")
            mimic_output = record.main_task_3
            
        record.save()
        
                    
        
        
    
        return JsonResponse({'mimic_output': mimic_output})

@csrf_exempt    
def upload_google_sheet_edited_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        target_prolific_id = data.get('pid')
        editedText = data.get('editedText')
        post=data.get('post')
        
        # print("upload_google_sheet_edited_task",data)

        try:
            record = User.objects.get(ProlificID=target_prolific_id)
        except User.DoesNotExist:
            print("upload_google_sheet_edited_task user not existed")

        if post == "1":
            record.edited_message_1 = editedText

        if post == "2":
            record.edited_message_2 = editedText
        
        if post == "3":
            record.edited_message_3 = editedText
        record.save()        
        
        
    
        return JsonResponse({'success': 'success'})
    
    

@csrf_exempt    
def upload_experience_thoughts_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        target_prolific_id = data.get('pid')
        exprience = data.get('exprience')
        thought = data.get('thought')
        post=data.get('post')
        

        try:
            record = ExperienceAndAttitude.objects.get(ProlificID=target_prolific_id)
        except ExperienceAndAttitude.DoesNotExist:
            print("upload_experience_thoughts_task user not existed")

        if post == "1":
            record.experience_1 = exprience
            record.thought_1 = thought

        if post == "2":
            record.experience_2 = exprience
            record.thought_2 = thought
        
        if post == "3":
            record.experience_3 = exprience
            record.thought_3 = thought

        record.save()        
        
        
    
        return JsonResponse({'success': 'success'})


@csrf_exempt
def get_google_sheet_example(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        target_prolific_id = data.get('pid')
        condition = data.get('condition')
        print("get_google_sheet_example",target_prolific_id)


        
        try:
            record = TaskOrder.objects.get(ProlificID=target_prolific_id)
        except User.DoesNotExist:
            print("get_google_sheet_example not find pid")
        
        row_order = [record.ProlificID,record.current,record.order1,record.order2,record.order3]
            
        record.save()
           

        
        
        if condition!="1":
            return JsonResponse({'current':row_order[1],
                            'order1': row_order[2],
                             'order2': row_order[3],
                             'order3': row_order[4]})    
        
        # print("examples",examples)
        

        return JsonResponse({
                            # 'example1': examples[1],
                            #  'example2': examples[2],
                            #  'example3': examples[3],
                            #  'example4': examples[4],
                             'current':row_order[1],
                            'order1': row_order[2],
                             'order2': row_order[3],
                             'order3': row_order[4]})


@csrf_exempt
def update_current_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        target_prolific_id = data.get('pid')
        print("update_current_task",data)

        try:
            record = TaskOrder.objects.get(ProlificID=target_prolific_id)
        except TaskOrder.DoesNotExist:
            print("update_current_task not exist")
            

        
        record.current = int(record.current)+1
        print("record.current",int(record.current)+1)
        record.save()
        
        

        return JsonResponse({'success': 'success'})


    
@csrf_exempt
def update_support_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        target_prolific_id = data.get('pid')
        post = data.get('post')
        text = data.get('text')
        print("update_support_message",data)
        try:
            record = User.objects.get(ProlificID=target_prolific_id)
        except User.DoesNotExist:
            print("update_support_message not exist")
            

        if post == "1":
            if not record.main_task_1:
                record.main_task_1 = text
        if post == "2":
            if not record.main_task_2:        
                record.main_task_2 = text  
        if post == "3":
            if not record.main_task_3:
                record.main_task_3 = text
        
        record.save()

        

        return JsonResponse({'text upload': text})

        
@csrf_exempt
def update_training_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        target_prolific_id = data.get('pid')
        post = data.get('post')
        text = data.get('text')
        # print("update_training_message",data)
        try:
            record = Training.objects.get(ProlificID=target_prolific_id)
        except Training.DoesNotExist:
            print("update_training_message not exist")
            
        # print("post",post)
        # print("text",text)
        if post == "1":
            record.training_1 = text
        if post == "2":
            record.training_2 = text
        if post == "3":
            record.training_3 = text

        record.save()


        return JsonResponse({'text upload': text})
    

    
@csrf_exempt
def update_time_row(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        target_prolific_id = data.get('pid')
        training_start_1 = data.get('training_start_1')
        training_start_2 = data.get('training_start_2')
        training_start_3 = data.get('training_start_3')
        training_end_1 = data.get('training_end_1')
        training_end_2 = data.get('training_end_2')
        training_end_3 = data.get('training_end_3')
        main_task_start_1 = data.get("main_task_start_1")
        main_task_start_2 = data.get("main_task_start_2")
        main_task_start_3 = data.get("main_task_start_3")
        main_task_end_1 = data.get("main_task_end_1")
        main_task_end_2 = data.get("main_task_end_2")
        main_task_end_3 = data.get("main_task_end_3")
        editing_end_1 = data.get("editing_end_1")
        editing_end_2 = data.get("editing_end_2")
        editing_end_3 = data.get("editing_end_3")
        editing_start_1 = data.get("editing_start_1")
        editing_start_2= data.get("editing_start_2")
        editing_start_3= data.get("editing_start_3")
        question_start_1= data.get("question_start_1")
        question_start_2= data.get("question_start_2")
        question_start_3= data.get("question_start_3")
        question_end_1= data.get("question_end_1")
        question_end_2= data.get("question_end_2")
        question_end_3= data.get("question_end_3")
          
        
        print("update_time_row",data)

        Time.objects.create(pid=target_prolific_id,
                        training_start_1=training_start_1,
                        training_start_2=training_start_2,
                        training_start_3=training_start_3,
                        
                        training_end_1=training_end_1,
                        training_end_2=training_end_2,
                        training_end_3=training_end_3,
                        
                        main_task_start_1=main_task_start_1,
                        main_task_start_2=main_task_start_2,
                        main_task_start_3=main_task_start_3,
                        main_task_end_1=main_task_end_1,
                        main_task_end_2=main_task_end_2,
                        main_task_end_3=main_task_end_3,
                        editing_end_1=editing_end_1,
                        editing_end_2=editing_end_2,
                        editing_end_3=editing_end_3,
                        editing_start_1=editing_start_1,
                        editing_start_2=editing_start_2,
                        editing_start_3=editing_start_3,
                        question_start_1 = question_start_1,
                        question_start_2 = question_start_2,
                        question_start_3 = question_start_3,
                        question_end_1= question_end_1,
                        question_end_2=question_end_2,
                        question_end_3=question_end_3,)
        

        return JsonResponse({'timp upload': 'success'})