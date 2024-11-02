import streamlit as st
import pandas as pd
import plotly.express as px

# Load your dataset
@st.cache_data
def load_data():
    return pd.read_csv("C:/vscode/after_K-means.csv")

df = load_data()

# Streamlit app title
st.title('Workers Population by Industry and Geography')

# Sidebar for filtering
st.sidebar.header('Filter Options')

# Select a state
states = df['India/States'].unique()
selected_state = st.sidebar.selectbox('Select State', states)

# Filter divisions based on the selected state
divisions = df[df['India/States'] == selected_state]['Division'].unique()
selected_division = st.sidebar.selectbox('Select Division', divisions)

# Filter districts based on the selected state and division
districts = df[(df['India/States'] == selected_state) & (df['Division'] == selected_division)]['District Code'].unique()
selected_district = st.sidebar.selectbox('Select District', districts)

# Filter the data based on selections
filtered_data = df[(df['India/States'] == selected_state) & 
                   (df['Division'] == selected_division) & 
                   (df['District Code'] == selected_district)]

# Display a summary of the filtered data
st.write(f"### Summary of Workers in {selected_state} - Division: {selected_division} - District: {selected_district}")
st.write(filtered_data)

# Check if there is data to plot
if not filtered_data.empty:
    # Plotting Total Main Workers by Industry
    fig_total = px.bar(
        filtered_data,
        x='Cleaned NIC Name',
        y='Main Workers - Total -  Persons',
        title='Total Main Workers by Industry',
        labels={'Main Workers - Total -  Persons': 'Total Workers', 'Cleaned NIC Name': 'Industry'},
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    st.plotly_chart(fig_total)

    # Plotting Total Female Workers by Industry
    fig_female = px.bar(
        filtered_data,
        x='Cleaned NIC Name',
        y='Main Workers - Total - Females',
        title='Total Female Workers by Industry',
        labels={'Main Workers - Total - Females': 'Total Female Workers', 'Cleaned NIC Name': 'Industry'},
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_female)

    # Plotting Total Male Workers by Industry
    fig_male = px.bar(
        filtered_data,
        x='Cleaned NIC Name',
        y='Main Workers - Total - Males',
        title='Total Male Workers by Industry',
        labels={'Main Workers - Total - Males': 'Total Male Workers', 'Cleaned NIC Name': 'Industry'},
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    st.plotly_chart(fig_male)
else:
    st.write("No data available for the selected filters.")