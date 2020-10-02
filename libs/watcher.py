import os
import sys
from time import sleep

from multiprocessing import Process

from ._html_watcher import watch_html
from ._src_watcher import watch_src


def watch(
    src="./script.py",
    html="./public/index.html"
):
    src_path = os.path.abspath(src)
    html_path = os.path.abspath(html)
    dst = os.path.dirname(html_path)

    print("watching source from:", src_path, file=sys.stderr)
    print("writing figures to:", html_path, file=sys.stderr)
    src_path = os.path.basename(src_path)

    src_watcher = Process(target=watch_src, args=(src_path, html_path))
    html_watcher = Process(target=watch_html, args=(dst, ))

    src_watcher.start()
    html_watcher.start()

    try:
        while True:
            sleep(0.5)

    except KeyboardInterrupt:
        print("terminating...", file=sys.stderr)
        src_watcher.terminate()
        html_watcher.terminate()

    finally:
        src_watcher.join()
        html_watcher.join()
