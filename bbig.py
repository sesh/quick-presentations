import sys
import mistune
import thttp
import os
from pathlib import Path
import hashlib

# TODO:
# Single image of a slide gets wrapped with <p> and breaks layout
# Image slide with footnote


SCRIPTS = [
    "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js",
    "https://unpkg.com/twemoji@latest/dist/twemoji.min.js",
    "https://raw.githubusercontent.com/tmcw/big/master/big.js",
]

STYLES = [
    "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/tokyo-night-dark.min.css",
    "https://raw.githubusercontent.com/tmcw/big/master/big.css",
    "https://raw.githubusercontent.com/tmcw/big/master/themes/light.css",
]


def cached_get(url, enable_cache=True):
    m = hashlib.sha256()
    m.update(url.encode())
    fn = m.hexdigest()

    cache_dir = Path('.cache')
    cache_dir.mkdir(exist_ok=True)
    cached_file = cache_dir / fn

    if enable_cache and cached_file.exists():
        with open(cached_file, 'r') as f:
            return f.read()
    else:
        content = thttp.request(url).content.decode()

        with open(cached_file, 'w') as f:
            f.write(content)

        return content


def parse_args(args):
    result = {
        a.split("=")[0]: int(a.split("=")[1])
        if "=" in a and a.split("=")[1].isnumeric()
        else a.split("=")[1]
        if "=" in a
        else True
        for a in args
        if "--" in a
    }
    result["[]"] = [a for a in args if not a.startswith("--")]
    return result


def parse_slides(slides_fn):
    with open(slides_fn) as f:
        text = f.read()
        slides = text.split("\n---\n")
        return slides


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])

    slides_fns = args.get("[]")

    if not slides_fns:
        print("Slide filenames must be provided as arguments")
        sys.exit(1)

    for slides_fn in slides_fns:
        print(f"Processing {slides_fn}...")
        slides = parse_slides(slides_fn)

        html = """<!doctype html>
	<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta name="description" content="">
		<script>BIG_ASPECT_RATIO=2;</script>
	"""

        for style_url in STYLES:
            content = cached_get(style_url)
            html += f"<style>\n{content}</style>\n"

        for script_url in SCRIPTS:
            content = cached_get(script_url)
            html += f"<script>\n{content}</script>\n"

        html += """
		<style>
			img.emoji {
				height: 1em;
				width: 1em;
				margin: 0 .05em 0 .1em;
				vertical-align: -0.1em;
			}

			.footnote {
		  	    font-size: 14px;
		  	    position: absolute;
		  	    bottom: 20px;
			}
		</style>
	</head>
	<body>
	"""

        for slide in slides:
            body_class = ''
            if "<!-- body-class:" in slide:
                body_class = slide.split("<!-- body-class:")[1].split('-->')[0].strip()

            slide_html = f"    <div data-body-class='{body_class}'>" + mistune.html(slide).strip() + "</div>\n"
            html += slide_html

        html += """<script>hljs.initHighlightingOnLoad();twemoji.parse(document.body, {
				folder: 'svg',
				ext: '.svg'
		});</script>"""
        html += "</body>\n"
        html += "</html>"

        docs = Path("docs")
        out_fn = docs / slides_fn.replace(".md", ".html")
        Path(os.path.dirname(out_fn)).mkdir(parents=True, exist_ok=True)

        with open(out_fn, "w") as f:
            print(f"Saving to {out_fn}...")
            f.write(html)
