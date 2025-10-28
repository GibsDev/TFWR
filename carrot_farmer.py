import u
import plots

# We could optimize this strat when we have water
# With watered plots, we could get away with farming a single row loop

carrot_plots = plots.get_plots(0, 0, get_world_size(), 1)
carrot_plots2 = plots.get_plots(0, 4, get_world_size(), 1)
for plot in carrot_plots2:
	carrot_plots.append(plot)

def setup():
	quick_print("Prepping carrot layout")
	change_hat(Hats.Carrot_Hat)
	
	clear()
	for plot in carrot_plots:
		u.go_to_plot(plot)
		harvest()
		u.set_ground_type(Grounds.Soil)
		plant(Entities.Carrot)

def run():
	quick_print("Farming carrot")
	
	for plot in carrot_plots:
		u.go_to_plot(plot)
		quick_print(get_companion())
		harvest()
		plant(Entities.Carrot)