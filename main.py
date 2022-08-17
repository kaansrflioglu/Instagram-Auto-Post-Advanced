import tkinter as tk
import second

pencere = tk.Tk()
pencere.title("Instagram Share App")
pencere.geometry("360x480")


def pressButton():
    link = ent1.get()
    second.getLink(link)

    username = ent2.get()
    password = ent3.get()
    artist = ent4.get()
    location = ent5.get()
    date = ent6.get()
    second.share(username, password, artist, location, date)


e1 = tk.Label(text="Image Link", font="Arial 12 bold")
e1.pack()
ent1 = tk.Entry(width=30)
ent1.pack()
e2 = tk.Label(text="Username", font="Arial 12 bold")
e2.pack()
ent2 = tk.Entry(width=30)
ent2.pack()
e3 = tk.Label(text="Password", font="Arial 12 bold")
e3.pack()
ent3 = tk.Entry(width=30)
ent3.pack()
e4 = tk.Label(text="Artist", font="Arial 12 bold")
e4.pack()
ent4 = tk.Entry(width=30)
ent4.pack()
e5 = tk.Label(text="Location", font="Arial 12 bold")
e5.pack()
ent5 = tk.Entry(width=30)
ent5.pack()
e6 = tk.Label(text="Date", font="Arial 12 bold")
e6.pack()
ent6 = tk.Entry(width=30)
ent6.pack()


b1 = tk.Button(text="Upload", bg="black", fg="white", font="Arial 20 bold", command=pressButton)
b1.pack()


pencere.mainloop()
second.delete()