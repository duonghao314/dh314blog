from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from blog.models import Category, Article
from Controller import Functions, Email
from blog import forms

# Create your views here.
def index(request):
    currrentPage = request.GET.get('page')
    if currrentPage is None:
        currrentPage = 1



    categories = Category.objects.all()

    intHeadArt = (int(currrentPage) -1)*7
    intBegin = intHeadArt+1
    intEnd = intHeadArt+7

    countPage = int(len(Article.objects.all())/7) + 1
    print(countPage)
    headingArticle = Article.objects.all().order_by('-id')[intHeadArt]
    headingArticle.artContent = Functions.cutContent(headingArticle.artContent)
    try:
        articles = Article.objects.all().order_by('-id')[intBegin:intEnd]
    except BaseException:
        articles = Article.objects.all().order_by('-id')[intBegin:]

    for art in articles:
        art.artContent = Functions.cutContent(art.artContent)
    return render(request, 'blog/index.html', {'cats': categories, 'arts': articles, 'headArt': headingArticle, 'currentPage':currrentPage,'countPage':range(1,countPage+1),'maxPage':countPage})


def cat(request, catName):
    categories = Category.objects.all()
    whereIsTheCat = Category.objects.get(catKeyWord=catName).id
    nameCurrentCat = Category.objects.get(catKeyWord=catName).catName
    articles = Article.objects.filter(artCat=whereIsTheCat)

    for art in articles:
        art.artContent = Functions.cutContent(art.artContent)
    return render(request, 'blog/cat.html', {'cats': categories, 'arts': articles, 'currentCat': nameCurrentCat})


def art(request, url, id):


    categories = Category.objects.all()
    categoriesRanked = Category.objects.all().order_by('-catViews')
    try:
        artWhereID = Article.objects.get(id=id)
        artWhereID.artViews += 1
        catOfArt = Category.objects.get(id=artWhereID.artCat.id)
        catOfArt.catViews += 1
        catOfArt.save()
        artWhereID.save()
    except BaseException:
        print(BaseException.__str__())

    return render(request, 'blog/art.html', {'cats': categories, 'art': artWhereID, 'catsRanked': categoriesRanked})

@csrf_exempt
def uploadCmnt(request):
    categories = Category.objects.all()
    if request.method == 'POST':

        form = forms.CommentForms(request.POST)

        if form.is_valid:
            comment = form['replyFormComment'].value()
            name = form['replyFormName'].value()
            fromEmail = form['replyFormEmail'].value()
            email = Email.EMail()
            print(email.sendMail(name,comment,fromEmail))
            imgURL = 'img/thankyou.jpg'
        else:
            imgURL = 'img/sorry.jpg'
        return render(request, 'blog/return.html', {'cats': categories, 'img': imgURL})