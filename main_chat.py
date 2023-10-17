import customtkinter as ctk
from PIL import Image
import tkinter as tk
from tkinter import ttk
#pip install customtkinter
#pip install pillow
import time
import os
import apifree
import threading
import login_and_register_screen

# app = ctk.CTk()
# app.title("Bot Bugs")
# app.geometry("1310x695")
# app.iconbitmap()
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")
# frame_main_chat = ctk.CTkFrame(master = app,
#                                     width =1220,
#                                     height=720,
#                                     corner_radius=40,
#                                     fg_color="#36195B")
# frame_main_chat.pack(padx = 10, pady = 10)


def chat_main(app,frame_main_chat, loadmainchat, logout_button):
    global intro
    class NotificationPanel(ctk.CTkFrame):
        def __init__(self, parent, start_pos, end_pos):
            super().__init__(master = parent,width=405, height=641, fg_color="#7801A1", corner_radius=23,border_color="#ffcad7")

            # general attributes 
            self.start_pos = start_pos 
            self.end_pos = end_pos - 0.01
            self.width = abs(start_pos - end_pos)

            # animation logic
            self.pos = self.start_pos
            self.in_start_pos = True

            # layout
            self.place(relx = self.start_pos, rely = 0.03, )

        def animate(self):
            if self.in_start_pos:
                self.animate_forward()
            else:
                self.animate_backwards()

        def animate_forward(self):
            if self.pos > self.end_pos:
                self.pos -= 0.008
                self.place(relx = self.pos, rely = 0.03, )
                self.after(10, self.animate_forward)
            else:
                self.in_start_pos = False

        def animate_backwards(self):
            if self.pos < self.start_pos:
                self.pos += 0.008
                self.place(relx = self.pos, rely = 0.03, )
                self.after(10, self.animate_backwards)
            else:
                self.in_start_pos = True


    current_path = os.getcwd()
    def send(text_box):
        text_box.configure(state = "normal")
        textbox_text = chat_bar.get("0.0","end")
        ans = apifree.AI(textbox_text) + "\n"
        text_box.insert("end", text=textbox_text)
        text_box.insert("end", text=ans)
        text_box.configure(state = "disabled")

    def get_response(question):
        ans = apifree.AI(question=question)
        return ans
    def on_enter(event):
        text_box.configure(state = "normal")
        textbox_text = chat_bar.get("0.0","end")
        thread = threading.Thread(target=get_response, daemon=True, args=(textbox_text,))
        chat_bar.delete("0.0","end")
        print(thread.is_alive())
        thread.start()
        print("loadding")
        print(thread.is_alive())
        text_box.insert("end", text=textbox_text)
        
        thread.join()

        text_box.insert("end", text=get_response(textbox_text))
        text_box.configure(state = "disabled")

    def clock():
        now = time.time()
        hour = time.strftime("%H", time.localtime(now))
        minute = time.strftime("%M", time.localtime(now))
        second = time.strftime("%S", time.localtime(now))
        clock_label.configure(text = hour + ":" + minute + ":" + second)
        clock_label.after(1, clock)

    def out():
            text_box.configure(state = "normal")
            text_box.delete("0.0", "end")
            text_box.insert("0.0", text=intro)
            text_box.configure(state = "disabled")

    def log_out():
        out()
        loadmainchat()
        warning_entry.place_forget()


    def power():
        warning_entry.place(relx = 0.46, rely = 0.5, anchor = "center")


    def hide_warning():
        warning_entry.place_forget()
    
    logout_button.configure(command = lambda: power())

    name_app_label = ctk.CTkLabel(master = frame_main_chat, 
                                        text = ("Simple ChatBot"), 
                                        font=("Inter",30,"bold"))
    name_app_label.place(relx = 0.15, rely = 0.059, anchor = "center")
    name_bot_label = ctk.CTkLabel(master=frame_main_chat, 
                                        text= "bot bugs",
                                        width=13,
                                        height=13, 
                                        text_color="#BF8EFD",
                                        font=("SourceCodePro-SemiBold", 12)) 
    name_bot_label.place(relx = 0.082, rely = 0.028, anchor = "center")

    clock_label = ctk.CTkLabel(master = frame_main_chat,
                                     text = None,
                                     font = ("Inter", 28,"bold"),
                                     fg_color="#36195B",
                                     text_color="#BF8EFD")
    clock_label.place(relx = 0.7, rely = 0.059, anchor = "center")
    clock()
    infor_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\information.png"),
                           size=(30,30))
    infor_button = ctk.CTkButton(master=frame_main_chat,
                             image=infor_image,
                             width=10,
                             height=10,
                             fg_color="#36195B",
                             hover_color="white",
                            #  command= lambda: get_info(),
                             text=None)
    notification_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\notification.png"),
                                            size = (30,30))
    notification_button = ctk.CTkButton(master = frame_main_chat, 
                                              image=notification_image, 
                                              width=10,
                                              height=10,
                                              fg_color="#36195B",
                                              hover_color="white",
                                            #   command=notification_panel.animate,
                                              text=None)
    

    setting_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\setting.png"),
                                       size=(30,30))
    setting_button = ctk.CTkButton(master = frame_main_chat,
                                         image=setting_image,
                                         fg_color="#36195B",
                                         width= 20,
                                         height=20,
                                         hover_color="white",
                                         text=None)
   
    infor_button.place(relx = 0.78, rely = 0.059, anchor = "center")
    notification_button.place(relx = 0.825, rely = 0.059, anchor = "center")
    setting_button.place(relx = 0.87, rely = 0.059, anchor = "center")
  


    chat_bar = ctk.CTkTextbox(frame_main_chat,
                            width=1080,
                            height=14,
                            corner_radius=25, 
                            fg_color="#2E1A47",
                            font=("Source Code Pro",14, "bold"))

    chat_bar.place(relx = 0.5, rely = 0.91, anchor = "center",)
    text = """Hãy nhập gì đó vào đây """
    chat_bar.insert("0.0",text)
    chat_bar.bind("<Return>", on_enter)
    send_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\send.png"),
                            size=(35,35))
    send_button = ctk.CTkButton(chat_bar,
                                image=send_image,
                                text=None,
                                width=10,
                                height=10,
                                hover_color="#ff52bd",
                                corner_radius=100,
                                fg_color="#2E1A47",
                                command= lambda: send(text_box))
    send_button.place(relx=0.97, rely=0.5, anchor = "center")
    

    

    




    frame = ctk.CTkFrame(frame_main_chat,
                        width=1080,
                        height=495,
                        corner_radius=20,
                        fg_color="#2E1A47"
                                    )
    frame.place(relx=0.5,rely = 0.46, anchor = "center")
    logo_image_mini = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\logo.png"),
                                        size=(55, 55))

    logo_mini_label = ctk.CTkLabel(master = frame_main_chat, 
                                image=logo_image_mini, 
                                text=None, 
                                fg_color="#2E1A47")

    logo_mini_label.place(relx = 0.1, rely = 0.15, anchor = "center")
    text_box = ctk.CTkTextbox(frame,
                            font=("Source Code Pro",20,"bold"),
                            fg_color="#2E1A47",
                            width=990,
                            height=470)
    text_box.place(relx=0.54, rely =0.518, anchor = "center")

    intro = """I'm Simple Chatbot, your creative and helpful partner. I have some 
limitations and they're not always right. However, your feedback will help 
me improve
"""
    text_box.insert("0.0",text=intro)

    text_box.configure(state = "disabled")
    warning_entry = ctk.CTkEntry(master=text_box,
                                 placeholder_text=None,
                                 text_color="#2E1A47",
                                 border_color="#fd3754",
                                 width=500,
                                 height=215,
                                 corner_radius=20,
                                 fg_color="#c39de2")
    warning_entry.configure(state = "readonly")
    lable = ctk.CTkLabel(warning_entry,
                         text="Do you wants to log out ?",
                         text_color="black",
                         font=("Source Code Pro",28,"bold"))
    lable.place(relx = 0.5, rely = 0.25, anchor = "center")

    yes_button = ctk.CTkButton(warning_entry,
                               text="Yes",
                               text_color="white",
                               font=("Source Code Pro",28, "bold"),
                               width=170,
                               height=65,
                               hover_color="#aea7f1",
                               fg_color="#36195B",
                               command=lambda: log_out())
    yes_button.place(relx = 0.75, rely = 0.67, anchor = "center")

    no_button = ctk.CTkButton(warning_entry,
                              text="No",
                              text_color="white",
                              font=("Source Code Pro",28, "bold"),
                              width=170,
                              height=65,
                              hover_color="#aea7f1",
                              fg_color="#36195B",
                              command=lambda:hide_warning())
    no_button.place(relx = 0.25, rely = 0.67, anchor = "center")





    notification_panel = NotificationPanel(frame_main_chat, 1.01, 0.66)
    
    goback_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\goback1.png"),
                                size=(30,30))
    goback_button = ctk.CTkButton(notification_panel,
                                image=goback_image,
                                width=10,
                                height=10,
                                fg_color="red",
                                text=None,
                                command=notification_panel.animate)
    goback_button.place(relx = 0.1, rely = 0.3, anchor = "center")
    notification_button.configure(command = notification_panel.animate,)


# chat_main(frame_main_chat)
# app.resizable(False,False)
# app.mainloop()
