toggle := false

F3::
    toggle := !toggle
    if (toggle) {
        SetTimer, PressBtn, 10
    } else {
        SetTimer, PressBtn, Off
    }
return

PressBtn:
    Send, r
return
