import sys
import time
from io import StringIO

from hotreload import Loader

template = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Figure from {}</title>
  </head>
  <body>{}</body>
</html>
"""


def _generate_html(src_path, html_path, fig, save_ext):
    buffer = StringIO()

    fig.savefig(buffer, format="svg", bbox_inches="tight")

    if save_ext and save_ext != "py":
        filename = src_path.rsplit(".")[0] + "." + save_ext
        fig.savefig(filename, bbox_inches="tight")

    with open(html_path, "w", encoding="utf-8") as g:
        g.write(template.format(src_path, buffer.getvalue()))


def watch_src(src_path, html_path):
    script = Loader(src_path)

    while True:
        if script.has_changed():
            values = script.main()
            try:
                fig, save_ext = values
            except:
                fig, save_ext = values, None
            _generate_html(src_path, html_path, fig, save_ext)

        time.sleep(1)
