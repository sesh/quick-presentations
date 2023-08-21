import sys
import subprocess


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


def usage():
    print("Quickly take screenshots of a presentation using shot-scraper")
    print("")
    print("Usage:")
    print("  python screenshots.py --num-slide=10 <url>")


def take_screenshots(url, num_slides):
    for i in range(num_slides + 1):
        subprocess.run(["shot-scraper", f"{url}#{i}", "--retina", "--width", "920", "--height", "560"])


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    base_url_list = args["[]"]
    num_slides = args.get("--num-slides")

    if len(base_url_list) != 1 or not num_slides:
        usage()
        sys.exit(1)

    try:
        num_slides = int(num_slides)
        url = base_url_list[0]
    except:
        usage()
        sys.exit(1)

    take_screenshots(url, num_slides)
