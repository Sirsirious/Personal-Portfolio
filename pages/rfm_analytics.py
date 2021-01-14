import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from pages.navbar import navbar_layout

nav = navbar_layout()

body = dbc.Container(
    [
        dbc.Row([dbc.Col([html.H3("RFM Analytics")])], className="mt-4"),
        dbc.Row([dbc.Col([dcc.Markdown(
"""This is an example of RFM analysis performed over the E-commerce dataset from 
UCI Machine Learning.

The dashboard is made using Google Cloud Data Studio and the computations are all 
made using Google Big Query.

You can find this report natively at: 
https://datastudio.google.com/reporting/794c3170-36a5-42f6-867d-9207755fba10 

P.s.: Since the data is from 2011, there's significant skew in 
Recency. To cope with that, I've removed 3200 days from every totals 
(I'm using 11 december 2020 as 'current date' to compute recency), but with real 
data, the recency will be much closer to 1 in the best performing classes."""
        )])],
                className="mt-4"),
        dbc.Row(
            [dbc.Col([
                html.Iframe(src="https://datastudio.google.com/embed/reporting/794c3170-36a5-42f6-867d-9207755fba10"
                                "/page/GXvsB", width=1000, height=800)
            ])], className="mt-4")])


def rfm_layout():
    layout = html.Div([
        body
    ])
    return layout
