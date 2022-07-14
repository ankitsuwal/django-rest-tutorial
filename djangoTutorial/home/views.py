from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializer import TodoSerializer


# Create your views here.
class Home(APIView):

    def get(self, request):
        print("\nHome: Get" * 3)
        return Response({'status': 200,
                         'message': 'Yes! Django rest framework is working !!!',
                         'method': 'GET'})

    def post(self, request):
        print("\nHome: Post" * 3)
        return Response({'status': 200,
                         'message': 'Yes! Django rest framework is working !!!',
                         'method': 'POST'})


class ToDo(APIView):

    def post(self, request):
        try:
            data = request.data
            print("data: ", data)
            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 200, 'message': 'Valid Serializer.!!!', 'method': 'POST',
                                 'data': serializer.data})

            return Response({'status': 401, 'message': 'invalid data.!!!', 'method': 'POST',
                             'data': serializer.errors})
        except Exception as err:
            print(err)
        return Response({'status': 400, 'message': 'something went wrong.!!!', 'method': 'POST'})

    def get(self, request):
        todo_obj = Todo.objects.all()
        serializer = TodoSerializer(todo_obj, many=True)
        return Response({'status': 200, 'message': 'Todo model data.', 'method': 'GET', 'data': serializer.data})
