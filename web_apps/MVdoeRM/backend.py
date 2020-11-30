import numpy as np

from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from bokeh.plotting import figure
import bokeh
import seaborn as sns; sns.set_theme()
import matplotlib.pyplot as plt

print(bokeh.__version__)

uniform_data = np.random.rand(10, 12)
ax = sns.heatmap(uniform_data)

fig, ax = plt.subplots(figsize=(11, 9))
sns.heatmap(uniform_data)


# Set up data
N = 200
x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)
source = ColumnDataSource(data=dict(x=x, y=y))


# Set up plot
plot = figure(plot_height=400, plot_width=400, title="my sine wave",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[0, 4*np.pi], y_range=[-2.5, 2.5])

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)



# Set up layouts and add to document
curdoc().add_root(row(inputs, fig, width=800))
curdoc().title = "Sliders"