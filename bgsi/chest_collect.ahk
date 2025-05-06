toggle := false

F3::
    Gosub, SendT ; Open map
    ClickArea(1092, 226) ; Click chest #1
    Loop, 3 {
        ClickArea(1326, 285) ; Scroll up to chest #2
    }
    ClickArea(838, 399) ; Click chest #2
    ClickArea(1733, 132) ; Exit map

    Gosub, SendF ; Open inventory
    ClickArea(1406, 443) ; Swap to team #2
    ClickArea(1436, 264) ; Exit inventory

    Gosub, SendT ; Open map
    Loop, 6 {
        ClickArea(1326, 285) ; Scroll up to chest #3
    }
    ClickArea(1092, 766) ; Click chest #3
    ClickArea(1733, 132) ; Exit map

    Gosub, SendF ; Open inventory
    ClickArea(733, 443) ; Swap back to team #1
    ClickArea(1436, 264) ; Exit inventory
return

ClickArea(x, y) {
    MouseMove, x, y
    Click, right
    Sleep, 100
    Click
    Sleep, 400

    return
}

SendT:
    SendInput {t down}
    Sleep, 2500
    SendInput {t up}
return

SendF:
    SendInput {f down}
    Sleep, 500
    SendInput {f up}
return