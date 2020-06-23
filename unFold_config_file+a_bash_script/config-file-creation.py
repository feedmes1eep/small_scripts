def left_button(app_name,version,path,path2,desc):
    file_name=app_name+" Left.ini"
    image_name=app_name+" Left.png"
    side="Left"
    file=open(file_name,'w')
    file.write('[Rainmeter]\nUpdate=1000\nBackgroundMode=2\nSolidColor=0,0,0,1\n\n')
    file.write('[Metadata]\nName=unFold\nAuthor=feedmes1eep\nVersion={}\nLicense=GNU General Public License v2.0\n'.format(version))
    if desc != True:
            file.write('Information=The left side button for {}. {}\n\n'.format(app_name,desc))
    elif desc == True:
        file.write('Information=The left side button for {}\n\n'.format(app_name))
    file.write('[Variables]\nOffset=-150\nU=[!UpdateMeasureGroup Sliders][!UpdateMeterGroup Items][!Redraw]\n\n')
    file.write('[{}]\nMeter=Image\nGroup=Items\nImageName=#@#Buttons\Transparent\{}\n;ImageTint is if you want to change the color of the button. RGB color codes only. example: 255,255,255\nImageTint=\nH=50\nX=#Offset#\nDynamicVariables=1\nMouseOverAction=[!CommandMeasure MeasureSlider "Stop 1"][!CommandMeasure MeasureSlider "Execute 2"]\nMouseLeaveAction=[!CommandMeasure MeasureSlider "Stop 2"][!CommandMeasure MeasureSlider "Execute 1"]\nLeftMouseDownAction=[!SetOption "#CURRENTSECTION#" "ImageAlpha" "150"][!Update]\nLeftMouseUpAction=[!SetOption "#CURRENTSECTION#" "ImageAlpha" "255"][!Update]["{}"]\n'.format(app_name,image_name,path))
    if path2 == True:
        file.write('RightMouseDownAction=[!SetOption "#CURRENTSECTION#" "ImageAlpha" "150"][!Update]\nRightMouseUpAction=[!SetOption "#CURRENTSECTION#" "ImageAlpha" "255"][!Update][{}]\n\n'.format(path2))
    else:
        file.write('RightMouseDownAction=[!Update]\n\n')
    file.write('[MeasureSlider]\nMeasure=Plugin\nPlugin=ActionTimer\nGroup=Sliders\nActionList1=Repeat Left,5,30\nLeft=[!SetVariable Offset "(Clamp(#Offset#-5,-150,0))"]#U#\nActionList2=Repeat Right,5,30\nRight=[!SetVariable Offset "(Clamp(#Offset#+5,-150,0))"]#U#\nDynamicVariables=1\n')
    file.close()

def right_button(app_name,version,path,path2,desc):
    file_name=app_name+" Right.ini"
    image_name=app_name+" Right.png"
    side="Right"
    file=open(file_name,'w')
    file.write('[Rainmeter]\nUpdate=1000\nDynamicWindowSize=1\nAccurateText=1\nSkinWidth=180\nSkinHeight=50\nBackgroundMode=2\nSolidColor=0,0,0,1\n\n')
    file.write('[Metadata]\nName=unFold\nAuthor=feedmes1eep\nVersion={}\nLicense=GNU General Public License v2.0\n'.format(version))
    if desc != True:
        file.write("Information=The right side button for {}. {}\n\n".format(app_name,desc))
    elif desc == True:
        file.write('Information=The right side button for {}\n\n'.format(app_name))
    file.write('[Variables]\nOffset=130\nState=1\nU=[!UpdateMeasure MeasureSlider][!UpdateMeter *][!Redraw]\n\n')
    file.write('[{}]\nMeter=Image\nGroup=Items\nImageName=#@#Buttons\Transparent\{}\n;ImageTint is if you want to change the color of the button. RGB color codes only. example: 255,255,255\nImageTint=\nW=200\nH=50\nX=#OffSet#\nDynamicVariables=1\nMouseOverAction=[!CommandMeasure MeasureSlider "Execute #State#"]\nMouseLeaveAction=[!CommandMeasure MeasureSlider "Execute #State#"]\nLeftMouseDownAction=[!SetOption "#CURRENTSECTION#" "ImageAlpha" "130"][!Update]\nLeftMouseUpAction=[!SetOption "#CURRENTSECTION#" "ImageAlpha" "255"][!Update]["{}"]\n'.format(app_name,image_name,path))
    if path2 == True:
        file.write('RightMouseDownAction=[!SetOption "#CURRENTSECTION#" "ImageAlpha" "130"][!Update]\nRightMouseUpAction=[!SetOption "#CURRENTSECTION#" "ImageAlpha" "255"][!Update][{}]\n\n'.format(path2))
    else:
        file.write('RightMouseDownAction=[!Update]\n\n')
    file.write('[MeasureSlider]\nMeasure=Plugin\nPlugin=ActionTimer\nActionList1=Repeat SlideLeft, 5, 30\nSlideLeft=[!SetVariable State "2"][!SetVariable OffSet "(Clamp(#OffSet#-5,0,130))"]#U#\nActionList2=Repeat SlideRight, 5, 30\nSlideRight=[!SetVariable State "1"][!SetVariable OffSet "(Clamp(#OffSet#+5,0,130))"]#U#\nDynamicVariables=1\n\n')
    file.close()

app_name=input('Application name: ')
ver=float(input('Version: '))
cdesc=input("Custom Description (CDesc) or Default Description (DDesc)?")
if cdesc == "CDesc":
    cdesc=input("Your Description for the button: ")
elif cdesc == "DDesc":
    cdesc = True
path=input('Path to executable or link: ')
path2=0
nd2=input('Will there be a second path (for right click) (Type yes or no): ')
if nd2 == 'yes' or nd2 == 'Yes' or nd2 == 'YES' or nd2 == 'YeS' or nd2 == 'YEs':
    path2=input('A second path: ')

left_button(app_name,ver,path,path2,cdesc)
right_button(app_name,ver,path,path2,cdesc)