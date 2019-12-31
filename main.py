import warnings
from utils.fromImage import fromImage
from utils.fromVideo import fromVideo

def main():
    in1 = input("1)Image or 2)Video\n")
    if int(in1) == 1:
        fromImage.image()
    elif int(in1) == 2:
        fromVideo.video()
    else:
        print("Enter Valid Choice")


if __name__ == "__main__":
    main()
