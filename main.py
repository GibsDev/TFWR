import u
import plots
import algos

import pumpkin_farmer
import sunflower_farmer
import hay_farmer
import wood_farmer
import carrot_farmer
import cactus_farmer

# Keep track of the most recently used farm strategy
last_farm = ""

# Resource order [function, min, base]
# 0: function is the callback to start harvesting that resource
# 1: min is the threshold when farming should begin
# 2: base is how long to farm until if min is triggered
farm = {
	Items.Power:[sunflower_farmer, 100, 2000],
	Items.Hay:[hay_farmer, 500000, 5000000],
	Items.Wood:[wood_farmer, 500000, 5000000],
	Items.Carrot:[carrot_farmer, 500000, 1500000],
	Items.Pumpkin:[pumpkin_farmer, 500000, 1500000],
	Items.Cactus:[cactus_farmer, 10000, 100000],
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


target_unlock = Unlocks.Pumpkins
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

last_target = None

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
				# Setup if we are migrating farmers
				if target != last_target:
					farm[target][0].setup()
				# Run the farmer
				farm[target][0].run()
				last_target = target
				continue
		
	
	# Unlock the thing
	unlock(target_unlock)
		