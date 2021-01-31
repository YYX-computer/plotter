import turtle as t
t.colormode(255)
t.speed(0)
t.delay(0)
def _draw_axis(op,xlab,ylab,p):
    t.hideturtle()
    xsize = max([i[0] for i in p]) + abs(min([i[0] for i in p]))
    ysize = max([i[1] for i in p]) + abs(min([i[1] for i in p]))
    canv = t.getcanvas()
    w,h = canv.winfo_width() - 30,canv.winfo_height() - 30
    if(op == 2):
        xfac = w / 2 / xsize
        yfac = h / 2 / ysize
        t.penup()
        t.goto(0,0)
        t.pendown()
        t.pensize(5)
        t.goto(0,h / 2 - 10)
        t.goto(0,-h / 2 + 10)
        t.goto(0,0)
        t.goto(w / 2 - 10,0)
        t.goto(-w / 2 + 10,0)
        t.goto(0,0)
        t.pensize(2)
        return 15,15,xfac,yfac
    else:
        bx = abs(min(min([i[0] for i in p]), 0))
        by = abs(min(min([i[1] for i in p]), 0))
        bx = int(bx) if(int(bx) == bx) else int(bx) + 1
        by = int(by) if(int(by) == by) else int(by) + 1
        xfac = w / xsize
        yfac = h / ysize
        bx,by = bx * xfac,by * yfac
        t.penup()
        t.goto(-w / 2 + 10,-h / 2 + 10)
        t.pendown()
        t.pensize(5)
        t.goto(w / 2 + 10,-h / 2 + 10)
        t.goto(-w / 2 + 10, -h / 2 + 10)
        t.goto(-w / 2 + 10,h / 2 + 10)
        t.penup()
        t.goto(0,0)
        t.pendown()
        t.pensize(2)
        return -w / 2 + 15 + bx, -h / 2 + 15 + by,xfac,yfac
def _get_gradient(l,r,n,h):
    r1,g1,b1 = l
    r2,g2,b2 = r
    f1 = float(n)
    f2 = float(h - n)
    r3 = int(r1 * f1 + r2 * f2)
    g3 = int(g1 * f1 + g2 * f2)
    b3 = int(b1 * f1 + b2 * f2)
    return (r3,b3,g3)
def draw_curve_matplotlib_style(points,xlabel = '',ylabel = '',linecolor=(0,0,190)):
    xf,yf,xfac,yfac = _draw_axis(1,xlabel,ylabel,points)
    t.pencolor(linecolor)
    t.penup()
    t.goto(points[0][0] + xf,points[0][1] + yf)
    t.pendown()
    for i in points:
        x, y = i
        x, y = x * xfac, y * yfac
        t.goto(x + xf,y + yf)
    t.mainloop()
def draw_scatter_matplotlib_style(points,xlabel = '',ylabel = '',pointcolor=(0,0,190),pointr=1):
    xf,yf,xfac,yfac = _draw_axis(1, xlabel, ylabel,points)
    t.pencolor(pointcolor)
    t.fillcolor(pointcolor)
    for i in points:
        x,y = i
        x,y = x * xfac,y * yfac
        t.penup()
        t.goto(x + xf,y + yf)
        t.pendown()
        t.begin_fill()
        t.circle(pointr)
        t.end_fill()
    t.mainloop()
def draw_contour_matplotlib_style(points,xlabel = '',ylabel = '',low=(0,50,50),high=(0,255,255)):
    xf,yf,xfac,yfac = _draw_axis(1,xlabel,ylabel,points)
    plot = {}
    highest = float('-inf')
    for i in points:
        x, y, z = i
        highest = max(highest, y)
        if (y in plot):
            plot[y].append((x, z))
        else:
            plot[y] = [(x, z)]

    for i in plot:
        t.penup()
        t.goto(plot[i][0][0] + xf,plot[i][0][1] + yf)
        t.pendown()
        t.fillcolor(_get_gradient(low, high, i, highest))
        t.begin_fill()
        for j in plot[i]:
            x, y = j
            x, y = x * xfac, y * yfac
            t.goto(x + xf, y + yf)
        t.end_fill()
    t.mainloop()
def draw_bar_chart_matplotlib_style(points,xlabel = '',ylabel = '',barcolor=(0,0,190),barwidth=5):
    xf,yf,xfac,yfac = _draw_axis(1,xlabel,ylabel,points)
    half_width = barwidth / 2
    t.pencolor(barcolor)
    t.fillcolor(barcolor)
    for i in points:
        x,y = i
        x, y = x * xfac, y * yfac
        t.penup()
        t.goto(x - half_width + xf,yf)
        t.pendown()
        t.begin_fill()
        t.goto(x + half_width + xf,yf)
        t.goto(x + half_width + xf,y + yf)
        t.goto(x - half_width + xf, y + yf)
        t.goto(x - half_width + xf, yf)
        t.end_fill()
    t.mainloop()
def draw_curve_plotter_style(points,xlabel = '',ylabel = '',linecolor=(0,0,190)):
    xf,yf,xfac,yfac = _draw_axis(2,xlabel,ylabel,points)
    t.pencolor(linecolor)
    t.penup()
    t.goto(points[0][0] + xf, points[0][1] + yf)
    t.pendown()
    t.begin_fill()
    for i in points:
        x, y = i
        x, y = x * xfac, y * yfac
        t.goto(x + xf, y + yf)
    t.end_fill()
    t.mainloop()
def draw_scatter_plotter_style(points,xlabel = '',ylabel = '',pointcolor=(0,0,190),pointr=1):
    xf,yf,xfac,yfac = _draw_axis(2,xlabel,ylabel,points)
    t.pencolor(pointcolor)
    t.fillcolor(pointcolor)
    for i in points:
        x, y = i
        x, y = x * xfac, y * yfac
        t.penup()
        t.goto(x + xf, y + yf)
        t.pendown()
        t.begin_fill()
        t.circle(pointr)
        t.end_fill()
    t.mainloop()
def draw_contour_plotter_style(points,xlabel = '',ylabel = '',low=(0,50,50),high=(0,255,255)):
    xf,yf,xfac,yfac = _draw_axis(2,xlabel,ylabel,points)
    plot = {}
    highest = float('-inf')
    for i in points:
        x,y,z = i
        highest = max(highest,y)
        if(y in plot):
            plot[y].append((x,z))
        else:
            plot[y] = [(x,z)]
    for i in plot:
        t.fillcolor(_get_gradient(low,high,i,highest))
        t.penup()
        t.goto(plot[i][0][0] + xf, plot[i][0][1] + yf)
        t.pendown()
        t.begin_fill()
        for j in plot[i]:
            x, y = j
            x, y = x * xfac, y * yfac
            t.goto(x + xf, y + yf)
        t.end_fill()
    t.mainloop()
def draw_bar_chart_plotter_style(points,xlabel = '',ylabel = '',barcolor=(0,0,190),barwidth=5):
    xf,yf,xfac,yfac = _draw_axis(2,xlabel,ylabel,points)
    half_width = barwidth / 2
    t.pencolor(barcolor)
    t.fillcolor(barcolor)
    for i in points:
        x, y = i
        x, y = x * xfac, y * yfac
        t.penup()
        t.goto(x - half_width + xf, yf)
        t.pendown()
        t.begin_fill()
        t.goto(x + half_width + xf, yf)
        t.goto(x + half_width + xf, y + yf)
        t.goto(x - half_width + xf, y + yf)
        t.goto(x - half_width + xf, yf)
        t.end_fill()
    t.mainloop()