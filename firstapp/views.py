from django.shortcuts import render

# Create your views here.
# render함수를 이용해 파일이 어떻게 열리는지 설정

def index(request):
    return render(request, 'index.html')