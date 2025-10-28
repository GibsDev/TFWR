import u
import plots
import algos

target_sunflower_plots = plots.get_plots_alternating(0, 0, 10, 10)

def sunflower_comp(a, b):
	return b["pedals"] - a["pedals"]

def setup():
	quick_print("Setting up sunflower farmer")
	change_hat(Hats.Sunflower_Hat)

def run():
	quick_print("Farming sunflowers")
	
	max_pedals = 0
	# Ordered list of plots to farm highest first
	harvest_queue = []

	# Plant the sunflowers
	quick_print("Planting sunflowers")
	for plot in target_sunflower_plots:
		u.go_to_plot(plot)

		if get_entity_type() == Entities.Sunflower:
			pedals = measure()
		else:
			harvest()
			u.set_ground_type(Grounds.Soil)
			plant(Entities.Sunflower)
			pedals = measure()

		# Insert the current plot into the harvesting queue
		data = {"plot": plot, "pedals": pedals}
		algos.binary_insert(harvest_queue, data, sunflower_comp)

	# Harvest the sunflowers
	quick_print("Harvesting sunflowers")
	while len(harvest_queue) > 10:
		u.go_to_plot(harvest_queue[0]["plot"])
		if can_harvest():
			harvest()
			harvest_queue.pop(0)
		else:
			# Use this as a delay function
			d_e_l_a_y = 1