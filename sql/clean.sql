-- Creates a cleaned copy of the raw churn table and cleans the data.

-- make duplicate of raw table 
CREATE TABLE churn_cleaned AS
SELECT *
FROM churn;

-- When total charge is null at evry situation tenure is 0. that means new user that not fulfill first month
UPDATE churn_cleaned
SET total_charges = 0
WHERE total_charges IS NULL;

-- Check rows where total_charges was replaced with 0, with their tenure
SELECT tenure, monthly_charges, total_charges
FROM churn_cleaned
WHERE total_charges = 0;