from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request, 'home.html')
def about(request):
    num=request.GET["enter number"]
    num2=num.split()
    return render(request, 'about.html',{"enter number":'num','num2':num2})
def count(request):
    res = request.GET["enter data"]
    word_list=res.split()
    dictionary= {}
    for i in word_list:
        if i in dictionary:
            dictionary[i]+=1
        else:
            dictionary[i]=1
    sortedlist= sorted(dictionary.items(),key= operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{"enter data":'res','count':len(word_list),'sortedlist':sortedlist})
