class DestinationListView(APIView):
   def get(self, request, account_id):
        account = Account.objects.get(account_id=account_id)
        destinations = Destination.objects.filter(account=account)
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)
