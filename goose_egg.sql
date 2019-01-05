SELECT 
    count(*) as 'Goose Eggs', pitcher
FROM
    (SELECT 
        *,
            SUM(outs_on_play) AS 'IPOUTS',
            SUM(IF(batter_dest >= 4, 1, 0)) + SUM(IF(runner_on_1st_dest >= 4, 1, 0)) + SUM(IF(runner_on_2nd_dest >= 4, 1, 0)) + SUM(IF(runner_on_3rd_dest >= 4, 1, 0)) AS 'RUNS'
    FROM
        retrosheet.events
    GROUP BY game_id , pitcher , inning) AS subtableA
WHERE
    inning >= 7
        AND ((batting_team = 0
        AND home_score - vis_score >= 0
        AND home_score - vis_score <= 2)
        OR (batting_team = 1
        AND vis_score - home_score >= 0
        AND vis_score - home_score <= 2)
        OR (batting_team = 0
        AND home_score - vis_score >= 0
        AND home_score - vis_score <= 1 + IF(first_runner IS NULL, 0, 1) + IF(second_runner IS NULL, 0, 1) + IF(third_runner IS NULL, 0, 1))
        OR (batting_team = 1
        AND vis_score - home_score >= 0
        AND vis_score - home_score <= 1 + IF(first_runner IS NULL, 0, 1) + IF(second_runner IS NULL, 0, 1) + IF(third_runner IS NULL, 0, 1)))
        AND IPOUTS + IF(first_runner IS NULL, 0, 1) + IF(second_runner IS NULL, 0, 1) + IF(third_runner IS NULL, 0, 1) >= 3
        AND RUNS = 0
        AND year_id = 2016
GROUP BY pitcher