def get_coords(xs: str, ys: str) -> None:
    i = 0
    # Outer while loop to iterate over each character in xs
    while i < len(xs):
        j = 0
        # Inner while loop to iterate over each character in ys
        while j < len(ys):
            print(f"({xs[i]}, {ys[j]})")
            j += 1
        i += 1
    return None
