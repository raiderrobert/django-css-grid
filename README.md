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
    
    
    
    # templates/polls/list.html
    <!DOCTYPE html>
    {% load css_grid %}

    <html>
        <head>
            <title>Hello World!</title>
            <meta charset="utf-8">
            <style>
                {% css_grid %}
            </style>
        </head>
        <body>
            <div class="wrapper">
                <div class="header">
                    Hello World!
                </div>
                <div class="sidebar">
                    Pssst
                </div>
                <div class="content">
                    The main thang!
                </div>
            </div>
        </body>
    </html>
