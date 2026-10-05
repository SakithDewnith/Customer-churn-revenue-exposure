-- Understand the RAW table (churn).

-- 1. Row count
SELECT COUNT(*) AS total_rows 
FROM churn;

-- Understand data with there types
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'churn';

-- Check missing total charges
SELECT COUNT(*)
FROM churn
WHERE total_charges IS NULL;

-- Check missing monthly charges
SELECT COUNT(*)
FROM churn
WHERE monthly_charges IS NULL;

-- Check negative monthly charges
SELECT COUNT(*)
FROM churn
WHERE monthly_charges < 0;

-- Check negative total charges
SELECT COUNT(*) 
FROM churn 
WHERE total_charges<0;

-- Check missing total charges with tenure and monthly charges
SELECT tenure, monthly_charges, total_charges
FROM churn
WHERE total_charges IS NULL;

-- Check duplicates
SELECT customer_id, COUNT(*)
FROM churn
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- Check missing churn labels
SELECT COUNT(*)
FROM churn
WHERE Churn IS NULL;

-- Check churn labels and there counts
SELECT Churn, COUNT(*)
FROM churn
GROUP BY Churn;