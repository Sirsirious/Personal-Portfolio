### Data

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from nlptools.core.structures import tokenize
from nlptools.preprocessing.tagging import MLTagger
from nlptools.preprocessing.lemmatization import DictionaryLemmatizer

## Navbar
from .navbar import navbar_layout

nav = navbar_layout()
tagger = MLTagger(force_ud=True)
lemmatizer = DictionaryLemmatizer()

header = html.H3(
    'Insert a text to be lemmatized'
)

options = [{'label': 'blue'}]

body = dbc.Container(
    [
        dbc.Row(
            dbc.Col([
                html.H3(
                    'Insert a text to be lemmatized.'
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
                    'Lemmatized tokens appear here'
                )])
        ]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Textarea(
                            id='lemma-input',
                            value='Insert to lemmatize words.',
                            style={'width': '100%', 'height': 150},
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.Div(id='lemma-output', style={'whiteSpace': 'pre-line'})
                    ]
                ),
            ],
            className="mt-4",
        ),
        ])


def lemmatizer_layout():
    layout = html.Div([
        body
    ])
    return layout


def generate_lemma_pills(token, lemma, idx):
    return html.Div([make_pill(lemma, idx), make_tooltip(token, idx)])


def make_pill(lemma, idx):
    return dbc.Badge(
        lemma, pill=True, color="info", className="mr-1",
        id=f"tooltip-target-tag-{idx}"
    )


def make_tooltip(token, idx):
    return dbc.Tooltip(
        f"Tag: {token.PoS}, Raw: {token.raw}",
        target=f"tooltip-target-tag-{idx}",
        placement="top"
    )


def generate_lemmas(text):
    tagged_tokens = tagger.tag(text.lower())
    lemmatized_words = [lemmatizer.lemmatize(word, word.PoS) for word in tagged_tokens.tokens[1:-1]]
    list_of_pills = [generate_lemma_pills(token, lemma, idx) for idx, (lemma, token) in enumerate(zip(lemmatized_words, tagged_tokens[1:-1]))]
    tags_div = html.Div(list_of_pills, style={"display": "flex", "flexWrap": "wrap"}, )
    return tags_div
