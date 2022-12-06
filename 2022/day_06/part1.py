def main():
    with open("input.txt", "r") as input_file:
        datastream = input_file.readline().strip()
        for idx in range(len(datastream) - 4):
            if len(set(datastream[idx : idx + 4])) == 4:
                print("detected: ", idx + 4)
                break


if __name__ == "__main__":
    main()
