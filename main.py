import tkinter as tk
from tkinter import messagebox, filedialog
from auth import register_user, authenticate_user
from encryption import encrypt_file, decrypt_file
import os
from datetime import datetime

LOG_FILE = 'logs/audit.log'

# Ensure folders exist
os.makedirs('logs', exist_ok=True)
os.makedirs('transferred_files', exist_ok=True)

# Log activity
def log_action(action, user):
    with open(LOG_FILE, 'a') as log:
        log.write(f"[{datetime.now()}] {user}: {action}\n")

# === New window for file operations ===
def open_file_window(username):
    window = tk.Tk()
    window.title(f"Secure File Transfer - {username}")
    window.geometry("400x250")
    
    def encrypt_action():
        file_path = filedialog.askopenfilename(title="Select file to encrypt")
        if file_path:
            enc_path = encrypt_file(file_path)
            messagebox.showinfo("Encrypted", f"File encrypted and saved to:\n{enc_path}")
            log_action(f"Encrypted file: {file_path}", username)

    def decrypt_action():
        file_path = filedialog.askopenfilename(title="Select file to decrypt")
        if file_path:
            output_path, msg = decrypt_file(file_path)
            if output_path:
                messagebox.showinfo("Decrypted", f"File decrypted to:\n{output_path}")
                log_action(f"Decrypted file: {file_path}", username)
            else:
                messagebox.showerror("Error", f"Decryption failed:\n{msg}")
                log_action(f"Failed to decrypt file: {file_path}", username)

    tk.Button(window, text="Encrypt File", command=encrypt_action, width=30).pack(pady=20)
    tk.Button(window, text="Decrypt File", command=decrypt_action, width=30).pack(pady=10)
    
    window.mainloop()

# === Login/Register Window ===
root = tk.Tk()
root.title("Secure File Transfer - Login")
root.geometry("300x250")
root.resizable(False, False)

tk.Label(root, text="Username:").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password:").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack()

def login():
    username = entry_username.get()
    password = entry_password.get()
    if authenticate_user(username, password):
        messagebox.showinfo("Success", "Login successful!")
        log_action("Logged in", username)
        root.destroy()
        open_file_window(username)
    else:
        messagebox.showerror("Error", "Invalid username or password.")

def register():
    username = entry_username.get()
    password = entry_password.get()
    success, message = register_user(username, password)
    if success:
        messagebox.showinfo("Success", message)
        log_action("Registered new user", username)
    else:
        messagebox.showerror("Error", message)

tk.Button(root, text="Login", command=login).pack(pady=10)
tk.Button(root, text="Register", command=register).pack()

root.mainloop()
