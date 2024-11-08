from cmu_graphics import *

def onAppStart(app):
    app.points = [ ]

def redrawAll(app):
    drawLabel('Click to add points to the polygon', app.width/2, 30, size=16)
    drawPolygon(*app.points, fill='cyan', border='black')

    # to make things clearer, let's draw a dot on each point
    for i in range(0, len(app.points), 2):
        cx, cy = app.points[i], app.points[i+1]
        drawCircle(cx, cy, 1)
    print(app.points)

def onMousePress(app, mouseX, mouseY):
    app.points.append(mouseX)
    app.points.append(mouseY)

def main():
    runApp()

main()