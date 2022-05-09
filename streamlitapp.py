import streamlit as st
import pandas as pd
from st_btn_select import st_btn_select
import matplotlib.pyplot as plt
import tkinter
import seaborn as sns
import altair as alt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

income = pd.read_csv("Poverty_by_Race_and_Ethnicity.csv")

page = st_btn_select(
  # The different pages
  ('Home Page','Poverty by Race'),
  # Enable navbar
  nav=False
)



# Display the right things according to the page
if page == 'Home Page':
    st.image('People.png',use_column_width=True)

    st.write(


# Intro text

    '''
    # Poverty by Race in North Carolina (2013 - 2019)
    '''
    )
    

    
    st.write(
    '''
    Utilizing the public dataset from **[Data USA: North Carolina](https://datausa.io/profile/geo/north-carolina)** the user can explore poverty in North Carolina between the years of 2013 and 2019.
    Does the number of persons in poverty in North Carolina depend on race? Review the visualization on the *Poverty by Race* tab, to determine if race plays a role in poverty.
    
    To fully explore whether race plays and role in education, income, and poverty, please review the R-Shiny app which is made availabe via this **[link.](https://weeksmarian.shinyapps.io/NC_Race/)**
    '''
    )

if page == 'Poverty by Race':
    st.sidebar.write(
    '''
    ### Poverty Population by Race
       
    This visualization displays the counts and percentages of person in poverty by race.

    '''
    )

    st.sidebar.text("")
    st.sidebar.text("")

    st.sidebar.write(
    '''

    *NOTE: These percentages were calculated using the total number of persons in poverty for a given year.* 

    '''
    )
    
    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.text("")


    select_year = st.sidebar.selectbox("Select a year.",[2013,2014,2015,2016,2017,2018,2019])
    
    st.sidebar.text("")
    st.sidebar.text("")


    select_view = st.sidebar.radio("How would you like to view the data?",['Counts','Percentages'])


    new2013 = income[income['Year']== 2013]   
    new2014 = income[income['Year']==2014] 
    new2015 = income[income['Year']==2015]  
    new2016 = income[income['Year']==2016] 
    new2017 = income[income['Year']==2017] 
    new2018 = income[income['Year']==2018] 
    new2019 = income[income['Year']==2019] 


    if select_view == "Counts":
        if select_year == 2013:
            fig, ax = plt.subplots()
            plt.bar(new2013["Race"], new2013["Poverty_Population"], align='center', alpha=0.5)
            plt.ylabel('Count of Persons in Poverty', fontsize = 14)
            plt.xlabel('Race', fontsize = 14)
            plt.title('Poverty Population by Race', fontsize = 20)
            plt.xticks(rotation = 45)

        elif select_year == 2014:
            fig, ax = plt.subplots()
            plt.bar(new2014["Race"], new2014["Poverty_Population"], align='center', alpha=0.5)
            plt.ylabel('Count of Persons in Poverty', fontsize = 14)
            plt.xlabel('Race', fontsize = 14)
            plt.title('Poverty Population by Race', fontsize = 20)
            plt.xticks(rotation = 45)

        elif select_year == 2015:
            fig, ax = plt.subplots()
            plt.bar(new2015["Race"], new2015["Poverty_Population"], align='center', alpha=0.5)
            plt.ylabel('Count of Persons in Poverty', fontsize = 14)
            plt.xlabel('Race', fontsize = 14)
            plt.title('Poverty Population by Race', fontsize = 20)
            plt.xticks(rotation = 45)

        elif select_year == 2016:
            fig, ax = plt.subplots()
            plt.bar(new2016["Race"], new2016["Poverty_Population"], align='center', alpha=0.5)
            plt.ylabel('Count of Persons in Poverty', fontsize = 14)
            plt.xlabel('Race', fontsize = 14)
            plt.title('Poverty Population by Race', fontsize = 20)
            plt.xticks(rotation = 45)

        elif select_year == 2017:
            fig, ax = plt.subplots()
            plt.bar(new2017["Race"], new2017["Poverty_Population"], align='center', alpha=0.5)
            plt.ylabel('Count of Persons in Poverty', fontsize = 14)
            plt.xlabel('Race', fontsize = 14)
            plt.title('Poverty Population by Race', fontsize = 20)
            plt.xticks(rotation = 45)

        elif select_year == 2018:
            fig, ax = plt.subplots()
            plt.bar(new2018["Race"], new2018["Poverty_Population"], align='center', alpha=0.5)
            plt.ylabel('Count of Persons in Poverty', fontsize = 14)
            plt.xlabel('Race', fontsize = 14)
            plt.title('Poverty Population by Race', fontsize = 20)
            plt.xticks(rotation = 45)

        else: 
            fig, ax = plt.subplots()
            plt.bar(new2019["Race"], new2019["Poverty_Population"], align='center', alpha=0.5)
            plt.ylabel('Count of Persons in Poverty', fontsize = 14)
            plt.xlabel('Race', fontsize = 14)
            plt.title('Poverty Population by Race', fontsize = 20)
            plt.xticks(rotation = 45)
        

    else: 
        if select_year ==2013:
            fig,ax = plt.subplots()
            plt.bar(new2013["Race"], new2013["share"]*100, align='center', alpha=0.5)
            plt.ylabel('Percentages by Total Persons in Poverty', fontsize = 14)
            plt.xlabel('Race', fontsize = 14)
            plt.title('Poverty Population by Race', fontsize = 20)
            plt.xticks(rotation = 45)

        elif select_year ==2014:
            fig,ax = plt.subplots()
            plt.bar(new2014["Race"], new2014["share"]*100, align='center', alpha=0.5)
            plt.ylabel('Percentages by Total Persons in Poverty', fontsize = 14)
            plt.xlabel('Race', fontsize = 14)
            plt.title('Poverty Population by Race', fontsize = 20)
            plt.xticks(rotation = 45)

        elif select_year ==2014:
            fig,ax = plt.subplots()
            plt.bar(new2014["Race"], new2014["share"]*100, align='center', alpha=0.5)
            plt.ylabel('Percentages by Total Persons in Poverty', fontsize = 14)
            plt.xlabel('Race', fontsize = 14)
            plt.title('Poverty Population by Race', fontsize = 20)
            plt.xticks(rotation = 45)

        elif select_year ==2015:
            fig,ax = plt.subplots()
            plt.bar(new2015["Race"], new2015["share"]*100, align='center', alpha=0.5)
            plt.ylabel('Percentages by Total Persons in Poverty', fontsize = 14)
            plt.xlabel('Race', fontsize = 14)
            plt.title('Poverty Population by Race', fontsize = 20)
            plt.xticks(rotation = 45)

        elif select_year ==2016:
            fig,ax = plt.subplots()
            plt.bar(new2016["Race"], new2016["share"]*100, align='center', alpha=0.5)
            plt.ylabel('Percentages by Total Persons in Poverty', fontsize = 14)
            plt.xlabel('Race', fontsize = 14)
            plt.title('Poverty Population by Race', fontsize = 20)
            plt.xticks(rotation = 45)

        elif select_year ==2017:
            fig,ax = plt.subplots()
            plt.bar(new2017["Race"], new2017["share"]*100, align='center', alpha=0.5)
            plt.ylabel('Percentages by Total Persons in Poverty', fontsize = 14)
            plt.xlabel('Race', fontsize = 14)
            plt.title('Poverty Population by Race', fontsize = 20)
            plt.xticks(rotation = 45)

        else:
            fig,ax = plt.subplots()
            plt.bar(new2019["Race"], new2019["share"]*100, align='center', alpha=0.5)
            plt.ylabel('Percentages by Total Persons in Poverty', fontsize = 14)
            plt.xlabel('Race', fontsize = 14)
            plt.title('Poverty Population by Race', fontsize = 20)
            plt.xticks(rotation = 45)





    st.pyplot(fig)