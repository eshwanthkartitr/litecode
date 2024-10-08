SELECT 
    query_name,
    ROUND(AVG(rating::numeric / position), 2) AS quality,
    ROUND(100.0 * SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*), 2) AS poor_query_percentage
FROM 
    Queries
GROUP BY 
    query_name
Having 
    query_name is not null