import pandas as pd
import numpy as np
import warnings
import os
import plotly.graph_objs as go

warnings.filterwarnings("ignore")

## This function is used to generate 1K random samples with n observations each
## We calculate the mean sample for each random sample and then we plot its ditribution

def mean_sample_distribution(sample_size: int, probability: float = 0.35):
    estimations = np.zeros(shape= 1000)
    for i in np.arange(start= 0, stop= 1000, step= 1):
        sample = np.random.binomial(n= 1, p= probability, size= sample_size)
        estimations[i] = np.mean(sample)
    
    hist = go.Histogram(histfunc= "count",
                        x= estimations,
                        nbinsx= 15,
                        marker= dict(color= "#4DBAC1",
                                     line= dict(width= 1, color= "black")
                                    )
                        )
    fig = go.Figure(data= [hist])
    fig.update_layout(yaxis= dict(title= "Frequency",
                                  showline= True,
                                  linecolor= "black",
                                  ticks= "outside",
                                  gridcolor= "lightgrey"),
                      xaxis= dict(showline= True,
                                  linecolor= "black",
                                  ticks= "outside",
                                  gridcolor= "lightgrey",
                                  range= [0, 1]),
                      plot_bgcolor= "white",
                      title= dict(text= f"Sample Mean distribution with n = {sample_size}",
                                  font= dict(size= 16, color= "black", family= "Arial Black")
                                  ),
                      height= 800  
                      )          
    return fig