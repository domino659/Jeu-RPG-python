extends CanvasLayer

signal close()

onready var anim:=$menu/anim
onready var button_resume:=$menu/cont/button_resume
onready var button_settings:=$menu/cont/button_settings
onready var button_quit:=$menu/cont/button_quit

onready var buttons:=[button_resume,button_settings,button_quit]

var options_packed:=preload("res://scenes/options.tscn")

func _ready()->void:
	pass
func _input(event:InputEvent)->void:
	if (event.is_action("menu") or event.is_action("ui_cancel")) and !has_node("options") and event.is_pressed():
		close()

func close()->void:
	if not $menu/anim.is_playing():
		anim.play_backwards("open")
	
func destroy()->void:
	emit_signal("close")
	queue_free()

func option()->bool:
	
	if not anim.is_playing():
		
		if !has_node("options"):
			anim.play("option")
			var options=options_packed.instance()
			options.connect("close",self,"option")
			add_child(options)
		else:
			anim.play_backwards("option")
			button_resume.grab_focus()
			get_node("options").queue_free()
			button_settings.pressed=false
		for button in buttons:
			if button!=button_settings:
				if button.disabled:
					button.disabled=false
				else:
					button.disabled=true
		return true
	else:
		return false


func _on_anim_animation_finished(anim_name:String)->void:
	if anim_name=="open":
		if anim.get_current_animation_position()==0:
			destroy()
		else:
			button_resume.grab_focus()



func _on_button_settings_pressed():
	option()


func _on_button_resume_pressed():
	close()


func _on_button_quit_pressed():
	get_tree().quit()
