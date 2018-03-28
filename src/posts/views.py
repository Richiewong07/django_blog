from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Post

def post_create(request):
    return HttpResponse("<h1>Create</h1>")



def post_detail(request):

    # WILL GIVE ERRORS --> NOT RECOMMENDED TO USE
    # instance = Post.objects.get(id=1)

    # USE THIS METHOD PROVIDED BY DJANGO --> GET CERTAIN ITEMS BASED ON QUERY FIELD
    # instance WILL HAVE THE CONTENT FROM THE POST CLASS FOR SPECIFIC QUERY
    instance = get_object_or_404(Post, id="3")

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





def post_update(request):
    return HttpResponse("<h1>Update</h1>")




def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")