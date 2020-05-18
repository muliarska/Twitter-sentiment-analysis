# Project name: Emotions Detector


## Topic: Setting the mood and emotional state of a Twitter user.


## Purpose
Quarantine has now begun around the world due to the spread of Coronavirus. People sit at home and hardly go outside.
Many people are depressed or just in a bad mood. The purpose of the project is to give people the resources to track
their mood and changes to improve their mood and emotional state.

## Description
The project aims are to make people happier and give them a resource with statistics of emotions.
The project is implemented as a web application. The user can get various statistics of his mood and emotional state.
The following options are available: for the last time or a specific day, divided into eight different emotions (anger,
anticipation, disgust, fear, joy, sadness, surprise, trust), only into two (positive and negative) or choose a particular
feeling and get statistics only for it. Statistics are visualized using pie and bar charts.

Statistics can be displayed only for Twitter users. If the user didn't post anything for a long time,
statistics would not be displayed.

The central part of the project is developed using Python programming language; also, there are used CSS, HTML and JS.
The project uses abstract data types, structures, Python libraries and modules, etc.

This is not all about the input data's capabilities, so the functionality of the program and statistics can be developed.

More information about the project is provided on its WIKI page.

## Contents

## Prerequisites

Install nltk, plotly, flask, dash

pip install nltk

pip install plotly

pip install flask

pip install dash==0.31.1  (The core dash backend)

pip install dash-html-components==0.13.2  (HTML components)

pip install dash-core-components==0.38.1  (Supercharged components)


## Usage example
![](https://github.com/muliarska/homeworks_ucu/blob/master/usage_examples/screen1.PNG)

![](https://github.com/muliarska/homeworks_ucu/blob/master/usage_examples/screen2.PNG)

![](https://github.com/muliarska/homeworks_ucu/blob/master/usage_examples/screen3.PNG)

![](https://github.com/muliarska/homeworks_ucu/blob/master/usage_examples/screen4.PNG)

![](https://github.com/muliarska/homeworks_ucu/blob/master/usage_examples/screen5.PNG)

![](https://github.com/muliarska/homeworks_ucu/blob/master/usage_examples/screen6.PNG)

### Another statistic for the same user:

![](https://github.com/muliarska/homeworks_ucu/blob/master/usage_examples/screen7.PNG)

## Input/Output data

Input data is generated using Twitter API. Also, the project uses database NRC-Emotion-Intensity-Lexicon-v1.
Resource from which this database is taken: http://www.saifmohammad.com/WebPages/AffectIntensity.htm

The output data is statistics that are visualized using pie and bar charts.

## Program structure

## Credits
### Yana Muliarska, Computer Science student in Ukrainian Catholic University, 2020
