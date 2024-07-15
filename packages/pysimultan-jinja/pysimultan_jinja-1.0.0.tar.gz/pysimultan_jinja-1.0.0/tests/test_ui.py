from PySimultan2.src.PySimultan2 import DataModel
from PySimultanUI.src.pysimultanui import run_ui
from pysimultan_jinja.src.pysimultan_jinja import mapper, method_mapper, view_manager


from PySimultanUI.src.pysimultanui import user_manager

user_manager.mapper_manager.create_mapping(name='Jinja',
                                           mapper=mapper,
                                           method_mapper=method_mapper,
                                           view_manager=view_manager)
del user_manager.mapper_manager.available_mappings['Default']


def create_jinja_component():
    from pysimultan_tabs.src.pysimultan_tabs.mapping.functions import create_building_component

    data_model = DataModel.create_new_project(project_path='test_set_dictionary.simultan',
                                              user_name='admin',
                                              password='admin')

    JinjaTemplate = mapper.get_mapped_class('jinja_template')
    Example = mapper.get_mapped_class('example')

    new_example = Example(val_a='a',
                          val_b='b',
                          val_c='c',
                          data_model=data_model,
                          object_mapper=mapper)

    template = JinjaTemplate.from_string(name='template',
                                         content='This ia a template that uses the following values: '
                                                 '{{ rendered_component.val_a }} '
                                                 '{{ rendered_component.val_b }} '
                                                 '{{ rendered_component.val_c }}.',
                                         rendered_component=new_example,
                                         data_model=data_model,
                                         output_filename='output.txt',
                                         object_mapper=mapper)

    template.render()



if __name__ in {"__main__", "__mp_main__"}:

    template = create_jinja_component()
    run_ui(reload=False)
