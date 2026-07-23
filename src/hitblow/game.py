from .core import make_secret, judge
from .hint import hint  # 呪文で使うヒント関数


def show_stage(stage, monster, digits, hp, ascii_art):
    print("=" * 40)
    print(f"         STAGE {stage}")
    print("=" * 40)
    if ascii_art:
        print(ascii_art)
    print(f"{monster} が あらわれた！")
    print()
    print(f"HP : {'♥' * hp} ({hp})")
    print(f"数字 : {digits}桁")
    print()
    print("1. 戦う (数字を予想)")
    print("2. 呪文 (ヒントを見る)")
    print("3. にげる (やめる)")
    print("=" * 40)


def play(stage, digits, monster, hp, ascii_art):
    secret = make_secret(digits)

    while hp > 0:
        show_stage(stage, monster, digits, hp, ascii_art)
        command = input("> ").strip()

        if command == "1":
            guess = input(f"{digits}桁の数字を入力してください > ").strip()

            # 入力チェック
            if len(guess) != digits or not guess.isdigit():
                print(f"【ミス！】{digits}桁の数字じゃないと攻撃できない！")
                continue

            # 攻撃（Hit & Blow 判定）
            hit, blow = judge(secret, guess)
            print(f"【攻撃！】 {guess} を放った！ => Hit={hit} Blow={blow}")

            if hit == digits:
                print(f"やった！ {monster} をたおした！")
                return True
            else:
                print(f"{monster} の反撃！ HPが1減った。")
                hp -= 1

        elif command == "2":
            print("【呪文！】 魔法でヒントを読み取った！")
            # 呪文の場合は guess がないので空文字などを渡すか、仕様に合わせて調整
            print(f"ヒント: {hint(secret, '')}")
            print("体力を消耗した... HPが1減った。")
            hp -= 1

        elif command == "3":
            print("勇者は逃げ出した...")
            return False

        else:
            print("1～3を入力してください")

        print()  # 空行を入れて見やすくする

    # HPが0になった場合
    print("=" * 40)
    print("HPがなくなった… GAME OVER")
    print(f"正解は {secret} だった...")
    print("=" * 40)
    return False


def campaign_mode():
    print("\n★★★ 裏モード「RPG編」スタート！ ★★★\n")

    # スライムのアスキーアート
    slime_art = "     ／￣＼\n   ／・ω・＼\n   ＼＿＿／"

    # ステージ設定（ステージ数, 桁数, モンスター名, HP, アート）
    stages = [
        {"stage": 1, "digits": 3, "monster": "スライム", "hp": 8, "art": slime_art},
        {"stage": 2, "digits": 4, "monster": "ゴーレム", "hp": 15, "art": ""},
        {"stage": 3, "digits": 5, "monster": "魔王", "hp": 20, "art": ""},
    ]

    for s in stages:
        # ステージ実行
        is_clear = play(s["stage"], s["digits"], s["monster"], s["hp"], s["art"])

        if not is_clear:
            print("世界は闇に包まれた...")
            return  # 負けたらそこで終了

        if s["stage"] < len(stages):
            print("\n>> 次のステージへ進む...\n")

    print("\n==================================")
    print("完全クリア！世界に平和が戻った！")
    print("==================================")
