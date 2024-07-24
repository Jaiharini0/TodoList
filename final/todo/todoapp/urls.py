from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('list/',views.list,name="list"),
    path('list/index',views.index,name="index"),
    path('planner_today/',views.planner_today,name="planner_today"),
    path('planner_tomorrow/',views.planner_tomorrow,name="planner_tomorrow"),
    path('completed/',views.completed,name="completed"),
    path('planner_today/lists',views.lists,name="lists"),
    path('list/planner_today',views.planner_today,name="planner_today"),
    path('list/lists',views.lists,name="lists"),
    path('list/planner_tomorrow',views.planner_tomorrow,name="planner_tomorrow"),
    path('list/list',views.list,name="list"),
    path('myapp/index',views.index,name="index"),
    path('myapp/list',views.list,name="list"),
    path('myapp/planner_today',views.planner_today,name="planner_today"),
    path('myapp/planner_tomorrow',views.planner_tomorrow,name="planner_tomorrow"),
    path('myapp/completed',views.completed,name="completed"),
    path('planner_today/planner_today',views.planner_today,name="planner_today"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('update/<int:id>',views.update,name="update"),
    path('update/planner_today',views.planner_today,name="planner_today"),
    path('update/list',views.list,name="list"),
]