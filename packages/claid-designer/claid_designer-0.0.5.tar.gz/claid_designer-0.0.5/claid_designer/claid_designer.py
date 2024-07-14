from ui.claid_designer_ui import CLAIDDesignerUI
from PyQt5.QtCore import Qt, QPointF, QEvent, QCoreApplication
from PyQt5.QtWidgets import QApplication
import sys
import os

from ui.landing_page import LandingPage

class CLAIDDesigner:

    def __init__(self):
        self.claid = None
        self.__attached_to_claid = False

        self.ip = ""

    def attach(self, claid):

        if self.__attached_to_claid:
            raise RuntimeError("Already attached to claid")
        
        # Those two functions will be called later by CLAID once it has started.
        claid.register_external_function_on_claid_thread_run_once(self.__init_application)
        claid.register_external_function_on_claid_thread_repeat_indefinitely(self.__update)

        self.claid = claid
        
        self.__attached_to_claid = True

    def start(self, host_name, user_id, device_id, module_factory):
        
        self.app = QApplication(sys.argv)

        landing_page = LandingPage()
        # self.landing_page.on_start_clicked.connect(self.on_landing_page_start_clicked)
        landing_page.show()

        while landing_page.isVisible():
            self.__update()

        self.ip = landing_page.get_ip()

        current_file_path = os.path.abspath(__file__)

        # Get the directory containing the currently executed Python file
        current_directory = os.path.dirname(current_file_path)

        self.__replace_in_file(os.path.join(current_directory, "empty_workshop_config.json"), "config.claid", "$(workshop_smartwatch_ip_to_replace)", self.ip)
    
        self.claid.start("config.claid", host_name, user_id, device_id, module_factory)    

        self.available_modules = self.claid.get_available_modules_on_this_host()



    def __init_application(self):
        #TODO: Scale the whole application depending on screen resolution
        self.claid.enable_designer_mode()
        self.mainWindow = CLAIDDesignerUI(self.claid, self.ip)

        # Get screen resolution
        screen = self.app.primaryScreen()
        rect = screen.availableGeometry()
        screenWidth = rect.width()
        screenHeight = rect.height()

        # Window size
        winWidth = int(screenWidth // 1.4)
        winHeight = int(screenHeight // 1.6)

        # Calculate window position
        x = (screenWidth - winWidth) // 2
        y = (screenHeight - winHeight) // 2

        self.mainWindow.setGeometry(x, y, winWidth, winHeight)
        self.mainWindow.setWindowTitle("CLAID Designer")
        self.mainWindow.show()

        


    def __update(self):
        QCoreApplication.processEvents()


    def __on_connected_to_server(self):
        pass

    def __on_disconnected_from_server(self):
        pass

    def __replace_in_file(self, file_path, output_file_path, old_string, new_string):
        try:
            # Open the file for reading
            with open(file_path, 'r') as file:
                file_content = file.read()

            # Replace the specified string
            modified_content = file_content.replace(old_string, new_string)

            # Open the file for writing and overwrite its content
            with open(output_file_path, 'w') as file:
                file.write(modified_content)

            print(f"String '{old_string}' replaced with '{new_string}' in {file_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")