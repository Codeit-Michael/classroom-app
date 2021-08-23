from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	path('',views.students),
	path('view_student/<int:id>',views.view_student),
	path('add_student/',views.add_student),
	path('remove_student/<int:id>',views.remove_student),
	path('update_student/<int:id>',views.update_student),
	# path('',views.first.as_view()),	# for class based views
]

urlpatterns = format_suffix_patterns(urlpatterns)