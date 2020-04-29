import os

from pywps import Process, LiteralInput
from pywps import ComplexInput, ComplexOutput
from pywps import Format, FORMATS
from pywps.app.Common import Metadata

import logging
LOGGER = logging.getLogger("PYWPS")


PROCESSES_HOME = os.path.abspath(os.path.dirname(__file__))
MOVIE_PLOT = os.path.join(PROCESSES_HOME, "movieplotter.gif")


class MoviePlotter(Process):
    """A wrapper process for the freva movie plotter."""
    def __init__(self):
        inputs = [
            ComplexInput('input', 'Input',
                         abstract='NetCDF file(s) to be plotted (up to 9) with all variables inside.',
                         min_occurs=0,
                         max_occurs=9,
                         default='http://esgf1.dkrz.de/thredds/dodsC/cmip5/cmip5/output1/MPI-M/MPI-ESM-LR/historical/mon/atmos/Amon/r1i1p1/v20120315/tasmax/tasmax_Amon_MPI-ESM-LR_historical_r1i1p1_185001-200512.nc',  # noqa
                         supported_formats=[FORMATS.DODS]),
            LiteralInput('title', 'Title',
                         abstract='Option to choose a title for the movie, please set like "Movie for".',
                         data_type='string',
                         default='Test Movie Plotter'),
            LiteralInput('seldate', 'Seldate',
                         abstract='Option to choose timerange start,end via YYYY-MM-DDThh:mm:ss,YYYY-MM-DDThh:mm:ss.',
                         data_type='string',
                         default='2005-01-01T12:00:00,2005-03-01T12:00:00'),
        ]
        outputs = [
            ComplexOutput('output', 'Results',
                          abstract='Generated Movie Plot',
                          as_reference=True,
                          supported_formats=[Format('image/gif', extension='.gif', encoding='base64')]),
        ]

        super(MoviePlotter, self).__init__(
            self._handler,
            identifier='movieplotter',
            title='Movie Plotter',
            abstract='Plots 2D lon/lat movies in GIF format.',
            keywords=['freva', 'demo'],
            metadata=[
                Metadata('PyWPS', 'https://pywps.org/'),
                Metadata('Birdhouse', 'http://bird-house.github.io/'),
                Metadata('Freva', 'https://www-miklip.dkrz.de/'),
            ],
            version='1.0.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    @staticmethod
    def _handler(request, response):
        response.outputs['output'].file = MOVIE_PLOT
        return response
