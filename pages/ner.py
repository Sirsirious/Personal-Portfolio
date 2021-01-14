### Data

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from nlptools.core.structures import tokenize
from nlptools.preprocessing.tagging import MLTagger
from ai.ner import predict

## Navbar
from .navbar import navbar_layout

nav = navbar_layout()

tag_colors = {
    "geo": {'background-color': '#2826FF',
            'color': 'white',
            },
    "gpe": {'background-color': '#FAFF11',
            'color': 'black',
            },
    "per": {'background-color': '#B9791A',
            'color': 'black',
            },
    "org": {'background-color': '#B9191C',
            'color': 'black',
            },
    "tim": {'background-color': '#49A3B9',
            'color': 'black'},
    "art": {'background-color': '#9B4FB9',
            'color': 'black',
            },
    "nat": {'background-color': '#029E30',
            'color': 'black',
            },
    "eve": {'background-color': '#02161E',
            'color': 'white'},
}


def generate_pos_subtitles():
    return html.Div([html.H5("Tag colors")] +
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
                            id='ner-input',
                            value='If I were in the United States, my name would be James.',
                            style={'width': '100%', 'height': 150},
                        ),
                        dbc.Row([
                            dbc.Col([
                                dbc.Button('Tag', id='ner-button', color='primary', className='float-right')
                            ])
                        ]),
                    ]
                ),
                dbc.Col(
                    [
                        html.Div(id='ner-output', style={'whiteSpace': 'pre-line'})
                    ]
                ),
            ],
            className="mt-4",
        ),

        dbc.Row([
            generate_pos_subtitles()])])


def ner_layout():
    layout = html.Div([
        body
    ])
    return layout


def generate_tag_dropdown(token, tag, idx):
    return html.Div([make_pill(token, tag, idx), make_tooltip(token, tag, idx)])


def make_pill(token, tag, idx):
    return dbc.Badge(
        token, pill=True, color="primary", className="mr-1", style=tag_colors[tag[2:]],
        id=f"tooltip-target-tag-{idx}"
    )


def make_tooltip(token, tag, idx):
    return dbc.Tooltip(
        f"Tag: {tag}",
        target=f"tooltip-target-tag-{idx}",
        placement="top"
    )


def generate_ner_text(text, model, vocab, tags):
    token_dict = predict(text, model, vocab, tags)
    text_div_content = []
    for idx in sorted(token_dict.keys()):
        item_to_add = token_dict[idx]['token']
        if token_dict[idx]['tag'] != "O":
            item_to_add = generate_tag_dropdown(token_dict[idx]['token'], token_dict[idx]['tag'], idx)
        text_div_content.append(item_to_add)
        text_div_content.append(" ")
    tags_div = html.Div(text_div_content, style={"display": "flex", "flexWrap": "wrap"}, )
    return tags_div
