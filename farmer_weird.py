import u

# We don't currently need a lot of weird substance, so it doesn't have to be super efficient

def setup():
	quick_print("Setting up weird substance farmer")
	change_hat(Hats.Wizard_Hat)
	u.go_to(0, 0)
	u.safe_harvest()

def run():
	quick_print("Farming weird substance")

	u.set_ground_type(Grounds.Soil)
	plant(Entities.Tree)
	use_item(Items.water)
	use_item(Items.Fertilizer)
	while not can_harvest():
		wait_please = 0
	harvest()

if __name__ == "__main__":
	setup()
	while True:
		run()
