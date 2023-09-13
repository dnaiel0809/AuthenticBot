"""writing_assistant_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from writing_assistant_backend import writingAssistViews
def trigger_error(request):
  division_by_zero = 1 / 0
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', writingAssistViews.signup),
    path('login/', writingAssistViews.login),
    path('writing_assistant/', writingAssistViews.writing_assistant),
    # path('writing_mimic/', writingAssistViews.writing_mimic),
    path('writing_regeneration/', writingAssistViews.writing_regeneration),
    # path('save_prompt/', writingAssistViews.save_prompt),
    # path('get_prompt/', writingAssistViews.get_prompt),
    # path('delete_prompt/', writingAssistViews.delete_prompt),
    path('text/', writingAssistViews.text),
    # path('get_google_sheet_linguistic_style/', writingAssistViews.get_google_sheet_linguistic_style),
    path('update_current_task/', writingAssistViews.update_current_task),        
    path('get_google_sheet_mimic_task/', writingAssistViews.get_google_sheet_mimic_task),
    path('upload_google_sheet_edited_task/', writingAssistViews.upload_google_sheet_edited_task),                
    path('update_support_message/', writingAssistViews.update_support_message),             
    path('update_training_message/', writingAssistViews.update_training_message),             
    # path('update_time/', writingAssistViews.update_time),             
    path('update_time_row/', writingAssistViews.update_time_row),      
    path('get_google_sheet_example/', writingAssistViews.get_google_sheet_example),      
    path('sentry-debug/', trigger_error),
    
    
            

    
]

