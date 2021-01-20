import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

with open('./texts/bio_body.md') as f:
    body_text = f.read()

body = dbc.Container([dcc.Markdown(body_text)])

def bio_layout():
    return html.Div(body)