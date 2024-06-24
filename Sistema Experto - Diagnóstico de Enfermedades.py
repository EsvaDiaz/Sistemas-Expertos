import tkinter as tk
from tkinter import messagebox

class SistemaExpertoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Experto de Diagnóstico Médico (3ra Edad)")
        
        self.base_de_conocimiento = {
            'fiebre': ['gripe', 'infección urinaria'],
            'tos': ['gripe', 'bronquitis'],
            'dolor de cabeza': ['migraña', 'gripe'],
	    'dolores musculares': ['COVID-19', 'gripe'],
            'fatiga': ['COVID-19', 'bronquitis'],
            'confusión': ['Alzheimer', 'diabetes'],
	    'desorientación': ['Alzheimer', 'Parkinson'],
            'rigidez': ['Alzheimer', 'Parkinson'],
            'trastornos del sueño': ['Parkinson'],
	    'pérdida del equilibrio': ['Parkinson'],
        }
        
        self.create_widgets()

    def create_widgets(self):
        # Instrucción
        self.label = tk.Label(self.root, text="Ingresa los síntomas separados por comas:")
        self.label.pack()
        
        # Entrada de texto para los síntomas
        self.sintomas_entry = tk.Entry(self.root, width=50)
        self.sintomas_entry.pack()
        
        # Botón para realizar el diagnóstico
        self.diagnostico_button = tk.Button(self.root, text="Diagnosticar", command=self.diagnosticar)
        self.diagnostico_button.pack()
        
    def diagnosticar(self):
        sintomas = self.sintomas_entry.get().split(',')
        sintomas = [sintoma.strip().lower() for sintoma in sintomas]
        enfermedades_posibles = set()
        for sintoma in sintomas:
            enfermedades_posibles.update(self.base_de_conocimiento.get(sintoma, []))
        
        if enfermedades_posibles:
            messagebox.showinfo("Diagnóstico", f"Las posibles enfermedades son: {', '.join(enfermedades_posibles)}")
        else:
            messagebox.showinfo("Diagnóstico", "No se encontraron enfermedades con los síntomas proporcionados.")

def main():
    root = tk.Tk()
    app = SistemaExpertoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
