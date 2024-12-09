from dash import Dash, html, dcc, Input, Output
import pandas as pd
import requests
import fetch_data as fd
import plotly.express as px


app = Dash(__name__)

global_df = fd.fetch_global_data()

#getting all countries names for drop down
names = fd.fetch_countries_data()
countries = names['country']

app.layout = html.Div([
    html.H1("Covid-19 Dashboard"),

    html.Div([
        html.H2("Global Statistics"),
        html.P(f"Total Confirmed Cases: {global_df['cases'].values[0]}"),
        html.P(f"Total Deaths: {global_df['deaths'].values[0]}"),
        html.P(f"Total Recoverd: {global_df['recovered'].values[0]}"),
        html.P(f"Total Active Cases: {global_df['active'].values[0]}"),
    ]),

    html.Div([
        html.H2("Select a Country"),
        dcc.Dropdown(
            id='country-dropdown',
            options = [{'label':country, 'value':country} for country in countries],
            value ='India' #default value
        )
        
    ]),
    dcc.Graph(id="cumulative-graph"),

    html.Div(id='country-stats'),

    dcc.Graph(id="daily-graph")

])

#callback to update country specific stats
@app.callback(
    Output('country-stats','children'),
    Output('cumulative-graph','figure'),
    Output('daily-graph','figure'),
    [Input('country-dropdown','value')]
)
def update_country_stats(selected_country):
    country_df = fd.fetch_country_data(selected_country)

    cumulative_fig = px.bar(
        x = ['Total Confirmed', 'Total Deaths', 'Total Recovered'],
        y = [country_df['cases'].values[0], country_df['deaths'].values[0],country_df['recovered'].values[0]],
        title = f'Cumulative COVID-19 Data for {selected_country}',
        labels = {'x': 'Category', 'y':'Count'}
    )

    daily_fig = px.bar(
        x=['New Cases', 'New Deaths'],
        y=[country_df['todayCases'].values[0], country_df['todayDeaths'].values[0]],
        title=f'Daily COVID-19 Data for {selected_country}',
        labels={'x': 'Category', 'y': 'Count'}
    )
    return [
        html.H2(f"{selected_country} Statistics"),
        html.P(f"Total Confirmed Cases: {country_df['cases'].values[0]}"),
        html.P(f"Total Deaths: {country_df['deaths'].values[0]}"),
        html.P(f"Total Recovered: {country_df['recovered'].values[0]}"),
        html.P(f"Total Active Cases: {country_df['active'].values[0]}"),
    ], cumulative_fig, daily_fig



if __name__ == "__main__":
    app.run_server(debug=True)