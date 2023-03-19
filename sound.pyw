import customtkinter
import winsound


def main():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    app = customtkinter.CTk()
    app.geometry("800x600")
    app.title("Sound")


    def start_sound():
        winsound.Beep(int(frequency.get()), int(time.get()))

    border = customtkinter.CTkFrame(master=app)
    border.pack(pady=20, padx=20, fill="both", expand=True)

    
        
    frequency = customtkinter.CTkEntry(
        master=border, width=200, placeholder_text="Frequency"
    )
    frequency.pack(pady=10, padx=10)

    time = customtkinter.CTkEntry(
        master=border, width=200, placeholder_text="Time"
        )
    time.pack(pady=10, padx=10)

    
    # Start Button
    start_button = customtkinter.CTkButton(
        master=border,
        command=start_sound,
        width=700,
        height=500,
        font=(customtkinter, 100),
        text="Sound",
    )
    start_button.pack(pady=10, padx=10)

    app.mainloop()


if __name__ == "__main__":
    main()
