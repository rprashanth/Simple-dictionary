from django.http import HttpResponse
from dictionary.models import Wordsense,Meanings,Relate,Synonym,Hypernym,Examples
from django.shortcuts import render
# Create your views here.
def search(request):
    q=Wordsense.objects.all()
    l=len(q)
    a,b=[],[]
    p=round(l/2)
    r=l-p
    i=0
    while i!=p:
        a.append(q[i])
        i=i+1
    i=0
    while i!=r:
        b.append(q[p+i])
        i=i+1
    return render(request,'dictionary/search.html',{'q':q,'a':a,'b':b})


def results(request):
    value=request.POST['w']
    try:
        s=Wordsense.objects.get(word=value)
    except:
        return render(request,'dictionary/notp.html')
    nom=Meanings.objects.all().filter(word_id1=value,wortype='noun')
    noe=Examples.objects.all().filter(wordsense=value,wordtype='noun')
    r=Relate.objects.all().filter(word_id2=value)
    sy=Synonym.objects.all().filter(word_id3=value)
    adm=Meanings.objects.all().filter(word_id1=value,wortype='adverb')
    ade=Examples.objects.all().filter(wordsense=value,wordtype='adverb')
    adjm=Meanings.objects.all().filter(word_id1=value,wortype='adjective')
    adje=Examples.objects.all().filter(wordsense=value,wordtype='adjective')
    verm=Meanings.objects.all().filter(word_id1=value,wortype='verb')
    vere=Examples.objects.all().filter(wordsense=value,wordtype='verb')
    h=Hypernym.objects.all().filter(word_id4=value)
    context={'s':s,'nom':nom,'noe':noe,'r':r,'sy':sy,'adm':adm,'ade':ade,'adjm':adjm,
             'adje':adje,'verm':verm,'vere':vere,'h':h}
    return render(request,'dictionary/results.html',context)

    
