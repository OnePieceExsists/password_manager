import tkinter as tk
from tkinter import messagebox
from password_generator import PasswordGenerator
from password_manager import PasswordManager

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.configure(bg="#D2B48C")  # light brown window background

        self.pm = PasswordManager()

        # Main frame with light brown bg
        self.frame = tk.Frame(root, bg="#D2B48C")
        self.frame.pack(padx=20, pady=20)

        # Input Fields
        tk.Label(self.frame, text="Website", bg="#D2B48C").grid(row=0, column=0, sticky="e", padx=5, pady=8)
        self.website_entry = tk.Entry(self.frame, width=40)
        self.website_entry.grid(row=0, column=1, padx=5, pady=8)

        tk.Label(self.frame, text="Username", bg="#D2B48C").grid(row=1, column=0, sticky="e", padx=5, pady=8)
        self.username_entry = tk.Entry(self.frame, width=40)
        self.username_entry.grid(row=1, column=1, padx=5, pady=8)

        tk.Label(self.frame, text="Description", bg="#D2B48C").grid(row=2, column=0, sticky="e", padx=5, pady=8)
        self.desc_entry = tk.Entry(self.frame, width=40)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=8)

        tk.Label(self.frame, text="Password", bg="#D2B48C").grid(row=3, column=0, sticky="e", padx=5, pady=8)
        self.password_entry = tk.Entry(self.frame, width=40)
        self.password_entry.grid(row=3, column=1, padx=5, pady=8)

        # Buttons with colors and spacing
        tk.Button(self.frame, text="Generate", command=self.generate_password, bg="green", fg="white")\
            .grid(row=3, column=2, padx=10, pady=8)
        tk.Button(self.frame, text="Save", command=self.save_entry, bg="blue", fg="white")\
            .grid(row=4, column=1, padx=10, pady=8)

        self.view_btn = tk.Button(self.frame, text="View Saved", command=self.show_password_prompt, bg="#800080", fg="white")  # Purple bg, white text
        self.view_btn.grid(row=4, column=2, padx=(5, 10), pady=8)

        # Hidden password prompt for viewing saved passwords
        self.view_password_frame = tk.Frame(self.frame, bg="#D2B48C")
        self.view_password_frame.grid(row=5, column=0, columnspan=3, pady=8)
        self.view_password_frame.grid_remove()  # hidden initially

        tk.Label(self.view_password_frame, text="Enter password to view:", bg="#D2B48C").grid(row=0, column=0, padx=5)
        self.view_password_entry = tk.Entry(self.view_password_frame, show="*")
        self.view_password_entry.grid(row=0, column=1, padx=5)
        self.submit_btn = tk.Button(self.view_password_frame, text="Submit", command=self.check_view_password, bg="#800080", fg="white")
        self.submit_btn.grid(row=0, column=2, padx=5)

        # List Display (blurred by default)
        self.listbox = tk.Listbox(self.frame, width=60)
        self.listbox.grid(row=6, column=0, columnspan=3, pady=10)
        self.refresh_list(blur=True)

    def generate_password(self):
        pg = PasswordGenerator()
        pwd = pg.generate()
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, pwd)

    def save_entry(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        description = self.desc_entry.get()

        if not website or not username or not password:
            messagebox.showwarning("Missing info", "Please fill out all required fields.")
            return

        self.pm.add_entry(website, username, password, description)
        self.refresh_list(blur=True)
        messagebox.showinfo("Saved", "Password entry saved!")

    def refresh_list(self, blur=True):
        self.listbox.delete(0, tk.END)
        for entry in self.pm.passwords:
            website = entry['website']
            username = entry['username']
            password = entry['password']
            if blur:
                # Blur password and username by replacing with asterisks
                display_text = f"{website} - {username} - {'*' * len(password)}"
            else:
                display_text = f"{website} - {username} - {password}"
            self.listbox.insert(tk.END, display_text)

    def show_password_prompt(self):
        self.view_password_entry.delete(0, tk.END)
        self.view_password_frame.grid()  # show the password prompt frame

    def check_view_password(self):
        entered = self.view_password_entry.get()
        if entered == "12345":  # simple hardcoded password to view saved passwords
            self.view_password_frame.grid_remove()
            self.refresh_list(blur=False)
        else:
            messagebox.showerror("Access denied", "Incorrect password!")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
