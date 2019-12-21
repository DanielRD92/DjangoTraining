from django.shortcuts import render
from django.http import HttpResponse
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool # HoverTool is used to format graphs

# Create your views here.


def starter(request):
    # This is an instance of an object figure which
    # contains methods to draw plots, glyphs, etc.
    plot=figure()

    # This is a method to draw a chart with circle 
    # points.
    plot.circle([1, 12, 34, 27],[0, 0, 0, 0], size=20, color="blue")

    # This returns a script and a div to embed the html 
    # with the graph.
    script, div = components(plot)
    return render(request, 'starter.html' , {'script': script, 'div':div})

def learning_graph(request):
    x = [1, 2, 3, 4, 5]
    y = [6, 10, 2, -4, 10]
    title = 'My Leaning Graph'

    plot = figure(title= title , 
        x_axis_label= 'High and Lows', 
        y_axis_label= 'Learning Topics', 
    
        plot_width =700,
        plot_height =700, tools="",
              toolbar_location=None,)
    
    #Formatting Graph
    cr = plot.circle(x, y, size=10, color= "blue", fill_color="grey", hover_fill_color="firebrick",
                fill_alpha=0.05, hover_alpha=0.3,
                line_color=None, hover_line_color="white")
    
    plot.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))            
    plot.title.text_font_size = '20pt'
    plot.line(x, y, legend= 'Leaning Line', line_width = 4, line_color = "brown", line_dash = 'dashed')
    plot.background_fill_color = "lightgrey"
    plot.border_fill_color = "whitesmoke"
    plot.min_border_left = 40
    plot.min_border_right = 40
    plot.outline_line_width = 7
    plot.outline_line_alpha = 0.2
    plot.outline_line_color = "purple"

    #Store components 
    script, div = components(plot)
   
    return render(request, 'learning_graph.html' , {'script': script, 'div':div})


def home(request):
    first_graph="My first bokeh graph will be rendered on this page"
    return render(request, 'home.html')