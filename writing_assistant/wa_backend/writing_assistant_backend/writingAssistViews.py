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
from .models import Prompts, Person, Login, User, TaskOrder, Training, Time
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
                openai.api_key = ''  # openai key
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
        # pwd = data.get('pwd')
        print("signup",data)

    #     credentials = ServiceAccountCredentials.from_json_keyfile_name(
    # auth_json_path, gss_scopes)
    #     gss_client = gspread.authorize(credentials)
        

        print("received name", target_prolific_id)
        # print('received pwd', pwd)

        # user_single_root = os.path.join(single_root, target_prolific_id)
        # if not os.path.exists(user_single_root):
        #     Login.objects.create(name=target_prolific_id)
        #     # 创建以用户名为名称的文件夹
        #     ensure_dir_exists(user_single_root)

        
        taskOrder = [1, 2]
        random.shuffle(taskOrder)
        
        condition = User.objects.count()%3+1
        condition = 2
        User.objects.create(ProlificID=target_prolific_id,condition = condition)
        TaskOrder.objects.create(ProlificID=target_prolific_id,current="0", order1 = taskOrder[0],order2 = taskOrder[1])
        Training.objects.create(ProlificID=target_prolific_id)
        # retry_count = 0
        # while retry_count < 10:  # Retry up to 3 times
        #     try:
        #         sheet = gss_client.open_by_key(spreadsheet_key).worksheet('training')
        #         sheet.append_row([target_prolific_id])
        #         sheet = gss_client.open_by_key(spreadsheet_key).worksheet('task_order')
        #         sheet.append_row([target_prolific_id]+[0]+taskOrder)
        #         sheet = gss_client.open_by_key(spreadsheet_key).worksheet('user')
        #         sheet.append_row([target_prolific_id])
                

        #         prolific_ids = sheet.col_values(1)
        #         target_row_index = prolific_ids.index(target_prolific_id) + 1
        #         condition = target_row_index%3+1
        #         print(condition)
        #         sheet.update_cell(target_row_index,
        #                 2, condition)                
        #         break  # Successful update, break out of the retry loop
        #     except APIError as e:
        #         if e.response.status_code == 429:  # Rate limit error
        #             print("signup: Rate limit encountered, waiting and retrying...")
        #             time.sleep(2)  # Wait for a few seconds before retrying
        #             retry_count += 1
        #         else:
        #             raise  # Re-raise other API errors

        return JsonResponse({'success': 'success','condition':condition,'order1': taskOrder[0],'order2': taskOrder[1]})
        # else:
        #     print('user existed')
            

        #     return JsonResponse({'success': 'success'})
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



# @csrf_exempt
# def uploadGoogleSheetlinguisticStyle(Pid, data, info_or_emotional):
#     credentials = ServiceAccountCredentials.from_json_keyfile_name(
#     auth_json_path, gss_scopes)
#     gss_client = gspread.authorize(credentials)
    

#     # Define the target ProlificID and the new linguistic style value
#     target_prolific_id = Pid
#     new_linguistic_style = data

    
#     retry_count = 0
#     while retry_count < 10:  # Retry up to 3 times
#         try:
#             sheet = gss_client.open_by_key(spreadsheet_key).worksheet('user')    
#             prolific_ids = sheet.col_values(1)
#             print(prolific_ids)
#             target_row_index = prolific_ids.index(target_prolific_id) + 1
#             print(target_row_index)
            
        
#             linguistic_style_column_index = int(info_or_emotional)+1
#             cell_to_update = sheet.cell(
#                 target_row_index, linguistic_style_column_index)
#             cell_to_update.value = new_linguistic_style
#             sheet.update_cell(target_row_index,
#                         linguistic_style_column_index, new_linguistic_style)
#             break  # Successful update, break out of the retry loop
#         except APIError as e:
#             if e.response.status_code == 429:  # Rate limit error
#                 print("uploadGoogleSheetlinguisticStyle: Rate limit encountered, waiting and retrying...")
#                 time.sleep(2)  # Wait for a few seconds before retrying
#                 retry_count += 1
#             else:
#                 raise  # Re-raise other API errors

#     print(f"Linguistic style updated for ProlificID: {target_prolific_id}")

@csrf_exempt
def uploadGoogleSheetMimicTask(Pid, data, post):
    
    try:
        record = User.objects.get(ProlificID=Pid)
    except User.DoesNotExist:
        print("uploadGoogleSheetMimicTask user not existed")

    if post == "1":
        record.main_task_1 = data
        record.save()
    if post == "2":
        record.main_task_2 = data
        record.save()

    # credentials = ServiceAccountCredentials.from_json_keyfile_name(
    # auth_json_path, gss_scopes)
    # gss_client = gspread.authorize(credentials)
    # sheet = gss_client.open_by_key(spreadsheet_key).worksheet('user')

    # target_prolific_id = Pid
    # mimic_output = data
    
    # prolific_ids = sheet.col_values(1)
    # print(prolific_ids)
    # target_row_index = prolific_ids.index(target_prolific_id) + 1
    # print(target_row_index)
    
    # headers = sheet.row_values(1)
    # mimic_output_column = "main_task_"+post
    # mimic_output_column_index = headers.index(mimic_output_column) + 1


    # cell_to_update = sheet.cell(
    #     target_row_index, mimic_output_column_index)
    # cell_to_update.value = mimic_output
    # sheet.update_cell(target_row_index,
    #                   mimic_output_column_index, mimic_output)

    # print(f"Linguistic style updated for ProlificID: {target_prolific_id}")


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
            
        record.save()
        
                    
        # retry_count = 0
        # while retry_count < 10:  # Retry up to 3 times
        #     try:
        #         sheet = gss_client.open_by_key(spreadsheet_key).worksheet('user')

        #         print(target_prolific_id)
        #         prolific_ids = sheet.col_values(1)
        #         mimic_output_row = "main_task_"+post
        #         headers = sheet.row_values(1)

        #         mimic_output_column_index = headers.index(mimic_output_row) + 1
                
                
        #         target_row_index = prolific_ids.index(target_prolific_id) + 1
        #         print(sheet.cell(
        #             target_row_index, mimic_output_column_index).value)
        #         mimic_output = sheet.cell(target_row_index, mimic_output_column_index).value            
        #         break  # Successful update, break out of the retry loop
        #     except APIError as e:
        #         if e.response.status_code == 429:  # Rate limit error
        #             print("get_google_sheet_mimic_task: Rate limit encountered, waiting and retrying...")
        #             time.sleep(2)  # Wait for a few seconds before retrying
        #             retry_count += 1
        #         else:
        #             raise  # Re-raise other API errors
        
        
    
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
            print("uploadGoogleSheetMimicTask user not existed")

        if post == "1":
            record.edited_message_1 = editedText

        if post == "2":
            record.edited_message_2 = editedText
        record.save()        
        # retry_count = 0
        # while retry_count < 10:  # Retry up to 3 times
        #     try:
        #         sheet = gss_client.open_by_key(spreadsheet_key).worksheet('user')
        #         print(target_prolific_id)
        #         prolific_ids = sheet.col_values(1)
        #         print('prolific_ids', prolific_ids)
        #         target_row_index = prolific_ids.index(target_prolific_id) + 1
                
        #         mimic_output_row = "edited_message_"+post
        #         headers = sheet.row_values(1)

        #         print('prolific_ids', headers)
        #         mimic_output_column_index = headers.index(mimic_output_row) + 1       
                
        #         sheet.update_cell(target_row_index, mimic_output_column_index, editedText)            
        #         break  # Successful update, break out of the retry loop
        #     except APIError as e:
        #         if e.response.status_code == 429:  # Rate limit error
        #             print("upload_google_sheet_edited_task: Rate limit encountered, waiting and retrying...")
        #             time.sleep(2)  # Wait for a few seconds before retrying
        #             retry_count += 1
        #         else:
        #             raise  # Re-raise other API errors
        
    
        return JsonResponse({'success': 'success'})

# @csrf_exempt
# def get_google_sheet_linguistic_style(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         target_prolific_id = data.get('pid')
#         condition = data.get('condition')
#         print("get_google_sheet_linguistic_style",target_prolific_id)

#         sheet = gss_client.open_by_key(spreadsheet_key).worksheet('task_order')
#         prolific_ids = sheet.col_values(1)
#         target_row_index = prolific_ids.index(target_prolific_id) + 1
#         row_order = sheet.row_values(target_row_index)
#         sheet = gss_client.open_by_key(spreadsheet_key).worksheet('user')

#         print(target_prolific_id)
#         prolific_ids = sheet.col_values(1)
#         print('prolific_ids', prolific_ids)
#         target_row_index = prolific_ids.index(target_prolific_id) + 1

#         style = sheet.row_values(target_row_index)
#         print("row_order",row_order)
#         if condition!="1":
            
#             return JsonResponse({'condition':style[1],
#                              'current':row_order[1],
#                             'order1': row_order[2],
#                              'order2': row_order[3]})    
        
#         print("style",style)
        

#         return JsonResponse({'condition':style[1],
#                              'info_style': style[2],
#                              'emo_style': style[3],
#                              'current':row_order[1],
#                             'order1': row_order[2],
#                              'order2': row_order[3]})


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
        
        row_order = [record.ProlificID,record.current,record.order1,record.order2]
            
        record.save()
           

        # retry_count = 0
        # while retry_count < 10:  # Retry up to 3 times
        #     try:
        #         sheet = gss_client.open_by_key(spreadsheet_key).worksheet('task_order')
        #         prolific_ids = sheet.col_values(1)
        #         target_row_index = prolific_ids.index(target_prolific_id) + 1
        #         row_order = sheet.row_values(target_row_index)
        #         # sheet = gss_client.open_by_key(spreadsheet_key).worksheet('training')

        #         # print(target_prolific_id)
        #         # prolific_ids = sheet.col_values(1)
        #         # print('prolific_ids', prolific_ids)
        #         # target_row_index = prolific_ids.index(target_prolific_id) + 1

        #         # examples = sheet.row_values(target_row_index)
        #         print("row_order",row_order)       
        #         break  # Successful update, break out of the retry loop
        #     except APIError as e:
        #         if e.response.status_code == 429:  # Rate limit error
        #             print("get_google_sheet_example: Rate limit encountered, waiting and retrying...")
        #             time.sleep(2)  # Wait for a few seconds before retrying
        #             retry_count += 1
        #         else:
        #             raise  # Re-raise other API errors
        
        if condition!="1":
            return JsonResponse({'current':row_order[1],
                            'order1': row_order[2],
                             'order2': row_order[3]})    
        
        # print("examples",examples)
        

        return JsonResponse({
                            # 'example1': examples[1],
                            #  'example2': examples[2],
                            #  'example3': examples[3],
                            #  'example4': examples[4],
                             'current':row_order[1],
                            'order1': row_order[2],
                             'order2': row_order[3]})


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
        
        # retry_count = 0
        # while retry_count < 10:  # Retry up to 3 times
        #     try:
        #         sheet = gss_client.open_by_key(spreadsheet_key).worksheet('task_order')
        #         prolific_ids = sheet.col_values(1)
        #         target_row_index = prolific_ids.index(target_prolific_id) + 1
        #         row_order = sheet.row_values(target_row_index)
        #         print(row_order)
        #         current_column_index=2
        #         sheet.update_cell(target_row_index,
        #                     current_column_index, int(row_order[1])+1)
        #         break  # Successful update, break out of the retry loop
        #     except APIError as e:
        #         if e.response.status_code == 429:  # Rate limit error
        #             print("update_current_task: Rate limit encountered, waiting and retrying...")
        #             time.sleep(2)  # Wait for a few seconds before retrying
        #             retry_count += 1
        #         else:
        #             raise  # Re-raise other API errors

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
            record.main_task_1 = text
        if post == "2":
            record.main_task_2 = text
        
        record.save()

        # retry_count = 0
        # while retry_count < 10:  # Retry up to 3 times
        #     try:
        #         sheet = gss_client.open_by_key(spreadsheet_key).worksheet('user')
        #         prolific_ids = sheet.col_values(1)
        #         target_row_index = prolific_ids.index(target_prolific_id) + 1
        #         row_order = sheet.row_values(target_row_index)
        #         print(row_order)
        #         headers = sheet.row_values(1)
        #         current_row= "main_task_"+post
        #         current_column_index = headers.index(current_row) + 1
        #         sheet.update_cell(target_row_index,
        #                 current_column_index, text)
        #         break  # Successful update, break out of the retry loop
        #     except APIError as e:
        #         if e.response.status_code == 429:  # Rate limit error
        #             print("update_support_message: Rate limit encountered, waiting and retrying...")
        #             time.sleep(2)  # Wait for a few seconds before retrying
        #             retry_count += 1
        #         else:
        #             raise  # Re-raise other API errors

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
        if post == "4":
            record.training_4 = text
        record.save()
        # retry_count = 0
        # while retry_count < 10:  # Retry up to 3 times
        #     try:
        #         sheet = gss_client.open_by_key(spreadsheet_key).worksheet('training')
        #         prolific_ids = sheet.col_values(1)
        #         target_row_index = prolific_ids.index(target_prolific_id) + 1
        #         headers = sheet.row_values(1)
        #         current_row= "training_"+post
        #         current_column_index = headers.index(current_row) + 1
                
                
        #         print("current_column_index",current_column_index)
        #         print("target_row_index",target_row_index)
        #         sheet.update_cell(target_row_index,
        #                 current_column_index, text)
        #         break  # Successful update, break out of the retry loop
        #     except APIError as e:
        #         if e.response.status_code == 429:  # Rate limit error
        #             print("update_training_message: Rate limit encountered, waiting and retrying...")
        #             time.sleep(2)  # Wait for a few seconds before retrying
        #             retry_count += 1
        #         else:
        #             raise  # Re-raise other API errors


        return JsonResponse({'text upload': text})
    

# @csrf_exempt
# def update_time(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         target_prolific_id = data.get('pid')
#         task = data.get('task')
        
#         retry_count = 0
#         while retry_count < 10:  # Retry up to 3 times
#             try:
#                 sheet = gss_client.open_by_key(spreadsheet_key).worksheet('time')
#                 headers = sheet.row_values(1)
#                 header_row_index = headers.index(task) + 1

#                 prolific_ids = sheet.col_values(1)
#                 target_row_index = prolific_ids.index(target_prolific_id) + 1
                
#                 print("time_current_column_index",header_row_index)
#                 print("time_target_row_index",target_row_index)
#                 sheet.update_cell(target_row_index,
#                       header_row_index, time.time())
#                 break  # Successful update, break out of the retry loop
#             except APIError as e:
#                 if e.response.status_code == 429:  # Rate limit error
#                     print("update_time: Rate limit encountered, waiting and retrying...")
#                     time.sleep(2)  # Wait for a few seconds before retrying
#                     retry_count += 1
#                 else:
#                     raise  # Re-raise other API errors
        
#         return JsonResponse({'timp upload': time.time()})
    
@csrf_exempt
def update_time_row(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        target_prolific_id = data.get('pid')
        training_start_1 = data.get('training_start_1')
        training_start_2 = data.get('training_start_2')
        training_start_3 = data.get('training_start_3')
        training_start_4 = data.get('training_start_4')
        training_end_1 = data.get('training_end_1')
        training_end_2 = data.get('training_end_2')
        training_end_3 = data.get('training_end_3')
        training_end_4 = data.get('training_end_4')
        main_task_start_1 = data.get("main_task_start_1")
        main_task_start_2 = data.get("main_task_start_2")
        main_task_end_1 = data.get("main_task_end_1")
        main_task_end_2 = data.get("main_task_end_2")
        editing_end_1 = data.get("editing_end_1")
        editing_end_2 = data.get("editing_end_2")

        print("update_time_row",data)

        Time.objects.create(pid=target_prolific_id,
                        training_start_1=training_start_1,
                        training_start_2=training_start_2,
                        training_start_3=training_start_3,
                        training_start_4=training_start_4,
                        training_end_1=training_end_1,
                        training_end_2=training_end_2,
                        training_end_3=training_end_3,
                        training_end_4=training_end_4,
                        main_task_start_1=main_task_start_1,
                        main_task_start_2=main_task_start_2,
                        main_task_end_1=main_task_end_1,
                        main_task_end_2=main_task_end_2,
                        editing_end_1=editing_end_1,
                        editing_end_2=editing_end_2)
        
        # retry_count = 0
        # while retry_count < 10:  # Retry up to 3 times
        #     try:
                    
        #         sheet = gss_client.open_by_key(spreadsheet_key).worksheet('time_v3')
                
        #         data = [target_prolific_id, 
        #                 training_start_1,	training_start_2,	training_start_3,	training_start_4,
        #                 training_end_1,	training_end_2,	training_end_3,	training_end_4,
        #                 main_task_start_1, main_task_start_2, main_task_end_1, main_task_end_2, editing_end_1, editing_end_2]
                        

        #         sheet.append_row(data)
        #         break  # Successful update, break out of the retry loop
        #     except APIError as e:
        #         if e.response.status_code == 429:  # Rate limit error
        #             print("update_time_row: Rate limit encountered, waiting and retrying...")
        #             time.sleep(2)  # Wait for a few seconds before retrying
        #             retry_count += 1
        #         else:
        #             raise  # Re-raise other API errors


        return JsonResponse({'timp upload': 'success'})