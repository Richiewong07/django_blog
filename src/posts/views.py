
from urllib.parse import quote_plus

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

from .forms import PostForm
from .models import Post

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404("YOU ARE NOT LOGIN. ONLY USERS MAY CREATE/EDIT/DELETE A POST")

    # if not request.user.is_authenticated():
    #     raise Http404

    # CREATES FORM (DJANGO FORM METHOD) --> request.POST or None FOR VALIDATION ERRORS
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # SAVES FORM CONTENT TO DATABASE
        instance = form.save(commit = False)

        # print(form.cleaned_data.get("title"))

        # REQUIRES USER
        instance.user = request.user

        instance.save()
        # MESSAGE SUCCESS
        messages.success(request, "Successful Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.error(request, "Not Successful Created")



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

    # ADDS SOCIAL SHARE LINKS IN post_detail.html
    share_string = quote_plus(instance.content)

    # PASSED TO post_detail.html
    context = {
        "title": instance.title,
        "instance": instance,
        "share_string": share_string,
    }

    return render(request, 'post_detail.html', context)

    # return HttpResponse("<h1>Detail</h1>")




def post_list(request):

    # GIVES YOU OBJECTS IN DB FROM POST MODEL
    queryset_list = Post.objects.all() #.order_by("-timestamp")

    # ADDED PAGINATION
    paginator = Paginator(queryset_list, 5)  # Show 5 contacts per page
    page_req_var = "page"
    page = request.GET.get(page_req_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)


    context = {
        "object_list" : queryset,
        "title" : "List",
        "page_req_var" : page_req_var,
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

    return render(request, 'post_list.html', context)


    # return HttpResponse("<h1>List</h1>")








def post_update(request, id = None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404("YOU ARE NOT LOGIN. ONLY USERS MAY CREATE/EDIT/DELETE A POST")

    # NEED INSTANCE
    instance = get_object_or_404(Post, id=id)

    # ADD instance = instance to show content
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # ADDED POPUP MESSAGE
        messages.success(request, "Items Saved")
        # instance.get_absolute_url() METHOD FROM Post Model Instance IN models.py
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }

    return render(request, 'post_form.html', context)




def post_delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404("YOU ARE NOT LOGIN. ONLY USERS MAY CREATE/EDIT/DELETE A POST")

    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("posts:list")

