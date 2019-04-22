from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')


def count(request):
    data=request.GET['Fulltextarea']
    word_list=data.split()
    list_length=len(word_list)
    word_dict={}
    for word in word_list:
        if word in word_dict:
            word_dict[word] +=1
        else:
            word_dict[word] =1
    sort_list = sorted(word_dict.items(), key=operator.itemgetter(1),reverse=True)
    return render(request, 'count.html',{'fulltext':data, 'words_count':list_length,'word_dict':sort_list})




def about_us(request):
    return render(request,'about.html')