# pysimultan_jinja

-----

## Table of Contents

- [Overview](#overview)
- [How does it work?](#how-does-it-work)


## Overview
The pysimultan_jinja package is a toolbox for rendering Jinja2 templates in PySimultanUI.


## How does it work?
The package implements a JinjaTemplate class that is used to render Jinja2 templates in PySimultanUI. 

With the package, a JinjaTemplate Component can be created, which can be used to render Jinja2 templates with it's 
rendered_component as content.

The class has the following attributes:

- name: The name of the component
- template_file: The Jinja2 template file. This is a File which contains the Jinja2 template.
- rendered_component: The rendered component or parameter. This component or parameter is passed to the Jinja2 template 
  for rendering.
- result: The result of the rendering. This is a File which contains the rendered template.
- output_filename: The name of the output file. This is the name of the file that will be created after rendering the 
  template.


## license
This project is licensed under the GNU Lesser General Public License v3.0 - see the [LICENSE](LICENSE.txt) file for details.
```
