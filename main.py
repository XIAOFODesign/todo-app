import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("简易待办事项管理器")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # 设置样式
        self.style = ttk.Style()
        self.style.configure("TButton", font=('微软雅黑', 10))
        self.style.configure("TLabel", font=('微软雅黑', 12))
        self.style.configure("Header.TLabel", font=('微软雅黑', 14, 'bold'))

        # 创建UI组件
        self.create_widgets()

        # 加载任务数据
        self.task_file = os.path.join(os.path.dirname(__file__), 'tasks.json')
        self.load_tasks()

    def create_widgets(self):
        # 标题
        header_frame = ttk.Frame(self.root)
        header_frame.pack(pady=10, fill=tk.X, padx=20)

        ttk.Label(header_frame, text="待办事项列表", style="Header.TLabel").pack(anchor=tk.W)

        # 任务列表框
        list_frame = ttk.Frame(self.root)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

        self.task_listbox = tk.Listbox(list_frame, font=('微软雅黑', 11), selectbackground='#a6a6a6', selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)

        # 按钮区域
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill=tk.X, padx=20, pady=10)

        ttk.Button(button_frame, text="添加任务", command=self.add_task).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="删除任务", command=self.delete_task).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="清空列表", command=self.clear_tasks).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="保存任务", command=self.save_tasks).pack(side=tk.RIGHT, padx=5)

    def add_task(self):
        task = simpledialog.askstring("添加任务", "请输入新任务:", parent=self.root)
        if task and task.strip():
            self.task_listbox.insert(tk.END, task.strip())
            messagebox.showinfo("成功", "任务已添加!")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            messagebox.showinfo("成功", "任务已删除!")
        except IndexError:
            messagebox.showwarning("警告", "请先选择要删除的任务!")

    def clear_tasks(self):
        if self.task_listbox.size() > 0:
            confirm = messagebox.askyesno("确认", "确定要清空所有任务吗?")
            if confirm:
                self.task_listbox.delete(0, tk.END)
                messagebox.showinfo("成功", "所有任务已清空!")
        else:
            messagebox.showinfo("提示", "任务列表已为空!")

    def save_tasks(self):
        tasks = [self.task_listbox.get(i) for i in range(self.task_listbox.size())]
        try:
            with open(self.task_file, 'w', encoding='utf-8') as f:
                json.dump(tasks, f, ensure_ascii=False, indent=2)
            messagebox.showinfo("成功", f"任务已保存到 {self.task_file}")
        except Exception as e:
            messagebox.showerror("错误", f"保存失败: {str(e)}")

    def load_tasks(self):
        if os.path.exists(self.task_file):
            try:
                with open(self.task_file, 'r', encoding='utf-8') as f:
                    tasks = json.load(f)
                    for task in tasks:
                        self.task_listbox.insert(tk.END, task)
            except Exception as e:
                messagebox.showerror("错误", f"加载失败: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()