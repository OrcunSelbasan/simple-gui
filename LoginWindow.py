"""
    Stage: Development-01
    @author:
    @author:
"""

import tkinter as tk

class LoginWindow:
    # constructor
    def __init__(self):
        self.window = tk.Tk()

        self._initializeGUI()
        self._addGUIElementsToFrame()

        # start the GUI frame
        self.window.mainloop()


    """
        Initialize GUI elements. If it is necessary, you can add
        more elements.

        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """
    def _initializeGUI(self):
        self.usernameLabel = tk.Label(text="Username")
        self.passwordLabel = tk.Label(text="Password")

        self.usernameInput = tk.Entry()
        self.passwordInput = tk.Entry(show="*")
 
        self.exitBtn = tk.Button(text="Exit")
        self.loginBtn = tk.Button(text="Login")

        self.loginBtn.bind("<Button-1>", self.handleLogin)
        self.exitBtn.bind("<Button-1>", self.handleExit)


    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.usernameLabel.grid(row=0, column=0, padx=10, pady=5)
        self.usernameInput.grid(row=0, column=1, padx=10, pady=5)

        self.passwordLabel.grid(row=1, column=0, padx=10, pady=5)
        self.passwordInput.grid(row=1, column=1, padx=10, pady=5)

        self.loginBtn.grid(row=2, column=1, padx=10, pady=5)
        self.exitBtn.grid(row=2, column=0, padx=10, pady=5)

    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.

        :param event: action event for detecting which button is clicked
    """
    def handleLogin(self, event):
        username = "JohnDoe"
        password = "12345"
        conditionName = self.usernameInput.get() == username
        conditionPassword = self.passwordInput.get() == password
        if (conditionName and conditionPassword):
            print("SUCESS")
        else: 
            print("Failed")




    def handleExit(self, event):
        self.window.destroy()


# main method for testing the application
if __name__ == "__main__":
    LoginWindow()

lw = LoginWindow();
lw
