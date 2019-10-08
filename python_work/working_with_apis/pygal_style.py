from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Create the style for use in visualization
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

# Create the style for use in bar_descriptions.py
bar_style = LS('#333366', base_style=LCS)
