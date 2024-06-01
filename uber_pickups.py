
import pandas as pd
import plotly.express as px
import streamlit as st

# Load the dataset
df = pd.read_csv('C:\\Users\\vikto\\Documents\\CAs\\datasets\\GlobalLandTemperaturesByCountry.csv')

# Parse the date column
df['dt'] = pd.to_datetime(df['dt'])

# Filter data for the past 5 years
recent_years = df['dt'].dt.year.max() - 5
df_recent = df[df['dt'].dt.year > recent_years]

# Filter data for specific continents
continents = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
df_recent = df_recent[df_recent['Country'].isin(continents)]

# Extract year from the date column
df_recent['Year'] = df_recent['dt'].dt.year

# Group by Year and Continent, and calculate the mean temperature
df_yearly_continent = df_recent.groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()

# Streamlit app
st.title('Interactive Yearly Average Temperatures for Continents (Past 5 Years)')

# Create a plotly line plot
fig = px.line(df_yearly_continent, x='Year', y='AverageTemperature', color='Country', markers=True,
              title='Yearly Average Temperatures for Continents (Past 5 Years)',
              labels={'AverageTemperature': 'Average Temperature (°C)', 'Country': 'Continent'})

# Show the plot
st.plotly_chart(fig)
