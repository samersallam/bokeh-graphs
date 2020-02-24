"""
Credits to
https://davidhamann.de/2018/02/11/integrate-bokeh-plots-in-flask-ajax/?fbclid=IwAR27tc3D51n7xX_HgmqAdJ0yIB3mvwIRz-DNZfg5XyEp__CFEHLrlpldXTA
"""
"""
Be careful from the bokeh library version and the script version inside the layout file
"""

from flask import render_template
from bokeh.plotting import figure
from bokeh.embed import components

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/dashboard/')
def show_dashboard():
    plots = []
    plots.append(make_plot())

    return render_template('dashboard.html', plots=plots)

def make_plot():
    plot = figure(plot_height=300, sizing_mode='scale_width')

    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [2**v for v in x]

    plot.line(x, y, line_width=4)

    script, div = components(plot)
    return script, div


if __name__ == '__main__':
    app.run(debug=True)