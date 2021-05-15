extends TabContainer


onready var file_dialog=$Buttons/file_dialog
onready var progress_bar=$Inputs/h_box_container/v_box_container2/progress_bar


func _ready():
	file_dialog.get_ok().text="open"
	set_tab_disabled(3,true)


func _on_h_slider_value_changed(value):
	progress_bar.value=value


func _on_button_pressed():
	file_dialog.popup_centered()
