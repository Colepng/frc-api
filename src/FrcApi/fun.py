"""A collection of functions for use in the FRC API."""


def season_check(season: int, season2: int):
    """Check if season is None, if it is set it to season2."""
    if season is None:
        return season2
    if season >= 2015 and season <= 2023:
        return season
    else:
        raise ValueError("Invalid season number must be between 2015 and 2023")
