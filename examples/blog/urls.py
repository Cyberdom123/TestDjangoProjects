from django.urs import path
from . import view

app_name = 'blog'

urlpatterns = [
patch('', view.post_list, name= 'post_list'),
patch('<int:year>/<int:month>/<int:day>/<slug:post>/',
views.post_detail, name= 'post_detail'),

]