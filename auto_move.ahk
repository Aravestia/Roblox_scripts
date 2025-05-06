toggle := false

F3::
    toggle := !toggle
    if (toggle) {
        SetTimer, PressKey, 100  ; Adjust the interval (ms) as needed
    } else {
        SetTimer, PressKey, Off
    }
return

PressKey:
    var := 0
    Random, var, 1, 4

    time := 0
    Random, time, 50, 200

    IfEqual, var, 1, SendInput {w down}
    IfEqual, var, 2, SendInput {a down}
    IfEqual, var, 3, SendInput {s down}
    IfEqual, var, 4, SendInput {d down}

    Sleep, time

    IfEqual, var, 1, SendInput {w up}
    IfEqual, var, 2, SendInput {a up}
    IfEqual, var, 3, SendInput {s up}
    IfEqual, var, 4, SendInput {d up}
return