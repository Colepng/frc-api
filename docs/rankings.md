# Rankings

Here is an example of how you would initalize the ranking class

```py
rankings = FrcApi.Rankings()
```

## Event Rankings

### Usage

This function is used to get the ranking information for a certin event.
An example use cause would be to get a teams qual average points.

### Arguments

- The event_code argument is a shorthand for a certain event, you can find out what they are through this API or [the blue allience](https://www.thebluealliance.com/) or [frc events](https://frc-events.firstinspires.org/).

- The optional team_number argument when provided will only return info related to that team

- An optional argument top will return top N teams

- Season an optional argument on every funcation this will over The event_code argument is a shorthand for a certain event, you can find out what they are through this API or [the blue allience](https://www.thebluealliance.com/) or [frc events](https://frc-events.firstinspires.org/).

- The optional team_number argument when provided will only return info related to that team

- An optional argument top will return top N teams

### Examples

This example will return reankings for Humber College 2022

```py
rankings.event_rankings(event_code="on305", season=2022)
```

Here is another example, this will return the top 5 teams at the same event as above.

```py
rankings.event_rankings(event_code="on305", top=5, season=2022)
```

## District Rankings

### Parameters

- district_code (str): The district you want to get the rankings for. Ex: "NE" or "ONT". Optional.

- team_number (int): The team number of the team. Optional.

- top (int): The number of teams to return. Optional.

- page (int | list | str): The page of the rankings you want to get.
Can't be used with top. Optional.

- page_min (int): The minimum page number. Default is 1.

- page_max (int): The maximum page number. Default is None.

- season (int): The season for which you want to get the rankings. Default is None.

### Returns

- (dict | list) : Rankings as a dictionary or a list of dictionaries, depending on the input provided.

### Description

This function is used to retrieve rankings for a specific district and/or team from a data source.

### Note

- If a team_number is provided, none of the other arguments can be used.

- page parameter can be an integer, string, or list, but it cannot be used with the top parameter.

- If the page parameter is an integer, the function will return the rankings for that specific page.

- If the page parameter is a string, the function will return the rankings for all pages up to the maximum page number.

- If the page parameter is a list, the function will return the rankings for the specific pages in the list.

- Error handling for invalid input is included, such as using the team_number and other arguments at the same time, using the top and page parameters at the same time, and providing a page parameter that is not an integer, string, or list.

### Example

This example will return the rankings for the Ontario district both pages 1 and 2

```py
rankings.district_rankings(district_code="ONT", page_min=1, page_max=2, season=2022)
```

Here is another example, this will return page 2 of the rankings for the Ontario district. The advantage to use a list instead of a int would be to supply a range of different numbers like [1, 5, 3, 9]

```py
rankings.district_rankings(district_code="ONT", page=[2], season=2022)
```
