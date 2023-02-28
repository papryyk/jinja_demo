from tkinter import *
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from templates import *


def refresh():
    environment = Environment(loader=FileSystemLoader("templates/"))
    try:
        template = environment.get_template(chosen_template.get()+".txt")
        for index, value in enumerate(templates):
            if value == chosen_template.get():
                template_index = index
                for ind, kw in enumerate(template_kw[index]):
                    template_data[index][kw] = option_list[ind].get()
                content = template.render(template_data[template_index])
                with open("/Users/patrykgaszczyk/IdeaProjects/jinja_demo/generated_file.txt", mode="w", encoding="utf-8") as message:
                    message.write(content)

        textarea.delete(0.0, END)
        tf = open("/Users/patrykgaszczyk/IdeaProjects/jinja_demo/generated_file.txt", 'r')
        data = tf.read()
        textarea.insert(END, data)
        tf.close()
    except TemplateNotFound:
        pass


def template_choice(template):
    for index, value in enumerate(templates):
        if value == template:
            template_index = index
            for ind, kw in enumerate(template_kw[template_index]):
                buttons_list[ind].set(kw)
    for option_var in option_var_list:
        option_var.set("")
    refresh()


ws = Tk()
ws.title("Simple Template Generator")
ws.geometry("630x700")

textarea = Text(width=89, height=40)
textarea.grid(column=0, row=0, columnspan=3)
textarea.insert(0.0, "Choose Your template!")
option_1_var = StringVar()
button_1_var = StringVar()
option_2_var = StringVar()
button_2_var = StringVar()
option_3_var = StringVar()
button_3_var = StringVar()
option_4_var = StringVar()
button_4_var = StringVar()
chosen_template = StringVar()
option_1 = Entry(background="black", textvariable=option_1_var)
option_2 = Entry(background="black", textvariable=option_2_var)
option_3 = Entry(background="black", textvariable=option_3_var)
option_4 = Entry(background="black", textvariable=option_4_var)
option_1.grid(column=0, row=2)
option_2.grid(column=1, row=2)
option_3.grid(column=0, row=4)
option_4.grid(column=1, row=4)
Button(textvariable=button_1_var, state="disabled", disabledforeground="black").grid(column=0, row=1)
Button(textvariable=button_2_var, state="disabled", disabledforeground="black").grid(column=1, row=1)
Button(textvariable=button_3_var, state="disabled", disabledforeground="black").grid(column=0, row=3)
Button(textvariable=button_4_var, state="disabled", disabledforeground="black").grid(column=1, row=3)
Button(ws, text="Load changes", command=refresh).grid(column=0, row=5, columnspan=3, sticky="EW")

chosen_template.set("Templates")
templates_drop = OptionMenu(ws, chosen_template, command=template_choice, *templates)
templates_drop.grid(column=0, row=6, columnspan=3, sticky="EW")


buttons_list = [button_1_var, button_2_var, button_3_var, button_4_var]
option_list = [option_1, option_2, option_3, option_4]
option_var_list = [option_1_var, option_2_var, option_3_var, option_4_var]


if __name__ == "__main__":
    ws.mainloop()
