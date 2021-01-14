import dash_bootstrap_components as dbc


def navbar_layout():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(nav=True,
                in_navbar=True,
                label="More about me",
                children=[
                    dbc.DropdownMenuItem("Bio", href='/bio'),
                ]),
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="NLP",
                children=[
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("NLPTools Samples", header=True),
                    dbc.DropdownMenuItem("Tokenizer", href="/tokenizer"),
                    dbc.DropdownMenuItem("Stemmer", href="/stemmer"),
                    dbc.DropdownMenuItem("Tagger", href="/tagger"),
                    dbc.DropdownMenuItem("Lemmatizer", href='/lemmatizer'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Other NLP Tasks", header=True),
                    dbc.DropdownMenuItem("NER Tagging", href="/ner"),
                ],
            ),
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Analytics",
                children=[
                    dbc.DropdownMenuItem("RFM", href="/rfm"),
                ],
            ),
        ],
        brand="Tiago Duque",
        brand_href="/home",
        sticky="top",
    )
    return navbar
