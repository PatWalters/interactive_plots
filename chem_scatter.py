#!/usr/bin/env python

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from rdkit import Chem
from rdkit.Chem.Draw import MolsToGridImage
import base64
from io import BytesIO

df = pd.read_csv("tsne.csv")
active = df.query("is_active == 1")
decoy = df.query("is_active == 0")

graph_component = dcc.Graph(
    id='tsne',
    config={'displayModeBar': False},
    figure={
        'data': [
            go.Scattergl(
                x=decoy.X,
                y=decoy.Y,
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 5,
                    'color': 'orange',
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name="Decoy"
            ),
            go.Scattergl(
                x=active.X,
                y=active.Y,
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 10,
                    'color': 'blue',
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name="Active"
            )
        ],
        'layout': go.Layout(
            height=400,
            xaxis={'title': 'X'},
            yaxis={'title': 'Y'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 1, 'y': 1},
            hovermode=False,
            dragmode='select'
        )
    }
)

image_component = html.Img(id="structure-image")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([graph_component]),
    html.Div([image_component])
])

@app.callback(
    Output('structure-image', 'src'),
    [Input('tsne', 'selectedData')])
def display_selected_data(selectedData):
    max_structs = 12
    structs_per_row = 6
    empty_plot = "data:image/gif;base64,R0lGODlhAQABAAAAACwAAAAAAQABAAA="
    if selectedData:
        if len(selectedData['points']) == 0:
            return empty_plot
        match_idx = [x['pointIndex'] for x in selectedData['points']]
        match_df = df.iloc[match_idx]
        smiles_list = list(match_df.SMILES)
        name_list = list(match_df.Name)
        active_list = list(df.is_active)
        mol_list = [Chem.MolFromSmiles(x) for x in smiles_list]
        name_list = [x + " " + str(y) for (x, y) in zip(name_list, active_list)]
        img = MolsToGridImage(mol_list[0:max_structs], molsPerRow=structs_per_row, legends=name_list)
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        encoded_image = base64.b64encode(buffered.getvalue())
        src_str = 'data:image/png;base64,{}'.format(encoded_image.decode())
    else:
        return empty_plot
    return src_str

if __name__ == '__main__':
    import socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)    
    app.run_server(debug=True,host=IPAddr)
    
    
