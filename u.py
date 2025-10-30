# Returns a list of tuples [(direction, length/distance)]
def get_path_to(dx, dy):
	cx = get_pos_x()
	cy = get_pos_y()
	s = get_world_size()

	path = []

	delta_x = (dx - cx + s) % s
	if delta_x != 0:
		if delta_x <= s / 2:
			path.append((East, delta_x))
		else:
			path.append((West, s - delta_x))

	delta_y = (dy - cy + s) % s
	if delta_y != 0:
		if delta_y <= s / 2:
			path.append((North, delta_y))
		else:
			path.append((South, s - delta_y))

	return path

# Moves to a specific coordinate
# Optionally will perform a callback function at each step
# Callback can be configured to occur on the first step or not
def go_to(x, y, step_func=None, first_step=False):
	if first_step and step_func != None:
		step_func()
	path = get_path_to(x, y)
	while len(path) > 0:
		direction, length = path.pop()
		for i in range(length):
			move(direction)
			if step_func != None:
				step_func()
				
def go_to_plot(plot):
	go_to(plot[0], plot[1])
		
def get_item_counts():
	weights = {}
	for item in Items:
		weights[item] = num_items(item)
	return weights

def set_ground_type(type):
	if get_ground_type() != type:
		till()

def safe_harvest():
	if can_harvest():
		harvest()

def safe_plant(plant_type):
	safe_harvest()
	if plant_type == Entities.Grass:
		set_ground_type(Grounds.Grassland)
	elif plant_type == Entities.Carrot:
		set_ground_type(Grounds.Soil)
	elif plant_type == Entities.Sunflower:
		set_ground_type(Grounds.Soil)
	elif plant_type == Entities.Cactus:
		set_ground_type(Grounds.Soil)
	elif plant_type == Entities.Pumpkin:
		set_ground_type(Grounds.Soil)
	plant(plant_type)

# Returns a random int from 0-max (exclusive)
def random_int(max):
	return random() * max // 1

def random_elem(list):
	return list[random_index(len(list))]

def fill(item, count):
	out = []
	for i in range(count):
		out.append(item)
	return out