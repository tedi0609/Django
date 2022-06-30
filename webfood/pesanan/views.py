
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello, Kakak, Mau Pesan Apa nih?.")
