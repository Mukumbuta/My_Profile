from rest_framework.response import Response 
from rest_framework.decorators import api_view


@api_view(['GET'])
def profile_details(request):
    if request.method == 'GET':
        data = {
            "slackUsername": "Emmanuel Simasiku",
            "backend": True,
            "age": 30,
            "bio": "A passionate Software ddeveloper with a passionate to build programs that expedite the efficiency and effectiveness of organizatiomnal success. During my free time, I paint or watch movies"
            
        }

        return Response(data)