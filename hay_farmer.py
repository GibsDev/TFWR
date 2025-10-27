import u
import plots

hay_plots = plots.get_plots_alternating(0, 0, get_world_size(), 1)

def setup():
	quick_print("Setting up hay farmer")
	change_hat(Hats.Straw_Hat)
	
def run():
	quick_print("Farming hay")
	
	# Farm hay
	u.go_to(0, 0)
	for i in world_range:
		move(East)
		harvest()
