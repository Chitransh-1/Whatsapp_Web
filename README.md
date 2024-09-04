"This repository is based on WhatsApp Web. It provides a basic structure for WhatsApp Web and is used in businesses to send bulk messages."

"SUMMARY"
- This code creates a WhatsApp Web-like interface using the `customtkinter` library. It allows users to view and interact with chat lists, display message history, and send new messages. 
- The application organizes the interface into different sections, including a sidebar, a chat list area, a message history display, and a message input field. 
- It also handles user interactions like selecting a chat to view details and sending messages. 
- The main functionality revolves around dynamically displaying chat data and updating the interface based on user actions.

"ABOUT CODE"
This code creates a GUI application using the `customtkinter` library, which is a modified version of the `tkinter` library with enhanced features for modern-looking interfaces. The application simulates a WhatsApp Web interface, allowing users to interact with chat data, send messages, and view message history. Here’s a breakdown of what each section does:

### Importing Libraries
- `customtkinter as ctk`: Imports the custom `tkinter` library as `ctk` for easier reference.
- `from tkinter import *`: Imports all modules from the standard `tkinter` library.
- `from datetime import datetime`: Imports the `datetime` module to handle date and time operations.
- `import whtsap_function as fun`: Imports a custom module named `whtsap_function`, likely containing functions to interact with WhatsApp data.

### Setting Up the Main Window
- `root = ctk.CTk()`: Initializes the main window using `customtkinter`.
- `root.title("WhatsApp Web")`: Sets the title of the window to "WhatsApp Web".
- `root.geometry("1200x800")`: Defines the size of the window.

### Creating Frames
- `sidebar_frame`: A narrow, dark green sidebar on the left side of the window.
- `numbers_frame`: A white frame to the right of the sidebar, displaying chat details.
- `number_scroll`: A scrollable frame within `numbers_frame` for scrolling through chat lists.
- `info_frame`: A frame at the top to display information like contact name and number.
- `scroll_frame`: A large scrollable frame below `info_frame`, displaying the message history.
- `message_frame`: A frame at the bottom for composing and sending new messages.

### Sending a Message
- The `insert_mess` function retrieves the text from the entry field and sends it using a function from the `whtsap_function` module.

### Handling User Interactions
- The `get_frame` function is triggered when a chat box is clicked. It:
  - Identifies the selected chat.
  - Retrieves and displays the corresponding contact details and message history.
  - Converts message timestamps to a specific format.
  - Clears the previous messages from `scroll_frame` and populates it with the selected chat's messages.

### Displaying Chat List
- The `display_data_in_boxes` function retrieves chat data using a function from `whtsap_function` and displays them as clickable boxes in `numbers_frame`. These boxes trigger `get_frame` when clicked.

### Main Application Loop
- The `root.mainloop()` keeps the GUI running, allowing users to interact with the application.

### Additional Components
- A button at the bottom of the window (`btn`) can be clicked to refresh the chat list by calling `display_data_in_boxes` again.
