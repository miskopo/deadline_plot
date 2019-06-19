from setuptools import setup
setup(
    name='deadline_plot',
    version='0.0.1',
    packages=['deadline_plot'],
    entry_points={
        'console_scripts': [
            'deadline_plot = deadline_plot.__main__:main'
         ]
    })
