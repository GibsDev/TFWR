import u
import plots

setup_plots = plots.get_plots(0, 4, get_world_size(), 3)
setup_plots2 = plots.get_plots(0, 0, get_world_size(), 3)

def setup():
	quick_print("Setting up hay farmer")
	change_hat(Hats.Straw_Hat)
	clear()
	for plot in setup_plots:
		u.go_to_plot(plot)
		u.safe_plant(Entities.Bush)
	for plot in setup_plots2:
		u.go_to_plot(plot)
		u.safe_plant(Entities.Bush)
	u.go_to(0, 3)
	
def run():
	quick_print("Farming hay")
	
	# Farm hay
	for i in range(get_world_size()):
		move(East)
		harvest()
