# -*- coding: utf-8 -*-

"""Console script for tourplanner."""


from itertools import combinations
import click
import googlemaps


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
        distance = route["rows"][0]["elements"][0]["distance"]["value"]
        duration = route["rows"][0]["elements"][0]["duration"]["value"]
        waypoint_distances[frozenset([waypoint1, waypoint2])] = distance
        waypoint_durations[frozenset([waypoint1, waypoint2])] = duration




if __name__ == "__main__":
    main()
