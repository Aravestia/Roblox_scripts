toggle := false

F3::
toggle := !toggle
if (toggle) {
    SetTimer, Move, 200
} else {
    SetTimer, Move, Off
}
return

Move:

Gosub, Teleport
Gosub, LMove

time1 := 700
time2 := 200
time3 := 800

SnakeMove(time1, time2, time3)
SnakeMove(time3, time2, time1)
SnakeMove(time1, time2)
SnakeMove(time1, time2)

SendInput {w down}
Sleep, time1
SendInput {w up}

Sleep, 5000

return

Teleport:

SendInput {t down}
Sleep, 20
SendInput {t up}

Sleep, 2000

Click, WU, 5
Sleep, 100

MouseMove, 970, 970
Click, right
Click

Sleep, 2000

return

LMove:

SendInput {a down}
Sleep, 300
SendInput {a up}

SendInput {w down}
Sleep, 300
SendInput {w up}

SendInput {s down}
Sleep, 300
SendInput {s up}

SendInput {d down}
Sleep, 300
SendInput {d up}

SendInput {w down}
Sleep, 500
SendInput {w up}

SendInput {a down}
Sleep, 500
SendInput {a up}

return

SnakeMove(time1, time2, time3:=0, time4:=0) {
    If (time3 == 0)
    {
        time3 := time1
    }

    If (time4 == 0)
    {
        time4 := time2
    }  

    SendInput {w down}
    Sleep, time1
    SendInput {w up}

    SendInput {a down}
    Sleep, time2
    SendInput {a up}

    SendInput {s down}
    Sleep, time3
    SendInput {s up}

    SendInput {a down}
    Sleep, time4
    SendInput {a up}

    return
}