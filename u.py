def get_path_to(dx, dy):
	cx = get_pos_x()
	cy = get_pos_y()
	s = get_world_size()

	path = []

	# --- X axis ---
	delta_x = (dx - cx + s) % s
	if delta_x != 0:
		if delta_x <= s / 2:
			path.append({"direction": East, "length": delta_x})
		else:
			path.append({"direction": West, "length": s - delta_x})

	# --- Y axis ---
	delta_y = (dy - cy + s) % s
	if delta_y != 0:
		if delta_y <= s / 2:
			path.append({"direction": North, "length": delta_y})
		else:
			path.append({"direction": South, "length": s - delta_y})

	return path

# Moves to a specific coordinate
# Optionally will perform a callback function at each step
# Callback can be configured to occur on the first step or not
def go_to(x, y, step_func=None, first_step=False):
	if first_step and step_func != None:
		step_func()
	path = get_path_to(x, y)
	while len(path) > 0:
		segment = path.pop()
		for i in range(segment["length"]):
			move(segment["direction"])
			if step_func != None:
				step_func()
				
def go_to_plot(plot):
	go_to(plot["x"], plot["y"])
	

def go(x, y, harvest=True):
	size = get_world_size()
	if x < 0 or y < 0 or x > size - 1 or y > size - 1:
		quick_print("Move out of bounds: { x: ", x, ", y: ", y, " }")
	while get_pos_x() != x or get_pos_y() != y:
		step_to(x, y)
		if harvest:
			try_harvest()
		
def get_item_counts():
	weights = {}
	for item in list(Items):
		weights[item] = num_items(item)
	return weights

def set_ground_type(type):
	if get_ground_type() != type:
		till()

def try_harvest():
	if can_harvest():
		harvest()

def random_index(length):
	return random() * length // 1
	

def random_elem(list):
	return list[random_index(len(list))]
	
def fill_array(len, fill):
	arr = []
	for i in range(len):
		arr.append(fill)
	return arr

def weighted_pick(items, weights):
	total_weight = 0
	for weight in weights:
		total_weight = total_weight + weight
	percents = []
	for weight in weights:
		percent = weight / total_weight
		percents.append(percent)
	roll = random()
	for i in range(len(weights)):
		if roll <= percents[i]:
			return items[i]
		else:
			roll = roll - percents[i]
	return items[len(items) - 1]
	
# Breaks down the items in a dictionary
# into a list of tuples [key, value]
def items(dict):
	out = []
	for key in list(dict):
		out.append([key, dict[key]])
	return out

# Plant and wait for a companion and return back
def assert_companion():
	x = get_pos_x()
	y = get_pos_y()
	com_plant_type, (com_x, com_y) = get_companion()
	go_to(com_x, com_y)
	if get_entity_type() != com_plant_type:
		plant(com_plant_type)
	while not can_harvest():
		do_a_flip()
	go_to(x, y)