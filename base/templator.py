from jinja2 import Environment, FileSystemLoader
from base.settings import TEMPLATES


def render(template_name, folder=TEMPLATES, **kwargs):
    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template_name)
    return template.render(**kwargs)
