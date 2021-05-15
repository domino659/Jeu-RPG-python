extends CanvasLayer

signal close()

var timer_text:Array=["MENU_NONE","MENU_LEVEL","MENU_BOTH"]
onready var button_langue:Button=get_node("reglage/Button_langue")
onready var button_chrono:Button=get_node("reglage/Button_chrono")
onready var button_text:Button=get_node("reglage/Button_text")
onready var text_music:Label=get_node("reglage/text_volumemusic")
onready var text_son:Label=get_node("reglage/text_volumeson")
onready var button_fullscreen:Button=get_node("reglage/button_fullscreen")
var varkeybinding:bool=false
func _ready()->void:
	get_node("reglage/musique").value=global.music_volume
	get_node("reglage/son").value=global.sound_volume
	var button_vsync:Button=get_node("reglage/button_vsync")
	button_chrono.set_text(timer_text[global.timer_choice])
	button_langue.set_text(global.lang)
	button_chrono.grab_focus()
	text_son.set_text(str(global.sound_volume))
	text_music.set_text(str(global.music_volume))
	refresh_textspeed()
	if OS.vsync_enabled:
		button_vsync.pressed=true
	if OS.window_fullscreen:
		button_fullscreen.pressed=true
	if global.high_quality:
		get_node("reglage/button_particle").pressed=true
	if OS.get_name()=="Android":
		button_fullscreen.disabled=true

func _input(event:InputEvent)->void:
	if event.is_action("menu_special"):
		keybinding()
	if (event.is_action("menu") or event.is_action("ui_cancel")) and not varkeybinding:
		get_parent().option("options")
func close()->void:
	if not $anim.is_playing():
		get_node("anim").play("close")
		if self.has_node("keybinding"):
			$keybinding.close()
func destroy()->void:
	emit_signal("close")
	queue_free()


func _on_fps_pressed()->void:
	if global.show_fps:
		global.show_fps=false
	else:
		global.show_fps=true
	global.save_to_config("reglage","fps",global.show_fps)


func _on_Button_back_pressed():
	close()
	


func _on_button_vsync_pressed():
	if OS.vsync_enabled:
		OS.vsync_enabled=false
	else:
		OS.vsync_enabled=true
	global.save_to_config("reglage","vsync",OS.vsync_enabled)


func _on_Button_langue_pressed():
	
	if global.lang=="fr":
		global.lang="en"
	else:
		global.lang="fr"
	global.save_to_config("reglage","lang",global.lang)
	button_langue.set_text(global.lang)
	TranslationServer.set_locale(global.lang)


func _on_button_fullscreen_pressed():
	if OS.window_fullscreen:
		OS.window_fullscreen=false
	else:
		OS.window_fullscreen=true
	global.save_to_config("reglage","fullscreen",OS.window_fullscreen)


func _on_Button_chrono_pressed():
	if global.timer_choice<2:
		global.timer_choice+=1
	else:
		global.timer_choice=0
	button_chrono.set_text(timer_text[global.timer_choice])
	global.save_to_config("reglage","timer",global.timer_choice)


func _on_button_particle_pressed():
	global.switch_quality()


func _on_Button_text_pressed():
	if global.textspeed==0.05:
		global.textspeed=0.01
		
	elif global.textspeed==0.01:
		global.textspeed=0
	elif global.textspeed==0:
		global.textspeed=0.1
	else:
		global.textspeed=0.05
	refresh_textspeed()
	global.save_to_config("reglage","textspeed",global.textspeed)

func refresh_textspeed():
	if global.textspeed==0.01:
		button_text.set_text("MENU_FAST")
	elif global.textspeed==0.1:
		button_text.set_text("MENU_SLOW")
	elif global.textspeed==0:
		button_text.set_text("MENU_INSTANT")
	else:
		button_text.set_text("MENU_MED")
		
		

func _on_musique_value_changed(value:int):
	text_music.set_text(str(value))
	global.music_volume=value
	global.save_to_config("reglage","music_volume",global.music_volume)

func _on_son_value_changed(value:int):
	text_son.set_text(str(value))
	global.sound_volume=value
	global.save_to_config("reglage","sound_volume",global.sound_volume)


func _on_Button_input_pressed():
	keybinding()
func keybinding():
	if not $anim.is_playing() and not varkeybinding:
		varkeybinding=true
		var menu
		menu=preload("res://scenes/keybinding.tscn")
		var menu_instance=menu.instance()
		menu_instance.connect("hide_parent",self,"hide_reglage")
		menu_instance.connect("show_parent",self,"show_reglage")
		menu_instance.connect("disable_keybinding",self,"disable_keybinding")
		add_child(menu_instance)

func hide_reglage():
	$reglage.hide()

func show_reglage():
	$reglage.show()
	button_chrono.grab_focus()

func disable_keybinding():
	varkeybinding=false
