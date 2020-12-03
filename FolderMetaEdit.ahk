#Persistent
#NoEnv
SetWorkingDir %A_ScriptDir%

F10::
Clipboard =
Send ^c
ClipWait, 2, 1
Selection := Clipboard
if Selection = 
Return
Clipboard =
bracket := InStr(Selection, "`(", False, 1)
year := SubStr(Selection, (bracket+1), 4)
FileDelete, %selection%\desktop.ini
FileAppend,`[`{F29F85E0-4FF9-1068-AB91-08002B27B3D9`}`]`nProp2`=31`,Title`nProp3`=31`,%year%`nProp4`=31`,Author`nProp5`=31`,Keywords`(Tags`)`nProp6`=31`,Comment`n[`{56A3372E-CE9C-11D2-9F0E-006097C686F6`}`]`nProp5`=31`,Year`nProp11`=31`,Genre, %selection%\desktop.ini 
Return