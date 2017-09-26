# django-css-grid

## Install via pip

    pip install git+https://github.com/raiderrobert/django-css-grid/

## Working from Django tutorial

I'm going to make some assumptions about what's around us. These are predicated on following the Django tutorial: https://docs.djangoproject.com/en/1.11/intro/tutorial01/

## Add to installed apps
    INSTALLED_APPS = [
        ...
        'css_grid',
        'polls'
    ]

A django app for creating css grids
    
    # polls/models.py
    from django.db import models
    
    
    class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')

        def __str__(self):
            return self.question_text
    
    
    
    # polls/views.py
    from django.views import ListView
    from cssgrid import CSSGridMixin
    from .models import Question
    
    
    class PollsListView(CSSGridMixin, ListView):
        queryset = Question.objects.all()

        grid_wrapper = 'polls-wrapper'
        grid_template_columns = ['120px', '120px', '120px']
        grid_template_areas = [
            ['sidebar', 'content'],
            ['sidebar', 'content'],
            ['header', 'header']
        ]
        grid_gap = '10px'
    
    
    
    # polls/templates/polls/list.html
    {% load css_grid %}
    <!DOCTYPE html>

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
