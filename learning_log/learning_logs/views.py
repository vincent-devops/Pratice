from django.shortcuts import render


# Create your views here.
# 在这里创建视图
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')
