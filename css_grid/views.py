"""
CSS Grid Template
"""

class CSSGridMixin(object):
    """
    A mixin for adding css grid to any standard CBV
    """
    
    _prefix = 'css-grid'
    grid_wrapper = None
    grid_template_columns = None
    grid_template_areas = None
    grid_gap = None
    

    def get_context_data(self, **kwargs):
        """
        Insert the single object into the context dict.
        """
        context = super(SingleObjectMixin, self).get_context_data(**context)
        context.update({
            self._prefix: {
                'grid_wrapper': self.grid_wrapper,
                'grid-template-columns': self.grid_template_columns,
                'grid-template-areas': self.grid_template_areas,
                'grid-gap': self.grid_gap
            }
        })
        return context
