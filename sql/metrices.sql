-- Calculate the headline metrics. Factor screening and category metrics are done in Python.

-- Total customers
SELECT COUNT(*) AS total_customers
FROM churn_cleaned;

-- Churned customers
SELECT COUNT(*) AS churned_customers
FROM churn_cleaned
WHERE churn = 'Yes';

-- 3. Active customers
SELECT COUNT(*) AS active_customers
FROM churn_cleaned
WHERE churn = 'No';

-- Historical churn rate
SELECT 
    ROUND(
        COUNT(*) FILTER (WHERE churn = 'Yes') * 100.0 
        / COUNT(*), 
        2
    ) AS churn_rate
FROM churn_cleaned;

-- Monthly charges from churned customers (historical)
SELECT SUM(monthly_charges) AS monthly_charges_churned
FROM churn_cleaned
WHERE churn = 'Yes';

-- Active monthly revenue
SELECT SUM(monthly_charges) AS active_monthly_revenue
FROM churn_cleaned
WHERE churn = 'No';
