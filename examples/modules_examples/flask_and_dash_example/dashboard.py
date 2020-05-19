"""Example of module Dash"""
from dash import Dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from examples.modules_examples.plotly_example.plots import plot_bar, plot_circle
from examples.modules_examples.nltk_example.nltk_example import get_emotions


def dashboard_emotions(flask_app, tweet):
    """
    (Flask, int, str, Figure, Figure) -> Dash
    Returns a dashboard with the given figures and text
    using dash
    """
    dash_app = Dash(__name__, server=flask_app, routes_pathname_prefix='/example/',
                    suppress_callback_exceptions=True)

    dash_app.title = 'Statistics'

    dash_app.layout = html.Div([
        html.Div([
            html.P(children="Example")]),
        dcc.Tabs(id='tabs-example', value='tab-1', children=[
            dcc.Tab(label='Many emotions', value='tab-1'),
            dcc.Tab(label='Positive and negative', value='tab-2')
        ]),
        html.Div(id='tabs-example-content')

    ])

    @dash_app.callback(
        Output('tabs-example-content', 'children'),
        [Input('tabs-example', 'value')]
    )
    def statistic(tab):
        if tab == 'tab-1':
            return html.Div([
                dcc.Graph(id='example-graph', figure=plot_bar(get_emotions(tweet)[0]))
            ])
        elif tab == 'tab-2':
            return html.Div([
                dcc.Graph(id='example-graph', figure=plot_circle(get_emotions(tweet)[0]))
            ])

    return dash_app.server
