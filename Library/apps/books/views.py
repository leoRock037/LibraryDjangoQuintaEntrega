from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from apps.books.models import CategoryBook, News, Publisher, Author,Book,Contact
from apps.books.forms import LoginForm,addNewsForm,addPublisherForm,addAuthorForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect



def home(request):
	cat = Book.objects.filter(status = True)
	ctx = {"category":cat}
	return render_to_response('home.html',ctx,context_instance = RequestContext(request))


def index_books(request):
	book = Book.objects.filter(status = True)
	cat = CategoryBook.objects.filter(status = True)
	ctx = {"books":book,"category":cat}
	return render_to_response('index_books.html',ctx,context_instance = RequestContext(request))
	
	
def book(request,id_book):
	book_id = get_object_or_404(Book,pk=id_book)
	book = Book.objects.filter(status = True)
	cat = CategoryBook.objects.filter(status = True)
	return render_to_response('book.html',{'book':book_id,'books':book,"category":cat},context_instance = RequestContext(request))
	
	
def category_book(request):
	return render_to_response('CategoryBook.html')
	

def index_authors(request):
	auth = Author.objects.filter(status = True)
	ctx  = {"authors":auth} 
	return render_to_response('index_authors.html',ctx,context_instance = RequestContext(request))

def author(request, id_author):
	auth_id = get_object_or_404(Author,pk=id_author)#
	auth = Author.objects.filter(status = True)
	return render_to_response('author.html',{'author':auth_id,'authors':auth},context_instance = RequestContext(request))


def index_publishers(request):
	pub = Publisher.objects.filter(status = True)
	ctx = {"pub":pub}
	return render_to_response('index_publishers.html',ctx,context_instance = RequestContext(request))

def publisher(request,id_pub):
	pub_id = get_object_or_404(Publisher,pk=id_pub)
	pub = Publisher.objects.filter(status = True)
	return render_to_response('publisher.html',{'pub_id':pub_id,'pub':pub},context_instance = RequestContext(request))
	

def news(request):
	news = News.objects.filter(status = True)
	ctx = {"News":news}
	return render_to_response('news.html',ctx,context_instance = RequestContext(request))

def contact(request):
	cont = Contact.objects.filter(status=True)
	ctx = {"Contact":cont}
	return render_to_response('contact.html',ctx,context_instance = RequestContext(request))



def login_view(request):
	messaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/home')
	else:
		if request.method =="POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data["username"]
				password = form.cleaned_data["password"]
				user = authenticate(username = username,password = password)
				if user is not None and user.is_active:
					login(request,user)
					return HttpResponseRedirect('/sesion-admin')
				else:
					messaje = "usuario y/o password incorrecto"

		form = LoginForm()
		ctx = {"form":form,"messaje":messaje}
		return render_to_response('login.html',ctx,context_instance = RequestContext(request))		

	
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/home')

def sesion_admin_view(request):
	return render_to_response('sesion-admin.html')




def addNews_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addNewsForm(request.POST)
			info = "Loading information...."
			if form.is_valid():
				title 		= form.cleaned_data['title']
				newsImage	= form.cleaned_data['newsImage']
				date 		= form.cleaned_data['date']
				description = form.cleaned_data['description']

				news = News()#objeto de tipo Noticia y sus atributos
				news.title		= title
				news.newsImage	= newsImage
				news.date		= date
				news.description= description
				news.status		= True
				news.save()	#Guarda la informacion
				info ="saved information!"

			else:
				info = "incorrect information"
			
			form = addNewsForm()
			ctx = {'form':form,'information':info}
			return render_to_response('addNews.html',ctx,context_instance=RequestContext(request))

		else:
			form = addNewsForm()
			ctx = {'form':form}
			return render_to_response('addNews.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')


def addPublisher_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addPublisherForm(request.POST)
			info = "Loading information...."
			if form.is_valid():
				name 			= form.cleaned_data['name']
				address 		= form.cleaned_data['address']
				city 			= form.cleaned_data['city']
				state_province 	= form.cleaned_data['state_province']
				website 		= form.cleaned_data['website']
				logotype 		= form.cleaned_data['logotype']

				publisher = Publisher()#objeto de tipo Pulisher y sus atributos
				publisher.name		= name
				publisher.address	= address
				publisher.city		= city
				publisher.state_province = state_province
				publisher.website		= website
				publisher.logotype		= logotype
				publisher.status		= True
				publisher.save()	#Guarda la informacion
				info ="saved information!"

			else:
				info = "incorrect information"
			
			form = addPublisherForm()
			ctx = {'form':form,'information':info}
			return render_to_response('addPublisher.html',ctx,context_instance=RequestContext(request))

		else:
			form = addPublisherForm()
			ctx = {'form':form}
			return render_to_response('addPublisher.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')


def addAuthor_view(request):
	if request.user.is_authenticated():
		
		if request.method == "POST":
			form = addAuthorForm(request.POST)
			info = "Loading information...."
			if form.is_valid():

				first_name 		= form.cleaned_data['first_name']
				last_name 		= form.cleaned_data['last_name']
				email 			= form.cleaned_data['email']
				biography 		= form.cleaned_data['biography']
				photo 			= form.cleaned_data['photo']


				author = Author()#objeto de tipo Author y sus atributos
				author.first_name		= first_name
				author.last_name	= last_name
				author.email		= email
				author.biography 	= biography
				author.photo		= photo
				author.status		= True

				author.save()	#Guarda la informacion
				info ="saved information!"

			else:
				info = "incorrect information"
			
			form = addAuthorForm()
			ctx = {'form':form,'information':info}
			return render_to_response('addAuthor.html',ctx,context_instance=RequestContext(request))

		else:
			form = addAuthorForm()
			ctx = {'form':form}
			return render_to_response('addAuthor.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')
