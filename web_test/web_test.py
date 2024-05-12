data = [5, 10, 8, 3, 2, 7]
bar_width = 50
x_pos = 5


def setup():
    createCanvas(600, 400)
    noStroke()
    textAlign(CENTER)


def draw():
    global x_pos, bar_width, data
    # background(255)
    fill(0)
    textSize(20)
    text("Bar Chart", width / 2, 30)

    for i in range(len(data)):
        fill(200, 0, 0)
        rect(x_pos, height - data[i] * 10, bar_width, data[i] * 10)
        fill(0)
        text(str(data[i]), x_pos + bar_width / 2, height - data[i] * 10 - 10)
        x_pos += bar_width + 10
