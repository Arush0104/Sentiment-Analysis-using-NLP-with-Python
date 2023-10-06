import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd

with st.sidebar:
    selected = option_menu(
        menu_title="Final Project",
        options=["Main Menu","OnePlus","Oppo","RealMe","Redmi 9","Redmi 10","Redmi 11","Samsung","Vivo"]
    )
df = pd.read_csv("Flipkart_Amazon Mobile Reviews - Flipkart_Amazon Mobile Reviews.csv")
if selected == "Main Menu":
    st.header("Welcome to the menu, select a phone to see the reviews")
if selected == "OnePlus":
    #Data Set
    countries=['Positive Reviews', 'Negative Reviews']
    values = [2781, 789]
    #The plot
    fig = go.Figure(
        go.Pie(
        labels = countries,
        values = values,
        hoverinfo = "percent",
    ))
    st.header(":green[Reviews of OnePlus Nord CE 2 5G (Gray Mirror, 8GB RAM, 128GB Storage)]")
    st.plotly_chart(fig)
    
    option = st.selectbox(
    'Select the category of reviews',
    ('General', 'Camera', 'Performace','Battery','Display','Value for Money'))
    
    if(option=="General"):
        for i in range(5,3570,20):
            st.header(df["Review_Title"].iloc[i])
            st.write(df["rating"].iloc[i])
            st.markdown(df["Review_Body"].iloc[i])
            
    if(option=="Camera"):
        for i in range(5,3570,20):
            if(df["Label"].iloc[i]=="camera"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Performace"):
        for i in range(5,3570,20):
            if(df["Label"].iloc[i]=="performance"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Battery"):
        for i in range(5,3570,20):
            if(df["Label"].iloc[i]=="battery"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Display"):
        for i in range(5,3570,20):
            if(df["Label"].iloc[i]=="display"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Value for Money"):
        for i in range(5,3570,20):
            if(df["Label"].iloc[i]=="value for money"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    
            
if selected == "Oppo":
    #Data Set
    countries=['Positive Reviews', 'Negative Reviews']
    values = [3297, 1031]
    #The plot
    fig = go.Figure(
        go.Pie(
        labels = countries,
        values = values,
        hoverinfo = "percent",
    ))
    st.header(":green[Reviews of OPPO A31 (Mystery Black, 6GB RAM, 128GB Storage)]")
    st.plotly_chart(fig)
    
    option = st.selectbox(
    'Select the category of reviews',
    ('General', 'Camera', 'Performace','Battery','Display','Value for Money'))
    
    if(option=="General"):
        for i in range(3572,7900,20):
            st.header(df["Review_Title"].iloc[i])
            st.write(df["rating"].iloc[i])
            st.markdown(df["Review_Body"].iloc[i])
            
    if(option=="Camera"):
        for i in range(3572,7900,20):
            if(df["Label"].iloc[i]=="camera"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Performace"):
        for i in range(3572,7900,20):
            if(df["Label"].iloc[i]=="performance"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Battery"):
        for i in range(3572,7900,20):
            if(df["Label"].iloc[i]=="battery"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Display"):
        for i in range(3572,7900,20):
            if(df["Label"].iloc[i]=="display"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Value for Money"):
        for i in range(3572,7900,20):
            if(df["Label"].iloc[i]=="value for money"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    



         
if selected == "RealMe":
    #Data Set
    countries=['Positive Reviews', 'Negative Reviews']
    values = [1649, 515]
    #The plot
    fig = go.Figure(
        go.Pie(
        labels = countries,
        values = values,
        hoverinfo = "percent",
    ))
    st.header(":green[realme narzo 50A (Oxygen Blue , 4GB RAM + 64 GB Storage)]")
    st.plotly_chart(fig)
    
    option = st.selectbox(
    'Select the category of reviews',
    ('General', 'Camera', 'Performace','Battery','Display','Value for Money'))
    
    if(option=="General"):
        for i in range(7902,10055,20):
            st.header(df["Review_Title"].iloc[i])
            st.write(df["rating"].iloc[i])
            st.markdown(df["Review_Body"].iloc[i])
            
    if(option=="Camera"):
        for i in range(7902,10055,20):
            if(df["Label"].iloc[i]=="camera"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Performace"):
        for i in range(7902,10055,20):
            if(df["Label"].iloc[i]=="performance"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Battery"):
        for i in range(7902,10055,20):
            if(df["Label"].iloc[i]=="battery"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Display"):
        for i in range(7902,10055,20):
            if(df["Label"].iloc[i]=="display"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Value for Money"):
        for i in range(7902,10055,20):
            if(df["Label"].iloc[i]=="value for money"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])






if selected == "Redmi 9":
    #Data Set
    countries=['Positive Reviews', 'Negative Reviews']
    values = [3134, 1325]
    #The plot
    fig = go.Figure(
        go.Pie(
        labels = countries,
        values = values,
        hoverinfo = "percent",
    ))
    st.header(":green[Redmi 9 Activ (Carbon Black, 4GB RAM, 64GB Storage)]")
    st.plotly_chart(fig)
    
    option = st.selectbox(
    'Select the category of reviews',
    ('General', 'Camera', 'Performace','Battery','Display','Value for Money'))
    
    if(option=="General"):
        for i in range(13860,18293,20):
            st.header(df["Review_Title"].iloc[i])
            st.write(df["rating"].iloc[i])
            st.markdown(df["Review_Body"].iloc[i])
            
    if(option=="Camera"):
        for i in range(13860,18293,20):
            if(df["Label"].iloc[i]=="camera"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Performace"):
        for i in range(13860,18293,20):
            if(df["Label"].iloc[i]=="performance"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Battery"):
        for i in range(13860,18293,20):
            if(df["Label"].iloc[i]=="battery"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Display"):
        for i in range(13860,18293,20):
            if(df["Label"].iloc[i]=="display"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Value for Money"):
        for i in range(13860,18293,20):
            if(df["Label"].iloc[i]=="value for money"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])


    
           
           
if selected == "Redmi 10":
    #Data Set
    countries=['Positive Reviews', 'Negative Reviews']
    values = [2444, 1322]
    #The plot
    fig = go.Figure(
        go.Pie(
        labels = countries,
        values = values,
        hoverinfo = "percent",
    ))
    st.header(":green[Redmi 10 Prime (Bifrost Blue 4GB RAM 64GB ROM)]")
    st.plotly_chart(fig)
    
    option = st.selectbox(
    'Select the category of reviews',
    ('General', 'Camera', 'Performace','Battery','Display','Value for Money'))
    
    if(option=="General"):
        for i in range(10067,13830,20):
            st.header(df["Review_Title"].iloc[i])
            st.write(df["rating"].iloc[i])
            st.markdown(df["Review_Body"].iloc[i])
            
    if(option=="Camera"):
        for i in range(10067,13830,20):
            if(df["Label"].iloc[i]=="camera"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Performace"):
        for i in range(10067,13830,20):
            if(df["Label"].iloc[i]=="performance"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Battery"):
        for i in range(10067,13830,20):
            if(df["Label"].iloc[i]=="battery"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Display"):
        for i in range(10067,13830,20):
            if(df["Label"].iloc[i]=="display"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Value for Money"):
        for i in range(10067,13830,20):
            if(df["Label"].iloc[i]=="value for money"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
     

        
        

if selected == "Redmi 11":
    #Data Set
    countries=['Positive Reviews', 'Negative Reviews']
    values = [3134, 1325]
    #The plot
    fig = go.Figure(
        go.Pie(
        labels = countries,
        values = values,
        hoverinfo = "percent",
    ))
    st.header(":green[Redmi Note 11 (Space Black, 4GB RAM, 64GB Storage)]")
    st.plotly_chart(fig)
    
    option = st.selectbox(
    'Select the category of reviews',
    ('General', 'Camera', 'Performace','Battery','Display','Value for Money'))
    
    if(option=="General"):
        for i in range(18296,13830,20):
            st.header(df["Review_Title"].iloc[i])
            st.write(df["rating"].iloc[i])
            st.markdown(df["Review_Body"].iloc[i])
            
    if(option=="Camera"):
        for i in range(10067,13830,20):
            if(df["Label"].iloc[i]=="camera"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Performace"):
        for i in range(10067,13830,20):
            if(df["Label"].iloc[i]=="performance"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Battery"):
        for i in range(10067,13830,20):
            if(df["Label"].iloc[i]=="battery"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Display"):
        for i in range(10067,13830,20):
            if(df["Label"].iloc[i]=="display"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Value for Money"):
        for i in range(10067,13830,20):
            if(df["Label"].iloc[i]=="value for money"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])




if selected == "Samsung":
    #Data Set
    countries=['Positive Reviews', 'Negative Reviews']
    values = [851, 487]
    #The plot
    fig = go.Figure(
        go.Pie(
        labels = countries,
        values = values,
        hoverinfo = "percent",
    ))
    st.header(":green[Samsung M32]")
    st.plotly_chart(fig)
    
    option = st.selectbox(
    'Select the category of reviews',
    ('General', 'Camera', 'Performace','Battery','Display','Value for Money'))
    
    if(option=="General"):
        for i in range(21018,22357,20):
            st.header(df["Review_Title"].iloc[i])
            st.write(df["rating"].iloc[i])
            st.markdown(df["Review_Body"].iloc[i])
            
    if(option=="Camera"):
        for i in range(21018,22357,20):
            if(df["Label"].iloc[i]=="camera"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Performace"):
        for i in range(21018,22357,20):
            if(df["Label"].iloc[i]=="performance"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Battery"):
        for i in range(21018,22357,20):
            if(df["Label"].iloc[i]=="battery"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Display"):
        for i in range(21018,22357,20):
            if(df["Label"].iloc[i]=="display"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Value for Money"):
        for i in range(21018,22357,20):
            if(df["Label"].iloc[i]=="value for money"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
                
                
                
                
                





if selected == "Vivo":
    #Data Set
    countries=['Positive Reviews', 'Negative Reviews']
    values = [1649, 515]
    #The plot
    fig = go.Figure(
        go.Pie(
        labels = countries,
        values = values,
        hoverinfo = "percent",
    ))
    st.header(":green[Samsung M32]")
    st.plotly_chart(fig)
    
    option = st.selectbox(
    'Select the category of reviews',
    ('General', 'Camera', 'Performace','Battery','Display','Value for Money'))
    
    if(option=="General"):
        for i in range(21018,22357,20):
            st.header(df["Review_Title"].iloc[i])
            st.write(df["rating"].iloc[i])
            st.markdown(df["Review_Body"].iloc[i])
            
    if(option=="Camera"):
        for i in range(22360,23776,20):
            if(df["Label"].iloc[i]=="camera"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Performace"):
        for i in range(22360,23776,20):
            if(df["Label"].iloc[i]=="performance"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Battery"):
        for i in range(22360,23776,20):
            if(df["Label"].iloc[i]=="battery"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Display"):
        for i in range(22360,23776,20):
            if(df["Label"].iloc[i]=="display"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
    if(option=="Value for Money"):
        for i in range(22360,23776,20):
            if(df["Label"].iloc[i]=="value for money"):
                st.header(df["Review_Title"].iloc[i])
                st.write(df["rating"].iloc[i])
                st.markdown(df["Review_Body"].iloc[i])
                
                
                
                
                










    



    