import tkinter as tk
import json
import os

#Створює вікно
root = tk.Tk()
root.title("Поле і кнопка в одному рядку")
root.geometry("800x600")

#Змінні для основних значень
name=""
countl=0
start=[]
durl=0
durb=0
#Списки для підрахунку
data={}
entry_list=[]
breaks=[]
l=[]

#Функція для створення меню корекції перерв
def inp():
    global countl,start,durl,durb,name,entery_line, entry_list
    #Отримання данних з полей вводу в змінні
    countl=int(entery_countl.get())
    start=list(map(int, entery_start.get().split(":")))
    durl=int(entery_durl.get())
    durb=int(entery_durb.get())
    name=entery_name.get()

    #Вивід полей для корекції перерв
    ii=0
    for i in range(countl-1):
        entery_line= tk.Entry(root, font=("Arial", 14) )
        entery_line.insert(0,f"{durb}")
        text_line= tk.Label(root, text=f"Перерва №{i+1}", font=("Arial", 16), fg="black")

        text_line.grid(row=5+i ,column=0)
        entery_line.grid(row=5+i ,column=1)

        entry_list.append(entery_line)
        ii=i
    
    title=tk.Label(root, text="Редакція перерв", font=("Impact", 16), fg="black")
    title.grid(row=6+ii)
    cre=tk.Button(root, text="Створити файл", command=create)
    cre.grid(row=7+ii)

#Основний інтерфейс
entery_name= tk.Entry(root, font=("Arial", 14))
text_name= tk.Label(root, text="Ім'я розкладу", font=("Arial", 16), fg="black")

entery_countl= tk.Entry(root, font=("Arial", 14))
text_countl= tk.Label(root, text="Кількість уроків:", font=("Arial", 16), fg="black")

entery_start= tk.Entry(root, font=("Arial", 14))
text_start= tk.Label(root, text="Початок уроку:", font=("Arial", 16), fg="black")

entery_durl= tk.Entry(root, font=("Arial", 14))
text_durl= tk.Label(root, text="Тривалість уроку:", font=("Arial", 16), fg="black")

entery_durb= tk.Entry(root, font=("Arial", 14))
text_durb= tk.Label(root, text="Тривалість перерв:", font=("Arial", 16), fg="black")

a_but=tk.Button(root, text="Порахувати", command=inp)




def create():
    global entry,entry_list,breaks,l,start,countl,start,durl,durb,name,entery_line, entry_list,data,subdata
    #Додавання тривалості всіх перерв у список
    for i, entry in enumerate(entry_list):
        breaks.append(entry.get())
    ii=True
    startl=start[0]*60+start[1]#Перевод часу старту уроків у хвилини
    y=0
    l.append(startl)
    
    while ii==True:
        if len(breaks)==0:#Рахування тільки уроків якщо мерерв не залишилось
            ii=False
            les=l[i]+durl
            l.append(les)
            break
        else:#Рахування урока і перерви
            les=l[y]+durl
            l.append(les)

            per=les+int(breaks[0])
            l.append(per)
            breaks.pop(0)

        y+=2
    #Перевод з хвилин на нормальний час
    for i in range(len(l)):
        if l[i]%60==0:
            l[i]=f"{l[i]//60}:{l[i]%60}0"
        else:
            l[i]=f"{l[i]//60}:{l[i]%60}"
    
    for i in range(countl):
        if len(l)<=2:#Перевод в формат для json якщо перерв не залишилось
            data[f"Урок№{i + 1}"] = {
            "start": l[0],
            "end": l[1]
            }
            break
        else:#Перевод в формат для json 
            data[f"Урок№{i + 1}"] = {
            "start": l[0],
            "end": l[1]
            }
            data[f"Перерва№{i + 1}"] = {
            "start": l[1],
            "end": l[2]
            }
        l.pop(0)
        l.pop(0)
    print(data)
    #Запис файлу
    fp = os.path.dirname(__file__)
    with open(os.path.join(fp, f"{name}.json"), 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    



#Вивід основного інтерфейсу

text_name.grid(row=0 ,column=0)
entery_name.grid(row=0 ,column=1)

text_countl.grid(row=1 ,column=0)
entery_countl.grid(row=1 ,column=1)

text_start.grid(row=2 ,column=0)
entery_start.grid(row=2 ,column=1)

text_durl.grid(row=3 ,column=0)
entery_durl.grid(row=3 ,column=1)

text_durb.grid(row=4 ,column=0)
entery_durb.grid(row=4 ,column=1)













a_but.grid()

root.mainloop()