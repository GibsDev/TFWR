directions = [North, East, South, West]

# Returns a list of tuples [(direction, length/distance)]
def get_path_to(dx, dy):
	cx = get_pos_x()
	cy = get_pos_y()
	s = get_world_size()

	path = []

	delta_x = dx - cx
	if delta_x != 0:
		if delta_x > 0:
			path.append((East, abs(delta_x)))
		else:
			path.append((West, abs(delta_x)))

	delta_y = dy - cy
	if delta_y != 0:
		if delta_y > 0:
			path.append((North, abs(delta_y)))
		else:
			path.append((South, abs(delta_y)))

	return path

def go_to(x, y):
	path = get_path_to(x, y)
	while len(path) > 0:
		direction, length = path.pop()
		for i in range(length):
			move(direction)
	return get_pos_x() == x and get_pos_y() == y 

def setup():
	quick_print("Setting up dino farmer")
	clear()
	change_hat(Hats.Dinosaur_Hat)
	if get_entity_type() == Entities.Apple:
		next_x, next_y = measure()


def run():
	if get_entity_type() == Entities.Apple:
		next_x, next_y = measure()
	if not go_to(next_x, next_y):
		setup()
		

if __name__ == "__main__":
	setup()
	while True:
		run()
		