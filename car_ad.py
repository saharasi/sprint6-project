import pandas as pd
import streamlit as st
import plotly.express as px

st.header('Car Advertisement Data')
st.write(''' #### Filter the data below to see the ads by manufacturer''')

df = pd.read_csv('vehicles_us.csv')

models_choice = df['model'].unique()
make_choice_model = st.selectbox('Select Model:', models_choice)


min_year, max_year = int(df['model_year'].min()), int(df['model_year'].max())

year_range = st.slider('Choose year:', value=(
    min_year, max_year), min_value=min_year, max_value=max_year)

actual_range = list(range(year_range[0], year_range[1]+1))


df_filtered = df[(df['model'] == make_choice_model) &
                 (df.model_year.isin(list(actual_range)))]
st.table(df_filtered)

st.header('Price Analysis:')

list_for_hist = ['transmission', 'type', 'fuel', 'condition']
choice_for_hist = st.selectbox('Split for price distribution:', list_for_hist)
fig1 = px.histogram(df, x='price', color=choice_for_hist)
fig1.update_layout(
    title='<b> Split of price by {}</b>'.format(choice_for_hist))
st.plotly_chart(fig1)


# defining the age category of car

df['age'] = 2023-df['model_year']


def age_category(x):
    if x < 5:
        return '<5'
    elif x >= 5 and x < 10:
        return '5-10'
    elif x >= 10 and x < 20:
        return '10-20'
    else:
        return '>20'


df['age_category'] = df['age'].apply(age_category)


list_for_scatter = ['odometer', 'fuel', 'cylinders']
choice_for_scatter = st.selectbox('Price dependency on:', list_for_scatter)

fig2 = px.scatter(df, x='price', y=choice_for_scatter,
                  color='age_category', hover_data=['model_year'])

fig2.update_layout(title='<b>Price vs {}</b>'.format(choice_for_scatter))
st.plotly_chart(fig2)
