"""
CP1404/ Practical

"""
import os


def main():

    print("Starting directory is: {}".format(os.getcwd()))


    os.chdir('Lyrics/Christmas')


    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.'))
          for filename in os.listdir('.'):

        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {:<45} to {:<45}".format(filename, new_name))


        os.rename(filename, new_name)


def get_fixed_filename(filename):

    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")

    """ This only replaces it for name with a space
    for eg,  "This is Practical 9.txt"   goes to      "This_is_Practical_9.txt"
    eg,      "ThisIsPractical9.txt"       goes to      "ThisIsPractical9.txt"
    """
    return new_name


main()
