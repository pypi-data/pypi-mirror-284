import logging
from PySimultanUI.src.pysimultanui import MethodMapper
from .mapper import mapper

method_mapper = MethodMapper()

logger = logging.getLogger('jinja')


# map a class method
jinja_template = mapper.get_mapped_class('jinja_template')

method_mapper.register_method(
    cls=jinja_template,
    name='render',
    method=jinja_template.render,
    add_data_model_to_kwargs=False,
    add_user_to_kwargs=False,
    io_bound=False
)
