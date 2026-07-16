-- Understand data with there types
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'churn';

-- Check missing total charges
SELECT COUNT(*)
FROM churn
WHERE total_charges IS NULL;

-- Check duplicates
SELECT customer_id, COUNT(*)
FROM churn
GROUP BY customer_id
HAVING COUNT(*) > 1

-- check unique values in churn
SELECT DISTINCT churn 
FROM churn;

-- Check unique contract types
SELECT DISTINCT contract 
FROM churn;

-- Check total charges values are valid
SELECT COUNT(*) FROM churn WHERE total_charges<0;

-- Check tenure where total charges are 0
SELECT tenure, monthly_charges, total_charges
FROM churn_cleaned
WHERE total_charges IS NULL;