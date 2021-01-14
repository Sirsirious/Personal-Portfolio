### Data

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from nlptools.core.structures import tokenize
## Navbar
from .navbar import navbar_layout

nav = navbar_layout()


output = html.Div(id='tokenizer-output', style={'whiteSpace': 'pre-line'})

body = dbc.Container(
    [
        dbc.Row(
            dbc.Col([
                html.H3(
                    'Insert a text to be tokenized'
                )]
            )),
        dbc.Row([
            dbc.Col([
                html.H4(
                    'Insert text here'
                )]
            ),
            dbc.Col([
                html.H4(
                    'Tokens appear here'
                )])
        ]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Textarea(
                            id='tokenizer-input',
                            value='Break text into tokens.',
                            style={'width': '100%', 'height': 150},
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.Div(id='tokenizer-output', style={'whiteSpace': 'pre-line'})
                    ]
                ),
            ],
            className="mt-4",
        )])


def tokenizer_layout():
    layout = html.Div([
        body
    ])
    return layout


def generate_tokens(text):
    data = tokenize(text)
    string = [dbc.Button(token.raw, color="primary", className="mr-1") for token in data[1:-1]]
    return string