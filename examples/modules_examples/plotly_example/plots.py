"""Example of plotly module"""
import plotly.graph_objects as go


def create_lists(emotions_list):
    """
    (EmotionsList) -> list, list, list
    Creates lists with emotions, probabilities and colors
    to create charts
    """
    emotions = []
    probability = []
    max_probability = 0
    counter = 0
    max_el = 0

    for element in emotions_list:
        emotions.append(element[0])
        if max_probability <= element[1]:
            max_probability = element[1]
            max_el = counter
        probability.append(element[1])
        counter += 1

    colors = []
    for i in range(counter):
        if i == max_el:
            colors.append('crimson')
        else:
            colors.append('lightslategray')
    return emotions, probability, colors


def plot_bar(emotions_list):
    """
    (EmotionsList) -> Figure
    Creates a bar chart with statistics using EMOTIONS_LIST
    """
    emotions, probability, colors = create_lists(emotions_list)

    fig = go.Figure(data=[go.Bar(
        x=emotions,
        y=probability,
        marker_color=colors
    )])
    fig.update_layout(title_text='Emotions')
    return fig


def plot_circle(emotions_list):
    """
    (EmotionsList) -> Figure
    Creates a pie chart with statistics using EMOTIONS_LIST
    """
    emotions, probability, colors = create_lists(emotions_list)

    fig = go.Figure(data=[go.Pie(
        labels=emotions,
        values=probability
    )])
    return fig
