# django-css-grid
A django app for creating css grids

    # views.py
    from django.views import ListView
    from cssgrid import CSSGridMixin
    from .models import Poll
    
    
    class PollsListView(CSSGridMixin, ListView):
        
        queryset = Poll.objects.all()
        css_grid = [
          ['header', 'header', 'header],
          ['sidebar', 'content', 'content']
        ]
        
