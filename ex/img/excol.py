# Using the https://pypi.org/project/colorgram.py/

import colorgram

colo = colorgram.extract('p1.jpg', 30)
print(colo)

rgb_colors = []
for c in colo:
	r = c.rgb.r
	g = c.rgb.g
	b = c.rgb.b
	n_c = (r, g, b)
	rgb_colors.append(n_c)

print(rgb_colors)
