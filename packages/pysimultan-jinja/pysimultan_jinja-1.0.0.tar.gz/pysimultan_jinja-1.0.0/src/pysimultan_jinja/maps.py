from .mapper import mapper
from .contents import contents
from PySimultan2.src.PySimultan2.taxonomy_maps import TaxonomyMap

from .core.JinjaTemplate import JinjaTemplate
from .core.example import Example


jinja_template_map = TaxonomyMap(taxonomy_name='Jinja',
                                 taxonomy_key='jinja',
                                 taxonomy_entry_name='JinjaTemplate',
                                 taxonomy_entry_key='jinja_template',
                                 content=[contents['template_file'],
                                          contents['rendered_component'],
                                          contents['result'],
                                          contents['output_filename'],
                                          ]
                                 )

mapper.register(jinja_template_map.taxonomy_entry_key, JinjaTemplate, taxonomy_map=jinja_template_map)
MappedFreeCADGeometry = mapper.get_mapped_class(jinja_template_map.taxonomy_entry_key)


example_map = TaxonomyMap(taxonomy_name='Jinja',
                          taxonomy_key='jinja',
                          taxonomy_entry_name='Example',
                          taxonomy_entry_key='example',
                          content=[contents['val_a'],
                                   contents['val_b'],
                                   contents['val_c'],
                                   ]
                          )

mapper.register(example_map.taxonomy_entry_key, Example, taxonomy_map=example_map)
mapped_example = mapper.get_mapped_class(example_map.taxonomy_entry_key)
