from tkinter import *
from tkinter import filedialog
import os
from os import walk
import cv2


class MymenuDemo:
    def __init__(self, root):
        # create a menu bar
        self.menubar = Menu(root)

        # attach the menubar to the root window
        root.config(menu=self.menubar)

        # create filemenu
        self.filemenu = Menu(root, tearoff=0)

        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.filemenu.add_command(label="New", command=self.donothing)
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_files)

        # add a horinzontal line as separator
        self.filemenu.add_separator()

        # create another menu item below the seoarator
        self.filemenu.add_command(label="Exit", command=root.destroy)

        # creating crop drop down menu
        self.Cropmenu = Menu(root, tearoff=0)
        self.menubar.add_cascade(label="Crop", menu=self.Cropmenu)
        self.Cropmenu.add_command(label="Multiple Images", command=self.Multiple_images)
        self.Cropmenu.add_command(label="Single Images", command=self.donothing)
        # self.Cropmenu.add.command(label="Multiple select",command=self.Multiple)

        # creating pdfconverter option in the menubar

        self.ConvertToPDF = Menu(root, tearoff=0)
        self.menubar.add_cascade(label="pdfConverter", menu=self.ConvertToPDF)
        self.ConvertToPDF.add_command(label="Convert to PDF", command=self.donothing)

        # create edit menu
        self.editmenu = Menu(root, tearoff=0)
        # creating drop down menu of editmenu
        self.editmenu.add_command(label="Cut", command=self.donothing)
        self.editmenu.add_command(label="Copy", command=self.donothing)
        self.editmenu.add_command(label="Paste", command=self.donothing)
        # add the edit menu with a name 'Edit' to the menubar
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

    # creating donothing function method
    def donothing(self):
        pass

    # method for opening a file and display its contents in a text box
    def open_file(self):
        # open a file dialog box and acceot the filename
        self.filename = filedialog.askopenfilename(parent=root, title='Select a file',
                                                   filetypes=(("Python files,*.py"), ("All files", "*.*")))

        # if cancel button is not clicked in the dialog box
        if self.filename != None:
            # open the file inthe read mode
            f = open(self.filename, 'r')

            # read the contents of the
            contents = f.read()
            # create a Text Box and it to root window
            self.t = Text(root, width=80, height=20, wrap=WORD)
            self.t.pack()

            # insert the file contents in the text box

            self.t.insert(1.0, contents)

            # close the files

            f.close()

    # fucntion for save files
    def save_files(self):

        # Open a file dialog box and type a file name
        self.filename = filedialog.asksaveasfilename(parent=root, defaultextension=".txt")

        # if cacel button is not clicked in the dialog box
        if self.filename != None:
            # open the file in the read mode
            f = open("self.filename", 'w')

            # get the contents of the text box
            contents = str(self.t.get(1.0, END))

            # store trhe contents into the files
            f.write(contents)

            # close the file
            f.close()

    def Multiple_images(self):
        self.folder_selected = filedialog.askdirectory(title='Please select a directory')

        def input_dir():
            return [os.path.join(self.folder_selected, f) for f in os.listdir(self.folder_selected) if f.endswith('.jpg')]

        image = input_dir()

        self.folder_save = filedialog.askdirectory(title='Please select save file directory')

        readimg = []

        for images in image:
            readimg.append(cv2.imread(images, cv2.IMREAD_UNCHANGED))
        num = 0
        for img in readimg:
            height, width, channels = img.shape
            resized_image = cv2.resize(img, (911, 1280))
            crop_img = resized_image[240:1280, 0:890]
            cv2.imwrite(os.path.join(self.folder_save, str(num) + ".jpg"), crop_img)
            num += 1


# program closing process


# create a root window
root = Tk()

# title for root window
root.title("EYR")

# create object to ourr class
obj = MymenuDemo(root)

# Define the size of the root window
root.geometry('600x350')

# Handle any events
root.mainloop()
