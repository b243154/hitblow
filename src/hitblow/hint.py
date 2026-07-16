# hint.py

def hint(secret, guess):
    """
    入力された数字の和と正解の数字の和を比較してヒントを返す
    """

    # 数字の和を計算
    secret_sum = sum(int(x) for x in secret)
    guess_sum = sum(int(x) for x in guess)

    if guess_sum < secret_sum:
        return "ヒント：入力した数字の和は正解より小さいです。"
    elif guess_sum > secret_sum:
        return "ヒント：入力した数字の和は正解より大きいです。"
    else:
        return "ヒント：入力した数字の和は正解と同じです。"