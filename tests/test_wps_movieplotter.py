from pywps import Service
from pywps.tests import client_for, assert_response_success

from .common import get_output
from frevas.processes.wps_movieplotter import MoviePlotter


def test_wps_movieplotter():
    client = client_for(Service(processes=[MoviePlotter()]))
    datainputs = "title=Test Move Plotter"
    resp = client.get(
        "?service=WPS&request=Execute&version=1.0.0&identifier=movieplotter&datainputs={}".format(
            datainputs))
    assert_response_success(resp)
    assert 'movieplotter.gif' in get_output(resp.xml)['output']
