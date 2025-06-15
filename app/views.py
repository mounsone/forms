from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserInfo, Contact
from .serializers import UserInfoSerializer, ContactSerializer


@api_view(['GET', 'POST'])
def submit_form(request):
    if request.method == 'POST':
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Form submitted successfully!', 'data': serializer.data},
                status=status.HTTP_201_CREATED
            )
        print(serializer.errors)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET
    users = UserInfo.objects.all()
    serializer = UserInfoSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def contacts(request):
    """
    /api/contacts/ → GET list  |  POST create
    """
    if request.method == 'GET':
        qs = Contact.objects.all()
        serializer = ContactSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'message': 'Form submitted successfully!', 'data': serializer.data},
            status=status.HTTP_201_CREATED
        )
    print(serializer.errors)  
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
