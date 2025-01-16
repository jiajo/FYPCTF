import base64

class BufferOverflowChallenge:
    def __init__(self):
        self._x = bytes([119, 97, 116, 101, 114, 95, 111, 118, 101, 114, 102, 108, 111, 119, 95, 49, 50, 51])
        self.buffer = [""] * 25

    def input_data(self, data):
        if len(data) > len(self.buffer):
            print("\nBuffer overflow detected!")
            flag = "CTF{" + self._x.decode() + "}"
            print(f"Congratulations! Here's the flag: {flag}")
            return True
        else:
            print("Data stored successfully.")
            return False

if __name__ == "__main__":
    print("Welcome to the Buffer Overflow Challenge!")
    print("Overflow the buffer to reveal the flag!")
    challenge = BufferOverflowChallenge()

    while True:
        user_input = input("\nEnter your data: ")
        if challenge.input_data(user_input):
            break
