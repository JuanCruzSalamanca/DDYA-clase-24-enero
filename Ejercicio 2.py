def notas(x):
    l_data = x.split()
    names = []
    notes = []
    aprove = []
    for i in range (1,len(l_data),2):
        names.append(l_data[i-1])
        notes.append(float(l_data[i]))
    
    for i in range (len(notes)):
        if notes[i] >= 3:
            aprove.append(names[i])
    return aprove

def main():
    est_note = input("Escriba el nombre de los estudiantes y sus notas separadas por espacio: ")
    print("==================")
    aprov_names = notas(est_note)
    answer = " ".join(aprov_names)
    print(answer)
main()