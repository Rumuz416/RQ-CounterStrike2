import tkinter as tk
import subprocess
import threading
import sys

class PS_Terminal:
    def __init__(self, root):
        self.root = root
        self.root.title("Python PowerShell Terminal")
        self.root.geometry("900x600")

        # UI Tasarımı
        self.text_area = tk.Text(root, bg="#012456", fg="white", insertbackground="white", 
                                 font=("Cascadia Code", 11), padx=10, pady=10)
        self.text_area.pack(expand=True, fill='both')

        self.entry = tk.Entry(root, bg="#012456", fg="white", insertbackground="white", 
                              font=("Cascadia Code", 11), borderwidth=0, highlightthickness=1)
        self.entry.pack(fill='x', side="bottom", padx=5, pady=5)
        self.entry.bind("<Return>", self.send_to_ps)

        # Arka planda PowerShell sürecini başlat
        self.ps_process = subprocess.Popen(
            ["powershell.exe", "-NoLogo", "-Command", "-"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )

        # Çıktıları okumak için ayrı bir thread (iş parçacığı) başlat
        threading.Thread(target=self.read_output, daemon=True).start()
        
        self.text_area.insert(tk.END, "PowerShell oturumu hazır...\n")
        self.entry.focus_set()

    def send_to_ps(self, event):
        cmd = self.entry.get()
        self.entry.delete(0, tk.END)
        self.text_area.insert(tk.END, f"PS > {cmd}\n", "cmd_style")
        
        # Komutu PowerShell'e gönder
        self.ps_process.stdin.write(cmd + "\n")
        self.ps_process.stdin.flush()

    def read_output(self):
        while True:
            line = self.ps_process.stdout.readline()
            if line:
                self.text_area.insert(tk.END, line)
                self.text_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    # Komut yazılan satırı renklendirmek için tag ekle
    app = PS_Terminal(root)
    root.mainloop()