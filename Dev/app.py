from dash import Dash, html, dcc, Output, Input
from figures import mean_sample_distribution

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children= "Sample Mean Distribution"),
    dcc.Markdown('''
                 Calculates a thousand sample means from random samples with `n` observations. Each observation is a Bernoulli test with probability `p`.
                 '''),
    # dcc.Dropdown([50, 200, 500, 1000], value= 50, id= "sample-size"),
    html.Div(children= [
        html.Div(children= [
            html.H5(children= "Sample size:"),
            dcc.Slider(min= 100, max= 1000, step= 100, value= 100, id= "sample-size", tooltip= {"placement": "bottom", "always_visible": True})
        ], style= dict(width= "50%")),
        html.Div(children= [
            html.H5(children= "Probability:"),
            dcc.Dropdown([.1, .35, .5, .75], value= .35, id= "probability")
        ], style= dict(width= "50%"))
    ], style= dict(display= "flex")),
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