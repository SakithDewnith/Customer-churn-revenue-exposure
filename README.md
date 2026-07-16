# Customer Retention & Churn Risk Analytics for Telecom
## Executive Summary:

Customer churn directly impacts recurring revenue, and the company needs to identify which customer groups contribute most to revenue loss and where retention efforts should be focused. Using SQL and Python, I analyzed 7,043 customer records, segmented customers by contract, tenure, and payment behavior, and performed churn driver analysis to identify high-impact retention opportunities.

The analysis identified Month-to-month customers as the highest-impact segment, accounting for $120.8K in historical monthly revenue loss with a 42.71% churn rate. Further analysis revealed that customers without Online Security and Tech Support were associated with over $102K each in historical monthly revenue loss, while active customers with these risk characteristics represented significant future revenue exposure.

Based on these findings, I recommend:

Increasing adoption of Online Security and Tech Support services among Month-to-month customers.
Providing incentives to move customers toward longer-term contracts.
Investigating Fiber optic customer experience issues.
Implementing targeted retention campaigns for high-risk customer groups.

## Business Problem:
Customer retention is essential for this telecom company since recurring customers directly contribute to monthly revenue. Business stakeholders have noticed a high customer churn rate and need to understand which customer groups are driving revenue loss and where retention efforts should be focused.

How can we identify the customer segments contributing the most to churn-related revenue loss, determine the key factors associated with customer attrition, and identify current customers who represent potential future revenue exposure to improve retention strategies?

## Methodology:
SQL Analysis:Extracted and cleaned customer subscription data.
Calculated churn rate, customer counts, and monthly recurring revenue impact.
Segmented customers by contract type, tenure, and payment method.
Identified the highest-impact customer segments.

Python Analysis:Performed exploratory data analysis using Pandas.
Analyzed churn rates across service features and payment behavior.
Evaluated historical revenue loss among churned customers.
Estimated future revenue exposure among active customers based on historical churn patterns.

## Skills:
SQL: Data cleaning, Aggregations, CASE statements, GROUP BY analysis, Customer segmentation, Revenue calculations

Python:Pandas, NumPy, Data transformation, Exploratory data analysis, Customer segmentation, Business impact analysis

## Results & Business Recommendations:
Identified Month-to-month customers as the highest-impact segment, accounting for $120.8K in historical monthly revenue loss with a 42.71% churn rate, making them the primary retention target.

Found key churn drivers within the priority segment, where customers without Online Security and Tech Support were associated with over $102K each in historical monthly revenue loss, indicating major service adoption gaps.

Estimated future revenue exposure among active customers, identifying $93K+ exposed revenue from customers lacking Tech Support and $91K+ from customers lacking Online Security based on historical churn patterns.

Recommended targeted retention strategies, including increasing service adoption through Online Security and Tech Support offers, encouraging longer-term contracts, and investigating Fiber optic customer experience issues.

## Next Steps:

- Develop a churn prediction model to identify individual customer-level churn risk scores.
- Perform A/B testing on retention offers and service bundle promotions to measure impact on churn reduction.
- Monitor customer retention metrics after implementing targeted campaigns.
- Analyze customer feedback and service usage patterns to identify additional churn prevention opportunities.
