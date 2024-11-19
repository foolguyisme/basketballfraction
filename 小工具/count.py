import tkinter as tk
from tkinter import messagebox

class BasketballScoreboard:
    def __init__(self, root):
        self.root = root
        self.root.title("籃球計分")
        
        self.team1_name = tk.StringVar()
        self.team2_name = tk.StringVar()
        self.team1_score = 0
        self.team2_score = 0
        self.win_score = tk.IntVar(value=21)  # 預設贏分

        # 輸入框與標籤
        tk.Label(root, text="隊伍 1 名稱:").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.team1_name).grid(row=0, column=1)

        tk.Label(root, text="隊伍 2 名稱:").grid(row=1, column=0)
        tk.Entry(root, textvariable=self.team2_name).grid(row=1, column=1)

        tk.Label(root, text="設定贏分:").grid(row=2, column=0)
        tk.Entry(root, textvariable=self.win_score).grid(row=2, column=1)

        # 顯示分數
        self.team1_score_label = tk.Label(root, text="0", font=("Arial", 24))
        self.team1_score_label.grid(row=3, column=0)
        self.team2_score_label = tk.Label(root, text="0", font=("Arial", 24))
        self.team2_score_label.grid(row=3, column=1)

        # 加分按鈕
        self.team1_button = tk.Button(root, text="隊伍 1 加分", command=self.add_score_team1)
        self.team1_button.grid(row=4, column=0)
        self.team2_button = tk.Button(root, text="隊伍 2 加分", command=self.add_score_team2)
        self.team2_button.grid(row=4, column=1)

        # 重製按鈕
        self.reset_score_button = tk.Button(root, text="重製分數", command=self.reset_score)
        self.reset_score_button.grid(row=5, column=0)

        self.reset_all_button = tk.Button(root, text="重製設定", command=self.reset_all)
        self.reset_all_button.grid(row=5, column=1)

    # 隊伍1加分
    def add_score_team1(self):
        self.team1_score += 1
        self.team1_score_label.config(text=str(self.team1_score))
        self.check_winner()

    # 隊伍2加分
    def add_score_team2(self):
        self.team2_score += 1
        self.team2_score_label.config(text=str(self.team2_score))
        self.check_winner()

    # 檢查是否有隊伍贏
    def check_winner(self):
        if self.team1_score >= self.win_score.get():
            messagebox.showinfo("比賽結束", f"{self.team1_name.get()} 贏了!")
            if messagebox.askyesno("重製", "需要重製分數嗎?"):
                self.reset_score()
        elif self.team2_score >= self.win_score.get():
            messagebox.showinfo("比賽結束", f"{self.team2_name.get()} 贏了!")
            if messagebox.askyesno("重製", "需要重製分數嗎?"):
                self.reset_score()

    # 重製分數
    def reset_score(self):
        self.team1_score = 0
        self.team2_score = 0
        self.team1_score_label.config(text="0")
        self.team2_score_label.config(text="0")

    # 重製所有設定
    def reset_all(self):
        self.reset_score()
        self.team1_name.set("")
        self.team2_name.set("")
        self.win_score.set(21)

# 主程式
if __name__ == "__main__":
    root = tk.Tk()
    app = BasketballScoreboard(root)
    root.mainloop()
