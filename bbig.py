import sys
import mistune
import thttp
from pathlib import Path


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
        print("Slide filesnames must be provided as arguments")
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
            content = thttp.request(style_url).content.decode()
            html += f"<style>\n{content}</style>\n"

        for script_url in SCRIPTS:
            content = thttp.request(script_url).content.decode()
            html += f"<script>\n{content}</script>\n"

        html += """
		<style>
			body {
				background-color: #ffd52e;
				color: #000;
			}

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
            slide_html = "    <div>" + mistune.html(slide).strip() + "</div>\n"
            html += slide_html

        html += """<script>hljs.initHighlightingOnLoad();twemoji.parse(document.body, {
				folder: 'svg',
				ext: '.svg'
		});</script>"""
        html += "</body>\n"
        html += "</html>"

        out = Path("out")
        if not out.is_dir():
            out.mkdir()

        with open(out / slides_fn.replace(".md", ".html"), "w") as f:
            print(f"Saving to {out / slides_fn.replace('.md', '.html')}...")
            f.write(html)
