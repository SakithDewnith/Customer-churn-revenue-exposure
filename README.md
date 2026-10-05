# Customer Churn & Revenue Exposure Analytics
🚀 Live Demo: https://sakith-churn-analysis-dashboard.streamlit.app/

## Executive Summary

Customer churn is a common problem for telecom businesses. A high churn rate tells us there is a problem, but it doesn't tell us where the biggest impact is. The business needs to know which customer groups have the highest potential revenue exposure so retention efforts can be focused where they matter most.

Using SQL, Python (Pandas), and Power BI, I analyzed 7,043 customer records and found that 26.5% of customers had already churned.

I then screened **17 customer attributes across their different customer groups** to find the areas showing the strongest churn patterns and potential revenue impact. This narrowed the analysis to **Contract Type, Internet Service, and Payment Behaviour**.

Next, I identified the priority segment within each of these three areas and estimated the potential monthly revenue exposure among their active customers.

I then looked deeper into these priority segments, using the remaining customer attributes to find the subcategories with the highest potential revenue exposure and highlight areas worth investigating for retention.



Key focus areas include:

- Understand past customer churn and identify the groups with the highest churn rates

- Estimate potential monthly revenue exposure among currently active customers

- Investigate the customer characteristics behind higher churn and revenue exposure

- Highlight retention opportunities based on potential business impact
  
<br>

Customer Risk Analysis & Retention Workflow:
  
<br>
  <p align="center">
  <img 
    width="524" 
    height="100" 
    alt="Gemini_Generated_Image_g3te9bg3te9bg3te" 
    src="https://github.com/user-attachments/assets/24c919d4-67e4-425a-9e02-b8e4f0eb60e8"
  />
</p>

<br>
  
## Business Problem:

Customer retention is essential for this telecom company, since recurring monthly charges are directly tied to revenue. With a limited retention budget, **which customer segments have the highest churn, where is the most revenue at risk, and what should we focus on first?**


## Methodology:
1. Clean and prepare the data with SQL and Python (Pandas).
2. Screen factors by churn-rate gap between categories, then check revenue exposure and business actionability
3. Prioritize segments within each focus factor using churn rate, active customers, and active revenue.
4. Analyze associated characteristics inside each priority segment, applying a minimum sample size.
5. Visualize the results in an interactive Power BI dashboard.

## Skills:
SQL (PostgreSQL): Data exploration(EDA), data cleaning, validation checks, aggregation, conditional aggregation (FILTER), GROUP BY analysis, calculated metrices

Python: Pandas, customer segmentation, factor screening, churn analysis, revenue exposure estimation, driver analysis, data visualization

Power BI: DAX measures, data modeling, interactive filtering, KPI cards, data visualization

## Results:
**Overall:** Of 7,043 customers, **26.5%** had churned, with **$139.1K** in monthly charges associated with churned customers.

**Factor screening:** 

We started with 17 customer attributes and compared churn rates across the categories of each one. We then looked for factors that:

1. show a large difference in churn between their categories,
2. contain a category with high estimated monthly revenue exposure,
3. have enough customers in each category to make the comparison meaningful, and
4. represent a business area the company can act on.

Based on these criteria, **Contract Type, Internet Service, and Payment Behaviour** were selected as focus factors, representing contracts, services, and billing/payment.**Contract Type** showed the widest churn spread, from **2.83% (Two-year) to 42.71%** (Month-to-month).

**Priority segments:** 
| Focus Factor | Priority Segment | Churn Rate | Active Customers | Est. Monthly Exposure |
|---|---|---:|---:|---:|
| Contract Type | Month-to-month | 42.71% | 2,220 | $58.3K |
| Internet Service | Fiber optic | 41.89% | 1,799 | $70.8K |
| Payment Behaviour | Electronic check | 45.29% | 1,294 | $43.5K |

- Exposure figures are shown separately for each focus factor and may overlap because the same customer can belong to multiple priority segments. They should not be added together.

**Deeper analysis:** After selecting the priority segments, we looked inside each one at the other customer characteristics. We looked for categories that:

1. have higher churn than the average for that priority segment,
2. have high estimated monthly revenue exposure, and
3. have enough customers to make the comparison meaningful.

These characteristics are associated with higher churn and highlight areas worth investigating for retention actions.

**Dashboard:** An interactive Power BI dashboard allows users to explore each focus factor and priority segment through **churn rate, estimated monthly revenue exposure, and driver-level subcategory analysis**.


<br>
<p align="center">
  <img 
    width="600" 
    height="390" 
    alt="image" 
    src="https://github.com/user-attachments/assets/bfd72051-6f91-42f8-b359-b5d5cde2dc38"
  />
</p>
<br>

## Business Recommend actions:

- Prioritize retention strategies for high-exposure Month-to-month customers.
- Test contract upgrade offers to encourage longer-term customer commitment.
- Test Tech Support and Online Security adoption campaigns for customers with identified service gaps.
- Measure retention impact through controlled experiments and continuously monitor future revenue exposure trends.
