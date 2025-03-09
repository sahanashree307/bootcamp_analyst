SELECT Year, Country, total_phones
FROM (
    SELECT Year, Country, SUM(cell_phones) AS total_phones,
           RANK() OVER (PARTITION BY Year ORDER BY SUM(cell_phones) DESC) AS rnk
    FROM cell_phones_final
    GROUP BY Year, Country
) ranked
WHERE rnk = 1;
