import streamlit as st


def display_work_experience(year):
    if year <= 2019:
        st.subheader("Assistant Business Manager - PTCL (Jan 2017- Aug 2020)")
        st.write("- Consulting with marketing department to identify high churn, potential and declining areas via SQL, Python and Geo spatial mappings.")
        st.write("- Applied predictive analytics and machine learning to model future sales, churn, and faults statistically.")
    elif year > 2019 and year < 2021:
        st.subheader("Manager Special Projects - PTCL (Sept 2020 - April 2021)")
        st.write("- Interpret patterns and trends to improve business and operational opportunities.")
        st.write("- Develop market analysis for opportunities, analysing and targeting growth for potential clients via machine learning.")
        st.write("- Drive marketing data using data science for actionable data driven marketing analytics")
    elif year > 2020 and year < 2023:
        st.subheader("Data Scientist Intern - PwC Deutschland (Sept 2022 - Feb 2023)")
        st.write("- Developing explainable AI (XAI) code and platform for improving business trust on machine learning based solutions in R & Python.")
        st.write("- Implementing predictive analytics and statistical solutions for forecasting product.")
        st.write("- Evaluating and improving existing machine learning model to improve predicting metrics.")
        st.write("- Optimizing machine learning pipeline using PySpark and parallelization.")
        st.write("- Implementing forecasting solutions in Palantir Foundry platform")
        st.write(" ")
        st.subheader("Data Scientist WerkStudent - Novuter GmbH (Sept 2021 - August 2022)")
        st.write("- Create competitive intelligence dashboard by mining , cleaning, and transforming data from various sources.")
        st.write("- Probabilistic and Bayesian modelling for product trend forecast.")
        st.write("- Data mining and Advance SQL Scripting for analysis.")
        st.write("- Convert data into analytical & actionable insights by predictive analytics and forecasting.")
        st.write("- Python Development and Database Management.")
    else:
        st.subheader("Data Scientist Endress+Hauser(Sept 2023 -present)")
        st.subheader("Data Scientist - Master's Thesis (March 2023 - Aug 2023)")
        st.write("- Developed and implemented Deep Learning models, specifically Autoencoders, to detect fraudulent transactions in SAP")
        st.write("- Conducted thorough Exploratory Data Analysis (EDA) to gain insights and leveraged advanced techniques in anomaly detection and unsupervised learning to improve the accuracy of fraud detection.")
        st.write("- Spearheaded a project focused on fine tuning the ChatGPT model using Azure ML and Azure OpenAI modules to train an internal Large Language Model (LLM) tailored for extracting valuable \
        insights for the company. Also Implemented Azure Cognitive Search and Vector Search Solution to improve LLM based on Retrieval-augmented generation - RAG.")
        st.write("- Developed a user friendly frontend using Streamlit and Fiori app in SAP, enabling seamless access and utilization of the trained LLM by both technical and non technical users.")