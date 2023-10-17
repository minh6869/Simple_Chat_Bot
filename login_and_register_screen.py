import customtkinter as ctk
from PIL import Image
#pip install customtkinter
#pip install pillow
import time
import os
import load
import main_chat


# app = ctk.CTk()
# app.geometry("1310x695")
# app.title("Bot Bugs")
# app.iconbitmap()

# frame_main = ctk.CTkFrame(master = app,
#                                         width =1220,
#                                         height=720,
#                                         corner_radius=20,
#                                         fg_color="#36195B")

def load_login_and_register_screen(app,frame_main):
    global tmp, temp
    class NotificationPanel(ctk.CTkFrame):
        def __init__(self, parent, start_pos, end_pos):
            super().__init__(master = parent, width=385, height=641, fg_color="#7801A1", corner_radius=30, border_color="red")

            # general attributes 
            self.start_pos = start_pos 
            self.end_pos = end_pos - 0.01
            self.width =  abs(start_pos - end_pos)

            # animation logic
            self.pos = self.start_pos
            self.in_start_pos = True

            # layout
            self.place(relx = 1.01, rely = 0.025, )

        def animate(self):
            if self.in_start_pos:
                self.animate_forward()
            else:
                self.animate_backwards()

        def animate_forward(self):
            if self.pos > self.end_pos:
                self.pos -= 0.006
                self.place(relx = self.pos, rely = 0.03, )
                self.after(10, self.animate_forward)
            else:
                self.in_start_pos = False

        def animate_backwards(self):
            if self.pos < self.start_pos:
                self.pos += 0.006
                self.place(relx = self.pos, rely = 0.03, )
                self.after(10, self.animate_backwards)
            else:
                self.in_start_pos = True



    current_path = os.getcwd()
    
    def get_info():
        global tmp, goback_button
        if tmp:
            frame_center.place_forget()
            frame_load.place(relx = 0.5, rely = 0.51, anchor = "center")
            frame_load.after(150, lambda:frame_load.place_forget())
            frame_info.place(relx = 0.5, rely = 0.51, anchor = "center")


            # app.frames[2].place_forget()
            # app.frames[5].place(relx = 0.5, rely = 0.51, anchor = "center")
        
            # app.after(150,  lambda: app.frames[5].place_forget())
            # app.frames[4].place(relx = 0.5, rely = 0.51, anchor = "center")
            
            tmp = False
        else:
            frame_info.place_forget()
            frame_load.place(relx = 0.5, rely = 0.51, anchor = "center")
            frame_load.after(150, lambda:frame_load.place_forget())
            frame_center.place(relx = 0.5, rely = 0.51, anchor = "center")



            # app.frames[4].place_forget()
            # app.frames[5].place(relx = 0.5, rely = 0.51, anchor = "center")
            # app.after(200,  lambda: app.frames[5].place_forget())
            # app.frames[2].place(relx = 0.5, rely = 0.51, anchor = "center")
            tmp = True


    tmp = True
    def clock():
        now = time.time()
        hour = time.strftime("%H", time.localtime(now))
        minute = time.strftime("%M", time.localtime(now))
        second = time.strftime("%S", time.localtime(now))
        clock_label.configure(text = hour + ":" + minute + ":" + second)
        clock_label.after(1, clock)

    def load_main_chat():
        global temp
        if temp:
            frame_main.pack_forget()
            frame_main_chat.pack(padx = 10 , pady = 10)
            logout_button.place(relx = 0.915, rely = 0.059, anchor = "center")
            temp = False
        else:
            frame_main_chat.pack_forget()
            frame_main.pack(padx = 10, pady = 10)
        #     # app.frames[6].pack_forget
        #     # app.frames[0].pack(padx = 10, pady = 10)
            temp = True
    loadmainchat = lambda: load_main_chat()
    temp = True
    def sign_up():
        username = username_entry.get()
        msv = email_entry.get()
        password = password_entry.get()
        verify_password = verify_password_entry.get()



    def sign_in():
        username = uname_entry.get()
        password = passwd_entry.get()
        





    # tạo frame
    


    frame_logo = ctk.CTkFrame(master = frame_main,
                                        width = 1200,
                                        height= 100,
                                        corner_radius=41,
                                        fg_color="#36195B")


    frame_center = ctk.CTkFrame(master= frame_main,
                                        width= 1200,
                                        height= 450,
                                        fg_color="#36195B" )

    frame_support = ctk.CTkFrame(master = frame_main,
                                        width = 1200,
                                        height=90,
                                        corner_radius=300,
                                        border_color="red",
                                        fg_color="#36195B")

    frame_info = ctk.CTkFrame(master= frame_main,
                                        width= 1200,
                                        height= 450,
                                        fg_color="#36195B" )

    frame_load = ctk.CTkFrame(master= frame_main,
                                        width= 1200,
                                        height= 450,
                                        fg_color="#36195B" )
    frame_main_chat = ctk.CTkFrame(master = app,
                                        width =1220,
                                        height=720,
                                        corner_radius=20,
                                        fg_color="#36195B")
    load.load_info(frame_info)
    # main_chat.chat_main(app,frame_main_chat)
    # loadgiftest.load(frame_load)


    frame_main.pack(padx = 10 , pady = 10)
    frame_logo.place(relx = 0.5, rely = 0.1,anchor = "center")
    frame_center.place(relx = 0.5, rely = 0.51, anchor = "center")
    frame_support.place(relx = 0.5, rely = 0.913,anchor = "center")


    # thêm các thành phần vào frame_logo

    logo_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\logo.png"),
                                        size=(80, 80))
    logo_label = ctk.CTkLabel(master = frame_logo, image=logo_image, text=None)

    name_app_label = ctk.CTkLabel(master = frame_logo, 
                                            text = ("Simple ChatBot"), 
                                            font=("Inter",50,"bold"))


    name_bot_label = ctk.CTkLabel(master=frame_logo, 
                                            text= "bot bugs",
                                            width=13,
                                            height=13, 
                                            text_color="#BF8EFD",
                                            font=("SourceCodePro-SemiBold", 15)) 
                                            
    name_bot_label.place (relx = 0.1375, rely = 0.219,anchor = "center")

    clock_label = ctk.CTkLabel(master = frame_logo,
                                        text = None,
                                        font = ("Inter", 28,"bold"),
                                        fg_color="#36195B",
                                        text_color="#BF8EFD")

    infor_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\information.png"),
                            size=(30,30))
    infor_button = ctk.CTkButton(master=frame_logo,
                                image=infor_image,
                                width=10,
                                height=10,
                                fg_color="#36195B",
                                hover_color="white",
                                command= lambda: get_info(),
                                text=None)
    notification_panel = NotificationPanel(frame_main, 1.01, 0.682)
    goback_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\goback.png"),
                                size=(30,30))
    goback1_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\goback1.png"),
                                size=(30,30))
    goback_button = ctk.CTkButton(notification_panel,
                                image=goback1_image,
                                width=10,
                                height=10,
                                fg_color="red",
                                text=None,
                                command=notification_panel.animate)
    goback_button.place(relx = 0.1, rely = 0.3, anchor = "center")

    notification_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\notification.png"),
                                                size = (35,35))
    notification_button = ctk.CTkButton(master = frame_logo, 
                                                image=notification_image, 
                                                width=10,
                                                height=10,
                                                fg_color="#36195B",
                                                hover_color="white",
                                                command=notification_panel.animate,
                                                text=None)

    goback_button_info = ctk.CTkButton(frame_info,
                                    image=goback_image,
                                    fg_color="#36195B",
                                    width=10,
                                    height=10,
                                    command=lambda:get_info(),
                                    text=None,)
    goback_button_info.place(relx = 0.067, rely = 0.14, anchor = "center")


    setting_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\setting.png"),
                                        size=(30,30))
    setting_button = ctk.CTkButton(master = frame_logo,
                                            image=setting_image,
                                            fg_color="#36195B",
                                            width= 20,
                                            height=20,
                                            hover_color="white",
                                            text=None)
    logout_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\power.png"),
                              size=(30,30))
    logout_button = ctk.CTkButton(master=frame_main_chat,
                                text=None,
                                image=logout_image,
                                fg_color="#36195B",
                                width= 20,
                                height=20,
                                hover_color="white",)




    main_chat.chat_main(app,frame_main_chat, loadmainchat, logout_button)



    logo_label.place(relx = 0.065, rely = 0.5, anchor = "center")

    name_app_label.place(relx = 0.26, rely = 0.5, anchor = "center")

    clock_label.place(relx = 0.75, rely = 0.5, anchor = "center")

    infor_button.place(relx = 0.84, rely = 0.5, anchor = "center")

    notification_button.place(relx = 0.89, rely = 0.5, anchor = "center")

    setting_button.place(relx = 0.94, rely = 0.5, anchor = "center")


    # thêm các thành phần vào frame_center
    register_label = ctk.CTkLabel(master = frame_center,
                                            text = "register",
                                            fg_color="#36195B",
                                            font=("Source Code Pro",23,"bold"))


    username_entry = ctk.CTkEntry(master = frame_center,
                                            placeholder_text="username",
                                            placeholder_text_color="#BF8EFD",
                                            text_color="#fb8dd6",
                                            width=300,
                                            height=50,
                                            font=("Source Code Pro",20,"bold"),
                                            fg_color="#2E1A47",
                                            border_color="#ffcad7",
                                            corner_radius=18)


    email_entry = ctk.CTkEntry(master = frame_center,
                                        placeholder_text="user id",
                                        placeholder_text_color="#BF8EFD",
                                        text_color="#fb8dd6",
                                        width=300,
                                        height=50,
                                        font=("Source Code Pro",20,"bold"),
                                        fg_color="#2E1A47",
                                        border_color="#ffcad7",
                                        corner_radius=18)


    password_entry = ctk.CTkEntry(master = frame_center,
                                            placeholder_text="password",
                                            placeholder_text_color="#BF8EFD",
                                            text_color="#fb8dd6",
                                            width=300,
                                            height=50,
                                            font=("Source Code Pro",20,"bold"),
                                            fg_color="#2E1A47",
                                            show = "*",
                                            border_color="#ffcad7",
                                            corner_radius=18)


    verify_password_entry = ctk.CTkEntry(master = frame_center,
                                                placeholder_text="verify password",
                                                placeholder_text_color="#BF8EFD",
                                                text_color="#fb8dd6",
                                                width=300,
                                                height=50,
                                                font=("Source Code Pro",20,"bold"),
                                                fg_color="#2E1A47",
                                                border_color="#ffcad7",
                                                show = "*",
                                                corner_radius=18)


    sign_up_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\signup.png"),
                                        size=(35,35))
    sign_up_button = ctk.CTkButton(master = frame_center,
                                            image=sign_up_image,
                                            width=300,
                                            height=50,
                                            corner_radius=18,
                                            text="Sign Up",
                                            fg_color="#2E1A47",
                                            border_color="white",
                                            command= lambda: get_info(),
                                            hover_color="#ff52bd",
                                            font = ("Inter",24,"bold"),)


    login_label = ctk.CTkLabel(master = frame_center,
                                        text="login",
                                        font=("Source Code Pro",23,"bold"))


    uname_entry = ctk.CTkEntry(master = frame_center,
                                        placeholder_text="username",
                                        placeholder_text_color="#BF8EFD",
                                        text_color="#fb8dd6",
                                        width=300,
                                        height=50,
                                        font=("Source Code Pro",20,"bold"),
                                        fg_color="#2E1A47",
                                        border_color="#ffcad7",
                                        corner_radius=18)



    forgot_pass_button = ctk.CTkButton(master = frame_center,
                                                width=20,
                                                height=20,
                                                fg_color="#36195B",
                                                text_color="#BF8EFD",
                                                text="Forgot password?",
                                                hover_color="#fdd6ee",
                                                font=("Inter",13,"bold"))


    passwd_entry = ctk.CTkEntry(master = frame_center,
                                        placeholder_text="password",
                                        placeholder_text_color="#BF8EFD",
                                        text_color="#fb8dd6",
                                        width=300,
                                        height=50,
                                        font=("Source Code Pro",20,"bold"),
                                        fg_color="#2E1A47",
                                        border_color="#ffcad7",
                                        show = "*",
                                        corner_radius=18)


    login_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\login.png"),
                                        size=(35,35))
    sign_in_button = ctk.CTkButton(master = frame_center,
                                image=login_image,
                                width=300,
                                height=50,
                                text="Sign In",
                                font=("Inter",24,"bold"),
                                corner_radius=18,
                                hover_color="#ff52bd",
                                fg_color="#2E1A47",
                                command=lambda: load_main_chat())



    register_label.place(relx = 0.156, rely = 0.081, anchor = "center")

    username_entry.place(relx = 0.238, rely = 0.178, anchor = "center")

    email_entry.place(relx = 0.238, rely = 0.338, anchor = "center")

    password_entry.place(relx = 0.238, rely = 0.498, anchor = "center")


    verify_password_entry.place(relx = 0.238, rely = 0.658, anchor = "center")

    sign_up_button.place(relx = 0.238, rely = 0.818, anchor = "center")

    login_label.place(relx = 0.645, rely = 0.081, anchor = "center" )

    uname_entry.place(relx = 0.743, rely = 0.178, anchor = "center")

    passwd_entry.place(relx = 0.743, rely = 0.338, anchor = "center")

    forgot_pass_button.place(relx = 0.816, rely = 0.434, anchor = "center")

    sign_in_button.place(relx = 0.743, rely = 0.53, anchor = "center")

    # thêm các thành phần vào frame_support

    mailbox_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\mailbox.png"),
                                        size = (25,25))
    github_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\github.png"),
                                        size=(25,25))
    donate_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\donate.png"),
                                        size=(25,25))
    discord_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\discord.png"),
                                        size=(25,25))
    version_image = ctk.CTkImage(light_image=Image.open(rf"{current_path}\image\version.png"),
                                        size=(25,25))
    contact_button = ctk.CTkButton(master=frame_support,
                                            image=mailbox_image,
                                            text="Contact",
                                            font=("Source Code Pro",20,"bold"),
                                            fg_color="#36195B",
                                            corner_radius=10,
                                            border_color="white",
                                            text_color="#BF8EFD",
                                            hover_color="#fdd6ee",
                                            width=10,
                                            height=10)
    Github_button = ctk.CTkButton(master=frame_support,
                                            image=github_image,
                                            text="Github",
                                            font=("Source Code Pro",20,"bold"),
                                            text_color="#BF8EFD",
                                            fg_color="#36195B",
                                            corner_radius=10,
                                            hover_color="#fdd6ee",
                                            width=5,
                                            height=5)
    Donate_button = ctk.CTkButton(master=frame_support,
                                            image=donate_image,
                                            text="Donate",
                                            font=("Source Code Pro",20,"bold"),
                                            text_color="#BF8EFD",
                                            fg_color="#36195B",
                                            hover_color="#fdd6ee",
                                            width=10,
                                            height=10)
    Discord_button = ctk.CTkButton(master=frame_support,
                                            image=discord_image,
                                            text="Discord",
                                            font=("Source Code Pro",20,"bold"),
                                            text_color="#BF8EFD",
                                            fg_color="#36195B",
                                            hover_color="#fdd6ee",
                                            width=10,
                                            height=10)
    version_button = ctk.CTkButton(master=frame_support,
                                            image=version_image,
                                            text="v.0.0.0",
                                            font=("Source Code Pro",20,"bold"),
                                            text_color="#BF8EFD",
                                            fg_color="#36195B",
                                            hover_color="#fdd6ee",
                                            width=10,
                                            height=10)

    contact_button.place(relx = 0.075, rely = 0.63, anchor = "center")
    Github_button.place(relx = 0.178, rely = 0.63, anchor = "center")
    Donate_button.place(relx = 0.28, rely = 0.63, anchor = "center")
    Discord_button.place(relx = 0.386, rely = 0.63, anchor = "center")
    version_button.place(relx = 0.9, rely = 0.63, anchor = "center")

    # app.frames = [frame_main, frame_logo, frame_center, frame_support, frame_info, frame_load, frame_main_chat]

    clock()


# load_login_and_register_screen(app, frame_main)
# app.resizable(False,False)
# app.mainloop()