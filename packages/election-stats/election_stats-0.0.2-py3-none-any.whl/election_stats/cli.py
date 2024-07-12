from argparse import ArgumentParser
from . import heatmap
from . import bar

runners = {
    "heatmap": heatmap.run,
    "bar": bar.run
}

def main():
    parser = ArgumentParser(prog="election-stats")
    parser.add_argument("-d", "--debug", action="store_true", default=False, help="enable debug mode")
    subparsers = parser.add_subparsers(dest="command", required=True, title="commands", help="%(help)s")
    heatmap_parser = subparsers.add_parser("heatmap", help="create heatmaps comparing two election results")
    heatmap.parse(heatmap_parser)
    bar_parser = subparsers.add_parser("bar", help="create bar charts showing simple results")
    bar.parse(bar_parser)
    args = parser.parse_args()
    runners[args.command](args)