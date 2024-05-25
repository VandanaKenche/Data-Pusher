urlpatterns += [
    path('server/incoming_data/', DataHandlerView.as_view(), name='incoming_data'),
]
