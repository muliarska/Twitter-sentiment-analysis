"""Represents a dashboard with charts and statistics"""
from dash import Dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from modules.visualization.plots import plot_bar, plot_circle


def dashboard_emotions(flask_app, counter, main_text, figure1, figure2):
    """
    (Flask, int, str, Figure, Figure) -> Dash
    Returns a dashboard with the given figures and text
    using dash
    """
    dash_app = Dash(__name__, server=flask_app, url_base_pathname='/statistic{}/'.format(counter))

    dash_app.title = 'Statistics'

    dash_app.layout = html.Div([
        html.Div([
            html.P(children=main_text)]),
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
                dcc.Graph(id='example-graph', figure=figure1)
            ])
        elif tab == 'tab-2':
            return html.Div([
                dcc.Graph(id='example-graph', figure=figure2)
            ])

    return dash_app


def create_dash_app(server, counter, manager, app_type, nickname,
                    day=None, emotion=None):
    """
    (Flask, int, Functional, str, str, str, str) -> Dash
    Returns a dashboard with statistics according to
    the given parameters (for a specific day,
    for a specific emotion, etc.)
    """
    plot1 = None
    plot2 = None
    main_text = None

    if app_type == "many":
        if day is None:
            plot1 = plot_bar(manager.many_emotions_last_time())
            plot2 = plot_circle(manager.two_emotions_last_time())
            main_text = "Statistics of many emotions for last time for {}".format(nickname)
        else:
            plot1 = plot_bar(manager.many_emotions_specific_day(day))
            plot2 = plot_circle(manager.two_emotions_specific_day(day))
            main_text = "Statistics of many emotions for {} for {}".format(day, nickname)

    elif app_type == "specific":
        if day is None:
            prob = manager.one_emotion_last_time(emotion)[1]
            emotions_list = [(emotion, prob), ('other', 1-prob)]
            plot1 = plot_circle(emotions_list)
            plot2 = plot_circle(manager.two_emotions_last_time())
            main_text = "Intensity of {} for last time for {}".format(emotion, nickname)
        else:
            prob = manager.one_emotion_specific_day(emotion, day)[1]
            emotions_list = [(emotion, prob), ('other', 1 - prob)]
            plot1 = plot_circle(emotions_list)
            plot2 = plot_circle(manager.two_emotions_specific_day(day))
            main_text = "Intensity of {} for {} for {}".format(emotion, day, nickname)

    return dashboard_emotions(server, counter, main_text, plot1, plot2)
