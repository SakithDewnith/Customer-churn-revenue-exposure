-- Total customers
SELECT COUNT(*) AS total_customers
FROM churn_cleaned;

-- Churned customers
SELECT COUNT(*) AS churned_customers
FROM churn_cleaned
WHERE churn = 'Yes';

-- Churn rate
SELECT 
    ROUND(
        COUNT(*) FILTER (WHERE churn = 'Yes') * 100.0 
        / COUNT(*), 
        2
    ) AS churn_rate
FROM churn_cleaned;

-- Revenue at risk
SELECT 
    SUM(monthly_charges) AS monthly_revenue_at_risk
FROM churn_cleaned
WHERE churn = 'Yes';

-- Churn by contract
SELECT
    contract,
    COUNT(*) AS customers,
    ROUND(
        COUNT(*) FILTER (WHERE churn='Yes') * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM churn_cleaned
GROUP BY contract;

-- Revenue loss by segment
SELECT
    contract,
    SUM(monthly_charges) AS revenue_at_risk
FROM churn_cleaned
WHERE churn='Yes'
GROUP BY contract;