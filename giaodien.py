import tkinter as tk
#tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý sinh viên")
root.geometry("400x300")

#thêm nhãn văn bản
label = tk.Label(root, text="Hello các tình yêu", font=("Arial", 18))
label.pack(pady=20)

#thêm nút bấm
def on_button_click():
    label.config(text="Nút đã được bấm!")
button = tk.Button(root, text="Bấm vào!", command=on_button_click)
button.pack(pady=10)

#chạy vòng lập chính
root.mainloop()