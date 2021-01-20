from flask import Flask

from pages.bio import bio_layout
from pages.footer import footer_layout
from pages.homepage import homepage_layout
from pages.lemmatizer import lemmatizer_layout, generate_lemmas
from pages.navbar import navbar_layout
from pages.ner import generate_ner_text, ner_layout
from pages.rfm_analytics import rfm_layout
from pages.stemmer import stemmer_layout, generate_stems
from pages.tagger import generate_tags, tagger_layout
from pages.tokenizer import tokenizer_layout, generate_tokens

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from ai.ner import load_ner, load_vocabs

dash_app = Flask(__name__)

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"

dash_app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED, dbc.themes.BOOTSTRAP, FONT_AWESOME])
app = dash_app.server
dash_app.config.suppress_callback_exceptions = True

footer = footer_layout()

navbar = navbar_layout()

dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([navbar, html.Div(id='page-content'), footer]),
])
dash_app.title = "Tiago Duque"

word2idx, idx2word, tags2idx, idx2tags = load_vocabs()
model = load_ner()


@dash_app.callback(Output('page-content', 'children'),
                   [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/tokenizer':
        return tokenizer_layout()
    if pathname == '/stemmer':
        return stemmer_layout()
    if pathname == '/tagger':
        return tagger_layout()
    if pathname == '/lemmatizer':
        return lemmatizer_layout()
    if pathname == '/ner':
        return ner_layout()
    if pathname == '/rfm':
        return rfm_layout()
    if pathname == '/bio':
        return bio_layout()
    else:
        return homepage_layout()


@dash_app.callback(
    Output('tokenizer-output', 'children'),
    [Input('tokenizer-input', 'value')]
)
def generate_token_list(text):
    text = generate_tokens(text)
    return text


@dash_app.callback(
    Output('stemmer-output', 'children'),
    [Input('stemmer-input', 'value')]
)
def generate_stem_list(text):
    text = generate_stems(text)
    return text


@dash_app.callback(
    Output('tagger-output', 'children'),
    [Input('tagger-input', 'value')]
)
def generate_tag_list(text):
    text = generate_tags(text)
    return text


@dash_app.callback(
    Output('lemma-output', 'children'),
    [Input('lemma-input', 'value')]
)
def generate_lemma_list(text):
    text = generate_lemmas(text)
    return text


@dash_app.callback(
    Output('ner-output', 'children'),
    [Input('ner-input', 'value'),
     Input('ner-button', 'n_clicks')]
)
def generate_ner_list(text, n_clicks):
    if n_clicks and n_clicks > 0:
        try:
            text = generate_ner_text(text, model, word2idx, idx2tags)
            return text
        except AttributeError as e:
            return str(e)

if __name__ == "__main__":
    dash_app.run_server(debug=False)
