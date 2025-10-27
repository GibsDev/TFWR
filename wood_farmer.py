import u
import plots

wood_plots = plots.get_plots_alternating(0, 0, get_world_size(), 4)

def setup():
	quick_print("Setting up wood farmer")
	change_hat(Hats.Brown_Hat)
	
	clear()

def run():
	for plot in wood_plots:
		u.go_to_plot(plot)
		harvest()
		if plot["y"] % 2 == plot["x"] % 2:
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)