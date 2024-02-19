def outer_function():
    outer_variable = 10

    def inner_function():
        nonlocal outer_variable
        inner_variable += outer_variable

        print(f"Inner function: {inner_variable}")
        print(f"Inner function (updated): {outer_variable}")

    inner_function()
    print(f"Outer function: {outer_variable}")

# Run the outer function
outer_function()
