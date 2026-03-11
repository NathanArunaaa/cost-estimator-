import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class CollapsibleSection(ctk.CTkFrame):
    def __init__(self, parent, title):
        super().__init__(parent)

        self.expanded = False

        self.header = ctk.CTkFrame(self)
        self.header.pack(fill="x")

        self.checkbox_var = ctk.BooleanVar()

        self.checkbox = ctk.CTkCheckBox(
            self.header,
            text=title,
            variable=self.checkbox_var
        )
        self.checkbox.pack(side="left", padx=10, pady=10)

        self.toggle_button = ctk.CTkButton(
            self.header,
            text="▼",
            width=30,
            command=self.toggle
        )
        self.toggle_button.pack(side="right", padx=10)

        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.pack(fill="x", padx=20)
        self.content.pack_forget()

    def toggle(self):
        if self.expanded:
            self.content.pack_forget()
            self.toggle_button.configure(text="▼")
        else:
            self.content.pack(fill="x", padx=20, pady=10)
            self.toggle_button.configure(text="▲")
        self.expanded = not self.expanded


class ServiceEstimator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Student Works Cost Estimator")
        self.geometry("450x1080")

        self.scrollable_frame = ctk.CTkScrollableFrame(self, scrollbar_fg_color="#2B2B2B", scrollbar_button_color="#2B2B2B", scrollbar_button_hover_color="#2B2B2B")
        self.scrollable_frame.pack(fill="both", expand=True,)

        title = ctk.CTkLabel(
            self.scrollable_frame,
            text="Service Cost Estimator",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title.pack(pady=20, padx=20, anchor="w")

        self.create_window_section()
        self.create_gutter_section()
        self.create_guard_section()
        self.create_polymeric_section()

        total_frame = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
        total_frame.pack(fill="x", padx=20, pady=20)

        self.global_total_label = ctk.CTkLabel(
            total_frame,
            text="TOTAL ESTIMATE: $0.00",
            font=ctk.CTkFont(size=26, weight="bold")
        )
        self.global_total_label.pack(side="left", anchor="w")


        calculate_btn = ctk.CTkButton(
            self.scrollable_frame,
            text="Calculate Total",
            height=45,
            font=ctk.CTkFont(size=18),
            command=self.calculate_total
        )
        calculate_btn.pack(pady=10, padx=20, anchor="w")

        self.help_button = ctk.CTkButton(
            self,
            text="?",
            fg_color="#2B2B2B",
            hover_color="#2B2B2B",
            width=40,
            height=40,
            corner_radius=0, 
            font=ctk.CTkFont(size=18, weight="bold"),
            command=self.open_about_window
        )

        self.help_button.place(relx=1.0, rely=1.0, anchor="se", x=-20, y=-20)

        self.window_section.toggle()
        self.gutter_section.toggle()



    # ------------------ SECTION CREATION ------------------ #

    def create_window_section(self):
        self.window_section = CollapsibleSection(self.scrollable_frame, "🪟 Window Cleaning")
        self.window_section.pack(fill="x", padx=20, pady=10)

        self.window_section.content.grid_columnconfigure(0, weight=1)
        self.window_section.content.grid_columnconfigure(1, weight=0)

        self.window_size = ctk.StringVar(value="")

        self.window_prices = {
            "Small": (250, 350),
            "Medium": (350, 450),
            "Large": (450, 600),
            "X-Large": (600, 900)
        }

        row = 0
        for size in self.window_prices:

            radio = ctk.CTkRadioButton(
                self.window_section.content,
                text=size,
                variable=self.window_size,
                value=size,
                command=self.calculate_total
            )
            radio.grid(row=row, column=0, padx=10, pady=5, sticky="w")

            row += 1

        self.window_total = ctk.CTkLabel(
            self.window_section.content,
            text="Section Total: $0 - $0"
        )
        self.window_total.grid(row=row, column=0, padx=10, pady=10, sticky="w")

        copy_btn = ctk.CTkButton(
            self.window_section.content,
            text="⌃",
            width=10,
            height=25,
            font=ctk.CTkFont(size=12),
            command=lambda: self.copy_to_clipboard(self.window_total.cget("text"))
        )
        copy_btn.grid(row=row, column=1, padx=5, pady=10, sticky="w")

    def create_gutter_section(self):
        self.gutter_section = CollapsibleSection(self.scrollable_frame, "🍃 Gutter Cleaning")
        self.gutter_section.pack(fill="x", padx=20, pady=10)

        self.gutter_section.content.grid_columnconfigure(0, weight=1)
        self.gutter_section.content.grid_columnconfigure(1, weight=1)
        self.gutter_section.content.grid_columnconfigure(2, weight=0)

        ctk.CTkLabel(self.gutter_section.content, text="1st Floor (ft):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.gutter_length1 = ctk.CTkEntry(self.gutter_section.content)
        self.gutter_length1.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(self.gutter_section.content, text="2nd Floor (ft):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.gutter_length2 = ctk.CTkEntry(self.gutter_section.content)
        self.gutter_length2.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(self.gutter_section.content, text="3rd Floor (ft):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.gutter_length3 = ctk.CTkEntry(self.gutter_section.content)
        self.gutter_length3.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        self.gutter_total = ctk.CTkLabel(self.gutter_section.content, text="Section Total: $0.00")
        self.gutter_total.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.footage_total = ctk.CTkLabel(self.gutter_section.content, text="Linear Footage: 0 ft")
        self.footage_total.grid(row=3, column=1, padx=50, pady=10, sticky="w")

        copy_btn = ctk.CTkButton(
            self.gutter_section.content,
            text="⌃",
            width=10,
            height=25,
            font=ctk.CTkFont(size=12),
            command=lambda: self.copy_to_clipboard(self.gutter_total.cget("text"))
        )
        copy_btn.grid(row=3, column=1, padx=5, pady=10, sticky="w")

    def create_guard_section(self):
        self.guard_section = CollapsibleSection(self.scrollable_frame, "🛡️ Gutter Guard Installation")
        self.guard_section.pack(fill="x", padx=20, pady=10)

        self.guard_section.content.grid_columnconfigure(0, weight=1)
        self.guard_section.content.grid_columnconfigure(1, weight=1)
        self.guard_section.content.grid_columnconfigure(2, weight=0)

        ctk.CTkLabel(self.guard_section.content, text="Linear Feet:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.guard_length = ctk.CTkEntry(self.guard_section.content)
        self.guard_length.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(self.guard_section.content, text="Price per Foot ($):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.guard_price = ctk.CTkEntry(self.guard_section.content)
        self.guard_price.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.guard_total = ctk.CTkLabel(self.guard_section.content, text="Section Total: $0.00")
        self.guard_total.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        copy_btn = ctk.CTkButton(
            self.guard_section.content,
            text="⌃",
            width=10,
            height=25,
            font=ctk.CTkFont(size=12),
            command=lambda: self.copy_to_clipboard(self.guard_total.cget("text"))
        )
        copy_btn.grid(row=2, column=1, padx=5, pady=10, sticky="w")

    def create_polymeric_section(self):
        self.poly_section = CollapsibleSection(self.scrollable_frame, "🪏 Polymeric Sanding")
        self.poly_section.pack(fill="x", padx=20, pady=10)

        self.poly_section.content.grid_columnconfigure(0, weight=1)
        self.poly_section.content.grid_columnconfigure(1, weight=1)
        self.poly_section.content.grid_columnconfigure(2, weight=0)

        ctk.CTkLabel(self.poly_section.content, text="Square Footage:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.poly_sqft = ctk.CTkEntry(self.poly_section.content)
        self.poly_sqft.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(self.poly_section.content, text="Price per Sq Ft ($):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.poly_price = ctk.CTkEntry(self.poly_section.content)
        self.poly_price.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.poly_total = ctk.CTkLabel(self.poly_section.content, text="Section Total: $0.00")
        self.poly_total.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        copy_btn = ctk.CTkButton(
            self.poly_section.content,
            text="⌃",
            width=10,
            height=25,
            font=ctk.CTkFont(size=12),
            command=lambda: self.copy_to_clipboard(self.poly_total.cget("text"))
        )
        copy_btn.grid(row=2, column=1, padx=5, pady=10, sticky="w")


    # ------------------ ABOUT WINDOW ------------------ #

    def open_about_window(self):
        about_window = ctk.CTkToplevel(self)
        about_window.title("About")
        about_window.geometry("400x300")
        about_window.grab_set()  

        title = ctk.CTkLabel(
            about_window,
            text="About the Tool",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title.pack(pady=15, anchor="w", padx=20)

        info_text = (
            "Service Estimator App\n\n"
            "Created by: Nathan Aruna\n"
            "Built to simplify the estimating of job costs while on sales calls.\n\n"
            "Length multipliers are hard coded in this version :(\n\n"

            "Version 1.0\n"
            "2026"
        )

        info_label = ctk.CTkLabel(
            about_window,
            text=info_text,
            justify="left",
            wraplength=350
        )
        info_label.pack(padx=20, pady=10, anchor="w")

        close_button = ctk.CTkButton(
            about_window,
            text="Close",
            command=about_window.destroy
        )
        close_button.pack(pady=15, anchor="w", padx=20)

    # ------------------ CALCULATION & COPY ------------------ #
    def calculate_total(self):
        total = 0

        try:

            selected_size = self.window_size.get()

            if selected_size in self.window_prices:

                low, high = self.window_prices[selected_size]

                self.window_total.configure(
                    text=f"Section Total: ${low:,.0f} - ${high:,.0f}"
                )

            if self.window_section.checkbox_var.get():
                total += (low + high) / 2

            else:
                self.window_total.configure(text="Section Total: $0 - $0")


            # -------- GUTTER CLEANING --------
            if self.gutter_section.checkbox_var.get():
                g = float(self.gutter_length.get()) * float(self.gutter_price.get())
                self.gutter_total.configure(text=f"Section Total: ${g:,.2f}")
                total += g

            else:
                self.gutter_total.configure(text="Section Total: $0.00")

            # -------- GUTTER GUARD --------
            if self.guard_section.checkbox_var.get():
                guard = float(self.guard_length.get()) * float(self.guard_price.get())
                self.guard_total.configure(text=f"Section Total: ${guard:,.2f}")
                total += guard

            else:
                self.guard_total.configure(text="Section Total: $0.00")


            # -------- POLYMERIC SAND --------
            if self.poly_section.checkbox_var.get():
                p = float(self.poly_sqft.get()) * float(self.poly_price.get())
                self.poly_total.configure(text=f"Section Total: ${p:,.2f}")
                total += p

            else:
                self.poly_total.configure(text="Section Total: $0.00")


            # -------- GLOBAL TOTAL --------
            self.global_total_label.configure(
                text=f"TOTAL ESTIMATE: ${total:,.2f}"
            )

        except ValueError:
            self.global_total_label.configure(text="Please enter valid numbers.")

    def copy_to_clipboard(self, text):
        self.clipboard_clear()
        self.clipboard_append(text)


if __name__ == "__main__":
    
    app = ServiceEstimator()
    app.mainloop()