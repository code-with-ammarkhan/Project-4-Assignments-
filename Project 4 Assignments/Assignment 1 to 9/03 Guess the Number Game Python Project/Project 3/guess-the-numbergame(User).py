def guess_user_number():
    low = 1
    high = 100
    feedback = ''
    print("Socho ek number 1 se 100 ke beech. Computer usay guess karega.")

    while feedback != 'sahi':
        if low != high:
            guess = (low + high) // 2
        else:
            guess = low

        print(f"Computer ka guess: {guess}")
        feedback = input("Yeh guess 'bara', 'chhota', ya 'sahi' hai? ")

        if feedback == 'bara':
            high = guess - 1
        elif feedback == 'chhota':
            low = guess + 1

    print(f"Computer ne tumhara number guess kar liya: {guess} 🎉")

guess_user_number()
