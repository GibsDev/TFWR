import u
import plots

dino_plots = plots.get_all_plots_alternating()

def setup():
	quick_print("Setting up dino farmer")
	change_hat(Hats.Dinosaur_Hat)
	clear()

def run():
	quick_print("Farming dinosaur bones")
	
	#for plot in dino_plots:
		

if __name__ == "__main__":
	setup()
	while True:
		run()
		