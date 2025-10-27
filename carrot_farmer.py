import u
import plots

carrot_plots = plots.get_plots_alternating(0, 0, get_world_size(), 4)

def setup():
	quick_print("Prepping carrot layout")
	change_hat(Hats.Carrot_Hat)
	
	for plot in carrot_plots:
		u.go_to_plot(plot)
		harvest()
		u.set_ground_type(Grounds.Soil)
		plant(Entities.Carrot)

def run():
	quick_print("Farming carrot")
	
	for plot in carrot_plots:
		u.go_to_plot(plot)
		harvest()
		plant(Entities.Carrot)