import u
import plots

pumpkin_plots1 = plots.get_plots_alternating(0, 0, 6, 6)
pumpkin_plots2 = plots.get_plots_alternating(0, 7, 6, 6)

def setup():
	quick_print("Setting up pumpkin farmer")
	change_hat(Hats.Pumpkin_Hat)
	
def pumpkin(target_plots):
	u.go_to_plot(target_plots[0])
	first_id = measure()
	for plot in target_plots:
		u.go_to_plot(plot)
		if not (can_harvest() and get_entity_type() == Entities.Pumpkin):
			u.set_ground_type(Grounds.Soil)
			if can_harvest():
				harvest()
			plant_item(Entities.Pumpkin)
	if measure() == first_id:
		if can_harvest():
			harvest()
				
def run():
	quick_print("Farming pumpkin")
	pumpkin(pumpkin_plots1)
	pumpkin(pumpkin_plots2)

if __name__ == "__main__":
	setup()
	while True:
		run()
