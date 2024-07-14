import argh
from . import heatmap
from . import bar
def main():
    argh.dispatch_commands((heatmap.heatmap, bar.bar))