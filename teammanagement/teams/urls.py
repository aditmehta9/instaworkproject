
from django.urls import path

from . import views
app_name = 'teams'

urlpatterns = [
    path('', views.ListMemberView.as_view(), name='list_teams'),
    path('addmember', views.AddMemberView.as_view(), name='add_member'),
    path('updatemember/<int:pk>', views.UpdateMemberView.as_view(), name='update_member'),
    path('deletemember/<int:pk>', views.DeleteMemberView.as_view(), name='delete_member'),

]
