"""A collection of functions for use in the FRC API."""


def season_check(season: int, season2: int):
    """Check if season is None, if it is set it to season2."""
    if season is None:
        return season2
    return season
