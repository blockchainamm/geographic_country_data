# import required packages
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import kaleido 

# Print kaleido version
kaleido.__version__ 

import plotly
# Print plotly version
print(plotly.__version__)

# Load country geographic data set
country_data = px.data.gapminder()
country_data.tail()

map_fig = px.scatter_geo(country_data,
                         locations = 'iso_alpha',
                         projection = 'orthographic',
                         color = 'continent',
                         opacity = 0.8,
                         hover_name = 'country',
                         hover_data = ['lifeExp', 'pop', 'year' ]
)

# Show the geo scatter plot in a browser
map_fig.show()

# Save the scatter geo plot to a html file and open in a browser when auto_open is set to True
# Only save the scatter geo plot to a html file and not open in a browser when auto_open is set to False
plotly.offline.plot(map_fig, filename = "map.html", auto_open=False)

