import customtkinter as ctk
from PIL import Image
import time

def load_info(frame_info):

    line_one = ctk.CTkLabel(master=frame_info,
                        text = "Created with love by Bugs",
                        text_color="#BF8EFD",
                        bg_color="#36195B",
                        font= ("Source Code Pro", 20, "bold"))

    line_two = ctk.CTkLabel(master=frame_info,
                            text="Supported and expanded by awesome Team7",
                            text_color="#BF8EFD",
                            bg_color="#36195B",
                            font=("Source Code Pro", 20, "bold"))


    line_three = ctk.CTkLabel(master=frame_info,
                            text = "Launched on..... ",
                            text_color="#BF8EFD",
                            bg_color="#36195B",
                            font=("Source Code Pro", 20, "bold"))



    line_four = ctk.CTkLabel(master=frame_info,
                            text="About",
                            text_color="white",
                            bg_color="#36195B",
                            font=("Source Code Pro",22, "bold"))


    line_five = ctk.CTkLabel(master=frame_info,
                            text="Simple Chatbot is a minimalist style learning calendar notification app that can",
                            text_color="white",
                            bg_color="#36195B",
                            font= ("Source Code Pro",22, "bold"))


    line_six = ctk.CTkLabel(master=frame_info,
                            text="be customized to suit your preferences. Applications designed and developed to",
                            text_color="white",
                            bg_color="#36195B",
                            font= ("Source Code Pro",22, "bold"))


    line_seven = ctk.CTkLabel(master=frame_info,
                            text="make your learning tracking more vivid and intuitive.",
                            text_color="white",
                            bg_color="#36195B",
                            font= ("Source Code Pro",22, "bold"))

    line_eight = ctk.CTkLabel(master=frame_info,
                            text="Never regard study as a duty, but as the enviable opportunity to learn.",
                            text_color="white",
                            bg_color="#36195B",
                            font= ("Source Code Pro",22, "bold"))


    line_nine = ctk.CTkLabel(master=frame_info,
                            text= "“Albert Einstein”",
                            text_color="white",
                            bg_color="#36195B",
                            font= ("Source Code Pro",22, "bold"))

    line_one.place(relx = 0.5, rely = 0.1, anchor = "center")

    line_two.place(relx = 0.5, rely = 0.17, anchor = "center")

    line_three.place(relx = 0.5, rely = 0.24, anchor = "center")

    line_four.place(relx = 0.057, rely = 0.44)

    line_five.place(relx = 0.5, rely = 0.6, anchor = "center")

    line_six.place(relx = 0.49, rely = 0.67, anchor = "center")

    line_seven.place(relx = 0.352, rely = 0.74, anchor = "center")

    line_eight.place(relx = 0.452, rely = 0.9, anchor = "center")

    line_nine.place(relx = 0.1517, rely = 0.97, anchor = "center")

