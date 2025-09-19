from tkinter import*
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=694629e39afbde610dd74c26d6d7b811").json()
    w_label1.config(text=data["weather"][0]["main"])
 
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])


win=Tk()
win.title("Weather App")
win.config(bg = "maroon")
win.geometry("500x570")

name_label = Label(win, text="Rohan's Weather App", font=("Times New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win, text="Rohan's Weather App",values=list_name, font=("Times New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)



w_label = Label(win, text=" Weather Climate", font=("Times New Roman",20))
w_label.place(x=25,y=260,height=50,width=210)
w_label1 = Label(win, text="", font=("Times New Roman",20))
w_label1.place(x=250,y=260,height=50,width=210)



temp_label = Label(win, text="Temperature", font=("Times New Roman",20))
temp_label.place(x=25,y=330,height=50,width=210)
temp_label1 = Label(win, text="", font=("Times New Roman",20))
temp_label1.place(x=250,y=330,height=50,width=210)



per_label = Label(win, text="pressure", font=("Times New Roman",20))
per_label.place(x=25,y=400,height=50,width=210)
per_label1 = Label(win, text="", font=("Times New Roman",20))
per_label1.place(x=250,y=400,height=50,width=210)



done_button = Button(win, text="Done", font=("Times New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100, x=200)



win.mainloop()