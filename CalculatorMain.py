from tkinter import *
import re

# Calculator Properties
isCalculatorClear = True
typeOfCalculator = "Standard"
calculatorInputViewTop = 0
calculatorInputViewBottom = "{:,}".format(0)
calculatorStatement = [] # Math sentence

# Calculator Class
class mainCalculator:
    pass


# Button
class generalButtons:
    pass


#########################################################
# Center Window
def centerWindow(width, height, window):
    windowWidth = width
    windowHeight = height

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    screenX = (screenWidth / 2) - (windowWidth / 2)
    screenY = (screenHeight / 2) - (windowHeight / 2)

    window.geometry(f'{windowWidth}x{windowHeight}+{int(screenX)}+{int(screenY)}')

## Window ##
window = Tk()

# Window Properties
windowSizeX = 310
windowSizeY = 510
windowTitle = 'Calculator'
windowIcon = 'Images/calculatorLogo.png'
windowBackground = '#C2C2C2'

# Window UI
window.title(windowTitle)
window.resizable(False, False)
window.iconphoto(False, PhotoImage(file=windowIcon))
window.configure(background=windowBackground)
window.attributes('-alpha', 0.9)

# Functions Call
centerWindow(windowSizeX, windowSizeY, window)

#########################################################
# Calculator Properties
font = "Microsoft YaHei UI Light"
fontSize = 15
buttonOperationsColor = "#e6e6e6"
buttonNumbersColor = "#f2f2f2"
buttonSizeX = 73
buttonSizeY = 55

## Calculator UI ##

# Frame
calculatorFrame = Frame(window, background=windowBackground, width=windowSizeX, height=windowSizeY)
calculatorFrame.place(x=0, y=0)

# Label
typeOfCalculatorLabel = Label(calculatorFrame, text=typeOfCalculator, background=windowBackground,
                              font=(font + " Bold", fontSize))
typeOfCalculatorLabel.place(x=50, y=7)

calculatorInputViewBottomLabel = Label(calculatorFrame, text=str(calculatorInputViewBottom), background=windowBackground,
                                       font=(font + " Bold", fontSize + 20), anchor="e")
calculatorInputViewBottomLabel.place(x=10, y=70, width=280, height=60)

calculatorInputViewTopLabel = Label(calculatorFrame, text=str(calculatorInputViewTop), background=windowBackground,
                                    font=(font + " Bold", fontSize + 5), anchor="e")
calculatorInputViewTopLabel.place(x=10, y=35, width=280)

# Button
percentageButton = Button(calculatorFrame, text="%", background=buttonOperationsColor, font=(font, fontSize - 2),
                          anchor=CENTER, relief=FLAT)
percentageButton.place(x=5, y=160, width=buttonSizeX, height=buttonSizeY)

clearEntryButton = Button(calculatorFrame, text="CE", background=buttonOperationsColor, font=(font, fontSize - 2),
                          anchor=CENTER, relief=FLAT)
clearEntryButton.place(x=81, y=160, width=buttonSizeX, height=buttonSizeY)

clearButton = Button(calculatorFrame, text="C", background=buttonOperationsColor, font=(font, fontSize - 2),
                     anchor=CENTER, relief=FLAT)
clearButton.place(x=157, y=160, width=buttonSizeX, height=buttonSizeY)

removeOneNumberButton = Button(calculatorFrame, text="X", background=buttonOperationsColor, font=(font, fontSize - 2),
                               anchor=CENTER, relief=FLAT)
removeOneNumberButton.place(x=233, y=160, width=buttonSizeX, height=buttonSizeY)

oneDivideNumberButton = Button(calculatorFrame, text="¹⁄ₓ", background=buttonOperationsColor, font=(font, fontSize - 2),
                               anchor=CENTER, relief=FLAT)
oneDivideNumberButton.place(x=5, y=218, width=buttonSizeX, height=buttonSizeY)

squareNumberButton = Button(calculatorFrame, text="x²", background=buttonOperationsColor, font=(font, fontSize - 2),
                            anchor=CENTER, relief=FLAT)
squareNumberButton.place(x=81, y=218, width=buttonSizeX, height=buttonSizeY)

squareRootNumberButton = Button(calculatorFrame, text="2√x", background=buttonOperationsColor,
                                font=(font, fontSize - 2),
                                anchor=CENTER, relief=FLAT)
squareRootNumberButton.place(x=157, y=218, width=buttonSizeX, height=buttonSizeY)

divideButton = Button(calculatorFrame, text="÷", background=buttonOperationsColor, font=(font, fontSize + 5),
                      anchor=CENTER, relief=FLAT)
divideButton.place(x=233, y=218, width=buttonSizeX, height=buttonSizeY)

multiplyButton = Button(calculatorFrame, text="×", background=buttonOperationsColor, font=(font, fontSize + 5),
                        anchor=CENTER, relief=FLAT)
multiplyButton.place(x=233, y=276, width=buttonSizeX, height=buttonSizeY)

subtractButton = Button(calculatorFrame, text="−", background=buttonOperationsColor, font=(font, fontSize + 5),
                        anchor=CENTER, relief=FLAT)
subtractButton.place(x=233, y=334, width=buttonSizeX, height=buttonSizeY)

addButton = Button(calculatorFrame, text="+", background=buttonOperationsColor, font=(font, fontSize + 5),
                   anchor=CENTER, relief=FLAT)
addButton.place(x=233, y=392, width=buttonSizeX, height=buttonSizeY)

equalButton = Button(calculatorFrame, text="=", background="#74A5CB", font=(font, fontSize + 5),
                     anchor=CENTER, relief=FLAT)
equalButton.place(x=233, y=450, width=buttonSizeX, height=buttonSizeY)

numberSevenButton = Button(calculatorFrame, text="7", background=buttonNumbersColor,
                           font=(font + " Bold", fontSize - 1), anchor=CENTER, relief=FLAT)
numberSevenButton.place(x=5, y=276, width=buttonSizeX, height=buttonSizeY)

numberEightButton = Button(calculatorFrame, text="8", background=buttonNumbersColor,
                           font=(font + " Bold", fontSize - 1), anchor=CENTER, relief=FLAT)
numberEightButton.place(x=81, y=276, width=buttonSizeX, height=buttonSizeY)

numberNineButton = Button(calculatorFrame, text="9", background=buttonNumbersColor,
                          font=(font + " Bold", fontSize - 1), anchor=CENTER, relief=FLAT)
numberNineButton.place(x=157, y=276, width=buttonSizeX, height=buttonSizeY)

numberFourButton = Button(calculatorFrame, text="4", background=buttonNumbersColor,
                          font=(font + " Bold", fontSize - 1), anchor=CENTER, relief=FLAT)
numberFourButton.place(x=5, y=334, width=buttonSizeX, height=buttonSizeY)

numberFiveButton = Button(calculatorFrame, text="5", background=buttonNumbersColor,
                          font=(font + " Bold", fontSize - 1), anchor=CENTER, relief=FLAT)
numberFiveButton.place(x=81, y=334, width=buttonSizeX, height=buttonSizeY)

numberSixButton = Button(calculatorFrame, text="6", background=buttonNumbersColor,
                         font=(font + " Bold", fontSize - 1), anchor=CENTER, relief=FLAT)
numberSixButton.place(x=157, y=334, width=buttonSizeX, height=buttonSizeY)

numberOneButton = Button(calculatorFrame, text="1", background=buttonNumbersColor,
                         font=(font + " Bold", fontSize - 1), anchor=CENTER, relief=FLAT)
numberOneButton.place(x=5, y=392, width=buttonSizeX, height=buttonSizeY)

numberTwoButton = Button(calculatorFrame, text="2", background=buttonNumbersColor,
                         font=(font + " Bold", fontSize - 1), anchor=CENTER, relief=FLAT)
numberTwoButton.place(x=81, y=392, width=buttonSizeX, height=buttonSizeY)

numberThreeButton = Button(calculatorFrame, text="3", background=buttonNumbersColor,
                           font=(font + " Bold", fontSize - 1), anchor=CENTER, relief=FLAT)
numberThreeButton.place(x=157, y=392, width=buttonSizeX, height=buttonSizeY)

plusOverMinusButton = Button(calculatorFrame, text="+/-", background=buttonNumbersColor,
                             font=(font + " Bold", fontSize - 1), anchor=CENTER, relief=FLAT)
plusOverMinusButton.place(x=5, y=450, width=buttonSizeX, height=buttonSizeY)

numberZeroButton = Button(calculatorFrame, text="0", background=buttonNumbersColor,
                          font=(font + " Bold", fontSize - 1), anchor=CENTER, relief=FLAT)
numberZeroButton.place(x=81, y=450, width=buttonSizeX, height=buttonSizeY)

decimalButton = Button(calculatorFrame, text=".", background=buttonNumbersColor,
                       font=(font + " Bold", fontSize - 1), anchor=CENTER, relief=FLAT)
decimalButton.place(x=157, y=450, width=buttonSizeX, height=buttonSizeY)

#########################################################
# Button objects
operationButtons = [percentageButton, clearEntryButton, clearButton, removeOneNumberButton, oneDivideNumberButton,
                    squareNumberButton, squareRootNumberButton, divideButton, multiplyButton, subtractButton,
                    addButton, equalButton]

numberButtons = [numberSevenButton, numberEightButton, numberNineButton, numberFourButton, numberFiveButton,
                 numberSixButton, numberOneButton, numberTwoButton, numberThreeButton, numberZeroButton,
                 plusOverMinusButton, decimalButton]

# manipulate comma, float or int, font size
def formatResultValue(value):
    # convert to wether int or float
    if value % 1 == 0:
        value = "{:,}".format(int(str(value)))
    else:
        value = "{:,}".format(float(str(value)))

    # compress size
    if len(str(value)) < 10:
        calculatorInputViewBottomLabel.configure(font=(font + " Bold", fontSize + 20))
    elif len(str(value)) >= 10:
        calculatorInputViewBottomLabel.configure(font=(font + " Bold", fontSize + 8))

    return str(value)

# Number Button Click
def numberButtonClick(myButton):
    value = myButton['text']

    # prevent multiple decimal in input
    if value == "." and "." in calculatorStatement:
        return
    calculatorStatement.append(value)

    # check if more than equal 10 numbers
    if len(calculatorInputViewBottomLabel['text']) < 10:
        calculatorInputViewBottomLabel.configure(font=(font + " Bold", fontSize + 20))
    elif len(calculatorInputViewBottomLabel['text']) >= 10:
        calculatorInputViewBottomLabel.configure(font=(font + " Bold", fontSize + 8))

    # if decimal button clicked
    if myButton == decimalButton:
        calculatorInputViewBottomLabel['text'] = ''.join(calculatorStatement)

    # if not decimal
    else:
        if "." in calculatorStatement: # if the input is float
            calculatorInputViewBottomLabel['text'] = ''.join(calculatorStatement)
            calculatorInputViewBottomLabel['text'] = "{:,}".format(float(calculatorInputViewBottomLabel['text']))
            return

        # if integer and not float
        calculatorInputViewBottomLabel['text'] = ''.join(calculatorStatement)
        calculatorInputViewBottomLabel['text'] = "{:,}".format(int(calculatorInputViewBottomLabel['text']))

def operatorButtonClick(myButton):
    storedValue = [] # Topview label value

    # calculatorStatement = current value
    if not calculatorStatement:
        if '0' in calculatorStatement:
            calculatorStatement.append('0') # set default value
        else: # set current value from stored value
            calculatorStatement.append(re.findall(r'\d+', calculatorInputViewTopLabel['text'])[0])

    # Set current value wether float or int
    if "." in calculatorInputViewBottomLabel['text']:
        currentValue = float(''.join(calculatorStatement))
    else:
        currentValue = int(''.join(calculatorStatement))

    # Set the stored value wether float or int
    if "." in calculatorInputViewTopLabel['text']:
        value = re.findall('\d+\.\d+', calculatorInputViewTopLabel['text'])[0]
        storedValue.append(float(value))
    else:
        value = re.findall(r'\d+', calculatorInputViewTopLabel['text'])[0]
        storedValue.append(int(value))

    # If not the default value (0)
    if storedValue[0] != 0:
        if myButton['text'] == percentageButton['text']:
            pass

        elif myButton['text'] == addButton['text']:
            resultValue = storedValue[0] + currentValue
            calculatorInputViewTopLabel['text'] = str(resultValue) + " " + myButton['text']
            calculatorInputViewBottomLabel['text'] = formatResultValue(resultValue)

        elif myButton['text'] == subtractButton['text']:
            resultValue = storedValue[0] - currentValue
            calculatorInputViewTopLabel['text'] = str(resultValue) + " " + myButton['text']
            calculatorInputViewBottomLabel['text'] = formatResultValue(resultValue)

        elif myButton['text'] == multiplyButton['text']:
            resultValue = storedValue[0] * currentValue
            calculatorInputViewTopLabel['text'] = str(resultValue) + " " + myButton['text']
            calculatorInputViewBottomLabel['text'] = formatResultValue(resultValue)

        elif myButton['text'] == divideButton['text']:
            resultValue = storedValue[0] / currentValue

            # If the result is not float
            if resultValue % 1 == 0:
                resultValue = int(resultValue)

            calculatorInputViewTopLabel['text'] = str(resultValue) + " " + myButton['text']
            calculatorInputViewBottomLabel['text'] = formatResultValue(resultValue)

    # If stored value is 0
    else:
        if myButton['text'] == clearEntryButton['text']:
            calculatorInputViewBottomLabel['text'] = str(currentValue)
        # Transfer current value to stored value and set operator
        else:
            calculatorInputViewTopLabel['text'] = ''.join(calculatorStatement) + " " + myButton['text']
            calculatorInputViewBottomLabel['text'] = str(currentValue)

    # Clear entry
    if myButton['text'] == clearEntryButton['text']:
        calculatorInputViewBottomLabel['text'] = '0'
        calculatorInputViewBottomLabel.configure(font=(font + " Bold", fontSize + 20))
        calculatorStatement.clear()
        return

    elif myButton['text'] == clearButton['text']:
        calculatorInputViewBottomLabel['text'] = '0'
        calculatorInputViewTopLabel['text'] = '0'
        calculatorInputViewBottomLabel.configure(font=(font + " Bold", fontSize + 20))
        calculatorStatement.clear()
        storedValue.clear()
        return

    elif myButton['text'] == removeOneNumberButton['text']:
        pass

    # When transfered, clear the current value
    calculatorStatement.clear()

# Button Hover
def buttonHoverEnter(myButton, color):
    myButton['background'] = color

def buttonHoverExit(myButton, color):
    myButton['background'] = color

for button in operationButtons:
    button.bind("<Enter>", lambda event, myButton=button, color="#B8B8B8": buttonHoverEnter(myButton, color))
    button.bind("<Leave>", lambda event, myButton=button, color=buttonOperationsColor: buttonHoverExit(myButton, color))
    button.bind("<Button-1>", lambda event, myButton=button: operatorButtonClick(myButton))

for button in numberButtons:
    button.bind("<Enter>", lambda event, myButton=button, color="#B9B9B9": buttonHoverEnter(myButton, color))
    button.bind("<Leave>", lambda event, myButton=button, color=buttonNumbersColor: buttonHoverExit(myButton, color))
    button.bind("<Button-1>", lambda event, myButton=button: numberButtonClick(myButton))

#########################################################

# Mainloop
window.mainloop()
