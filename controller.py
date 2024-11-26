import tuke_openlab
import sys

# openlab controller
openlab = tuke_openlab.Controller(tuke_openlab.production_env())

# prank screens
screens = ["https://pranx.com/hacker/", "https://pranx.com/matrix-code-rain/", "https://pranx.com/fake-virus/"]


def reset_to_default():
    try:
        openlab.screens.panel_2x2.set_default()
        for i in range(1, 6):
            openlab.screens.vertical.get(i).set_default()

    except Exception as e:
        print(f"Error resetting screens: {e}")


def set_screens(url_index):
    try:
        openlab.screens.panel_2x2.set_url(screens[url_index])
        for i in range(1, 6):
            openlab.screens.vertical.get(i).set_url(screens[url_index])
        print(f"Screens set to: {screens[url_index]}")
    except IndexError:
        print("Invalid screen index. Please choose a value between 1 and 3.")

    except Exception as e:
        print(f"Error setting screens: {e}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python controller.py =0 to reset | 1-3 for prank screens")
    elif sys.argv[1] == "0":
        reset_to_default()
    else:
        try:
            set_screens(int(sys.argv[1]) - 1)
        except ValueError:
            print("Invalid argument. Please provide an integer.")


if __name__ == "__main__":
    main()
