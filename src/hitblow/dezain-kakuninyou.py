def show_stage(stage, monster, digits, hp):
    print("=" * 40)
    print(f"          STAGE {stage}")
    print("=" * 40)
    print()
    print(f"{monster} が あらわれた！")
    print()
    print(f"HP : {'♥' * hp} ({hp})")
    print(f"数字 : {digits}桁")
    print()
    print("1. 戦う")
    print("2. 呪文")
    print("3. やめる")
    print("=" * 40)


# デザイン確認用
stage = 1
monster = "スライム"
digits = 3
hp = 5

while hp > 0:
    show_stage(stage, monster, digits, hp)

    command = input("> ")

    if command == "1":
        guess = input(f"{digits}桁の数字を入力してください > ")

        # 本当はここでHit&Blowの判定
        print(f"{guess} を攻撃！")

        hp -= 1

    elif command == "2":
        print("呪文を唱えた！")
        print("ヒント：○○")
        hp -= 1

    elif command == "3":
        print("ゲームを終了します")
        break

    else:
        print("1～3を入力してください")

    print()

if hp == 0:
    print("=" * 40)
    print("HPがなくなった…")
    print("GAME OVER")
    print("=" * 40)


    