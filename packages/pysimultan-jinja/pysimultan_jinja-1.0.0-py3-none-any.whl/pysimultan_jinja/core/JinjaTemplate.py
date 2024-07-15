import os
from typing import Optional
from PySimultan2.src.PySimultan2.files import FileInfo
from PySimultan2.src.PySimultan2 import DataModel
from jinja2 import Environment, FileSystemLoader


template = FileSystemLoader('snappyHexMesh.jinja')


def create_empty_file_info(name: str,
                           data_model: DataModel):
    return FileInfo.from_string(filename=name,
                                content='',
                                data_model=data_model
                                )


class JinjaTemplate:

    @classmethod
    def from_string(cls,
                    name: str,
                    content: str = '',
                    *args,
                    **kwargs):

        file_info = FileInfo.from_string(filename=f'{name}.jinja',
                                         content=content,
                                         data_model=kwargs.get('data_model', None)
                                         )

        return cls(template_file=file_info, *args, **kwargs)

    def __init__(self,
                 *args,
                 **kwargs):
        self._env = None
        self._template = None

        self.template_file: Optional[FileInfo] = kwargs.get('template_file',
                                                            create_empty_file_info(kwargs.get('name', 'template_file')
                                                                                   + '.jinja',
                                                                                   self._data_model)
                                                            )
        self.rendered_component = kwargs.get('rendered_component')
        self.result: Optional[FileInfo] = kwargs.get('result', None)
        self.output_filename = kwargs.get('output_filename', None)

    def __load_init__(self, *args, **kwargs):
        self._env = None

    @property
    def env(self):
        if self._env is None and self.template_file is not None:
            self._env = Environment(loader=FileSystemLoader(
                os.path.dirname(self.template_file.file_path)
            )
            )
        return self._env

    @property
    def template(self):
        return self.env.get_template(os.path.basename(self.template_file.file_path))

    def render(self):
        result = self.template.render(rendered_component=self.rendered_component)

        filename = self.output_filename if self.output_filename is not None else self.template_file.name + '_render_result'

        self.result = FileInfo.from_string(filename=filename,
                                           content=result,
                                           data_model=self._data_model)
        return self.result
