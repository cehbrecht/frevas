from .wps_say_hello import SayHello
from .wps_movieplotter import MoviePlotter

processes = [
    SayHello(),
    MoviePlotter(),
]
