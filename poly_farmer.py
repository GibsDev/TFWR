import u

MAX_QUEUE_SIZE = get_world_size() * get_world_size()

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

	u.set_ground_type(Grounds.Soil)
	plant(Entities.Tree)
	plot = (get_pos_x(), get_pos_y())
	plot_queue.append(plot)
	planted[plot] = True
	# TODO replace with max size
	for i in range(MAX_QUEUE_SIZE):
		plant_type, plot = get_companion()
		if plot in planted:
			# Loop detected!
			quick_print("Loop detected at ", len(plot_queue), " plots")
			break
		else:
			u.go_to_plot(plot)
			u.safe_plant(plant_type)
			plot_queue.append(plot)
			planted[plot] = True

	quick_print(plot_queue)

	# Farm the chain in reverse order
	while len(plot_queue) > 0:
		target = plot_queue.pop(0)
		u.go_to_plot(target)
		while not can_harvest():
			use_item(Items.Fertilizer)
			do_some_waiting = 0
		harvest()
