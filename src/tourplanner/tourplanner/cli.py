# -*- coding: utf-8 -*-

"""Console script for tourplanner."""


from itertools import combinations
import click
import googlemaps
from pprint import pprint as pp


@click.command()
@click.argument('locations', type=click.File('r'))
@click.argument('key')
def main(locations, key):
    """Console script for tourplanner."""

    waypoint_distances = {}
    waypoint_durations = {}
    gmaps = googlemaps.Client(key=key)
    all_waypoints = [_.strip() for _ in locations.readlines()]
    for (waypoint1, waypoint2) in combinations(all_waypoints, 2):
        route = gmaps.distance_matrix(
            origins=[waypoint1],
            destinations=[waypoint2],
            mode='walking',
            language='English',
            units='metric'
        )
        distance = route.get("rows", {})[0].get("elements", {})[0].get("distance", {}).get("value")
        duration = route.get("rows", {})[0].get("elements", {})[0].get("duration", {}).get("value")
        if duration:
            waypoint_distances[frozenset([waypoint1, waypoint2])] = distance
            waypoint_durations[frozenset([waypoint1, waypoint2])] = duration

    for (waypoint1, waypoint2) in waypoint_distances.keys():
        data = {
            'from': waypoint1,
            'to': waypoint2,
            'distance': waypoint_distances[frozenset([waypoint1, waypoint2])],
        }
        pp(data)

    #pp(waypoint_distances)
    #pp(waypoint_durations)



if __name__ == "__main__":
    main()
