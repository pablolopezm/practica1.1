#!/usr/bin/env python
# coding: utf-8

# # Calcula as emisións dun medio de transporte

# ** Calcula a cantidade de emisións que produce certo medio de transporte tendo en conta os seus kms diarios, os días laborables da semana e as semanas totais, tendo en conta as emisións por km 

# In[12]:


#!/usr/bin/env python

# Cálculo de emisións

# Variables
KMS_DIARIOS = 20
DIAS_LABORAIS_SEMANAIS = 3
SEMANAS = 40

# Cada medio de transporte ten o seu índice de emisións medio (gramos por km)
# https://www.movilidad-idae.es/destacados/emisiones-de-co2-por-modos-de-transporte-motorizado
EMISION_X_KM = 121

cantidade_de_emisions = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM
print('O teu consumo é:', cantidade_de_emisions, 'gC02')


# In[13]:


#!/usr/bin/env python

# Cálculo de emisións

# Variables
KMS_DIARIOS = 100
DIAS_LABORAIS_SEMANAIS = 5
SEMANAS = 24

# Cada medio de transporte ten o seu índice de emisións medio (gramos por km)
# https://www.movilidad-idae.es/destacados/emisiones-de-co2-por-modos-de-transporte-motorizado
EMISION_X_KM = 121

cantidade_de_emisions = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM
print('O teu consumo é:', cantidade_de_emisions, 'gC02')


# In[18]:


#!/usr/bin/env python

# Cálculo de emisións


# Variables
KMS_DIARIOS = 20
DIAS_LABORAIS_SEMANAIS = 5
SEMANAS = 20

# Cada medio de transporte ten o seu índice de emisións medio (gramos por km)
# https://www.movilidad-idae.es/destacados/emisiones-de-co2-por-modos-de-transporte-motorizado
EMISION_X_KM_COCHE = 121
EMISION_X_KM_MOTO = 100

cantidade_de_emisions_coche = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM_COCHE
cantidade_de_emisions_moto = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM_MOTO

cantidade_de_emisions = cantidade_de_emisions_coche - cantidade_de_emisions_moto

print('O teu consumo do coche é:', cantidade_de_emisions_coche, 'gC02')
print('O teu consumo da moto é:', cantidade_de_emisions_moto, 'gC02')
print('A moto consume', cantidade_de_emisions, 'menos ca o coche', 'gC02')


# In[ ]:




