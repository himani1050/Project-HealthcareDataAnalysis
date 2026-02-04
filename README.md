Missed medical appointments are a major operational and financial challenge for healthcare providers. No-shows lead to:
- Revenue loss
- Underutilized clinical resources
- Increased patient wait times
- Reduced care quality

This project builds an end-to-end healthcare analytics pipeline to analyze patient appointment behavior, identify drivers of missed visits, and provide actionable insights through dashboards and predictive modeling.

Business Objective - 
To help healthcare organizations:
- Identify high-risk patient segments for no-shows
- Evaluate effectiveness of reminder systems
- Optimize appointment scheduling workflows
- Support data-driven healthcare operations decisions

Dataset - Public healthcare appointment dataset (~110K appointment records).

Data Includes:
- Patient demographics
- Chronic disease indicators
- Appointment scheduling behavior
- SMS reminder status
- Attendance outcome (No-Show vs Attended)

* Dataset is public and de-identified.
* Raw dataset is not redistributed in this repository.

Tech Stack - 
- Engineering
- Python (Pandas, NumPy)
- SQL (MySQL)
- ETL Pipeline Design
- Analytics & Modeling
- Feature Engineering
- Logistic Regression (No-Show Risk Prediction)
- Statistical Analysis
- Visualization
- Tableau Dashboard Development
- KPI Reporting
- Business Insight Storytelling

Project Architecture - 
Raw Healthcare Data
        ↓
Data Cleaning & ETL (Python)
        ↓
MySQL Database Storage
        ↓
Feature Engineering Pipeline
        ↓
Exploratory Data Analysis
        ↓
Predictive Modeling
        ↓
Tableau Executive Dashboard

Predictive Modeling - 
- Model Used: Logistic Regression
- Use Case: Patient No-Show Risk Prediction

Tableau Analysis strategy - 
- Trend Analysis: Comparing show vs. no-show rates across time-based variables (Waiting Days).
- Demographic Profiling: Evaluating how age groups and gender influence attendance.
- Socio-Economic Impact: Analyzing the effect of the "Scholarship" (welfare program) on patient reliability.
- Effectiveness of Communication: Measuring the correlation between SMS reminders and actual attendance.
- Geospatial Analysis: Identifying "Hotspots" of no-shows by neighborhood to suggest localized interventions.

Key Analytics KPIs - 
- Total Appointments: 110,521
- Global No-Show Rate: 20.19%.
- Avg. Waiting Time: 9 days.
- Show vs. No-Show Split
- Patient Demographics (Who is missing?)
- Appointment Logistics (Why are they missing?)
- Geographic Context (Top 30)

Key Insights - 
- Waiting Days is the primary driver.
- Young Adults are highest risk.
- The SMS Paradox: Counter-intuitively, the no-show rate for those who received an SMS (27.6%) is higher than those who didn't (16.7%). This suggests SMS is currently being sent to long-lead appointments which are already high-risk.
- Patients enrolled in the Welfare Scholarship program have a higher no-show rate (23.7%) compared to those who are not (19.8%), suggesting possible transport or child-care barriers.
- Regional hotspots: Neighborhoods like SANTOS DUMONT (28.9%) and ITARARÉ (26.2%) show significantly higher no-show rates than the average, warranting targeted outreach programs in these areas.

Dashboard Preview - 
- dashboard link: notebook/AnalysisDashboardLink.txt
- dashboard.jpg

Run Pipeline - 
- ETL: python src/etl.py
- Feature Engineering: python src/feature_engineering.py
- Model Training: python src/model.py

Data & Security Notes - 
- No patient-identifiable data used
- Public dataset only
- Database credentials not stored in repository
- Environment variables recommended for database access



