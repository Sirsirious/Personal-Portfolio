### Data

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from nlptools.core.structures import tokenize
from nlptools.preprocessing.tagging import MLTagger

## Navbar
from .navbar import navbar_layout

nav = navbar_layout()
tagger = MLTagger(force_ud=True)

tag_colors = {
    "ADJ": {'background-color': '#F3FF28',
            'color': 'black',
            },
    "ADP": {'background-color': '#FFB51D',
            'color': 'black',
            },
    "ADV": {'background-color': '#FF721A',
            'color': 'black',
            },
    "AUX": {'background-color': '#FFEAA3',
            'color': 'black',
            },
    "CCONJ": {'background-color': '#FFA88D',
              'color': 'black',
              },
    "DET": {'background-color': '#FFD6DD',
            'color': 'black',
            },
    "INTJ": {'background-color': '#FF1545',
             'color': 'black',
             },
    "NOUN": {'background-color': '#2AFF52',
             'color': 'black'},
    "NUM": {'background-color': '#CFFFC8',
            'color': 'black',
            },
    "PART": {'background-color': '#80FFE2',
             'color': 'black',
             },
    "PRON": {'background-color': '#26E1FF',
             'color': 'black',
             },
    "PROPN": {'background-color': '#0B72FF',
              'color': 'black',
              },
    "PUNCT": {'background-color': '#02161E',
              'color': 'white'},
    "SCONJ": {'background-color': '#B050BF',
              'color': 'black'},
    "SYM": {'background-color': '#BF78BB',
            'color': 'black'},
    "VERB": {'background-color': '#61BF04',
             'color': 'black',
             },
    "X": {'background-color': 'white',
          'color': 'black'}
}


def generate_pos_subtitles():
    return html.Div([html.H5("Label colors")] +
                    [dbc.Badge(pos, pill=True, color="primary", className="mr-1", style=tag_colors[pos]) for pos in
                     tag_colors])


header = html.H3(
    'Insert a text to be tagged'
)

options = [{'label': 'blue'}]

body = dbc.Container(
    [
        dbc.Row(
            dbc.Col([
                html.H3(
                    'Insert a text to be tagged'
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
                    'Tagged tokens appear here'
                )])
        ]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Textarea(
                            id='tagger-input',
                            value='Insert a text to find its pos tags.',
                            style={'width': '100%', 'height': 150},
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.Div(id='tagger-output', style={'whiteSpace': 'pre-line'})
                    ]
                ),
            ],
            className="mt-4",
        ),
        dbc.Row([
            generate_pos_subtitles()])])


def tagger_layout():
    layout = html.Div([
        body
    ])
    return layout


def generate_tag_dropdown(token, tag, idx):
    return html.Div([make_pill(token, tag, idx), make_tooltip(token, tag, idx)])


def make_pill(token, tag, idx):
    return dbc.Badge(
        token, pill=True, color="primary", className="mr-1", style=tag_colors[tag],
        id=f"tooltip-target-tag-{idx}"
    )


def make_tooltip(token, tag, idx):
    return dbc.Tooltip(
        f"Tag: {tag}",
        target=f"tooltip-target-tag-{idx}",
        placement="top"
    )


def generate_tags(text):
    tagged_tokens = tagger.tag(text.lower())
    list_of_tags = [generate_tag_dropdown(token.raw, token.PoS, idx) for idx, token in enumerate(tagged_tokens[1:-1])]
    tags_div = html.Div(list_of_tags, style={"display": "flex", "flexWrap": "wrap"}, )
    return tags_div
