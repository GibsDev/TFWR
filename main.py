import u
import plots
import algos

import farmer_pumpkin
import farmer_sunflower
import farmer_hay
import farmer_wood
import farmer_carrot
import farmer_cactus
import farmer_weird
import farmer_gold
import farmer_poly
import farmer_bone

# Resource order [function, min, base]
# 0: function is the callback to start harvesting that resource
# 1: min is the threshold when farming should begin
# 2: base is how long to farm until if min is triggered
farm = {
	Items.Power:[farmer_sunflower, 1000, 5000],
	Items.Hay:[farmer_hay, 500000, 5000000],
	Items.Wood:[farmer_wood, 500000, 5000000],
	Items.Carrot:[farmer_carrot, 500000, 1500000],
	Items.Pumpkin:[farmer_pumpkin, 500000, 1500000],
	Items.Cactus:[farmer_cactus, 100000, 1000000],
	Items.Weird_Substance:[farmer_weird, 1000000, 5000000],
	Items.Bone:[farmer_bone, 0, 0],
	Items.Gold:[farmer_gold, 0, 0],
}

target_unlock = Unlocks.Dinosaurs
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
	global last_farmer
	if last_farmer != farmer:
		farmer.setup()
	farmer.run()
	last_farmer = farmer

target_unlock_cost = get_cost(target_unlock)

while True:
	# quick_print("Unlock target: ", target_unlock)

	# Check if the target is reached
	remaining_items = get_remaining_items(target_unlock_cost)
	# quick_print(remaining_items)
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