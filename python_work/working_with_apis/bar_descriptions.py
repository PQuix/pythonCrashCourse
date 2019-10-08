import pygal

from pygal_style import bar_style

chart = pygal.Bar(style=bar_style, x_label_rotation=-45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['awesome-python', 'system-design-primer', 'public-apis']

plot_dicts = [
    {'value': 68010, 'label': 'Description of awesome-python.'},
    {'value': 63817, 'label': 'Description of system-design-primer.'},
    {'value': 57514, 'label': 'Description of public-apis.'}
]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')