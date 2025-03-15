^+a::  ; Ctrl + Shift + A
    CoordMode, Pixel, Screen  ; البحث عن الصور في كامل الشاشة
    CoordMode, Mouse, Screen  ; ضبط الإحداثيات على الشاشة بالكامل

    IfWinExist, ahk_class ApplicationFrameWindow
    {
        WinActivate  ; تفعيل النافذة
        Sleep, 300   ; تقليل التأخير

        ; 🔍 البحث عن زر المشبك
        ImageSearch, xClip, yClip, 0, 0, A_ScreenWidth, A_ScreenHeight, *80 clip_icon.png
        if (ErrorLevel = 0)
        {
            Click, %xClip%, %yClip%  
            Sleep, 10  ; تأخير أقل
        }
        else
        {
            MsgBox, لم يتم العثور على زر المشبك!
            Return
        }

        ; 🔍 البحث عن زر "Photos & Videos"
        Sleep, 200  ; تقليل التأخير أكثر
        ImageSearch, xPhoto, yPhoto, 0, 0, A_ScreenWidth, A_ScreenHeight, *100 photos_videos.png
        if (ErrorLevel = 0)
        {
            Click, %xPhoto%, %yPhoto%  
        }
        else
        {
            MsgBox, لم يتم العثور على زر "Photos & Videos"!
        }
    }
    else
    {
        MsgBox, WhatsApp غير مفتوح!
    }
Return