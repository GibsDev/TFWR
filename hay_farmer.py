import u
import plots

hay_plots = plots.get_plots_alternating(0, 0, get_world_size(), 1)

def setup():
	quick_print("Setting up hay farmer")
	change_hat(Hats.Straw_Hat)
	clear()
	
def run():
	quick_print("Farming hay")
	
	# Farm hay
	u.go_to(0, 0)
	for i in range(get_world_size()):
		move(East)
		harvest()
