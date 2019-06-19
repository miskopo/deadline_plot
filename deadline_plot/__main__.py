"""Deadline plotter.

Usage:
  deadline_plot -i <input_file> -o <output_file>
Options:
  -h --help     Show this screen.
  --version     Show version.
"""

from docopt import docopt


def main():
    arguments = docopt(__doc__, version='Deadline Plotter 0.0.1')


if __name__ == '__main__':
    main()
