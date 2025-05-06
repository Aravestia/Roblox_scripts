toggle := false

F3::
    toggle := !toggle
    if (toggle) {
        SetTimer, PressBtn, 20
    } else {
        SetTimer, PressBtn, Off
    }
return

PressBtn:
    Send, e
return
