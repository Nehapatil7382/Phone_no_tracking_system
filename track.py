from tkinter import*
import tkintermapview
import phonenumbers
import opencage
from tkinter.ttk import*
from tkinter import messagebox
from phonenumbers import geocoder
from phonenumbers import carrier


from key import key

from opencage.geocoder import OpenCageGeocode

root=Tk()
root.geometry("500x500")

label1=Label(text="Phone Number Tracker")
label1.pack()

def getResult():
    num = number.get("1.0",END)
    try:
        num1 = phonenumbers.parse(num)
    except:
        messagebox.showerror("Error","Number box is empty or the input is not numeric !!")

    location = geocoder.description_for_number(num1,"en")
    service_provider = carrier.name_for_number(num1,"en")

    ocg = OpenCageGeocode(key)
    query = str(location)
    results = ocg.geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    my_label = LabelFrame(root)
    my_label.pack(pady=20)

    map_widget = tkintermapview.TkinterMapView(my_label, width=450,corner_radius=0)
    map_widget.set_position(lat, lng)
    map_widget.set_marker(lat, lng, text="Phone Location")
    map_widget.set_zoom(10)
    map_widget.place(relx=0.5,rely=0.5,anchor=CENTER)
    map_widget.pack()

    adr= tkintermapview.convert_coordinates_to_address(lat, lng)

    result.insert(END,"The country of this number is:" + location)
    result.insert(END,"\nThe sim card of this number is:" +service_provider)

    result.insert(END, "\nLatitude is: " + str(lat))
    result.insert(END, "\nLongitude is: " + str(lng))

    result.insert(END, "\nStreet Address is: " + str(adr.street))
    result.insert(END, "\nCity Address is: " + str(adr.city))
    result.insert(END, "\nPostal Code is: " + str(adr.postal))
    

number=Text(height=1)
number.pack()

style=Style()
style.configure("TButton", font=('calibri',20,'bold'), borderwidth='4')
style.map('TButton',forground=[('active','disabled','green')],
          background=[('active','black')])
          


button=Button(text="Search", command=getResult)
button.pack(pady=10,padx=100)

result=Text(height=7)
result.pack()



root.mainloop()











