# Write your MySQL query statement below
SELECT product_id
FROM Products as a
WHERE a.low_fats = 'Y' AND a.recyclable = 'Y'