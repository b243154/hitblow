"""コマンドの入口。第3回で `hitblow` コマンドがここ（main）を呼ぶ。"""

from .game import play


def main():
    # 1. ユーザーに桁数を入力してもらう
    user_input = input("何桁で遊びますか？（そのままEnterで3桁）> ").strip()

    # 2. 数字が正しく入力されたらその桁数で、そうでなければデフォルト（3桁）で開始
    if user_input.isdigit() and int(user_input) > 0:
        digits = int(user_input)
        play(digits=digits)  # 指定された桁数を渡す
    else:
        play()  # デフォルト（3桁）で起動