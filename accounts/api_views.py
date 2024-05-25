import json
import requests

class DataHandlerView(APIView):
    def post(self, request):
        secret_token = request.META.get('HTTP_CL_X_TOKEN')
        if not secret_token:
            return Response({'error': 'Un Authenticate'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            account = Account.objects.get(app_secret_token=secret_token)
        except Account.DoesNotExist:
            return Response({'error': 'Un Authenticate'}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        for destination in account.destination_set.all():
            url = destination.url
            headers = destination.headers.copy()
            headers['Content-Type'] = 'application/json'
            if destination.http_method == 'GET':
                url += '?' + json.dumps(data)
                requests.get(url, headers=headers)
            else:
                requests.post(url, data=json.dumps(data), headers=headers)

        return Response({'message': 'Data sent to all destinations'})
