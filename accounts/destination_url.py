urlpatterns += [
    path('accounts/<account_id>/destinations/', DestinationListView.as_view(), name='destination_list'),
]
