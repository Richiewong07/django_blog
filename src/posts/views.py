from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404



# Create your views here.

from .forms import PostForm
from .models import Post

def post_create(request):

    # CREATES FORM, DJANGO FORM METHOD --> request.POST or None FOR VALIDATION ERRORS
    form = PostForm(request.POST or None)
    if form.is_valid():
        # SAVES FORM CONTENT TO DATABASE
        instance = form.save(commit = False)
        # print(form.cleaned_data.get("title"))
        instance.save()
        # MESSAGE SUCCESS 
        return HttpResponseRedirect(instance.get_absolute_url())

    # TO CAPTURE THE DATA GETTING POSTED --> NOT RECOMMENDED B/C NO FIELD IS REQUIRED
    # if request.method == "POST":
    #     print(request.POST.get("content"))
    #     print(request.POST.get("title"))
    #

    context = {
        "form": form,
    }

    return render(request, "post_form.html", context)



def post_detail(request, id):   # id PASSED FROM REG EXPRESSION IN post/urls.py

    # WILL GIVE ERRORS --> NOT RECOMMENDED TO USE
    # instance = Post.objects.get(id=1)

    # USE THIS METHOD PROVIDED BY DJANGO --> GET CERTAIN ITEMS BASED ON QUERY FIELD
    # instance WILL HAVE THE CONTENT FROM THE POST CLASS FOR SPECIFIC QUERY
    instance = get_object_or_404(Post, id = id)

    # PASSED TO post_detail.html
    context = {
        "title": instance.title,
        "instance": instance,
    }

    return render(request, 'post_detail.html', context)

    # return HttpResponse("<h1>Detail</h1>")




def post_list(request):

    # GIVES YOU OBJECTS IN DB FROM POST MODEL
    queryset = Post.objects.all()

    context = {
        "object_list" : queryset,
        "title" : "List"
    }

    # # TWO DIFFERENT CONTEXT DEPENDING ON IF USER IS LOGIN
    # if request.user.is_authenticated():
    #     context = {                     # PASS context TO EMPTY {} IN render
    #         "title": "My User List"     # PASS title THROUGH index.html
    #     }
    # else:
    #     context = {
    #         "title": "List"
    #     }

    return render(request, 'index.html', context)


    # return HttpResponse("<h1>List</h1>")





def post_update(request, id = None):
    instance = get_object_or_404(Post, id=id)

    # ADD instance = instance to show content
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # instance.get_absolute_url() METHOD FROM Post Model Instance IN models.py
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }

    return render(request, 'post_form.html', context)




def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")