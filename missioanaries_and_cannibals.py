boat = "right"
miss_on_left = 0
cann_on_left = 0
miss_on_right = 3
cann_on_right = 3

print(f"Total number of missionaries and cannibals are : M=3, C=3")
print(f"The letter B shows the side of the boat.")
print(f"M={miss_on_left}  C={cann_on_left} |--------------B| M={miss_on_right}   C={cann_on_right}")

while True:
    try:
        input_str = input("Enter the number of missionaries and cannibals (e.g., '2 1') or type 'exit' to exit the game: ")
        if input_str.lower() == "exit":
            print("Bye. Game Over!")
            break
        
        # Split the input string and convert to integers
        missionaries, cannibals = map(int, input_str.split())

        if boat == "right":
            if missionaries + cannibals < 1 or missionaries + cannibals > 2:
                print("Invalid move: The boat can carry 1 or 2 people.")
                continue

            if missionaries > miss_on_right or cannibals > cann_on_right:
                print("Invalid move: Not enough missionaries or cannibals on the right side.")
                continue

            miss_on_left += missionaries
            cann_on_left += cannibals
            miss_on_right -= missionaries
            cann_on_right -= cannibals
            boat = "left"
        else:
            if missionaries + cannibals < 1 or missionaries + cannibals > 2:
                print("Invalid move: The boat can carry 1 or 2 people.")
                continue

            if missionaries > miss_on_left or cannibals > cann_on_left:
                print("Invalid move: Not enough missionaries or cannibals on the left side.")
                continue

            miss_on_left -= missionaries
            cann_on_left -= cannibals
            miss_on_right += missionaries
            cann_on_right += cannibals
            boat = "right"

        print(f"M={miss_on_left}  C={cann_on_left} |{'B' if boat == 'left' else ''}-------------{'B' if boat == 'right' else ''}| M={miss_on_right}  C={cann_on_right}")

        if (miss_on_left > 0 and miss_on_left < cann_on_left) or (miss_on_right > 0 and miss_on_right < cann_on_right):
            print("You lose: One of the missionaries got eaten by cannibals.")
            break

        if miss_on_left == 3 and cann_on_left == 3:
            print("You win!")
            break
    except ValueError:
        print("Invalid input: Please enter the number of missionaries and cannibals as two integers separated by a space.")
