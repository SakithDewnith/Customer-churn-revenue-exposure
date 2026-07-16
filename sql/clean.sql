-- make duplicate of raw table 
CREATE TABLE churn_cleaned AS
SELECT *
FROM churn;

-- When total charge is null at evry situation tenure is 0. that means new user that not fulfill first month
UPDATE churn_cleaned
SET total_charges = 0
WHERE total_charges IS NULL;

