from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('poblacion_colombia.html')
    fig = figure(title="Crecimiento de población de Colombia en los últimos 10 años", x_axis_label='Año', y_axis_label='Población')
    
    total_years = 10
    x_vals = list(range(total_years))
    y_vals = []

    for x in x_vals:
        val = int(input(f'Población para el año {x+2013}: '))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
