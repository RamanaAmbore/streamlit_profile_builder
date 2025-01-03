

import plotly.express as px
import streamlit as st


def create_horizontal_bar_chart(data, title):
    fig = px.bar(data, x="Percentage", y="Skill", orientation="h")
    fig.update_layout(title_text=title, showlegend=False)
    return fig


def display_project_details(project): #use a dict to hold all projects and then
    data_dict = {
      'Project 1: Finetuning ChatGPT via Azure OpenAI':['Successfully led a transformative project focused on finetuning the ChatGPT model via Azure OpenAI modules to train a powerful internal Larg e Language Model (LLM). \
      This LLM was specifically d esigned to extract valuable insights for our company, revolutionizing our decision making processes.'],
       'Project 2: Integrating ChatGPT with Azure Cognitive Search and Langchain':['Creating a vector search via Azure Cognitive Search for in context learning of ChatGPT model for enterprise level solution and adding \
       Langchain for semantic search and retrieval to create a high performing , finetuned ChatGPT for organization level usage with minimalistic hallucinations'],
       'Project 3: Movie Recommendation System on Big Data':['Injecting and processing data into MS SQL studio via python and ORM architecture of SQLAlchemy Connecting the database remotely via Streamlit API to create web app \
        on MovieLens 25 million ratings dataset.', \
        "images/mov1.PNG", "images/mov2.PNG", "images/mov3.PNG"],
       'Project 4: Electric Vehicle Mobility detection':['Classify state of EV based on yearly data for several models and types of EV using data from emobpy and ACN and identifying data drift.', \
       "images/ev1.JPG", "images/ev2.JPG", "images/ev3.JPG"],
       'Project 5: UnConstrained optimization using PSO':['Implemented solution for un constrained optimizations using particle swarm algorithm.'],
       'Project 6: Object detection using transfer learning':['Created Traffic sign detection and classificat ion model using Inception ResnetV2 and VGG16', \
       "images/obj1.PNG", "images/obj2.PNG", "images/obj3.PNG"],
       'Project 7: Feature Selection via Boruta':['Implemented Boruta paper for feature selection based on entropy of decision tree classifiers and regressors.'],
       'Project 8: Explainable AI (XAI) and Palantir Foundry':['Developing and improving explainable AI module for PwC to improve customer trust in artificial intelligence and machine learning based solution to explain \
        how different drivers impact the decision. Also developed and deployed AI & ML solutions via Palantir Foundry platform specialized for time series and forecasting problems.'],
       'Project 9: Predicting Defaulters Based on Previous Payments':['A classical ML classification project done on Microsoft Azure, where I built two solutions one via AutoML and other with finetuning tree based models\
       to precisely predict defaulters based on previous payment patterns. I ensured fair ML practice by elimination algorithmic bias.', "images/az1.PNG", "images/az2.PNG", "images/az3.PNG"],
       'Project 10: Human Activity Recognition(HAR)':["Completed this project as part of IBM's Advance Data Science Capstone, I used deeplearning to recognize human activity via sensor data", \
        "images/har1.PNG", "images/har2.PNG", "images/har3.PNG"],
       'Project 11: Analyzing Spatial Business Opportunites via Follium':['Part of IBM Data Science certification, I created this dataset on my own using public data from Govt. of Paikstan and using Follium API to understand \
       trends and happenings in different areas of city, combined with spatial analysis to suggest prominent business opportunites in the city.', \
       "images/fol1.PNG", "images/fol2.PNG", "images/fol3.PNG"],
       'Project 12: Soccer Anyalsis':['A fun project to test some Visualization skills with my favorite game', "images/soc1.PNG", "images/soc2.PNG", "images/soc3.PNG"]

    }
    chart_dict = {
      'Project 1: Finetuning ChatGPT via Azure OpenAI':[["Python", "Machine Learning", "NLP", "Microsoft Azure", "OpenAI", "Data preprocessing", "Ethics and Bias Consideration"], [90, 80, 80, 100, 80, 90, 90]],
       'Project 2: Integrating ChatGPT with Azure Cognitive Search and Langchain':[["Azure Cognitive Search", "LangChain", "Vector & semantic search",  "Python", "API Integration", "JSON", "Project Management"], \
       [100, 85, 85, 80, 80, 80, 80]],
       'Project 3: Movie Recommendation System on Big Data':[["PySpark", "SQLAlchemy", "RDBMS", "Machine Learning", "Dashboard", "Matrix Factorization", "Feature Engineering", "Scalability and Performance", \
       "Parallel Computing", "Data Mining"], [90, 85, 90, 90, 90,80, 85, 90, 80, 80]],
       'Project 4: Electric Vehicle Mobility detection':[["Python", "Machine Learning", "Predictive Modeling", "Statistical Analysis", "Time Series Analysis"], [80, 80, 80, 90, 90]],
       'Project 5: UnConstrained optimization using PSO':[["Python", "Algorithm Design and Analysis", "Numerical Optimization", "Fitness Function Design", "Convergence Analysis"], [85, 90, 85, 100, 100]],
       'Project 6: Object detection using transfer learning':[["Computer Vision", "Deep Learning", "Data Annotation", "Transfer Learning", "Model Fine-Tuning"], [90, 80, 75, 90, 90]],
       'Project 7: Feature Selection via Boruta':[["Python", "Statistical Significance Testing", "Model Interpretability", "Hyperparameter Tuning", "Boruta Algorithm"], [70, 80, 90, 80, 80]],
       'Project 8: Explainable AI (XAI) and Palantir Foundry':[["Python", "R", "Explainable AI (XAI)", "Palantir Foundry", "Model Explanation Techniques", "Ethical AI"], [80, 80, 90, 80, 75, 70]],
       'Project 9: Predicting Defaulters Based on Previous Payments':[["Python", "Machine Learning", "Data Analysis", "Feature Engineering", "Imbalanced Data Handling"], [70, 80, 70, 75,80]],
       'Project 10: Human Activity Recognition(HAR)':[["Python", "Deep Learning", "Statistical Analysis", "Time Series Analysis"], [80, 80, 85, 80]],
       'Project 11: Analyzing Spatial Business Opportunites via Follium':[["Python", "Follium", "Machine Learning", "Geospatial Analysis", "Spatial Data Processing"], [85, 80, 80, 85, 75]],
       'Project 12: Soccer Anyalsis':[["Python", "Data Analysis", "Data Visualization", "JSON"], [80, 80, 75, 70]]

    }

    details_list = data_dict[project]
    plot_list = chart_dict[project]
    datap = {"Skill": plot_list[0], "Percentage": plot_list[1]}

    if len(details_list) <= 1:
        cold,cole = st.columns(2)

        with cold:
            st.subheader("Description:")
            st.write(details_list[0])
        with cole:
            chart1 = create_horizontal_bar_chart(datap, "Skills Used")
            st.plotly_chart(chart1, config={"displayModeBar": False}, use_container_width=True)

    if len(details_list) > 1:
        cold,cole = st.columns(2)

        with cold:
            st.subheader("Description:")
            st.write(details_list[0])
            chart1 = create_horizontal_bar_chart(datap, "Skills Used")
            st.plotly_chart(chart1, config={"displayModeBar": False}, use_container_width=True)

        with cole:
            st.image(details_list[1])
            st.image(details_list[2])
            st.image(details_list[3])