import numpy as np
from .sets import IntuitionisticFuzzySoftSet
from .similarities import ifss_similarity_Muthukumar_Sundara
"""In this example we took intuisionistic fuzzy soft set of 5 patients according to 3 parameters 
  as Body mass index (BMI),Blood glucose levels and Insulin resistance
"""
#Patients:
pt1 = IntuitionisticFuzzySoftSet([[0.4, 0.7, 0.6, 0.5], [0.5, 0.2, 0.1, 0.7], [0.6, 0.4, 0.5, 0.9]],
                                 [[0.9, 0.8, 0.7, 0.5], [0.3, 0.8, 0.3, 0.8], [0.1, 0.7, 0.5, 0.4]])

pt2 = IntuitionisticFuzzySoftSet([[0.3, 0.6, 0.7, 0.1], [0.7, 0.8, 0.4, 0.4], [0.3, 0.2, 0.5, 0.7]],
                                 [[0.3, 0.1, 0.6, 0.9], [0.7, 0.3, 0.8, 0.6], [0.6, 0.3, 0.9, 0.8]])

pt3 = IntuitionisticFuzzySoftSet([[0.6, 0.3, 0.9, 0.2], [0.7, 0.3, 0.8, 0.2], [0.6, 0.9, 0.3, 0.5]],
                                 [[0.9, 0.8, 0.7, 0.5], [0.3, 0.8, 0.3, 0.8], [0.1, 0.7, 0.5, 0.4]])

pt4 = IntuitionisticFuzzySoftSet([[0.5, 0.9, 0.4, 0.2], [0.8, 0.3, 0.6, 0.5], [0.3, 0.3, 0.6, 0.7]],
                                 [[0.3, 0.7, 0.8, 0.5], [0.8, 0.7, 0.5, 0.4], [0.6, 0.2, 0.8, 0.8]])

pt5 = IntuitionisticFuzzySoftSet([[0.6, 0.9, 0.3, 0.2], [0.7, 0.2, 0.8, 0.1], [0.2, 0.4, 0.5, 0.7]],
                                 [[0.9, 0.8, 0.7, 0.5], [0.3, 0.8, 0.3, 0.8], [0.4, 0.3, 0.4, 0.4]])
#IFSS model of diabetics
pm = IntuitionisticFuzzySoftSet([[0.1, 0.5, 0.7, 0.8], [0.3, 0.4, 0.6, 0.3], [0.5, 0.2, 0.4, 0.6]],
                                 [[0.6, 0.8, 0.2, 0.7], [0.2, 0.8, 0.2, 0.4], [0.6, 0.3, 0.8, 0.7]])

sim1 =ifss_similarity_Muthukumar_Sundara(pt1, pm)
sim2 =ifss_similarity_Muthukumar_Sundara(pt2, pm)
sim3 =ifss_similarity_Muthukumar_Sundara(pt3, pm)
sim4 =ifss_similarity_Muthukumar_Sundara(pt4, pm)
sim5 =ifss_similarity_Muthukumar_Sundara(pt5, pm)
print(sim1)
print(sim2)
print(sim3)
print(sim4)
print(sim5)
"""Here the patient 4 has the highest similarities show he is most likely to be diabetic
Output:
sim1 = 0.6224976167778838
sim2 = 0.5850860420650094
sim3 = 0.5881818181818181
sim4 = 0.6315280464216633
sim5 = 0.5980582524271846 """