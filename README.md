# Customer Churn & Revenue Exposure Analytics
🚀 Live Demo: https://sakith-churn-analysis-dashboard.streamlit.app/

## Executive Summary
Customer churn is a common problem for telecom businesses. A high churn rate tells us there is a problem, but it doesn't tell us where the biggest impact is. The business needs to know which customer groups have the highest potential revenue exposure so retention efforts can be focused where they matter most.

Using **SQL, Python (Pandas), and Power BI**, I analyzed 7,043 customer records and found that 26.5% of customers had already churned.

I then screened **17 customer attributes across their different customer groups** to find the areas showing the strongest churn patterns and potential revenue impact. This narrowed the analysis to **Contract Type, Internet Service, and Payment Behaviour**.

Next, I identified the priority segment within each of these three areas and estimated the potential monthly revenue exposure among their active customers.

I then looked deeper into these priority segments, using the remaining customer attributes to find the subcategories with the highest potential revenue exposure and highlight areas worth investigating for retention.


Key focus areas include:

- Understand past customer churn and identify the groups with the highest churn rates

- Estimate potential monthly revenue exposure among currently active customers

- Investigate the customer characteristics associated with higher churn and revenue exposure

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

## Methodology

1. **Clean and prepare** the data with SQL and Python (Pandas).
2. **Group** the 17 attributes by business area, then compare each factor's churn gap, estimated revenue exposure, and customer counts.
3. **Cross-check** the screening with Cramér's V and a logistic regression (permutation importance).
4. **Choose one factor per business area** based on the evidence and what the company can act on.
5. **Prioritize one segment** within each focus factor using churn rate, active customers, and active revenue.
6. **Run a driver analysis** inside each priority segment: one characteristic at a time, compared with the segment's own churn rate.
7. **Visualize** the results in an interactive Power BI dashboard.

**Estimated monthly revenue exposure** = active monthly revenue × historical churn rate of the group.


## Skills:
SQL (PostgreSQL): Data exploration(EDA), data cleaning, validation checks, aggregation, conditional aggregation (FILTER), GROUP BY analysis, calculated metrices

Python: Pandas, Matplotlib, SciPy and scikit-learn (Cramér's V, logistic regression cross-check), customer segmentation, factor screening, churn analysis, revenue exposure estimation, driver analysis, data visualization

Power BI: DAX measures, data modeling, interactive filtering, KPI cards, data visualization

## Results:
**Overall:** Of 7,043 customers, **26.5%** had churned, with **$139.1K** in monthly charges from churned customers.

**Factor screening:** We started with 17 customer attributes, grouped them by business area, and compared:

1. **Churn gap:** highest minus lowest category churn rate (cutoff: 30 points),
2. **Revenue exposure:** the highest category's estimated monthly exposure (cutoff: $40K),
3. **Group size:** every category has at least 682 customers, so small groups do not distort the results, and
4. **Actionability:** whether the company can act on it.

The ranking was cross-checked with Cramér's V and a logistic regression, which placed the same factors in the top tier. **Contract Type, Internet Service, and Payment Behaviour** were selected, one per business area (contracts, service, billing). Contract Type showed the widest churn spread, from **2.83% (Two-year) to 42.71%** (Month-to-month). Tenure is a supporting factor, because it overlaps with Contract Type and cannot be changed by the company.

**Priority segments:** 
| Focus Factor | Priority Segment | Churn Rate | Active Customers | Est. Monthly Exposure |
|---|---|---:|---:|---:|
| Contract Type | Month-to-month | 42.71% | 2,220 | $58.3K |
| Internet Service | Fiber optic | 41.89% | 1,799 | $70.8K |
| Payment Behaviour | Electronic check | 45.29% | 1,294 | $43.5K |

- Exposure figures are shown separately for each focus factor and may overlap because the same customer can belong to multiple priority segments. They should not be added together.

**Driver analysis:** A driver is another customer characteristic. Inside each priority segment, we checked one driver at a time and compared its subgroups with the segment's own churn rate. We kept subgroups that:

1. have churn clearly above the segment rate,
2. have estimated monthly exposure above the median for that driver, and
3. have at least 100 customers.

| Segment | Subgroup inside it | Share who left | Est. monthly exposure |
|---|---|---:|---:|
| **Month-to-month** (42.71%) | Without Tech Support | 50.37% | $46.9K |
| | Without Online Security | 51.05% | $46.5K |
| | Fiber optic | 54.61% | $46.3K |
| **Fiber optic** (41.89%) | Without Online Security | 49.36% | $51.0K |
| | Without Tech Support | 49.37% | $49.7K |
| | Month-to-month | 54.61% | $46.3K |
| **Electronic check** (45.29%) | Fiber optic | 53.23% | $36.6K |
| | Without Online Security | 53.17% | $33.5K |
| | Without Tech Support | 53.18% | $33.0K |

New customers paying by electronic check had the highest rate (61.96%), but with smaller exposure ($14.5K).

Categories within a driver do not overlap, but drivers overlap with each other, so exposure values are **not added across drivers**. These characteristics are associated with higher churn and are not proven causes.

**Dashboard:** An interactive Power BI dashboard allows users to explore each focus factor and priority segment through **churn rate, estimated monthly revenue exposure, and driver-level subcategory analysis**.

## Business Recommended Actions

These are **hypotheses to test**, not proven fixes. Cost and feasibility were not assessed.

- Test a contract-upgrade offer, starting with fiber optic Month-to-month customers.
- Test free trials or bundles of Online Security and Tech Support for customers without them.
- Improve the first months for new electronic check customers, and make automatic payment easier.
- Give each customer only one offer at a time, because the groups overlap.
- Run each test against a similar group that gets no offer, and compare churn after 2 to 3 months.

## Limitations

Findings are descriptive and show association, not cause. Exposure applies historical churn to current active customers and is an estimate, not a forecast.
