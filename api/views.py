from rest_framework import generics, permissions
from .models import User, Contact, Spam
from .serializers import UserSerializer, ContactSerializer, SpamSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # for registering users we don't have to worry about authentication as mentioned in the problem statement

class SearchView(generics.ListAPIView):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return Contact.objects.filter(name__icontains=query).distinct()

class SearchByPhoneView(generics.ListAPIView):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        phone_number = self.request.query_params.get('phone_number', '')
        return Contact.objects.filter(phone_number=phone_number).distinct()

class SpamView(generics.CreateAPIView):
    queryset = Spam.objects.all()
    serializer_class = SpamSerializer
    permission_classes = [IsAuthenticated]

class SpamLikelihoodView(generics.RetrieveAPIView):
    queryset = Spam.objects.all()
    serializer_class = SpamSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        phone_number = self.kwargs['phone_number']
        return Spam.objects.get(phone_number=phone_number)
