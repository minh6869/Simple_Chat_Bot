import customtkinter as ctk
#pip install customtkinter
#pip install pillow
# pip install google-generativeai
import login_and_register_screen


app = ctk.CTk()
app.geometry("1310x695")
app.title("Bot Bugs")
app.iconbitmap()
frame_main = ctk.CTkFrame(master = app,
                          width =1220,
                          height=720,
                          corner_radius=20,
                          fg_color="#36195B")

login_and_register_screen.load_login_and_register_screen(app, frame_main)

app.resizable(False,False)
app.mainloop()