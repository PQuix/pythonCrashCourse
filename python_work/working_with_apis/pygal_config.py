import pygal

# Create the config for use in visualization
my_config = pygal.Config()
my_config.x_label_rotation = -90
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000