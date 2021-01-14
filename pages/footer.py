import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc


def footer_layout():
    footer = html.Footer([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.P("Developed by Tiago Duque"), ]),
                dbc.Col([

                    dbc.Row([
                        dbc.Col([dbc.Row([html.A(href="https://www.linkedin.com/in/tfduque/",
                                                 className="btn btn-social-icon btn-linkedin",
                                                 children=[html.Span(className="fab fa-linkedin")])],
                                         style={'margin-top': '7px'}),
                                 dbc.Row([html.A(href="https://tfduque.medium.com",
                                                 className="btn btn-social-icon btn-reddit",
                                                 children=[html.Span(className="fab fa-medium")])],
                                         style={'margin-top': '7px'})]),
                        dbc.Col([dbc.Row([html.A(href="https://www.github.com/sirsirious",
                                                 className="btn btn-social-icon btn-github",
                                                 children=[html.Span(className="fab fa-github")])],
                                         style={'margin-top': '7px'}),
                                 dbc.Row([html.A(href="https://tfduque.medium.com",
                                                 className="btn btn-social-icon btn-pinterest",
                                                 children=[html.Span(className="fab fa-stack-overflow")])],
                                         style={'margin-top': '7px'}), ]), ])
                ]),
                dbc.Col([

                ], align="center")
            ], justify="center", style={'margin-top': '50px'})
        ])]
    )

    return footer
