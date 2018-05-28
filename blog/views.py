from django.shortcuts import redirect, render, get_object_or_404
from blog.models import Post
from blog.forms import post_crea_form
# Create your views here.

def index(request):
	#obetner los post que estan publicados
	posts = Post.objects.filter(published=True)
	#retornar el template
	return render(request, 'index.html', locals())

def post(request, slug):
#obtener un objeto post
	post = get_object_or_404(Post, slug=slug)
#tirar el template
	return render(request, 'post.html', locals())

def post_crea(request):
    if request.method == 'POST':
        form = post_crea_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #se puede poner alguna logica loca aqui entremedio
            post.save()
            return render(request, 'index.html', locals())
    else:
        form = post_crea_form()
        return render(request, 'post_crea.html', locals())

def post_edita(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = post_crea_form(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect(post, slug=post.slug)
    else:
        form = post_crea_form(instance = post)
        return render(request, 'post_crea.html', locals())