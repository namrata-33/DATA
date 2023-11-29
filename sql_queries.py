##a. The win records (percentage win and total wins) for each team by year and gender, excluding ties, matches with no result, and matches decided by the DLS method in the event that, for whatever reason, the planned innings can't be completed.


```sql

-- Query for win records by year and gender

SELECT

year,

gender,

team,

SUM(CASE WHEN result = 'won' THEN 1 ELSE 0 END) AS total_wins,

ROUND(

(SUM(CASE WHEN result = 'won' THEN 1 ELSE 0 END) /

COUNT(CASE WHEN result IN ('won', 'lost') THEN 1 END) * 100),

2

) AS win_percentage

FROM matches

WHERE

result IN ('won', 'lost') -- Excluding ties, matches with no result, and DLS method

GROUP BY year, gender, team;

```


##b. Which male and female teams had the highest win percentages in 2019?


```sql

-- Query for highest win percentages in 2019 by gender

WITH WinRecords AS (

SELECT

year,

gender,

team,

SUM(CASE WHEN result = 'won' THEN 1 ELSE 0 END) AS total_wins,

ROUND(

(SUM(CASE WHEN result = 'won' THEN 1 ELSE 0 END) /

COUNT(CASE WHEN result IN ('won', 'lost') THEN 1 END) * 100),

2

) AS win_percentage

FROM matches

WHERE

result IN ('won', 'lost') -- Excluding ties, matches with no result, and DLS method

GROUP BY year, gender, team

)

SELECT

year,

gender,

team,

win_percentage

FROM WinRecords

WHERE year = 2019

ORDER BY win_percentage DESC

LIMIT 1;

```


##c. Which players had the highest strike rate as batsmen in 2019? (Note to receive full credit, you need to account for handling extras properly.)


```sql

-- Query for players with the highest strike rate as batsmen in 2019

SELECT

player,

SUM(runs) AS total_runs,

SUM(CASE WHEN extras_type IS NULL THEN 1 ELSE 0 END) AS balls_faced

FROM deliveries

WHERE

match_id IN (

SELECT match_id FROM matches WHERE year = 2019

)

GROUP BY player

HAVING balls_faced >= 100 -- Minimum balls faced to consider

ORDER BY (SUM(runs) / SUM(CASE WHEN extras_type IS NULL THEN 1 ELSE 0 END)) DESC

LIMIT 1;

```
