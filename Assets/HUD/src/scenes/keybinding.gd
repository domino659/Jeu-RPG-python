extends CanvasLayer

signal hide_parent()
signal show_parent()
signal disable_keybinding()

var buttonactive

func _ready():
	set_buttons()
	for button in get_tree().get_nodes_in_group("keybinding"):
		button.connect("pressed", self, "_some_button_pressed", [button])
	$reglage/accept_dialog.get_ok().text="yes"
func set_buttons():
	for action_name in global.INPUT_ACTIONS:
		var action_list = InputMap.get_action_list(action_name)
		var levelouow="touche_monde"
		for this_event in action_list:
			if this_event is InputEventKey:
				var currbutton=get_node("reglage/"+levelouow+"/"+action_name+"/Button")
				currbutton.set_text(OS.get_scancode_string(this_event.scancode))
				currbutton.get_node("texture").set_texture(null)
			if this_event is InputEventMouseButton:

				var currbutton=get_node("reglage/"+levelouow+"/"+action_name+"/Button")
				currbutton.set_text("")
				currbutton.get_node("texture").set_texture(load("res://assets/icons/keybinding/mouse"+str(this_event.get_button_index())+".png"))
			if this_event is InputEventJoypadMotion:
				var currbutton=get_node("reglage/"+levelouow+"/"+action_name+"/Button2")
				currbutton.set_text("")
				currbutton.get_node("texture").set_texture(load("res://assets/icons/keybinding/axis"+str(this_event.axis)+str(this_event.axis_value)+".png"))

			if this_event is InputEventJoypadButton:
				var currbutton=get_node("reglage/"+levelouow+"/"+action_name+"/Button2")
				currbutton.set_text("")
				currbutton.get_node("texture").set_texture(load("res://assets/icons/keybinding/button"+str(this_event.get_button_index())+".png"))
	

func _input(event):
	
	if buttonactive!=null:
		
		if event.is_action_type():
			$reglage.accept_event()
		if event is InputEventJoypadMotion and buttonactive.name=="Button2":
			if abs(event.get_axis_value())==1:
				var actionname=buttonactive.get_parent().name
				buttonactive.set_text("")
				buttonactive.get_node("texture").set_texture(load("res://assets/icons/keybinding/axis"+str(event.axis)+str(event.axis_value)+".png"))
				erase_action(actionname,true)
				InputMap.action_add_event(actionname, event)
				buttonactive.pressed=false
				buttonactive=null
				save_inputs()
				
		elif event is InputEventJoypadButton and buttonactive.name=="Button2":
			var actionname=buttonactive.get_parent().name
			buttonactive.set_text("")
			buttonactive.get_node("texture").set_texture(load("res://assets/icons/keybinding/button"+str(event.get_button_index())+".png"))
			erase_action(actionname,true)
			InputMap.action_add_event(actionname, event)
			buttonactive.pressed=false
			buttonactive=null
			save_inputs()
		elif event is InputEventScreenTouch:
			if event.is_pressed():
				buttonactive.pressed=false
				buttonactive=null
		elif event is InputEventMouseButton and buttonactive.name=="Button" and OS.get_name()!="Android":
			var actionname=buttonactive.get_parent().name
			buttonactive.set_text("")
			buttonactive.get_node("texture").set_texture(load("res://assets/icons/keybinding/mouse"+str(event.get_button_index())+".png"))
			erase_action(actionname,false)
			InputMap.action_add_event(actionname, event)
			buttonactive.pressed=false
			buttonactive=null
			save_inputs()
		elif event is InputEventKey and buttonactive.name=="Button":
			var actionname=buttonactive.get_parent().name
			buttonactive.set_text(OS.get_scancode_string(event.scancode))
			buttonactive.get_node("texture").set_texture(null)
			erase_action(actionname,false)
			InputMap.action_add_event(actionname, event)
			buttonactive.pressed=false
			buttonactive=null
			save_inputs()
	else:
		if event.is_action_pressed("ui_cancel") or event.is_action_pressed("menu"):
			close()
		if event.is_action("menu_special"):
			save_inputs()
func erase_action(action_name,joy):
	for old_event in InputMap.get_action_list(action_name):
		if joy:
			if (old_event is InputEventJoypadButton or old_event is InputEventJoypadMotion):
				InputMap.action_erase_event(action_name, old_event)
		else:
			if (old_event is InputEventMouseButton or old_event is InputEventKey):
				InputMap.action_erase_event(action_name, old_event)
func close():
	
	if not $anim.is_playing():
		get_node("anim").play("close")
func destroy():
	queue_free()


func _on_Button_back_pressed():
	close()
	
func hideparent():
	emit_signal("hide_parent")
	
func showparent():
	emit_signal("show_parent")
func keybindingfalse():
	emit_signal("disable_keybinding")

func getallnodes(node,obj):
	for N in node.get_children():
		if N.get_child_count() > 1:
			getallnodes(N,obj)
		else:
			if (N is Button and N!=obj):
				N.pressed=false




func _some_button_pressed(button):
	if button.pressed:
		buttonactive=button
	else:
		buttonactive=null
	getallnodes(self,buttonactive)



func save_inputs():
	for action_name in global.INPUT_ACTIONS:
		global.save_to_input("input", action_name, InputMap.get_action_list(action_name))


func _on_Button_reset_pressed():
	$reglage/accept_dialog.popup_centered()


func _on_accept_dialog_confirmed():
	global.load_input(global.DEFAULT_INPUT_FILE)
	set_buttons()
	save_inputs()
