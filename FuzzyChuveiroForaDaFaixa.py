# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:43:42 2021

@author: Lucas Gava
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl



Tambiente = ctrl.Antecedent(np.arange(0, 101, 1), 'Tambiente')
Vazao = ctrl.Antecedent(np.arange(10, 101, 1), 'Vazao')
Tagua = ctrl.Consequent(np.arange(10, 31, 1), 'Tagua')




Tambiente['Quente'] = fuzz.trimf(Tambiente.universe, [50, 100, 100])
Tambiente['Mediana'] = fuzz.trimf(Tambiente.universe, [0, 50, 100])
Tambiente['Fria'] = fuzz.trimf(Tambiente.universe, [0, 0, 50])


Vazao['Alta'] = fuzz.trimf(Vazao.universe, [55, 100, 100])
Vazao['Média'] = fuzz.trimf(Vazao.universe, [10, 55, 100])
Vazao['Baixa'] = fuzz.trimf(Vazao.universe, [10, 10, 55])





Tagua['Muito Quente'] = fuzz.trimf(Tagua.universe, [25, 30, 30])
Tagua['Quente'] = fuzz.trimf(Tagua.universe, [20, 25, 30])
Tagua['Mediana'] = fuzz.trimf(Tagua.universe, [15, 20, 25])
Tagua['Frio'] = fuzz.trimf(Tagua.universe, [10, 15, 20])
Tagua['Muito Frio'] = fuzz.trimf(Tagua.universe, [10,10, 15])




Tambiente.view()



Vazao.view()



Tagua.view()



rule1 = ctrl.Rule(Tambiente['Fria'] & Vazao['Alta'], Tagua['Muito Frio'])
rule2 = ctrl.Rule(Tambiente['Fria'] & Vazao['Média'], Tagua['Frio'])
rule3 = ctrl.Rule(Tambiente['Fria'] & Vazao['Baixa'], Tagua['Mediana'])
rule4 = ctrl.Rule(Tambiente['Mediana'] & Vazao['Alta'], Tagua['Frio'])
rule5 = ctrl.Rule(Tambiente['Mediana'] & Vazao['Média'], Tagua['Mediana'])
rule6 = ctrl.Rule(Tambiente['Mediana'] & Vazao['Baixa'], Tagua['Quente'])
rule7 = ctrl.Rule(Tambiente['Quente'] & Vazao['Alta'], Tagua['Mediana'])
rule8 = ctrl.Rule(Tambiente['Quente'] & Vazao['Média'], Tagua['Quente'])
rule9 = ctrl.Rule(Tambiente['Quente'] & Vazao['Baixa'], Tagua['Muito Quente'])





Final_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])



Final = ctrl.ControlSystemSimulation(Final_ctrl)


Final.input['Tambiente'] = 0
Final.input['Vazao'] = 100


Final.compute()


print(Final.output['Tagua'])
Tagua.view(sim=Final)