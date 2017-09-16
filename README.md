# django-css-grid
A django app for creating css grids

    # views.py
    from django.views import ListView
    from cssgrid import CSSGridMixin
    from .models import Poll
    
    
    class PollsListView(CSSGridMixin, ListView):
        
        queryset = Poll.objects.all()
        
        grid-template-columns = ['120px', '120px', '120px']
        grid-template-areas = [
            ['header', 'header', 'header],
            ['sidebar', 'content', 'content']
        ]
        grid_gap = '10px'
        
