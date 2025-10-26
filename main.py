import u
import plots
import algos

# Keep track of the most recently used farm strategy
last_farm = ""

# Define farming strategies

hay_plots = plots.get_plots_alternating(0, 0, get_world_size(), 1)

def farm_hay():
	quick_print("Farming hay")
	global last_farm
	if not last_farm == "hay":
		# Prep hay
		quick_print("Prepping hay layout")
		for plot in hay_plots:
			u.go_to_plot(plot)
			u.set_ground_type(Grounds.Grassland)
		tree_plots = plots.get_plots(0, 1, get_world_size(), 3)
		other_tree_plots = plots.get_plots(0, get_world_size() - 3, get_world_size(), 3)
		for plot in other_tree_plots:
			tree_plots.append(plot)
		for plot in tree_plots:
			u.go_to_plot(plot)
			u.set_ground_type(Grounds.Grassland)
			plant(Entities.Tree)
	last_farm = "hay"
	
	# Farm hay
	u.go_to(0, 0)
	for i in range(get_world_size()):
		move(East)
		harvest()
	return

wood_plots = plots.get_plots_alternating(0, 0, get_world_size(), 4)

def farm_wood():
	quick_print("Farming wood")

	global last_farm
	if not last_farm == "wood":
		quick_print("Prepping wood layout")
		# Prep wood
		clear()
	last_farm = "wood"

	for plot in wood_plots:
		u.go_to_plot(plot)
		harvest()
		if plot["y"] % 2 == plot["x"] % 2:
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
	return

def farm_carrot():
	quick_print("Farming carrot")
	# TODO

pumpkin_plots1 = plots.get_plots_alternating(0, 0, 6, 6)
pumpkin_plots2 = plots.get_plots_alternating(0, 7, 6, 6)

def farm_pumpkin():
	quick_print("Farming pumpkin")

	global last_farm
	if not last_farm == "pumpkin":
		quick_print("Prepping pumpkin layout")
		# Prep pumpkin
	last_farm = "pumpkin"
	
	def pumpkin(plots):
		u.go_to_plot(plots[0])
		first_id = measure()
		for plot in plots:
			u.go_to_plot(plot)
			if not (can_harvest() and get_entity_type() == Entities.Pumpkin):
				u.set_ground_type(Grounds.Soil)
				if can_harvest():
					harvest()
				plant_item(Entities.Pumpkin)
		if measure() == first_id:
			if can_harvest():
				harvest()
		
	pumpkin(pumpkin_plots1)
	pumpkin(pumpkin_plots2)
	
def farm_cactus():
	quick_print("Farming cactus")
	# TODO

target_sunflower_plots = plots.get_plots_alternating(0, 0, 10, 10)

def sunflower_comp(a, b):
	return b["pedals"] - a["pedals"]

def farm_sunflower():
	quick_print("Farming sunflower")
	
	global last_farm
	if not last_farm == "sunflower":
		quick_print("Prepping sunflower layout")
		change_hat(Hats.Sunflower_Hat)
		# Prep pumpkin
	last_farm = "sunflower"
	
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

# Resource order [function, min, base]
# 0: function is the callback to start harvesting that resource
# 1: min is the threshold when farming should begin
# 2: base is how long to farm until if min is triggered
farm = {
	Items.Power:[farm_sunflower, 100, 2000],
	Items.Hay:[farm_hay, 500000, 1500000],
	Items.Wood:[farm_wood, 500000, 1500000],
	Items.Carrot:[farm_carrot, 500000, 1500000],
	Items.Pumpkin:[farm_pumpkin, 500000, 1500000],
	Items.Cactus:[farm_cactus, 10000, 100000],
}

# TODO weird substance

# if we run out of resources to plant something
# don't know it this works
def plant_item(item):
	costs = get_remaining_targets(get_cost(item))
	if costs != None:
		for cost in costs:
			farm[cost]()
	plant(item)


target_unlock = Unlocks.Carrots
targets = None

def get_remaining_targets(targets):
	remaining = {}
	added = False
	for target in targets:
		if num_items(target) < targets[target]:
			remaining[target] = targets[target]
			added = True
	if not added:
		return None
	return remaining

while True:
	# Get next target unlock
	for _unlock in Unlocks:
		# Attempt to unlock
		if unlock(_unlock):
			continue
		# TODO we need to come up with a better target selection algorithm
		# if get_remaining_targets(get_cost(_unlock)) != None and _unlock != Unlocks.Auto_Unlock:
		# 	target_unlock = _unlock
	
	quick_print("target_unlock: ", target_unlock)

	# Get resources needed for target unlock
	targets = get_cost(target_unlock)
	
	# Loop until target reached
	while True:
		quick_print("target_unlock: ", target_unlock)
		
		# Check if the target is reached
		remaining_targets = get_remaining_targets(targets)
		quick_print(remaining_targets)
		if remaining_targets == None:
			# Target reached!
			break
		
		# Ensure essentials
		for item in farm:
			func, min, base = farm[item]
			# Kick off farming if below min
			if num_items(item) <= min:
				# Farm until base value
				while num_items(item) < base:
					func()
				continue
		
		# Work toward the targets
		for target in remaining_targets:
			if num_items(target) < remaining_targets[target]:
				farm[target][0]()
				continue
		
	
	# Unlock the thing
	unlock(target_unlock)
		