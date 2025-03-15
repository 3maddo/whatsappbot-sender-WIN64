^+a::  ; Ctrl + Shift + A
    CoordMode, Pixel, Screen  ; Search for images across the entire screen
    CoordMode, Mouse, Screen  ; Set coordinates to the entire screen

    IfWinExist, ahk_class ApplicationFrameWindow
    {
        WinActivate  ; Activate the window
        Sleep, 300   ; Reduce delay

        ; 🔍 Search for the clip icon
        ImageSearch, xClip, yClip, 0, 0, A_ScreenWidth, A_ScreenHeight, *80 clip_icon.png
        if (ErrorLevel = 0)
        {
            Click, %xClip%, %yClip%  
            Sleep, 10  ; Less delay
        }
        else
        {
            MsgBox, Clip icon not found!
            Return
        }

        ; 🔍 Search for the "Photos & Videos" button
        Sleep, 200  ; Further reduce delay
        ImageSearch, xPhoto, yPhoto, 0, 0, A_ScreenWidth, A_ScreenHeight, *100 photos_videos.png
        if (ErrorLevel = 0)
        {
            Click, %xPhoto%, %yPhoto%  
        }
        else
        {
            MsgBox, "Photos & Videos" button not found!
        }
    }
    else
    {
        MsgBox, WhatsApp is not open!
    }
Return
