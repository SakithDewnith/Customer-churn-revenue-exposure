# Customer Retention & Revenue Exposure Analytics
🚀 Live Demo: https://sakith-churn-analysis-dashboard.streamlit.app/

## Executive Summary

Customer churn can create significant future revenue risk, but not all customer groups have the same financial impact. This project focuses on identifying where the largest future revenue exposure exists among active customers by analyzing historical churn behaviour and customer characteristics.

Using an **end-to-end analytics workflow with SQL, Python, and Streamlit**, I analyzed customer data to estimate potential revenue exposure, identify the highest-risk customer segments, and uncover the factors contributing to revenue risk. The analysis identified **Month-to-month customers as the largest future revenue exposure segment**, with **missing Tech Support and Online Security services as key exposure drivers**.

Key focus areas include:

- Identifying customer segments with the highest future revenue exposure

- Understanding the main factors contributing to revenue risk

- Prioritizing retention opportunities based on potential business impact
  
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

Customer churn creates future revenue risk, but not all customer segments have the same financial impact. With limited retention resources, the business needs to identify which active customer segments carry the highest future revenue exposure and what factors drive that risk. How can historical churn behaviour be used to estimate future revenue exposure and prioritize retention efforts where they will have the greatest business impact?

## Methodology:
1. SQL queries were used to clean, transform, and analyze customer data from the database.
2. Python was used for churn analysis, customer segmentation, and revenue exposure estimation.
3. A Streamlit dashboard was developed to provide visibility into risk segments, churn drivers, and retention opportunities.

## Skills:
SQL: Data cleaning, joins, filtering, aggregation, analytical queries

Python: Pandas, customer segmentation, churn analysis, revenue exposure analysis, exploratory data analysis (EDA), data visualization

Streamlit: Dashboard development, KPI reporting, Plotly visualizations, business insights

## Results:
The analysis evaluated **7,043 customer records** and identified a **26.5% historical churn rate**, highlighting potential future revenue risk among active customers. By applying historical churn behaviour to the active customer base, the analysis identified **Month-to-month customers as the highest future revenue exposure segment**, with a **42.71% churn rate, 2,220 active customers, and $58K+ projected monthly revenue exposure.**

Further analysis within this priority segment identified customers **without Tech Support ($93K+ projected exposure) and Online Security ($91K+ projected exposure)** as the largest revenue risk drivers. These findings allow retention efforts to be focused on customer groups where reducing churn could have the greatest financial impact.

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
