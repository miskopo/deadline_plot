"""Deadline plotter.

Usage:
  deadline_plot -i <input_file> -o <output_file>
  deadline_plot (-h | --help)
  deadline_plot --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

from docopt import docopt

from deadline_plot.file_processor import FileProcessor
from deadline_plot.output_producer import OutputProducer


def main():
    arguments = docopt(__doc__, version='Deadline Plotter 0.0.1')
    fp = FileProcessor(arguments['<input_file>'])
    fp()
    out = OutputProducer(arguments['<output_file>'], fp)
    out()


if __name__ == '__main__':
    main()
