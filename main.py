from selectoption import FromImage, FromVideo


class Main:
    def __init__(self):
        self.img = FromImage()
        self.vid = FromVideo()

    def main(self):
        in1 = input("Press 1 for Image or 2 for Video\n")
        if int(in1) == 1:
            self.img.image()
        elif int(in1) == 2:
            self.vid.video()
        else:
            print("Enter Valid Choice")


if __name__ == "__main__":
    runProg = Main()
    runProg.main()
