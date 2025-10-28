# This farmer spends a lot of time prepping, so I don't think it's really viable alone
# I think companions are better suited as an optimization for other algorithms
# It may come more into play if it can be parallelized using multiple drones

import u
import plots

MAX_QUEUE_SIZE = get_world_size() * get_world_size()

PREFFERED_CHAIN_MIN = 256

alternating_plots = plots.get_all_plots_alternating()

def setup():
	quick_print("Setting up poly farmer")
	# TODO This strategy probably works better with a smaller world
	# Set it here with the function once it's unlocked

	clear()
	u.go_to(0, 0)
	
def run():
	quick_print("Running poly farmer")
	
	plot_queue = []
	# Use a dictionary as a hash map to track
	# which plots we've already visited to detect loops
	planted = {}

	possible_start_plots = plots.get_all_plots_alternating()

	# TODO try and break the chain if the drone gets too far from the start point?
	# This could help harvesting speed by keeping the harvest path shorter
	u.set_ground_type(Grounds.Soil)
	plant(Entities.Tree)
	plot = (get_pos_x(), get_pos_y())
	plot_queue.append(plot)
	planted[plot] = True
	for i in range(MAX_QUEUE_SIZE):
		plant_type, plot = get_companion()
		if plot in planted:
			# Loop detected!
			quick_print("Loop detected at ", len(plot_queue), " plots")
			# Start a new chain from unused plot if the chain is too small
			if len(plot_queue) < MAX_QUEUE_SIZE / 2:
				new_chain_start = possible_start_plots.pop()
				while new_chain_start in planted:
					new_chain_start = possible_start_plots.pop()
				u.go_to_plot(new_chain_start)
				u.set_ground_type(Grounds.Soil)
				plant(Entities.Tree)
				plot_queue.append(new_chain_start)
				planted[new_chain_start] = True
				continue
			else:
				break
		else:
			u.go_to_plot(plot)
			u.safe_plant(plant_type)
			plot_queue.append(plot)
			planted[plot] = True

	# Farm the chain in order to take advantage of companions
	while len(plot_queue) > 0:
		target = plot_queue.pop(0)
		u.go_to_plot(target)
		while not can_harvest():
			use_item(Items.Fertilizer)
			do_some_waiting = 0
		harvest()

if __name__ == "__main__":
	setup()
	while True:
		run()
