from turtle import*

b=3
hideturtle()
pensize(5)
speed(3)
penup()
bgcolor('black')

#CỜ
goto(-240,90)
pendown()
color('red')
begin_fill()
for i in range(2): forward(480); right(90); forward(320);right(90)
end_fill()
penup()
begin_fill()

#NGÔI SAO
speed(b)
goto(-25,-50)
pendown()
color('yellow')
right(288)
canh=70
speed(b)
for i in range(5): forward(canh);right(144);forward(canh);left(72)
penup()
end_fill()

#CHỮ
a=3
c=230
y=180
hideturtle()

speed(a)
goto(-90,250)
pencolor('bisque')
penup()
write('Kỷ niệm',align='center',font=('Fz Manstein',30,'bold'))

speed(a)
goto(-30,c)
pencolor('white')
penup()
write('30',align='center',font=('1FTV Wolfers',30,'bold'))

speed(a)
goto(00,c)
pencolor('white')
penup()
write('/',align='center',font=('1FTV Wolfers',30,'bold'))

speed(a)
goto(20,c)
penup()
pencolor('white')
write('4',align='center',font=('1FTV Wolfers',30,'bold'))


speed(a)
goto(45,c)
penup()
pencolor('white')
write('/',align='center',font=('1FTV Wolfers',30,'bold'))

speed(a)
goto(90,c)
penup()
pencolor('white')
write('1975',align='center',font=('1FTV Wolfers',30,'bold'))

speed(a)
goto(-230,y)
penup()
pencolor('white')
write('GIẢI',font=('san',30,'bold'))

speed(a)
goto(-140,y)
penup()
pencolor('white')
write('PHÓNG',font=('san',30,'bold'))

speed(a)
goto(20,y)
penup()
pencolor('white')
write('MIỀN',font=('san',30,'bold'))

speed(a)
goto(130,y)
penup()
pencolor('white')
write('NAM,',font=('san',30,'bold'))

speed(a)
goto(-240,y-50)
penup()
pencolor('white')
write('THỐNG',font=('san',30,'bold'))

speed(a)
goto(-90,y-50)
penup()
pencolor('white')
write('NHẤT',font=('san',30,'bold'))

speed(a)
goto(30,y-50)
penup()
pencolor('white')
write('ĐẤT',font=('san',30,'bold'))

speed(a)
goto(120,y-50)
penup()
pencolor('white')
write('NƯỚC',font=('san',30,'bold'))

mainloop()