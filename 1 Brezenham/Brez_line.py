import matplotlib.pyplot as plt

def draw_circle(xc, yc, x, y):
    plt.plot(xc + x, yc + y, 'ro')
    plt.plot(xc - x, yc + y, 'ro')
    plt.plot(xc + x, yc - y, 'ro')
    plt.plot(xc - x, yc - y, 'ro')
    plt.plot(xc + y, yc + x, 'ro')
    plt.plot(xc - y, yc + x, 'ro')
    plt.plot(xc + y, yc - x, 'ro')
    plt.plot(xc - y, yc - x, 'ro')

def draw_bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r
    draw_circle(xc, yc, x, y)

    while y >= x:
        x += 1

        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6

        draw_circle(xc, yc, x, y)
        print(x, y)

draw_bresenham_circle(0, 0, 20)
plt.axis('scaled')
plt.show()
