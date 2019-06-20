import pandas as pd
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()


class FileProcessor:
    def __init__(self, file_path: str,):
        self.file_path: str = file_path
        self.df: pd.DataFrame = pd.DataFrame()

    def load_file(self):
        with open(self.file_path) as i_file:
            self.df = pd.read_csv(i_file, names=['dates', 'names'])

    def __call__(self, *args, **kwargs):
        self.load_file()
        self.process_data()
        print(self.df)

    def process_data(self):
        self.df['dates'] = pd.to_datetime(self.df['dates'])
        # self.df.set_index('dates', inplace=True)


