from tkinter import *
import backend


def get_selected_row(event):
    ''' Event listener function - fetches details of selected row in Listbox'''
    global selected_row
    index = listbox_all_data.curselection()[0]
    selected_row = listbox_all_data.get(index)
    # Filling the entry boxes on top with the selected row's data.
    entry_first_name.delete(0, END)
    entry_first_name.insert(END, selected_row[1])
    entry_last_name.delete(0, END)
    entry_last_name.insert(END, selected_row[2])
    entry_email.delete(0, END)
    entry_email.insert(END, selected_row[3])
    entry_age.delete(0, END)
    entry_age.insert(END, selected_row[4])

###########################################
# CALLBACK FUNCTIONS FOR BUTTONS
###########################################


def view_command():
    listbox_all_data.delete(0, END)
    for row in backend.view():
        listbox_all_data.insert(END, row)

###########################################


def search_command():
    listbox_all_data.delete(0, END)
    for row in backend.search(first_name_text.get(), last_name_text.get(), email_text.get(), age_text.get()):
        listbox_all_data.insert(END, row)

###########################################


def add_command():
    backend.insert(first_name_text.get(), last_name_text.get(),
                   email_text.get(), age_text.get())
    listbox_all_data.delete(0, END)
    listbox_all_data.insert(END, (first_name_text.get(), last_name_text.get(),
                                  email_text.get(), age_text.get()))

###########################################


def delete_command():
    backend.delete(selected_row[0])

###########################################


def update_command():
    backend.update(selected_row[0], first_name_text.get(
    ), last_name_text.get(), email_text.get(), age_text.get())


###########################################
# DEFINING THE INTERFACE
###########################################
window = Tk()

window.wm_title('Subscribers')

###########################################
# LABELS
###########################################
label_first_name = Label(window, text='First Name')
label_first_name.grid(row=0, column=0, pady=2)

label_last_name = Label(window, text='Last Name')
label_last_name.grid(row=0, column=2, pady=2)

label_email = Label(window, text='Email')
label_email.grid(row=1, column=0, pady=2)

label_age = Label(window, text='Age')
label_age.grid(row=1, column=2, pady=2)

###########################################
# ENTRY BOXES
###########################################
first_name_text = StringVar()
entry_first_name = Entry(window, textvariable=first_name_text)
entry_first_name.grid(row=0, column=1, pady=2)

last_name_text = StringVar()
entry_last_name = Entry(window, textvariable=last_name_text)
entry_last_name.grid(row=0, column=3, pady=2)

email_text = StringVar()
entry_email = Entry(window, textvariable=email_text)
entry_email.grid(row=1, column=1, pady=2)

age_text = StringVar()
entry_age = Entry(window, textvariable=age_text)
entry_age.grid(row=1, column=3, pady=2)

###########################################
# LISTBOX - DISPLAY THE DATA FROM DB
###########################################
listbox_all_data = Listbox(window, height=12, width=35)
listbox_all_data.grid(row=2, column=0, rowspan=6, columnspan=2, padx=7)

scrollbar_for_listbox = Scrollbar(window)
scrollbar_for_listbox.grid(row=2, column=2, rowspan=6)

listbox_all_data.configure(yscrollcommand=scrollbar_for_listbox.set)
scrollbar_for_listbox.configure(command=listbox_all_data.yview)

# Binding the listbox to an event listener function
listbox_all_data.bind('<<ListboxSelect>>', get_selected_row)

###########################################
# BUTTONS
###########################################
button_view_all = Button(window, text='View all',
                         width=12, command=view_command)
button_view_all.grid(row=2, column=3, pady=4)

button_search_entry = Button(
    window, text='Search entry', width=12, command=search_command)
button_search_entry.grid(row=3, column=3, pady=4)

button_add_entry = Button(window, text='Add entry',
                          width=12, command=add_command)
button_add_entry.grid(row=4, column=3, pady=4)

button_update_selected = Button(
    window, text='Update selected', width=12, command=update_command)
button_update_selected.grid(row=5, column=3, pady=4)

button_delete_selected = Button(
    window, text='Delete selected', width=12, command=delete_command)
button_delete_selected.grid(row=6, column=3, pady=4)

button_close = Button(window, text='Close', width=12, command=window.destroy)
button_close.grid(row=7, column=3, pady=4)

###########################################
window.mainloop()
