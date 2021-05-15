extends Control

onready var button_menu:=$button_menu
onready var button_inventory:=$button_inventory
onready var button_settings:=$button_settings

onready var buttons:=[button_menu,button_inventory,button_settings]

var menu_packed:=preload("res://scenes/menu.tscn")

func _input(event):
	if event.is_action("menu") and not event.is_pressed():
		if not $anim.is_playing() and !button_menu.disabled:
			if button_menu.pressed:
				_leaflet(false)
			else:
				_leaflet(true)
				
func close():
	$anim.play_backwards("open")
func finish():
	pass

func disable_buttons(obj):
	for b in buttons:
		if b!=obj:
			b.disabled=true
func recover_buttons():
	for b in buttons:
		b.disabled=false
		if b!=button_menu:
			b.pressed=false
func lost_focus():
	for b in buttons:
		b.release_focus()



func _on_button_settings_toggled(button_pressed):
	if not button_pressed:
		recover_buttons()
		if has_node("menu"):
			$menu.close()
	else:
		disable_buttons(button_settings)
		if not has_node("menu"):
			var menu:=menu_packed.instance()
			menu.connect("close",self,"menu_close")
			add_child(menu)
			 
func menu_close():
	recover_buttons()

func _on_button_inventory_toggled(button_pressed):
	if !$animation_preview.is_playing():
		if not button_pressed:
			recover_buttons()
			$animation_preview.play_backwards("open")
		else:
			disable_buttons(button_inventory)
			$animation_preview.play("open")


func _leaflet(open):
	if not $anim.is_playing():
		if not open:
			button_menu.pressed=false
			lost_focus()
			close()
			finish()
		else:
			button_menu.pressed=true
			button_inventory.grab_focus()
			
			$anim.play("open")
			get_tree().set_pause(true)


func _on_button_menu_toggled(button_pressed):
	if not $anim.is_playing():
		print(button_pressed)
		if not button_pressed:
			_leaflet(false)
		else:
			_leaflet(true)

