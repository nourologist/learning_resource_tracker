'''Defines url patterns for learning_resources app'''

from django.urls import path

from . import views

app_name = 'lrt'

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    # View all categories
    path('categories/', views.categories, name='categories'),
    # View all entries
    path('entries/', views.entries, name='entries'),
    # Detail page for a single category
    path('categories/<int:category_id>/', views.category, name='category'),
    # View all tags
    path('tags/', views.tags, name='tags'),
    # Detail page for a single tag
    path('tags/<int:tag_id>/', views.tag, name='tag'),
    # Add new category
    path('new_category/', views.new_category, name='new_category'),
    # Add new entry
    path('new_entry/', views.new_entry, name='new_entry'),
    # Edit an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
