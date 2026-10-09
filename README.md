# Customer Churn & Revenue Exposure Analytics
🚀 Live Demo: https://sakith-churn-analysis-dashboard.streamlit.app/

## Power BI Dashboard

The Power BI dashboard provides an interactive view of customer churn, estimated monthly revenue exposure, priority segments, and associated churn patterns.

![Customer Retention & Churn Risk Analytics Dashboard](dashboard/customer-churn-dashboard.png)

> **Power BI file:** [`Customer-Churn-Dashboard.pbix`](dashboard/Customer-Churn-Dashboard.pbix)

The `.pbix` file is included in the repository for review and can be opened in **Power BI Desktop**.


## Executive Summary
Customer churn is a common problem for telecom businesses. A high churn rate tells there is a problem, but it doesn't tell us where the biggest impact is. The business needs to know which customer groups have the highest potential revenue exposure so retention efforts can be focused where they matter most.

Using **SQL, Python (Pandas), and Power BI**, I analyzed 7,043 customer records and found that 26.5% of customers had already churned.

I then screened **17 customer attributes across their different customer groups** to find the areas showing the strongest churn patterns and potential revenue impact. This narrowed the analysis to **Contract Type, Internet Service, and Payment Behaviour**.

Next, I identified the priority segment within each of these three areas and estimated the potential monthly revenue exposure among their active customers.

Finally, I examined each priority segment from different angles by selecting one customer characteristic at a time, comparing each subgroup’s churn rate with the overall churn rate of that priority segment, and estimating the monthly revenue exposure for each subgroup.


Key focus areas include:

- Understand past customer churn and identify the groups with the highest churn rates

- Estimate potential monthly revenue exposure among currently active customers

- Investigate the customer characteristics associated with higher churn and revenue exposure

- Highlight retention opportunities based on potential business impact
  
<br>

Workflow:
  
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

2. **Screen factors** by apply four screening criteria
      - **Churn gap:** highest minus lowest category churn rate (cutoff: 30 points),
      - **Revenue exposure:** the highest category's estimated monthly exposure (cutoff: $40K),
      - **Group size:** every category has at least 682 customers, so small groups do not distort the results, and
      - **Actionability:** whether the company can act on it.

3. **Validate findings** Cross-checked the screening results using Cramér's V and a logistic regression (permutation importance).

4. **Select focus factors** Selected one factor from each business area based on the evidence and its potential for business action.

5. **Prioritize one segment** within each focus factor using churn rate, active customers, and active revenue.

6. **Run a driver analysis**
   - **Benchmark:** Compared each subgroup’s churn rate with its priority segment’s overall churn rate.
   - **Selection criteria:** Retained subgroups with at least 100 customers, a 95% confidence interval entirely above the segment’s churn rate, and actionable characteristics. Excluded Gender, Senior Citizen, Partner, and Dependents.
   - **Ranking:** Ranked qualifying subgroups by estimated monthly revenue exposure and reported the top three per segment. This reflects revenue exposure, not driver importance.
   - **Double-counting:** Exposure values should not be added together because customers may appear in subgroups across different drivers.

7. **Visualize** the results in an interactive Power BI dashboard.

**Estimated monthly revenue exposure** = active monthly revenue × historical churn rate of the group.

## Skills:
**SQL**: PostgreSQL, Data exploration(EDA), data cleaning, validation checks, aggregation, conditional aggregation (FILTER), GROUP BY analysis, calculated metrices

**Python**: Pandas, Matplotlib, SciPy and scikit-learn (Cramér's V, logistic regression cross-check), customer segmentation, factor screening, churn analysis, revenue exposure estimation, driver analysis, data visualization

**Power BI**: DAX measures, data modeling, interactive filtering, KPI cards, data visualization

## Results:
**Overall:** Of 7,043 customers, **26.5%** had churned, with **$139.1K** in monthly charges from churned customers.

After screening 17 customer attributes, **Contract Type, Internet Service, and Payment Behaviour** were selected based on their churn patterns and potential revenue impact. 

Contract Type showed the widest churn gap, ranging from 2.83% for Two-year contracts to 42.71% for Month-to-month contracts.

**Priority segments:** 
| Focus Factor | Priority Segment | Churn Rate | Active Customers | Est. Monthly Exposure |
|---|---|---:|---:|---:|
| Contract Type | Month-to-month | 42.71% | 2,220 | $58.3K |
| Internet Service | Fiber optic | 41.89% | 1,799 | $70.8K |
| Payment Behaviour | Electronic check | 45.29% | 1,294 | $43.5K |

- Exposure figures are shown separately for each focus factor and may overlap because the same customer can belong to multiple priority segments. They should not be added together.

**Driver analysis:** 
| Group | Subgroup inside it | Share who left | Higher than the group by | Monthly revenue at stake |
|---|---|---:|---:|---:|
| **Month-to-month** (43% left) | Without Tech Support | 50% | 1.18× | about $46.9K |
| | Without Online Security | 51% | 1.20× | about $46.5K |
| | On fiber optic internet | 55% | 1.28× | about $46.3K |
| **Fiber optic** (42% left) | Using paperless billing | 45% | 1.06× | about $55.9K |
| | Without Online Security | 49% | 1.18× | about $51.0K |
| | Without Tech Support | 49% | 1.18× | about $49.7K |
| **Electronic check** (45% left) | On fiber optic internet | 53% | 1.18× | about $36.6K |
| | Using paperless billing | 50% | 1.10× | about $34.3K |
| | Without Online Security | 53% | 1.17× | about $33.5K |


- **Month-to-month:** Customers without Tech Support have the highest estimated revenue exposure ($46.9K/month), while customers using fiber optic internet have the highest churn rate (55%).
- **Fiber optic:** Customers using paperless billing have the highest exposure ($55.9K/month), while customers without Online Security or Tech Support also show higher churn.
- **Electronic check:** Customers using fiber optic internet have the highest exposure ($36.6K/month), with a churn rate of 53%.
- **Common pattern:** Customers without Online Security appear among the top three subgroups in all three segments, while customers without Tech Support appear in two. Both are worth investigating for retention opportunities.

The same customer can appear in more than one row, because the groups and their subgroups overlap, so the revenue amounts are **not added together**. These are patterns associated with higher churn, not proven causes.

**Dashboard:** An interactive Power BI dashboard allows users to explore each focus factor and priority segment through **churn rate, estimated monthly revenue exposure, and driver-level subcategory analysis**.

## Business Recommended Actions

The following are proposed actions based on the analysis and have not been tested in practice.

| Target group | Recommended action |
|---|---|
| Month-to-month customers using fiber optic internet | Test incentives to encourage switching to longer-term contracts. |
| Month-to-month and Fiber optic customers without Tech Support | Test targeted retention offers for customers who do not use Tech Support. |
| Customers without Online Security across the three priority segments | Test free trials or bundled service offers and measure their effect on retention. |
| Electronic check customers using fiber optic internet | Investigate retention offers, as this subgroup has the highest estimated monthly revenue exposure within the Electronic check segment. |
| Fiber optic customers using paperless billing | Investigate further before targeting this group, as its churn rate is only slightly above the segment average. |

**First step:** Pilot a contract-switching offer for month-to-month customers using fiber optic internet over 2–3 months. Compare their churn with a similar group that does not receive the offer. Expand the offer only if the reduction in churn generates enough additional revenue to justify the cost.

## Limitations
- Findings are descriptive and show association, not cause.
- Estimated exposure applies each group's **historical churn rate, held constant**, to today's active customers. It is an estimate, not a forecast, because future churn may differ.
- - Thresholds (100 customers, 95% interval, $40K, 30 points) are chosen screening rules, not universal standards.
- Cost and feasibility of the recommended actions were not assessed.
