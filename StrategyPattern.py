class Route():
    def get_path(self, a, b):
        pass

class CityRoute(Route):
    def get_path(self, a, b):
        return {1: a, 2: b}

class Gps():
    _route: Route = None

    def __init__(self, route: Route):
        self._route = route

    def get_route(self, a, b):
        print(self._route.get_path(a, b))

route = CityRoute()
gps = Gps(route)
gps.get_route('Goiânia', 'Rio de Janeiro')