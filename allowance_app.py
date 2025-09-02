import json
import os

DATA_FILE = 'allowance_data.json'

class AllowanceApp:
    def __init__(self):
        self.balance = 0
        self.goal = None
        self.load()

    def load(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.balance = data.get('balance', 0)
                self.goal = data.get('goal')

    def save(self):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump({'balance': self.balance, 'goal': self.goal}, f)

    def add(self, amount):
        self.balance += amount
        self.save()
        print(f'{amount}円を追加しました。現在の残高: {self.balance}円')

    def spend(self, amount):
        if amount > self.balance:
            print('残高が足りません。')
            return
        self.balance -= amount
        self.save()
        print(f'{amount}円を使いました。現在の残高: {self.balance}円')

    def show(self):
        print(f'現在の残高: {self.balance}円')
        if self.goal is not None:
            print(f'目標金額: {self.goal}円')
            if self.balance >= self.goal:
                print('おめでとう! 目標を達成しました!')
            else:
                print(f'目標まであと {self.goal - self.balance}円')

    def set_goal(self, amount):
        self.goal = amount
        self.save()
        print(f'目標金額を{self.goal}円に設定しました。')

    def run(self):
        print('--- お小遣い管理アプリ ---')
        while True:
            cmd = input('add(追加)/spend(使う)/show(確認)/goal(目標設定)/exit: ').strip().lower()
            if cmd == 'add':
                amount = int(input('追加する金額: '))
                self.add(amount)
            elif cmd == 'spend':
                amount = int(input('使った金額: '))
                self.spend(amount)
            elif cmd == 'show':
                self.show()
            elif cmd == 'goal':
                amount = int(input('目標金額: '))
                self.set_goal(amount)
            elif cmd == 'exit':
                print('終了します。')
                break
            else:
                print('不明なコマンドです。')

if __name__ == '__main__':
    app = AllowanceApp()
    app.run()
