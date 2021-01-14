import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from .footer import footer_layout
from .navbar import navbar_layout

footer = footer_layout()

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Welcome"),
                        dcc.Markdown(
                            """Hi!

My name is Tiago Duque and I'm a Data Scientist. 

I work with Natural Language Processing as the main skill, sided by Data Analysis and Big Data.

In this webpage, you'll be able to find out more about my skills and past works.

For example, you can read more about my NLP Skills by accessing the NLP Menu. The same goes for my analytics skills.

You'll find many sample works in here, some of them even live. Due to the constraints of the machine where this website is running, 
not all my skills will be readily available for testing (for example, you'll have to head to colab notebooks to find 
about some of my deep learning skills).

Enjoy your stay!
"""
                        ),
                        html.A([dbc.Button("View details", color="secondary")], href='/bio'),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [html.Picture([
                        html.Source(srcSet="https://storage.googleapis.com/personal-portfolio-237318.appspot.com/Profile.jpg",
                                    style={"height": "20%"}),
                        html.Img(src="https://storage.googleapis.com/personal-portfolio-237318.appspot.com/Profile.jpg",
                                 className="img-fluid")], style={"height": "20%"})
                    ]
                , style={"width":"10%"}, md=4, align="center") ,
            ]
            , justify="center"
            )
    ],
    className="mt-4",
)


def homepage_layout():
    layout = html.Div([
        body,
    ])
    return layout
