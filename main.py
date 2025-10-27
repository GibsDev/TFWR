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

# TODO weird substance
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

target_unlock = Unlocks.Pumpkins
targets = None

def get_remaining_items(targets):
	remaining = {}
	added = False
	for target in targets:
		if num_items(target) < targets[target]:
			remaining[target] = targets[target]
			added = True
	if not added:
		return None
	return remaining

last_farmer = None

def run_farmer(farmer):
	if last_farmer != farmer:
		farmer.setup()
	farmer.run()

target_unlock_cost = get_cost(target_unlock)

while True:
	quick_print("Unlock target: ", target_unlock)
	
	# Check if the target is reached
	remaining_items = get_remaining_items(target_unlock_cost)
	quick_print(remaining_items)
	if remaining_items == None:
		# Target reached!
		unlock(target_unlock)
		break
	
	# Ensure essentials
	for item in farm:
		farmer, min, base = farm[item]
		# Kick off farming if below min
		if num_items(item) <= min:
			# Farm until base value
			while num_items(item) < base:
				run_farmer(farmer)
			continue
	
	# Work toward the target items
	for items in remaining_items:
		if num_items(items) < remaining_items[items]:
			farmer, min, base = farm[items]
			run_farmer(farmer)

quick_print("Target reached")