import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

body = dbc.Container([dcc.Markdown(
"""

# Biography

Born from an Electrical Engineer dad and an arts teacher mom in provincial southern Brazil, Tiago was raised among both math and culture.
His parents provided him all he needed to have a good education, paying good schools and providing all that was necessary.

In the early 90's, his dad brought home the first computer Tiago had access to. It was a rare thing back then in Brazil.
During his early youth, different from many developers and data scientist bios, Tiago did not learn to program or do magic with code.
Instead, he learned to play videogames, and this was his moto for a long time. He loved strategy and historical games such as Age of Empires,
The Settlers III and many others.
During his teen years, he got into more gaming, having access to the internet, he started to play some of the earlier MMO's, 
mainly with middle ages topic (that's why his github profile is called sirsirious).

In 2008, his dad went to Tallahassee, FL, to study for a Post Doctorate in Electrical Engineering in UFL. This is where Tiago
practiced some of the english that he learned while playing videogames.

All the passion for historical games got into him the love for History, which took him to the university to learn the topic from 2009 to 2012.

It was in the university that Tiago met his wife, Priscila, who was just finishing a technical degree on informatics.
Before graduating, Tiago asked Priscila to marry, and they are a team to the day.

One day, Priscila asked Tiago some help with her programming assignment, since many things were in english and she was not profficient in the language.
It was Tiago's first contact with programming. It was a simple html webpage with javascript callbacks. At first, it was all fussy,
but while looking at it, Tiago noted there were some patterns where he could just copy and change some parts.
He helped priscila get an A and saw that programming was not something that was not that hard.

""")])

def bio_layout():
    return html.Div(body)