import customtkinter
from PIL import Image
#pip install customtkinter
#pip install pillow
import time
import os
# Tạo cửa sổ chính
root = customtkinter.CTk()

def login():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    current_path = os.getcwd()
    def test():
        print("helolo")
    def clock():
        now = time.time()
        hour = time.strftime("%H", time.localtime(now))
        minute = time.strftime("%M", time.localtime(now))
        second = time.strftime("%S", time.localtime(now))
        clock_label.configure(text = hour + ":" + minute + ":" + second)
        clock_label.after(1, clock)

    app = customtkinter.CTk()
    app.geometry("2000x1300")
    app.title("Bot Bugs")
    # tạo frame
    frame_main = customtkinter.CTkFrame(master = app,
                                        width =1220,
                                        height=720,
                                        corner_radius=40,
                                        fg_color="black")
    frame_main.pack(padx = 10, pady = 10 )

    frame_logo = customtkinter.CTkFrame(master = frame_main,
                                        width = 1200,
                                        height= 100,
                                        corner_radius=41,
                                        fg_color="black")
    frame_logo.place(relx = 0.5, rely = 0.1, anchor = "center")

    frame_center = customtkinter.CTkFrame(master= frame_main,
                                        width= 1200,
                                        height= 450,
                                        fg_color="black" )
    frame_center.place(relx = 0.5, rely = 0.51, anchor = "center")

    frame_support = customtkinter.CTkFrame(master = frame_main,
                                        width = 1200,
                                        height=90,
                                        corner_radius=300,
                                        border_color="red",
                                        fg_color="black")
    frame_support.place(relx = 0.5, rely = 0.913, anchor = "center")

    # thêm các thành phần vào frame_logo
    logo_image = customtkinter.CTkImage(light_image=Image.open(rf"{current_path}\image\logo.png"),
                                        size=(80, 80))
    logo_label = customtkinter.CTkLabel(master = frame_logo, image=logo_image, text=None)
    logo_label.place(relx = 0.065, rely = 0.5, anchor = "center")

    name_app_label = customtkinter.CTkLabel(master = frame_logo, 
                                            text = ("Simple ChatBot"), 
                                            font=("Inter",50,"bold"))
    name_app_label.place(relx = 0.26, rely = 0.5, anchor = "center")

    name_bot_label = customtkinter.CTkLabel(master=frame_logo, 
                                            text= "bot bugs",
                                            width=13,
                                            height=13, 
                                            text_color="#BF8EFD",
                                            font=("SourceCodePro-SemiBold", 15)) 
                                            
    name_bot_label.place (relx = 0.1375, rely = 0.219, anchor = "center")

    clock_label = customtkinter.CTkLabel(master = frame_logo,
                                        text = None,
                                        font = ("Inter", 28,"bold"),
                                        fg_color="black",
                                        text_color="#BF8EFD")
    clock_label.place(relx = 0.73, rely = 0.5, anchor = "center")

    setting_image = customtkinter.CTkImage(light_image=Image.open(rf"{current_path}\image\setting.png"),
                                        size=(30,30))
    setting_button = customtkinter.CTkButton(master = frame_logo,
                                            image=setting_image,
                                            fg_color="black",
                                            width= 20,
                                            height=20,
                                            hover_color="white",
                                            text=None)
    setting_button.place(relx = 0.9, rely = 0.5, anchor = "center")

    notification_image = customtkinter.CTkImage(light_image=Image.open(rf"{current_path}\image\notification.png"),
                                                size = (30,30))
    notification_button = customtkinter.CTkButton(master = frame_logo, 
                                                image=notification_image, 
                                                width=10,
                                                height=10,
                                                fg_color="black",
                                                hover_color="white",
                                                text=None)
    notification_button.place(relx = 0.85, rely = 0.5, anchor = "center")

    # thêm các thành phần vào frame_center
    register_label = customtkinter.CTkLabel(master = frame_center,
                                            text = "register",
                                            fg_color="black",
                                            font=("Source Code Pro",16,"bold"))
    register_label.place(relx = 0.143, rely = 0.09, anchor = "center")

    username_entry = customtkinter.CTkEntry(master = frame_center,
                                            placeholder_text="username",
                                            placeholder_text_color="#BF8EFD",
                                            text_color="#fb8dd6",
                                            width=300,
                                            height=50,
                                            font=("Source Code Pro",20,"bold"),
                                            fg_color="#2E1A47",
                                            border_color="#ffcad7",
                                            corner_radius=18)
    username_entry.place(relx = 0.238, rely = 0.178, anchor = "center")

    email_entry = customtkinter.CTkEntry(master = frame_center,
                                        placeholder_text="email",
                                        placeholder_text_color="#BF8EFD",
                                        text_color="#fb8dd6",
                                        width=300,
                                        height=50,
                                        font=("Source Code Pro",20,"bold"),
                                        fg_color="#2E1A47",
                                        border_color="#ffcad7",
                                        corner_radius=18)
    email_entry.place(relx = 0.238, rely = 0.319, anchor = "center")

    password_entry = customtkinter.CTkEntry(master = frame_center,
                                            placeholder_text="password",
                                            placeholder_text_color="#BF8EFD",
                                            text_color="#fb8dd6",
                                            width=300,
                                            height=50,
                                            font=("Source Code Pro",20,"bold"),
                                            fg_color="#2E1A47",
                                            border_color="#ffcad7",
                                            corner_radius=18)
    password_entry.place(relx = 0.238, rely = 0.46, anchor = "center")

    verify_password_entry = customtkinter.CTkEntry(master = frame_center,
                                                placeholder_text="verify password",
                                                placeholder_text_color="#BF8EFD",
                                                text_color="#fb8dd6",
                                                width=300,
                                                height=50,
                                                font=("Source Code Pro",20,"bold"),
                                                fg_color="#2E1A47",
                                                border_color="#ffcad7",
                                                corner_radius=18)
    verify_password_entry.place(relx = 0.238, rely = 0.601, anchor = "center")

    sign_up_image = customtkinter.CTkImage(light_image=Image.open(rf"{current_path}\image\signup.png"),
                                        size=(35,35))
    sign_up_button = customtkinter.CTkButton(master = frame_center,
                                            image=sign_up_image,
                                            width=300,
                                            height=50,
                                            corner_radius=18,
                                            text="Sign Up",
                                            fg_color="#2E1A47",
                                            border_color="white",
                                            hover_color="#ff52bd",
                                            font = ("Inter",24,"bold"),)
    sign_up_button.place(relx = 0.238, rely = 0.742, anchor = "center")

    login_label = customtkinter.CTkLabel(master = frame_center,
                                        text="login",
                                        font=("Source Code Pro",16,"bold"))
    login_label.place(relx = 0.636, rely = 0.09, anchor = "center" )

    uname_entry = customtkinter.CTkEntry(master = frame_center,
                                        placeholder_text="username",
                                        placeholder_text_color="#BF8EFD",
                                        text_color="#fb8dd6",
                                        width=300,
                                        height=50,
                                        font=("Source Code Pro",20,"bold"),
                                        fg_color="#2E1A47",
                                        border_color="#ffcad7",
                                        corner_radius=18)
    uname_entry.place(relx = 0.743, rely = 0.178, anchor = "center")


    forgot_pass_button = customtkinter.CTkButton(master = frame_center,
                                                width=20,
                                                height=20,
                                                fg_color="black",
                                                text_color="#BF8EFD",
                                                text="Forgot password?",
                                                hover_color="#ff52bd",
                                                font=("Inter",13,"bold"))
    forgot_pass_button.place(relx = 0.816, rely = 0.415, anchor = "center")

    passwd_entry = customtkinter.CTkEntry(master = frame_center,
                                        placeholder_text="password",
                                        placeholder_text_color="#BF8EFD",
                                        text_color="#fb8dd6",
                                        width=300,
                                        height=50,
                                        font=("Source Code Pro",20,"bold"),
                                        fg_color="#2E1A47",
                                        border_color="#ffcad7",
                                        corner_radius=18)
    passwd_entry.place(relx = 0.743, rely = 0.319, anchor = "center")

    login_image = customtkinter.CTkImage(light_image=Image.open(rf"{current_path}\image\login.png"),
                                        size=(35,35))
    login_button = customtkinter.CTkButton(master = frame_center,
                                        image=login_image,
                                        width=300,
                                        height=50,
                                        text="Sign In",
                                        font=("Inter",24,"bold"),
                                        corner_radius=18,
                                        hover_color="#ff52bd",
                                        fg_color="#2E1A47")
    login_button.place(relx = 0.743, rely = 0.511, anchor = "center")

    # thêm các thành phần vào frame_support

    mailbox_image = customtkinter.CTkImage(light_image=Image.open(rf"{current_path}\image\mailbox.png"),
                                        size = (22,22))
    github_image = customtkinter.CTkImage(light_image=Image.open(rf"{current_path}\image\github.png"),
                                        size=(26,26))
    donate_image = customtkinter.CTkImage(light_image=Image.open(rf"{current_path}\image\donate.png"),
                                        size=(25,25))
    support_image = customtkinter.CTkImage(light_image=Image.open(rf"{current_path}\image\support.png"),
                                        size=(25,25))
    version_image = customtkinter.CTkImage(light_image=Image.open(rf"{current_path}\image\version.png"),
                                        size=(25,25))
    contact_button = customtkinter.CTkButton(master=frame_support,
                                            image=mailbox_image,
                                            text="Contact",
                                            font=("Source Code Pro",20,"bold"),
                                            fg_color="black",
                                            corner_radius=10,
                                            border_color="white",
                                            text_color="#BF8EFD",
                                            hover_color="#fdd6ee",
                                            width=10,
                                            height=10)
    Github_button = customtkinter.CTkButton(master=frame_support,
                                            image=github_image,
                                            text="Github",
                                            font=("Source Code Pro",20,"bold"),
                                            text_color="#BF8EFD",
                                            fg_color="black",
                                            hover_color="#fdd6ee",
                                            width=5,
                                            height=5)
    Donate_button = customtkinter.CTkButton(master=frame_support,
                                            image=donate_image,
                                            text="Donate",
                                            font=("Source Code Pro",20,"bold"),
                                            text_color="#BF8EFD",
                                            fg_color="black",
                                            hover_color="#fdd6ee",
                                            width=10,
                                            height=10)
    Support_button = customtkinter.CTkButton(master=frame_support,
                                            image=support_image,
                                            text="Support",
                                            font=("Source Code Pro",20,"bold"),
                                            text_color="#BF8EFD",
                                            fg_color="black",
                                            hover_color="#fdd6ee",
                                            width=10,
                                            height=10)
    version_button = customtkinter.CTkButton(master=frame_support,
                                            image=version_image,
                                            text="v.0.0.0",
                                            font=("Source Code Pro",20,"bold"),
                                            text_color="#BF8EFD",
                                            fg_color="black",
                                            hover_color="#fdd6ee",
                                            width=10,
                                            height=10)

    contact_button.place(relx = 0.075, rely = 0.4, anchor = "center")
    Github_button.place(relx = 0.178, rely = 0.4, anchor = "center")
    Donate_button.place(relx = 0.28, rely = 0.4, anchor = "center")
    Support_button.place(relx = 0.386, rely = 0.4, anchor = "center")
    version_button.place(relx = 0.9, rely = 0.4, anchor = "center")
    clock()

    app.mainloop()
# Tạo nút Login
login_button = customtkinter.CTkButton(root, text="Login", command=login)

# Thêm nút Login vào cửa sổ chính
login_button.pack()

# Hàm xử lý sự kiện click của nút Login

# Bắt đầu vòng lặp chính
root.mainloop()
