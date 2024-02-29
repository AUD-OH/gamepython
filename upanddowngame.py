import random
def play_game():
    valid_inputs = ['가위', '바위', '보']
    user_win_count = 0
    computer_win_count = 0
    tie_count = 0

    while True:
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ").lower()
        if user_choice not in valid_inputs:
            print("유효한 입력이 아닙니다.")
            continue

        computer_choice = random.choice(valid_inputs)
        print(f"사용자: {user_choice}, 컴퓨터: {computer_choice}")

        if user_choice == computer_choice:
            print("무승부!")
            tie_count += 1
        elif (user_choice == '가위' and computer_choice == '보') or \
                (user_choice == '바위' and computer_choice == '가위') or \
                (user_choice == '보' and computer_choice == '바위'):
            print("사용자 승리!")
            user_win_count += 1
        else:
            print("컴퓨터 승리!")
            computer_win_count += 1

        play_again = input("다시 하시겠습니까? (y/n): ")
        if play_again.lower() != 'y':
            print("게임을 종료합니다.")
            break

    print(f"승: {user_win_count} 패: {computer_win_count} 무승부: {tie_count}")


if __name__ == "__main__":
    play_game()
