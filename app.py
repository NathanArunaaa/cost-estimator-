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

    # ------------------ SECTION CREATION ------------------ #

    def create_window_section(self):
        self.window_section = CollapsibleSection(self.scrollable_frame, "🪟 Window Cleaning")
        self.window_section.pack(fill="x", padx=20, pady=10)

        self.window_section.content.grid_columnconfigure(0, weight=1)
        self.window_section.content.grid_columnconfigure(1, weight=1)
        self.window_section.content.grid_columnconfigure(2, weight=0)

        ctk.CTkLabel(self.window_section.content, text="Number of Windows:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.window_count = ctk.CTkEntry(self.window_section.content)
        self.window_count.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(self.window_section.content, text="Price per Window ($):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.window_price = ctk.CTkEntry(self.window_section.content)
        self.window_price.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.window_total = ctk.CTkLabel(self.window_section.content, text="Section Total: $0.00")
        self.window_total.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        copy_btn = ctk.CTkButton(
            self.window_section.content,
            text="⌃",
            width=10,
            height=25,
            font=ctk.CTkFont(size=12),
            command=lambda: self.copy_to_clipboard(self.window_total.cget("text"))
        )
        copy_btn.grid(row=2, column=1, padx=5, pady=10, sticky="w")

    def create_gutter_section(self):
        self.gutter_section = CollapsibleSection(self.scrollable_frame, "🍃 Gutter Cleaning")
        self.gutter_section.pack(fill="x", padx=20, pady=10)

        self.gutter_section.content.grid_columnconfigure(0, weight=1)
        self.gutter_section.content.grid_columnconfigure(1, weight=1)
        self.gutter_section.content.grid_columnconfigure(2, weight=0)

        ctk.CTkLabel(self.gutter_section.content, text="Linear Feet:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.gutter_length = ctk.CTkEntry(self.gutter_section.content)
        self.gutter_length.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(self.gutter_section.content, text="Price per Foot ($):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.gutter_price = ctk.CTkEntry(self.gutter_section.content)
        self.gutter_price.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.gutter_total = ctk.CTkLabel(self.gutter_section.content, text="Section Total: $0.00")
        self.gutter_total.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        copy_btn = ctk.CTkButton(
            self.gutter_section.content,
            text="⌃",
            width=10,
            height=25,
            font=ctk.CTkFont(size=12),
            command=lambda: self.copy_to_clipboard(self.gutter_total.cget("text"))
        )
        copy_btn.grid(row=2, column=1, padx=5, pady=10, sticky="w")

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

    # ------------------ CALCULATION & COPY ------------------ #
    def calculate_total(self):
        total = 0
        try:
            if self.window_section.checkbox_var.get():
                w = float(self.window_count.get()) * float(self.window_price.get())
                self.window_total.configure(text=f"Section Total: ${w:,.2f}")
                total += w
            else:
                self.window_total.configure(text="Section Total: $0.00")

            if self.gutter_section.checkbox_var.get():
                g = float(self.gutter_length.get()) * float(self.gutter_price.get())
                self.gutter_total.configure(text=f"Section Total: ${g:,.2f}")
                total += g
            else:
                self.gutter_total.configure(text="Section Total: $0.00")

            if self.guard_section.checkbox_var.get():
                guard = float(self.guard_length.get()) * float(self.guard_price.get())
                self.guard_total.configure(text=f"Section Total: ${guard:,.2f}")
                total += guard
            else:
                self.guard_total.configure(text="Section Total: $0.00")

            if self.poly_section.checkbox_var.get():
                p = float(self.poly_sqft.get()) * float(self.poly_price.get())
                self.poly_total.configure(text=f"Section Total: ${p:,.2f}")
                total += p
            else:
                self.poly_total.configure(text="Section Total: $0.00")

            self.global_total_label.configure(text=f"TOTAL ESTIMATE: ${total:,.2f}")
        except ValueError:
            self.global_total_label.configure(text="Please enter valid numbers.")

    def copy_to_clipboard(self, text):
        self.clipboard_clear()
        self.clipboard_append(text)


if __name__ == "__main__":
    app = ServiceEstimator()
    app.mainloop()