### Data

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from nlptools.core.structures import tokenize
from nlptools.preprocessing.stemming import PorterStemmer

## Navbar
from .navbar import navbar_layout

stemmer = PorterStemmer()

header = html.H3(
    'Insert a text to be stemmed'
)

options = [{'label': 'blue'}]

body = dbc.Container(
    [
        dbc.Row(
            dbc.Col([
                html.H3(
                    'Insert a text to be stemmed'
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
                    'Stems appear here'
                )])
        ]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Textarea(
                            id='stemmer-input',
                            value='Stemming is a normalization technique.',
                            style={'width': '100%', 'height': 150},
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.Div(id='stemmer-output', style={'whiteSpace': 'pre-line'})
                    ]
                ),
            ],
            className="mt-4",
        )])

output = html.Div(id='stemmer-output', style={'whiteSpace': 'pre-line'})


def stemmer_layout():
    layout = html.Div([
        body
    ])
    return layout

def generate_stem_dropdown(stemmed, raw):
    dropdown = dbc.DropdownMenu(
        label=stemmed,
        children=[
            dbc.DropdownMenuItem("Raw: "+raw),
        ],
        className="m-1"
    )
    return dropdown

def generate_stems(text):
    tokens = tokenize(text)
    stems = [stemmer.stem(token.raw) for token in tokens[1:-1]]
    list_of_stems = [generate_stem_dropdown(stem, token.raw) for stem, token in zip(stems, tokens[1:-1])]
    stem_div = html.Div(list_of_stems, style={"display": "flex", "flexWrap": "wrap"},)
    return stem_div
