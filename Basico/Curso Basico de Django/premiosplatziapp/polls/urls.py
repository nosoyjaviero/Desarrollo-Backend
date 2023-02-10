from django.shortcuts import render
from django.urls import path
from . import views 

# la razon de que sirva app_name= "polls" evitar confuciones futuras si yo en 
# premiosplatzi.urls.py cambio la url de "polls" por algun otro nombre que se me ocurra ("preguntas")
#todo el route se mantenie. 
# Pero aparacera el url nuevo 
app_name= "polls" #namespace

#para que esto funcione el archivo html debe 
# llevar 'polls:variable'. Variable es el nombre de la variable name que se encuentra en cada una de las path que se encuentran aca abajoo en pathpatterns . ejm path(name= 'detail')'. Entonces de debe ver asi con el ejemplo de detail: 
# 'polls:detail'



# la url se vera asi  
# http://127.0.0.1:8000/preguntas
# NombreDeLaURL_PuestaEn_premiosplatiziapp<int:id>/"<int:id>/detail/naruto"
# ejemplo:
# http://127.0.0.1:8000/preguntas/1//detail/naruto





urlpatterns =[
  # El archivo index,html se ejecto al acceder a la ruta raiz. ejectuta el codigo de views.index y muestra las preguntas. 
    
    # Function base views  
    # path ("", views.index, name="index"),
    # Function generic views
    
    path ("", views.IndexView.as_view(), name="index"),
    
      
    #   y dentro de este html atraves de la linea 
     # href="{% url 'polls:detail' question.id %}" 
    # accede al codigo de views.detail y crea un href (ojo no es el texto si no el hipervinculo)
     
     # Lo hacepreguntando por app_name= "polls" y busca finalmene a name='datail' en urlpatterns en su respectivo path. Con esto ejecuta el codigo de 
    # views.detail y y asi crea la ruta de los
     
    
# la url se vera asi 
# NombreDeLaURL_PuestaEn_premiosplatiziapp<int:id>/"<int:id>/detail/naruto"
# ejemplo:
# http://127.0.0.1:8000/preguntas/1//detail/naruto

#/detail/naruto esta de sobra. Sirve para mostrar lo dinamico que es esto.
#Bien solo puede ir <int:id>/ ya que se acede a este atraves del name

# Pero si hago esto con hardcoding debo poner  <int:id>/detail/

    
    
# Function base views
    # path ("<int:id>/", views.detail, name="detail"),
      # Function generic views
      path ("<int:pk>/", views.DetailView.as_view(), name="detail"),
    
    # Function generic views
    # path ("<int:id>/results", views.results, name="results"),
   
    path ("<int:pk>/results", views.ResultsView.as_view(), name="results"),
    
    # Function base views
    path ("<int:id>/vote", views.vote, name="vote"),
    
    
    
]