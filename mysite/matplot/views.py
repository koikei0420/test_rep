# coding:utf-8
from django.shortcuts import render


def index(request):
    return render(request, 'matplot/index.html')


def simple(request, func):
    from django.http import HttpResponse
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

    from io import BytesIO
    import urllib
    import matplotlib.pyplot as plt
    import numpy as np

    fig = plt.figure(figsize=(4,4))
    x = np.linspace(-np.pi/4, np.pi/4, 100)
    if func == 'sin':
        y = np.sin(x)
    elif func == 'cos':
        y = np.cos(x)
    elif func == 'tan':
        y = np.tan(x)
    else:
        y = x
    plt.plot(x, y)

    canvas = FigureCanvas(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)

    img_data = urllib.parse.quote(png_output.getvalue())
    return HttpResponse(img_data)
