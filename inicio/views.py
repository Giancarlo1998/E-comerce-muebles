from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.


def pre(request):


	
	return render(request,"inicio/pre.html", {
		
		
		})


def Bienvenida(request):


	queryset = request.GET.get("Search")
	todos= Product.objects.all().order_by('-id')#productos x listado_post
	paginator = Paginator(todos, 6)#num de productosxpagina!!!!
	pagina = request.GET.get("page") or 1
	productos = paginator.get_page(pagina)
	pag_act = int(pagina)
	paginas = range(1, productos.paginator.num_pages + 1)

	if queryset:
		
		todos = Product.objects.filter(nombre__icontains = queryset).order_by('nombre')

		if request.method=="POST":
			subject=request.POST["asunto"]
			message=request.POST["mensaje"]
			from_email =settings.EMAIL_HOST_USER #"82ea5e59d9-2a6ee2@inbox.mailtrap.io"
			to = ['j161298c@gmail.com']
			#to = ['82ea5e59d9-2a6ee2@inbox.mailtrap.io']
			send_mail(subject, message, from_email, to)
			messages.success(request, "¡Aquí hay productos increíbles que te pueden gustar!")
			return render(request,"inicio/gracias.html")


		return render(request,"inicio/search.html", {
		"products":todos,
		})



	return render(request,"inicio/bienvenida.html", {
		
		"productos":productos, 
		"paginas":paginas, 
		"pag_act":pag_act,
		
		})



def Cate(request):


	#filtro = request.GET.get("Filtros")
	todos = Category.objects.all().order_by("nombre")
	
	return render(request,"inicio/categorias.html", {
		"products":todos,
		})



'''
def detalle(request, product_id):
	
	
	product = Product.objects.get(id = product_id)
	listado_post = Product.objects.filter(nombre = product)
	product.view_count += 1
	product.save()
	#urljcv = Product.objects.get(linkjc=product)




	return render(request,"inicio/detalle.html", {
		"listado_post":listado_post,
		"product":product,	

		})


def detalle(request, product_id):
	
	
	product = Product.objects.get(id = product_id)
	listado_post = Product.objects.filter(nombre = product)
	getcat = Category.objects.get(product = product_id)
	cat = Product.objects.filter(categoria = getcat).order_by('nombre')
	product.view_count += 1
	product.save()
	

	return render(request,"inicio/detalle.html", {
		"listado_post":listado_post,
		"product":product,
		"cat":cat,	

		})
'''

def detalle(request, product_id):
	
	
	product = Product.objects.get(id = product_id)
	listado_post = Product.objects.filter(nombre = product)
	getcat = Category.objects.get(product = product_id)
	cat = Product.objects.filter(categoria = getcat).order_by('nombre')
	product.view_count += 1
	product.save()

	if request.method=="POST":
		subject=request.POST["asunto"]
		message=request.POST["mensaje"]
		from_email =settings.EMAIL_HOST_USER #"82ea5e59d9-2a6ee2@inbox.mailtrap.io"
		to = ['j161298c@gmail.com']
		#to = ['82ea5e59d9-2a6ee2@inbox.mailtrap.io']
		send_mail(subject, message, from_email, to)
		messages.success(request, "¡Gracias, en breve nos pondremos en contacto!")
		#return redirect(request,'Bienvenida')
	

	return render(request,"inicio/detalle.html", {
		"listado_post":listado_post,
		"product":product,
		"cat":cat,	

		})


def filtrojc(request, category_id):
	
	product = Category.objects.get(id = category_id)
	listado_post = Product.objects.filter(categoria = product)
	#todos= Product.objects.all().order_by('-id')#productos x listado_post
	paginator = Paginator(listado_post, 6)#num de productosxpagina!!!!
	pagina = request.GET.get("page") or 1
	productos = paginator.get_page(pagina)
	pag_act = int(pagina)
	paginas = range(1, productos.paginator.num_pages + 1)


	return render(request,"inicio/bienvenida.html", {
		
		"productos":productos, 
		"paginas":paginas, 
		"pag_act":pag_act,
		
		})




def linkjc(request, product_id):
	
	
	product = Product.objects.get(id = product_id)
	urljcv = Product.objects.filter(linkjc = product)
	

	return redirect(request,'{{urljcv}}')

def gracias(request):
	
		

	return render(request,"gracias")

