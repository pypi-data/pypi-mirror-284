from pathlib import Path

from jinja2 import Template
from nonebot import require

require("nonebot_plugin_alconna")
require("nonebot_plugin_htmlrender")

from nonebot_plugin_alconna import UniMessage
from nonebot_plugin_htmlrender import html_to_pic, get_new_page, template_to_pic


__dir = Path(__file__).parent.resolve().absolute()

html_templates = __dir / "html_template"


def get_template(name: str):
    return html_templates / name / "template.html"


async def get_html(content: str):
    template = Template("{{ content }}", enable_async=True)
    rendered = await template.render_async(content=content)
    return rendered


__all__ = ["UniMessage", "get_html", "html_to_pic", "get_new_page", "get_template", "template_to_pic"]
