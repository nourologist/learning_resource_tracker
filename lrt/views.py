from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Category, Entry, Tag
from .forms import CategoryForm, EntryForm

# Create your views here.

def home(request):
    '''The home page'''
    return render(request, 'lrt/home.html')

@login_required
def categories(request):
    '''View all categories associated with the logged in user'''
    categories = Category.objects.filter(owner=request.user).order_by('date_added') # Should I order by date_added or alphabetical?
    context = {'categories': categories}
    return render(request, 'lrt/categories.html', context)

@login_required
def entries(request):
    '''View all entries associated with the logged in user'''
    # Because Entry objects have no direct user or owner attribute, first we must retrieve the categories beloning to the logged in user, and then display only the entries associated with those categories
    # Why not just assign an owner to an entry directly, when the entry is first added?
    categories = Category.objects.filter(owner=request.user)
    entries = []
    for category in categories:
        entries += Entry.objects.filter(category = category)
    context = {'entries': entries}
    return render(request, 'lrt/entries.html', context)

@login_required
def category(request, category_id):
    '''Show a single category and all its associated entries'''
    category = Category.objects.get(id=category_id)
    if category.owner != request.user:
        raise Http404
    entries = category.entry_set.order_by('-date_added')
    context = {'category': category, 'entries': entries}
    return render(request, 'lrt/category.html', context)

@login_required
def tags(request):
    '''View all tags associated with the logged in user'''
    tags = Tag.objects.filter(owner=request.user).order_by('date_added')
    context = {'tags': tags}
    return render(request, 'lrt/tags.html', context)

@login_required
def tag(request, tag_id):
    '''View all entries associated with a tag'''
    tag = Tag.objects.get(id=tag_id)
    if tag.owner != request.user:
        raise Http404
    entries = tag.entry_set.order_by('-date_added')
    context = {'tag': tag, 'entries': entries}
    return render(request, 'lrt/tag.html', context)

@login_required
def new_category(request):
    '''Form to add a new category'''

    # Data: Figure out what data to load (and validate and save it, if any)
    if request.method != 'POST': # then it's probably GET, so:
        form = CategoryForm() # create a blank form
    else:
        form = CategoryForm(data=request.POST) # create a form with the data as per the POST request
        
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.owner = request.user
            new_category.save()
            return redirect('lrt:categories')
    
    # Dictionary & render(): Display a blank OR invalid form
    context = {'form': form}
    return render(request, 'lrt/new_category.html', context)

@login_required
def new_entry(request):
    'Form to add a new entry'

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.save()
            return redirect('lrt:entries')
    
    context = {'form': form}
    return render(request, 'lrt/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    'Form to edit an existing entry'

    entry = Entry.objects.get(id=entry_id)
    category = entry.category
    if category.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)

        if form.is_valid():
            form.save()
            #return redirect('lrt:entry', entry_id=entry.id)
            return redirect('lrt:entries')
    
    context = {'entry': entry, 'form': form}
    return render(request, 'lrt/edit_entry.html', context)
