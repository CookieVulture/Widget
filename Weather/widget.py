import tkinter as tk
from PIL import Image
from PIL import ImageTk
import requests

H = 500
W = 600

def func(entry):
    print("Button click", entry)
    
def weather(data):
    key = '61b652949defc856de6d7fbe910f7127'
    link = 'https://api.openweathermap.org/data/2.5/weather'
    para = {'APPID':key, 'q':data, 'units': 'Metric'}
    req = requests.get(link, params=para)
    info = req.json()

    lb['text'] = format(info)

def format(info):
    try:
        name = info['name']
        condition = info['weather'][0]['main']
        des = info['weather'][0]['description']
        temp = info['main']['temp']
        feel = info['main']['feels_like']
        result = "City : {}\n Weather Condition : {}\n Description : {}\n Temperature (Celsius) : {}\n Temperature feels like : {}".format(name,condition,des,temp,feel)
    except:
        result = "Can't find data. Try again!"

    return result


app = tk.Tk()
image = Image.open('img.png')
image = image.resize((500, 600))
image2 = ImageTk.PhotoImage(image)

screen = tk.Canvas(app, height=H, width=W)
screen.pack()

bg_lb = tk.Label(app, image=image2)
bg_lb.place(relwidth=1, relheight=1)

fr = tk.Frame(app, bg='#53ff1a', bd=5)
fr.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(fr, font=('Bahnschrift SemiBold SemiConden', 13))
entry.place(relwidth=0.65, relheight=1)

but = tk.Button(fr, text="Go", font=('Bahnschrift SemiBold SemiConden', 13), command=lambda: weather(entry.get()))
but.place(relx=0.7, relwidth=0.3, relheight=1)

low_fr = tk.Frame(app, bg='#53ff1a', bd=10)
low_fr.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

lb = tk.Label(low_fr, font=('Bahnschrift SemiBold SemiConden', 20), anchor='nw', justify='left', bd=4)
lb.place(relwidth=1, relheight=1)


app.mainloop()
