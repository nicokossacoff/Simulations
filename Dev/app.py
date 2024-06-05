from dash import Dash, html, dcc, Output, Input
from figures import mean_sample_distribution

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children= "Sample Mean Distribution"),
    dcc.Markdown('''
                 Calculates a thousand sample means from random samples with `n` observations. Each observation is a Bernoulli test with probability `p`.
                 '''),
    dcc.Dropdown([50, 200, 500, 1000], value= 50, id= "sample-size"),
    dcc.Dropdown([.1, .35, .5, .75], value= .35, id= "probability"),
    dcc.Graph(id= "dist-graph")
])

@app.callback (
    Output("dist-graph", "figure"),
    Input("sample-size", "value"),
    Input("probability", "value")
)
def update_graph(size, prob):
    figure = mean_sample_distribution(sample_size= size, probability= prob)
    return figure

if __name__ == '__main__':
    app.run(debug=True)