# Project name: Emotions Detector

## Topic: Setting the mood and emotional state of a Twitter user.

[![Made with](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)]

## Table of content

- [Purpose](#Purpose)
- [Description](#Description)
- [Contents](#Contents)
- [Installation](#Installation)
- [Usage example](#Usage example)
- [Input/Output data](#Input/Output data)
- [Credits](#Credits)


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

In the directory _main_, there is a file _main.py_ to run a program. The directory _modules_ are divided into separate directories that are responsible for different parts of the project.

Below you can find a more detailed description of the directories and links to them.

### Main module to run a program
[main.py](https://github.com/muliarska/homeworks_ucu/blob/master/main/main.py)

### Project modules
[EmotionsList ADT](https://github.com/muliarska/homeworks_ucu/tree/master/modules/emotion_list)

[TweetsLinkedList ADT](https://github.com/muliarska/homeworks_ucu/tree/master/modules/twitter_list_adt)

[Data structures for ADTs realizations](https://github.com/muliarska/homeworks_ucu/tree/master/modules/data_structures)

[Main program processes](https://github.com/muliarska/homeworks_ucu/tree/master/modules/program_process)

[Visualization](https://github.com/muliarska/homeworks_ucu/tree/master/modules/visualization)

### Examples modules
[Example of using Twitter API](https://github.com/muliarska/homeworks_ucu/tree/master/examples/api_example)

[Examples of using modules and librares](https://github.com/muliarska/homeworks_ucu/tree/master/examples/modules_examples)

[Example of using ADTs](https://github.com/muliarska/homeworks_ucu/tree/master/examples/adt_usage_example)

[ADTs realizations](https://github.com/muliarska/homeworks_ucu/tree/master/examples/adt_realization)

[Data structures for ADTs realizations](https://github.com/muliarska/homeworks_ucu/tree/master/examples/data_structures)

[Example of main program processes](https://github.com/muliarska/homeworks_ucu/tree/master/examples/process_module)

[ADT diagrams](https://github.com/muliarska/homeworks_ucu/tree/master/adt_diagrams)

[Screenshots of usage examples](https://github.com/muliarska/homeworks_ucu/tree/master/usage_examples)

### Wiki
[Topic of the project](https://github.com/muliarska/homeworks_ucu/wiki/%D0%A2%D0%B5%D0%BC%D0%B0-%D1%86%D0%B8%D0%BA%D0%BB%D1%83-%D0%B4%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%96%D1%85-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D1%8C)

[Homework №0](https://github.com/muliarska/homeworks_ucu/wiki/0.-%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%960)

[Homework №1](https://github.com/muliarska/homeworks_ucu/wiki/1.-%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%961)

[Homework №2](https://github.com/muliarska/homeworks_ucu/wiki/2.-%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%962)

[Homework №3](https://github.com/muliarska/homeworks_ucu/wiki/3.-%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%963)

[Homework №4](https://github.com/muliarska/homeworks_ucu/wiki/4.-%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%964)

[Homework №5](https://github.com/muliarska/homeworks_ucu/wiki/5.-%D0%94%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%94-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%965)



## Installation

* Clone

Clone this repository to your local machine using 
`git clone https://github.com/muliarska/homeworks_ucu.git`

* Prerequisites

Install nltk, plotly, flask, dash

`pip install nltk`

`pip install plotly`

`pip install flask`

`pip install dash==0.31.1`  (The core dash backend)

`pip install dash-html-components==0.13.2`  (HTML components)

`pip install dash-core-components==0.38.1`  (Supercharged components)


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

## Credits
### Yana Muliarska, Computer Science student in Ukrainian Catholic University, 2020
