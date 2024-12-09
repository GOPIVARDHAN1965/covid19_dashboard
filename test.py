from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Initialize the Dash app
app = Dash(__name__)

# Load your data
data = pd.read_csv('country_wise_latest.csv')

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='COVID-19 Dashboard'),

    # Dropdown for selecting a country
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in data['Country/Region'].unique()],
        value='Afghanistan'  # Default value
    ),

    # Dropdown for selecting the first metric
    dcc.Dropdown(
        id='metric1-dropdown',
        options=[
            {'label': 'Confirmed Cases', 'value': 'Confirmed'},
            {'label': 'Deaths', 'value': 'Deaths'},
            {'label': 'Recovered', 'value': 'Recovered'},
            {'label': 'Active Cases', 'value': 'Active'},
            {'label': 'New Cases', 'value': 'New cases'},
            {'label': 'New Deaths', 'value': 'New deaths'},
            {'label': 'New Recovered', 'value': 'New recovered'}
        ],
        value='Confirmed'  # Default value
    ),

    # Dropdown for selecting the second metric
    dcc.Dropdown(
        id='metric2-dropdown',
        options=[
            {'label': 'Confirmed Cases', 'value': 'Confirmed'},
            {'label': 'Deaths', 'value': 'Deaths'},
            {'label': 'Recovered', 'value': 'Recovered'},
            {'label': 'Active Cases', 'value': 'Active'},
            {'label': 'New Cases', 'value': 'New cases'},
            {'label': 'New Deaths', 'value': 'New deaths'},
            {'label': 'New Recovered', 'value': 'New recovered'}
        ],
        value='Deaths'  # Default value
    ),

    # Graph to display the selected metric
    dcc.Graph(
        id='line-chart'
    )
])

# Define the callback to update the graph based on dropdown selections
@app.callback(
    Output('line-chart', 'figure'),
    [Input('country-dropdown', 'value'),
     Input('metric1-dropdown', 'value'),
     Input('metric2-dropdown', 'value')]
)
def update_figure(selected_country, selected_metric1, selected_metric2):
    # Filter data for the selected country
    filtered_data = data[data['Country/Region'] == selected_country]
    
    # Extract the values for the selected metrics
    metric_value1 = filtered_data[selected_metric1].values[0]
    metric_value2 = filtered_data[selected_metric2].values[0]

    # Create a bar chart using Plotly
    fig = px.bar(
        x=[selected_metric1, selected_metric2],
        y=[metric_value1, metric_value2],
        title=f'{selected_metric1} and {selected_metric2} in {selected_country}',
        labels={'x': 'Metrics', 'y': 'Count'}
    )
    
    return fig

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)