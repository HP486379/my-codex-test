import random

CHOICES = ["グー", "チョキ", "パー"]


def judge(player: str, computer: str) -> str:
    """じゃんけんの勝敗を判定する."""
    if player == computer:
        return "あいこ"
    elif (player == "グー" and computer == "チョキ") or \
         (player == "チョキ" and computer == "パー") or \
         (player == "パー" and computer == "グー"):
        return "勝ち"
    else:
        return "負け"


def main() -> None:
    """ゲームのメイン処理."""
    player = input("手を選んでください (グー/チョキ/パー): ")
    if player not in CHOICES:
        print("無効な入力です。グー、チョキ、パーから選んでください。")
        return

    computer = random.choice(CHOICES)
    print(f"コンピューターの手: {computer}")
    result = judge(player, computer)
    print(f"結果: {result}")


if __name__ == "__main__":
    main()
