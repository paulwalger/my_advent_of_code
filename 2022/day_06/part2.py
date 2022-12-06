def main():
    with open("input.txt", "r") as input_file:
        datastream = input_file.readline().strip()
        for idx in range(len(datastream) - 14):
            if len(set(datastream[idx : idx + 14])) == 14:
                print("detected: ", idx + 14)
                break


if __name__ == "__main__":
    main()
