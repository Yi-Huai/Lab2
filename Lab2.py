def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    # 1. Read numbers entered by the user
    user_input = input()

    # 2. Split the string into a list of strings using ',' as separator
    str_list = user_input.split(',')

    # 3. Convert the list of strings to a list of floats
    float_list = []
    for num_str in str_list:
        float_list.append(float(num_str))
    return float_list
    # 4. Return the list of floats
    


def main():
    print("ET0735 (DevOps for AIoT) - Lab2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)


if __name__ == "__main__":
    main()

