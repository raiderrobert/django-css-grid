from django import template
from django.utils.safestring import mark_safe
register = template.Library()


@register.simple_tag(takes_context=True)
def grid(context):
    g = context.get('css-grid', None)
    wrapper = g.get('grid_wrapper', None)
    gap = g.get('grid-gap', None)
    template_columns = get_columns(g)
    areas = g.get('grid-template-areas', [])
    template_area = make_template_area(areas)

    css = f''' 
      .{wrapper} {{
          display: grid;
          grid-gap: {gap};
          grid-template-columns: {template_columns};
          grid-template-areas: {template_area};
      }}
      '''

    for area in flatten_areas(areas):
        css += f'''
        .{area} {{
            grid-area: {area};
        }}
        
        '''

    return mark_safe(css)


def make_template_area(areas):
    if any(isinstance(i, list) for i in areas):
        try:
            l =[make_template_area(sublist) for sublist in areas]
            return '\n'.join(l)
        except ValueError:
            pass

    return format_to_css(areas)


def flatten_areas(areas):
    if any(isinstance(i, list) for i in areas):
        try:
            return set([item for sublist in areas for item in sublist])
        except ValueError:
            pass
    return set(areas)


def format_to_css(l):
    return '\"' + ' '.join(l) + '\"'


def get_columns(g):
    columns = g.get('grid-template-columns', [])
    return format_to_css(columns)


@register.simple_tag(takes_context=True)
def grid_wrapper(context):
    grid_wrapper = context['css-grid'].get('grid_wrapper', None)
    return f'class={grid_wrapper}'

@register.simple_tag(takes_context=True)
def grid_area(context, area_name):
    return f'class={area_name}'

