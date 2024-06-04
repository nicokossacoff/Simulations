from dash import Dash, html, dcc, Output, Input
from figures import mean_sample_distribution

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children= "Sample Mean Distribution"),
    dcc.Dropdown([50, 200, 500, 1000], value= 50, id= "sample-size"),
    dcc.Graph(id= "dist-graph")
])

@app.callback (
    Output("dist-graph", "figure"),
    Input("sample-size", "value")
)
def update_graph(size):
    mean_sample_distribution(sample_size= size)

if __name__ == '__main__':
    app.run(debug=True)