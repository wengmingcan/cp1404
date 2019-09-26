"""
CP1404/CP5632 Practical

"""
import shutil
import os


def version_1():

    print("Starting directory is: {}".format(os.getcwd()))


    os.chdir('FilesToSort')

    try:
        os.mkdir('doc')
        os.mkdir('xls')
        os.mkdir('png')
        os.mkdir('txt')
        os.mkdir('docx')
        os.mkdir('xlsx')
        os.mkdir('jpg')
        os.mkdir('gif')
    except FileExistsError:
        pass


    for filename in os.listdir('.'):
        print(filename)

        if os.path.isdir(filename):
            continue


        if ".docx" in filename:
            shutil.move(filename, 'docx/' + filename)
        elif ".xlsx" in filename:
            shutil.move(filename, 'xlsx/' + filename)
        elif ".png" in filename:
            shutil.move(filename, 'png/' + filename)
        elif ".txt" in filename:
            shutil.move(filename, 'txt/' + filename)
        elif ".doc" in filename:
            shutil.move(filename, 'doc/' + filename)
        elif ".xls" in filename:
            shutil.move(filename, 'xls/' + filename)
        elif "jpg" in filename:
            shutil.move(filename, 'jpg/' + filename)
        elif ".gif" in filename:
            shutil.move(filename, 'gif/' + filename)



def version_2():

    print("Starting directory is: {}".format(os.getcwd()))


    os.chdir('FilesToSort')

    try:
        os.mkdir('Images')
        os.mkdir('Spreadsheets')
        os.mkdir('Documents')
    except FileExistsError:
        pass


    for filename in os.listdir('.'):

        if os.path.isdir(filename):
            continue


        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            shutil.move(filename, 'Images/' + filename)
        elif filename.lower().endswith(('.doc', '.docx', '.txt')):
            shutil.move(filename, 'Documents/' + filename)
        elif filename.lower().endswith(('.xls', '.xlsx')):
            shutil.move(filename, 'Spreadsheets/' + filename)


version_2()
