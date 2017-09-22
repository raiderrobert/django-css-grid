# django-css-grid
A django app for creating css grids

    # views.py
    from django.views import ListView
    from cssgrid import CSSGridMixin
    from .models import Poll
    
    
    class PollsListView(CSSGridMixin, ListView):
        
        queryset = Poll.objects.all()
        
        grid_wrapper = 'polls-wrapper'
        grid_template_columns = ['120px', '120px', '120px']
        grid_template_areas = [
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
                {% grid %}
            </style>
        </head>
        <body>
            <div {% grid_wrapper %}>
                <div {% grid_area 'header' %}>
                    Hello World!
                </div>
                <div {% grid_area 'sidebar' %}>
                    Pssst
                </div>
                <div {% grid_area 'content' %}>
                    The main thang!
                </div>
            </div>
        </body>
    </html>
