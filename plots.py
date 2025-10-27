def get_all_plots():
	return get_plots(0, 0, get_world_size(), get_world_size())

def get_all_plots_alternating():
	plots = []
	size = get_world_size()
	for y in range(size):
		row = range(0, size)
		if y % 2 == 1:
			row = range(size - 1, -1, -1)
		for x in row:
			plots.append((x, y))
	return plots

def get_plots(x, y, width, height):
	plots = []
	for yy in range(y, y + height):
			for xx in range(x, x + width):
				plots.append((xx, yy))
	return plots

def get_plots_alternating(x, y, width, height):
	plots = []
	for yy in range(y, y + height):
		row = range(x, x + width)
		if yy % 2 == 1:
			row = range(x + width - 1, x - 1, -1)
		for xx in row:
			plots.append((xx, yy))
	return plots

# Splits a chunk off a set of plots
def split_plots(source_plots, x, y, width, height):
	chunk_size = width * height
	chunk = []
	i = 0
	while i < len(source_plots):
		if source_plots[i][0] >= x and source_plots[i][0] < x + width and source_plots[i][1] >= y and source_plots[i][1] < y + height:
			chunk.append(source_plots.pop(i))
			i = i - 1
		if len(chunk) == chunk_size:
			break
		i = i + 1
	return [source_plots, chunk]

def filter(plots, filter):
	i = 0
	while i < len(plots):
		if not filter(plots[i]):
			plots.pop(i)
			i = i - 1
		i = i + 1
	return plots
