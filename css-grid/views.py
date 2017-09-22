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
            'grid_wrapper': self._prefix + self.grid_wrapper,
            'grid-template-columns': self._prefix + self.grid_template_columns,
            'grid-template-areas': self._prefix + self.grid_template_areas,
            'grid-gap': self._prefix + self.grid_gap
        })
        return context
