"""
CSS Grid Template
"""


class CSSGridMixin(object):
    """
    A mixin for adding css grid to any standard CBV
    """

    grid_wrapper = None
    grid_template_columns = None
    grid_template_areas = None
    grid_gap = None

    def get_context_data(self, **kwargs):
        """
        Insert the single object into the context dict.
        """
        context = super().get_context_data(**kwargs)
        context.update({
            'css-grid': {
                'grid_wrapper': self.grid_wrapper,
                'grid-template-columns': self.grid_template_columns,
                'grid-template-areas': self.grid_template_areas,
                'grid-gap': self.grid_gap
            }
        })
        return context
