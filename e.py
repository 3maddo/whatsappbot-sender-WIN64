^+a::  ; Ctrl + Shift + A
    ; عرض جميع النوافذ المفتوحة لتحديد نافذة WhatsApp
    WinGet, windows, List
    Loop, %windows%
    {
        this_window := windows%A_Index%
        WinGetClass, class, ahk_id %this_window%
        MsgBox, Class: %class%  ; يعرض الكلاس لكل نافذة مفتوحة
    }
Return