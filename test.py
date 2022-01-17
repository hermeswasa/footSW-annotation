import tkinter as tk

root = tk.Tk()
root.withdraw()

window = tk.Toplevel(root)
window.title('Hello Window')
window.geometry('%dx%d' % (400, 400))
window.protocol('WM_DELETE_WINDOW', root.destroy)

# ここでWidgetの初期化、配置

root.mainloop()