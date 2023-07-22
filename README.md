# Selenium-Python
Contains projects that were made for learning how to operate automation testing using Selenium

# Selenium: How to configure
1. Install Python at https://www.python.org/downloads/
2. Install Selenium Library in Command Prompt using 'pip install selenium'
3. Install Visual Studio Code at https://code.visualstudio.com/download
4. Open Visual Studio Code - Extension, then install Python Extension
5. If you're using Chrome Browser, then install Chrome Driver at https://chromedriver.chromium.org/downloads
   Make sure that the Chrome Driver and your Chrome Browser are the same version
6. Extract the Chrome Driver then add it to the Path
7. Open the Visual Studio Code then create your projects

# Pytest-Python
Related to Software Quality Assurance Engineer World that can conduct Unit Testing to System Integration Testing

# Pytest: How to configure
1. Install Pytest Library in Command Prompt using 'pip install pytest'
2. Just go to VS Code then start coding
3. Make a function (def) in your Code File. The name of the file and the function should contain the word 'test' in it
4. To run your code, go to the terminal, type 'pytest your_code_name, ' and press enter. If your terminal isn't in the right folder, type 'cd .\folder_name'
5. Don't forget to save the file before running the code

# How to get rid of "Error Logging"
1. mode = webdriver.ChromeOptions()
2. mode.add_experimental_option('excludeSwitches', ['enable-logging'])
3. driver = webdriver.Chrome(options=mode)

