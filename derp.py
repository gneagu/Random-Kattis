from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path

def createWindow():
    window = Tk()
    window.title("Test Application v0.0.1")
    window.geometry('300x150')

    filePath = ""
    buttonState = []

    def saveButtonStates():
        #Save state of buttons, then disable them.
        global buttonState
        buttonState = []
        buttonState += [loadPro["state"]] + [testPro["state"]] + [loadCustomTest["state"]] + [createTest["state"]]


    def disableRootWindow():
        createTest.config(state = "disabled")
        loadCustomTest.config(state = "disabled")
        loadPro.config(state = "disabled")
        testPro.config(state = "disabled")

    def enaleRootWindow(buttonStates):
        createTest.config(state = buttonStates[3])
        loadCustomTest.config(state = buttonStates[2])
        loadPro.config(state = buttonStates[0])
        testPro.config(state = buttonStates[1])

    def loadProgram():
        global filePath
        disableRootWindow()
        loadPro.config(state = "normal")

        try:
            fileLocation = filedialog.askopenfilenames()
            nameList = str(fileLocation[0]).split("/")
            fileName = nameList[-1]

            lbl3.configure(text = fileName)

            fileNameLength = len(fileName)
            path = str(fileLocation[0])
            path = path[:-fileNameLength]

            tempTestFileName = fileName.split(".")

            testFilePath = Path(path + tempTestFileName[0] + "_test.py")
            filePath = testFilePath

            print(testFilePath)
            loadCustomTest.config(state = "normal")

            if testFilePath.is_file():
                print("Test File, {}, Exists".format(tempTestFileName[0] + "_test.py"))
                lbl4.config(text = "Yes ({})".format(tempTestFileName[0] + "_test.py"))
                testPro.config(state = "normal")
            else:
                print("Test File, {}, Does Not Exist".format(tempTestFileName[0] + "_test.py"))
                createTest.config(state = "normal")
                # loadCustomTest.config(state = "normal")
        except:
            pass

    def createTest():
        print("Type in the contents of the test file.")

        def getInput():
            global filePath
            global buttonState
            lines = textBox.get("1.0", "end-1c")
            print(lines)
            childWindow.destroy()
            enaleRootWindow(buttonState)
            testPro.config(state = "normal")

            print(filePath)

            with open("/home/cmput274/Random-Kattis/train_test_test.txt", mode = 'w') as the_file:
                for i in lines:
                    the_file.write(i)


        def disableEvent():
            global buttonState
            enaleRootWindow(buttonState)
            childWindow.destroy()

        saveButtonStates()
        disableRootWindow()

        childWindow = Tk()
        childWindow.title("Insert Test Cases")
        childWindow.geometry('400x380')

        # loadCustomTest.grid(column=1, row=1)

        textBox = Text(childWindow, height = 20 , width = 50)
        textBox.pack()
        textBox.insert(END, "Insert Test Cases Here. \nPreceed test cases with 'Test Case:' \n \
        and \nPreceed Answers with 'Answer:'")

        destroyButton = Button(childWindow, text = "Submit Text", command = getInput, width = 15)
        destroyButton.pack()

        childWindow.protocol("WM_DELETE_WINDOW", disableEvent)

        # print(buttonState)

    lbl1 = Label(window, text="Program Name: ", width = 15)
    lbl1.grid(column=0, row=2)

    lbl2 = Label(window, text="Test File Exists:", width = 15)
    lbl2.grid(column=0, row=3)

    lbl3 = Label(window, text="None", width = 15)
    lbl3.grid(column=1, row=2)

    lbl4 = Label(window, text="No", width = 15)
    lbl4.grid(column=1, row=3)

    lbl5 = Label(window, text="Using Custom Test:", width = 15)
    lbl5.grid(column=0, row=4)

    lbl6 = Label(window, text="No", width = 15)
    lbl6.grid(column=1, row=4)

    loadPro = Button(window, text = "Load Program\n", command = loadProgram, width = 15)
    loadPro.grid(column=0, row=0)

    testPro = Button(window, text = "Test a\nProgram File", command = None, width = 15, state = DISABLED)
    testPro.grid(column=0, row=1)

    loadCustomTest = Button(window, text = "Load a Custom\nTest File", command = None, width = 15, state = DISABLED)
    loadCustomTest.grid(column=1, row=1)

    createTest = Button(window, text = "Create a\nTest File", command = createTest, width = 15, state = DISABLED)
    createTest.grid(column=1, row=0)

    window.mainloop()

createWindow()
