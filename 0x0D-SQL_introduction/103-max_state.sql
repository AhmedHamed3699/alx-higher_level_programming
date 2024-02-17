-- MAX Temperature
-- Query to display the top 3 of cities temperature during July and August
SELECT
  state,
  MAX(value) AS max_temp
FROM
  temperatures
GROUP BY
  state
ORDER BY
  state ASC;
