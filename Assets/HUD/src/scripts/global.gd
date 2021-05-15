extends Node


var music_volume:=0
var sound_volume:=0
var lang:="en"
var localisation:="world"
var high_quality:=false
var show_fps:=false
var vsync_enabled:=false
var timer_choice:=0
var textspeed:=0.0


const CONFIG_FILE:String = "user://options.cfg"
const INPUT_FILE:String = "user://input.cfg"
const DEFAULT_INPUT_FILE:String = "user://default_input.cfg"
const INPUT_ACTIONS:Array = ["move_up_ow","move_down_ow","move_right_ow","move_left_ow","interaction"]
var default_input_actions:Dictionary = {}

func _ready():
	load_config()
	load_input(DEFAULT_INPUT_FILE)
	load_input(INPUT_FILE)

func save_to_config(section, key, value):
	"""Helper function to redefine a parameter in the settings file"""
	var config = ConfigFile.new()
	var err = config.load(CONFIG_FILE)
	if err:
		print("Error code when loading config file: ", err)
	else:
		config.set_value(section, key, value)
		config.save(CONFIG_FILE)
func load_config():
	var config = ConfigFile.new()
	var err = config.load(CONFIG_FILE)
	if err:
		config.set_value("reglage","vsync",OS.vsync_enabled)
		#config.set_value("reglage","fps",show_fps)
		config.set_value("reglage","timer",timer_choice)
		config.set_value("reglage","lang",lang)
		config.set_value("reglage","music_volume",music_volume)
		config.set_value("reglage","sound_volume",sound_volume)
		config.set_value("reglage","high_quality",high_quality)
		config.set_value("reglage","textspeed",textspeed)
		config.set_value("reglage","fullscreen",OS.window_fullscreen)
		config.save(CONFIG_FILE)
	else:
		for name in config.get_section_keys("reglage"):
			if name=="sound_volume":
				sound_volume=config.get_value("reglage", name)
			if name=="music_volume":
				music_volume=config.get_value("reglage", name)
			if name=="high_quality":
				high_quality=config.get_value("reglage", name)
			if name=="timer":
				timer_choice=config.get_value("reglage", name)
			if name=="textspeed":
				textspeed=config.get_value("reglage", name)
			if name=="vsync":
				OS.vsync_enabled=config.get_value("reglage", name)
			if name=="lang":
				lang=config.get_value("reglage",name)
				TranslationServer.set_locale(lang)
			if name=="fullscreen":
				OS.window_fullscreen=config.get_value("reglage",name)
func load_input(file=INPUT_FILE):
	var config = ConfigFile.new()
	var err = config.load(file)
	if err:
		for action_name in INPUT_ACTIONS:
			var action_list = InputMap.get_action_list(action_name)

			config.set_value("input", action_name, action_list)
		config.save(file)
	else:
		for action_name in config.get_section_keys("input"):
			for old_event in InputMap.get_action_list(action_name):
				InputMap.action_erase_event(action_name, old_event)
			for new_event in config.get_value("input", action_name):
				InputMap.action_add_event(action_name, new_event)
				
func save_to_input(section, key, value):
	"""Helper function to redefine a parameter in the settings file"""
	var config = ConfigFile.new()
	var err = config.load(INPUT_FILE)
	if err:
		print("Error code when loading config file: ", err)
	else:
		config.set_value(section, key, value)
		config.save(INPUT_FILE)

func switch_quality():
	high_quality=!high_quality
	global.save_to_config("reglage","high_quality",global.high_quality)
#	for obj in get_tree().get_nodes_in_group("lightsetting"):
#		obj.reset()
