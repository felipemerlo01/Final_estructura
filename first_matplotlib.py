import matplotlib.pyplot as plt

# Plot
"""
year = [1950,1970,1990,2010] 
pop = [2.519,3.692,5.263,6.972]
plt.plot(year,pop) # El primero es eje X, el segundo eje Y
plt.show() # Es necesario asi aparece
"""

# Scatter plot
"""
year = [1950,1970,1990,2010] 
pop = [2.519,3.692,5.263,6.972]
plt.scatter(year,pop) # la diferencia es que no conecta con una linea los puntos
plt.show() # Es necesario asi aparece
"""

# Histogram
# Sirve para explorar un dataset y darte ideas de la distribución
"""
values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values, bins = 3) # bins indica la cantidad de columnas que queres, es 10 x default
plt.show()
# plt.clf() lo borra y resetea
"""

# Customization
year = [1950,1970,1990,2010] 
pop = [2.519,3.692,5.263,6.972]

plt.plot(year,pop) 
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("World population predictions")
plt.yticks([0,2,4,6,8,10],["0","2B","4B","6B","8B","10B"]) #Arranca desde 0,el segundo argumento es opcional, los nombres

plt.show() 
# plt.scatter(gdp_cap, life_exp, s = pop) -- La lista s es tamaños de las burbujas
# plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c=col, alpha = 0.8) -- col es color, alpha es opacidad 
# plt.grid(True) -- shows grid
"""
"""


