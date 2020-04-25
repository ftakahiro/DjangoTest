from django.urls      import path
from .                import views

urlpatterns=[
    path('',views.index,name='index'),
    path('<int:note_id>',views.detail,name='detail'),
    path('edit/<int:note_id>',views.edit),
    path('delete/<int:note_id>',views.delete),
    path('create/',views.create),
]