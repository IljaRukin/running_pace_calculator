from tkinter import *

mile = 1.609344

def calc_times(metric,pace,minutes,seconds,distances,fields):
	minutes = float(minutes)
	seconds = float(seconds)
	if metric==1:
		secs = minutes*60 + seconds
	else:
		secs = (minutes*60 + seconds)/mile
	n=0

	#pace
	m = secs//60
	s = secs -m*60
	pace[0].set(round(m))
	pace[1].set(round(s))
	#print('pace: ',round(m),':',round(s,2),'min/km')

	m = secs*mile//60
	s = secs*mile -m*60
	pace[2].set(round(m))
	pace[3].set(round(s))
	#print('pace: ',round(m),':',round(s,2),'min/mile')

	#time
	for d in distances:
		time = d*secs
		h = time//3600
		time -= h*3600
		m = time//60
		time -= m*60
		s = time
		fields[n][0].set(round(h))
		fields[n][1].set(round(m))
		fields[n][2].set(round(s))
		n+=1
	return None

#blank window
root = Tk()
root.title('RunCalc')

###
frame1 = Frame(root)
frame1.grid()

crow = 0
pace1 = Label(frame1, text='pace ')
minutes = Entry(frame1,width=5)
pace2 = Label(frame1, text=':')
seconds = Entry(frame1,width=5)
pace1.grid(row=crow,column=0, sticky=W)
minutes.grid(row=crow,column=1, sticky=E)
pace2.grid(row=crow,column=2, sticky=E)
seconds.grid(row=crow,column=3, sticky=E)

crow +=1
metric = IntVar()
metric.set(1)
R1 = Radiobutton(frame1, text="min/km", variable=metric, value=1)
R2 = Radiobutton(frame1, text="min/mile", variable=metric, value=0)
R1.grid(row=crow,column=0)
R2.grid(row=crow,column=1)

crow +=1
submit_row = crow

###
frame2 = Frame(root)
frame2.grid()

crow +=1
pace3 = Label(frame2, text='pace ')
min_km = IntVar()
m_km = Label(frame2, textvariable=min_km, width=5)
pace4 = Label(frame2, text=':')
sec_km = IntVar()
s_km = Label(frame2, textvariable=sec_km, width=5)
pace5 = Label(frame2, text='min/km')
pace3.grid(row=crow,column=0, sticky=W)
m_km.grid(row=crow,column=1, sticky=E)
pace4.grid(row=crow,column=2, sticky=E)
s_km.grid(row=crow,column=3, sticky=E)
pace5.grid(row=crow,column=4, sticky=E)

crow +=1
pace6 = Label(frame2, text='pace ')
min_mil = IntVar()
m_mil = Label(frame2, textvariable=min_mil, width=5)
pace7 = Label(frame2, text=':')
sec_mil = IntVar()
s_mil = Label(frame2, textvariable=sec_mil, width=5)
pace8 = Label(frame2, text='min/mile')
pace6.grid(row=crow,column=0, sticky=W)
m_mil.grid(row=crow,column=1, sticky=E)
pace7.grid(row=crow,column=2, sticky=E)
s_mil.grid(row=crow,column=3, sticky=E)
pace8.grid(row=crow,column=4, sticky=E)

###
frame3 = Frame(root)
frame3.grid()

#pace array
pace = [min_km,sec_km,min_mil,sec_mil]

crow +=1
d = Label(frame3, text='distance in km')
h = Label(frame3, text='h',width=5)
m = Label(frame3, text='m',width=5)
s = Label(frame3, text='s',width=5)
ddots = [Label(frame3, text=':'),Label(frame3, text=':')]
d.grid(row=crow,column=0, sticky=W)
h.grid(row=crow,column=1, sticky=E)
ddots[0].grid(row=crow,column=2, sticky=E)
m.grid(row=crow,column=3, sticky=E)
ddots[1].grid(row=crow,column=4, sticky=E)
s.grid(row=crow,column=5, sticky=E)

distances = [5,10,21.0975,42.195]
fields = []
for d in distances:
	fields.append([IntVar(),IntVar(),IntVar()])
	empty_field = [Label(frame3, text=d), Label(frame3, textvariable=fields[-1][0]), Label(frame3, textvariable=fields[-1][1]), Label(frame3, textvariable=fields[-1][2])]
	ddots = [Label(frame3, text=':'),Label(frame3, text=':')]
	crow +=1
	empty_field[0].grid(row=crow,column=0, sticky=W)
	empty_field[1].grid(row=crow,column=1, sticky=E)
	ddots[0].grid(row=crow,column=2, sticky=E)
	empty_field[2].grid(row=crow,column=3, sticky=E)
	ddots[1].grid(row=crow,column=4, sticky=E)
	empty_field[3].grid(row=crow,column=5, sticky=E)

submit = Button(frame2, text='submit', command = lambda: calc_times(metric.get(),pace,minutes.get(),seconds.get(),distances,fields))
submit.grid(row=submit_row,columnspan=5)

#keep window open
root.mainloop()
