from django.urls import path

from programs.views import (ProgramslView, ProgramShowView, ProgramRemoveView, ProgramItemsAddView,
                            ProgramItemsEditView, ProgramStartAddView, ProgramStartEditView)

urlpatterns = [
    path('', ProgramslView.as_view(), name='programs'),
    path('remove/<int:pr_id>/', ProgramRemoveView.as_view(), name='program-remove'),
    path('edit/<int:pr_id>/', ProgramShowView.as_view(), name='program-edit'),

    path('start_add/<int:pr_id>/', ProgramStartAddView.as_view(), name='program-start-add'),
    path('start_edit/<int:pr_id>/<int:st_id>/', ProgramStartEditView.as_view(), name='program-start-edit'),

    path('item_add/<int:pr_id>/', ProgramItemsAddView.as_view(), name='program-item-add'),
    path('item_edit/<int:pr_id>/<int:it_id>/', ProgramItemsEditView.as_view(), name='program-item-edit'),
]
