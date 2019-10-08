import pygal

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active
while True:
    # Make a random walk, and plot the points
    rw = RandomWalk(5000)
    rw.fill_walk()

    scatter = pygal.XY()
    scatter.title = 'Random Walkz'
    scatter.add('Random Walk', [(0, 0)])
    scatter.add('Start', [(0, 0)])
    scatter.add('End', [(rw.x_values, rw.y_values)])
    scatter.render_to_file('scatter.svg')
    
    