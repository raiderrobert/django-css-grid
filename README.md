# django-css-grid

A django app for creating css grids

## Install via pip

    pip install git+https://github.com/raiderrobert/django-css-grid/

## Working from Django tutorial

I'm going to make some assumptions about what's around us. These are predicated on following the Django tutorial: https://docs.djangoproject.com/en/1.11/intro/tutorial01/


## Assuming you have the following model
    
    # polls/models.py
    from django.db import models
    
    
    class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')

        def __str__(self):
            return self.question_text

## Add to installed apps
    INSTALLED_APPS = [
        ...
        'css_grid',
        'polls'
    ]


## Use the CSSGridMixin on a View
    
    # polls/views.py
    from django.views import ListView
    from cssgrid.views import CSSGridMixin
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
    
    
## Load the css_grid library and place the template tags appropriately
    # polls/templates/polls/list.html
    {% load css_grid %}
    <!DOCTYPE html>

    <html>
        <head>
            <title>Hello World!</title>
            <meta charset="utf-8">
            <style>
                {% grid %}
                
            .box {
              background-color: #444;
              color: #fff;
              border-radius: 5px;
              padding: 20px;
              font-size: 150%;
            }
            </style>
        </head>
        <body>
            <div {% grid_wrapper %}>
                <div class="header box">
                    Hello World!
                </div>
                <div class="sidebar box">
                    Pssst
                </div>
                <div class="content box">
                    The main thang!
                </div>
            </div>
        </body>
    </html>
