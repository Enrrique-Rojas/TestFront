# -*- coding: utf-8 -*-
"""
Created on April 27 2024
@authors: E. ROJAS - K. QUISPE 
"""

import streamlit as st
import pandas as pd
import json
import requests

api = "https://test-0phf.onrender.com"

from streamlit_option_menu import option_menu

showForm = 1

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Menu", ["Inicio", 'Formulario','Datos'],
        icons=['house', 'gear', 'gear'], menu_icon="cast", default_index=1)
    selected

if selected == "Inicio":
    showForm = 1
elif selected == "Formulario":
    showForm = 2
elif selected == "Datos":
    showForm = 3

fields = {
        'gender': 'Género',
        'age': 'Edad',
        'birthDistrict': 'Distrito de nacimiento',
        'currentDistrict': 'Distrito actual',
        'civilStatus': 'Estado civil',
        'typeInstitution': 'Tipo de institución',
        'provenanceLevel': 'Nivel de procedencia',
        'disability': 'Discapacidad',
        'enrolledCycle': 'Ciclo matriculado',
        'repeatedCourses': 'Cursos repetidos',
        'languageLevel': 'Nivel de inglés',
        'computingLevel': 'Nivel de cómputo',
        'isForeign': 'Es extranjero'  
}

genders = [
    'Masculino',
    'Femenino',
]
ages = [
    '16 a 19',
    '20 a 23',
    '24 a 27',
    '28 a 31',
    '32 a más'
]
districts = [
    'Trujillo - Victor Larco Herrera',
    'La Esperanza - Florencia de Mora - El Porvenir',
    'Huanchaco - Laredo - Salaverry - Moche',
    'Simbal - Poroto',
    'Otros'
]
civilStatuss = [
    'Soltero',
    'Casado'
]
typeInstitutions = [
    'Público',
    'Privado'
]
provenanceLevels = [
    'Básico',
    'Secundaria',
    'Secundaria para adultos',
    'Técnico',
    'Superior Universitaria'
]
disabilitys = [
    'Si',
    'No'
]
enrolledCycles = [
    'I - II',
    'III - IV',
    'V - XI',
    'XII - XIII',
    'IX - X'
]
repeatedCoursess = [
    'No tiene',
    '1 a 2',
    '3 a 4',
    '5 a 6',
    '7 a 8'
]
languageLevels = [
    'No tiene',
    '1 a 2',
    '3 a 4',
    '5 a 6',
    '7 a 8'
]
computingLevels = [
    'No tiene',
    '1',
    '2',
    '3',
    '4'
]
isForeigns = [
    'Si',
    'No'
]
listFieldsGeneral = {
    'gender': genders,
    'age':ages,
    'birthDistrict': districts,
    'currentDistrict': districts,
    'civilStatus': civilStatuss,
    'typeInstitution': typeInstitutions,
    'provenanceLevel': provenanceLevels,
    'disability': disabilitys,
    'enrolledCycle': enrolledCycles,
    'repeatedCourses': repeatedCoursess,
    'languageLevel': languageLevels,
    'computingLevel': computingLevels,
    'isForeign': isForeigns
}

adviceGeneral = [
    'Realizar charlas sobre como tu entorno puede influir de forma negativa en tus decisiones',
    'Realizar charlas sobre como tu entorno puede influir de forma negativa en tus decisiones',
    'Realizar charlas sobre como tu entorno puede influir de forma negativa en tus decisiones',
    'Realizar charlas sobre como tu entorno puede influir de forma negativa en tus decisiones',
    'Realizar charlas sobre como tu entorno puede influir de forma negativa en tus decisiones'
]
adviceCivilStatus = [
    'Realizar charlas sobre como tu entorno puede influir de forma negativa en tus decisiones',
    'Realizar charlas sobre organizacion de tiempos'
]
adviceTypeInstitution = [
    'Realizar charlas sobre como tu entorno puede influir de forma negativa en tus decisiones ',
    'Realizar charlas sobre como tu entorno puede influir de forma negativa en tus decisiones'
]
adviceProvenanceLevel = [
    'Realizar charlas sobre como tu entorno puede influir de forma negativa en tus decisiones',
    'Realizar charlas sobre como tu entorno puede influir de forma negativa en tus decisiones',
    'Realizar charlas sobre como tu entorno puede influir de forma negativa en tus decisiones',
    'Realizar charlas sobre como tu entorno puede influir de forma negativa en tus decisiones',
    'Realizar charlas sobre como tu entorno puede influir de forma negativa en tus decisiones'
]
adviceDisability = [
    'El area de tutoria deben motivar a los alumnos y tener pendiente que dificultades tiene dentro de la institución',
    'El area de tutoria debe fomentar y motivar a los alumnos a valorar el esfuerzo de sus padres'
]
adviceRepeatedCourses = [
    'El area de tutoria debe fomentar y motivar a los alumnos a valorar el esfuerzo de sus padres',
    'El area de tutoria debe fomentar y motivar a los alumnos a valorar el esfuerzo de sus padres',
    'El area de tutoria debe fomentar y motivar a los alumnos a valorar el esfuerzo de sus padres',
    'El area de tutoria debe fomentar y motivar a los alumnos a valorar el esfuerzo de sus padres',
    'El area de tutoria debe fomentar y motivar a los alumnos a valorar el esfuerzo de sus padres'
]
adviceLanguageLevel = [
    'El area de tutoria debe enseñarle las ventajas de aprender un nuevo idioma',
    'El area de tutoria debe enseñarle las ventajas de aprender un nuevo idioma',
    'El area de tutoria debe enseñarle las ventajas de aprender un nuevo idioma',
    'El area de tutoria debe enseñarle las ventajas de aprender un nuevo idioma',
    'El area de tutoria debe enseñarle las ventajas de aprender un nuevo idioma'
]
adviceComputingLevel = [
    'El area de tutoria debe enseñarle las ventajas de los cursos complementarios dentro de la carrera',
    'El area de tutoria debe enseñarle las ventajas de los cursos complementarios dentro de la carrera',
    'El area de tutoria debe enseñarle las ventajas de los cursos complementarios dentro de la carrera',
    'El area de tutoria debe enseñarle las ventajas de los cursos complementarios dentro de la carrera',
    'El area de tutoria debe enseñarle las ventajas de los cursos complementarios dentro de la carrera'
]
adviceIsForeign = [
    'El area de tutoria debe enseñarle a los alumnos a adaptarse a esta nueva sociedad',
    'El area de tutoria debe fomentar y motivar a los alumnos a valorar el esfuerzo de sus padres'
]

adviceAccordingAnswer = {
    'gender': adviceGeneral,
    'age':adviceGeneral,
    'birthDistrict': adviceGeneral,
    'currentDistrict': adviceGeneral,
    'civilStatus': adviceCivilStatus,
    'typeInstitution': adviceTypeInstitution,
    'provenanceLevel': adviceProvenanceLevel,
    'disability': adviceDisability,
    'enrolledCycle': adviceGeneral,
    'repeatedCourses': adviceRepeatedCourses,
    'languageLevel': adviceLanguageLevel,
    'computingLevel': adviceComputingLevel,
    'isForeign': adviceIsForeign
}

if(showForm==2):
    st.write("""
             # DESERCIÓN UNIVERSITARIA
             """)

    st.write("""
             ## Datos del estudiante:
             """)
    
    ### Nombre
    name = st.text_input("Apellidos y Nombres", "")

    ###  Genero
    st.write("""
             ### Género:
             """)

    '**1:** Masculino'
    '**2:** Femenino'

    optionGender = st.selectbox(
        'Opciones',
        ['Seleccionar',1, 2],
        key="genders",
        index=0,
        placeholder="Elige una opción")

    'Seleccionado: ', genders[optionGender-1] if optionGender != "Seleccionar" else "Sin seleccionar"

    ###  Edad
    st.write("""
             ### Edad:
             """)

    '**1:** 16 a 19'
    '**2:** 20 a 23'
    '**3:** 24 a 27'
    '**4:** 28 a 31'
    '**5:** 32 a más'

    optionAge = st.selectbox(
        'Opciones',
        ['Seleccionar',1, 2, 3, 4, 5],
        key="ages",
        index=0,
        placeholder="Elige una opción")

    'Seleccionado: ', ages[optionAge-1] if optionAge != "Seleccionar" else "Sin seleccionar"

    ###  Distrito de Nacimiento
    st.write("""
             #### Distrito de Nacimiento:
             """)

    '**1:** Trujillo - Victor Larco Herrera'
    '**2:** La Esperanza - Florencia de Mora - El Porvenir'
    '**3:** Huanchaco - Laredo - Salaverry - Moche'
    '**4:** Simbal - Poroto'
    '**5:** Otros'

    optionBirthDistrict = st.selectbox(
        "Opciones",
        ['Seleccionar',1, 2, 3, 4, 5],
        key="birthDistrict",
        index=0,
        placeholder="Elige una opción")

    'Seleccionado: ', districts[optionBirthDistrict-1] if optionBirthDistrict != "Seleccionar" else "Sin seleccionar"
    
    ###  Distrito Actual
    st.write("""
             #### Distrito Actual:
             """)

    '**1:** Trujillo - Victor Larco Herrera'
    '**2:** La Esperanza - Florencia de Mora - El Porvenir'
    '**3:** Huanchaco - Laredo - Salaverry - Moche'
    '**4:** Simbal - Poroto'
    '**5:** Otros'

    optionCurrentDistrict = st.selectbox(
        "Opciones",
        ['Seleccionar',1, 2, 3, 4, 5],
        key="currentDistrict",
        index=0,
        placeholder="Elige una opción")

    'Seleccionado: ', districts[optionCurrentDistrict-1] if optionCurrentDistrict != "Seleccionar" else "Sin seleccionar"

    ###  Estado Civil
    st.write("""
             ### Estado Civil:
             """)

    '**1:** Soltero'
    '**2:** Casado'

    optionCivilStatus = st.selectbox(
        "Opciones",
        ['Seleccionar',1, 2],
        key="civilStatus",
        index=0,
        placeholder="Elige una opción"
        )

    'Seleccionado: ', civilStatuss[optionCivilStatus-1] if optionCivilStatus != "Seleccionar" else "Sin seleccionar"

    ###  Tipo de Institución
    st.write("""
             ### Tipo de Institución:
             """)

    '**1:** Pública'
    '**2:** Privado'

    optionTypeInstitution = st.selectbox(
        "Opciones",
        ['Seleccionar',1, 2],
        key="typeInstitution",
        index=0,
        placeholder="Elige una opción")

    'Seleccionado: ', typeInstitutions[optionTypeInstitution-1] if optionTypeInstitution != "Seleccionar" else "Sin seleccionar"

    ###  Nivel Educativo de procedencia
    st.write("""
             ### Nivel Educativo de procedencia:
             """)

    '**1:** Básica'
    '**2:** Secundaria'
    '**3:** Secundaria para adultos'
    '**4:** Técnico'
    '**5:** Superior universitaria'

    optionProvenanceLevel = st.selectbox(
        'Opciones',
        ['Seleccionar',1, 2, 3, 4, 5],
        key="provenanceLevel",
        index=0,
        placeholder="Elige una opción")

    'Seleccionado: ', provenanceLevels[optionProvenanceLevel-1] if optionProvenanceLevel != "Seleccionar" else "Sin seleccionar"

    ###  Discapacidad
    st.write("""
             ### Discapacidad:
             """)

    '**1:** Si'
    '**2:** No'

    optionDisability = st.selectbox(
        'Opciones',
        ['Seleccionar', 1, 2],
        key="disability",
        index=0,
        placeholder="Elige una opción")

    'Seleccionado: ', disabilitys[optionDisability-1] if optionDisability != "Seleccionar" else "Sin seleccionar"

    ###  Ciclo matriculado
    st.write("""
             ### Ciclo matriculado:
             """)

    '**1:** I - II'
    '**2:** III - IV'
    '**3:** V - XI'
    '**4:** XII - XIII'
    '**5:** IX - X'

    optionEnrolledCycle = st.selectbox(
        'Opciones',
        ['Seleccionar',1, 2, 3, 4, 5],
        key="enrolledCycle",
        index=0,
        placeholder="Elige una opción")

    'Seleccionado: ', enrolledCycles[optionEnrolledCycle-1] if optionEnrolledCycle != "Seleccionar" else "Sin seleccionar"

    ###  Cursos repetidos
    st.write("""
             ### Cursos repetidos:
             """)

    '**1:** No tiene'
    '**2:** 1 a 2'
    '**3:** 3 a 4'
    '**4:** 5 a 6'
    '**5:** 7 a 8'

    optionRepeatedCourses = st.selectbox(
        'Opciones',
        ['Seleccionar',1, 2, 3, 4, 5],
        key="repeatedCourses",
        index=0,
        placeholder="Elige una opción")

    'Seleccionado: ', repeatedCoursess[optionRepeatedCourses-1] if optionRepeatedCourses != "Seleccionar" else "Sin seleccionar"
    
    ###  Nivel de inglés
    st.write("""
             ### Nivel de inglés:
             """)

    '**1:** No tiene'
    '**2:** 1 a 2'
    '**3:** 3 a 4'
    '**4:** 5 a 6'
    '**5:** 7 a 8'

    optionLanguageLevel = st.selectbox(
        'Opciones',
        ['Seleccionar',1, 2, 3, 4, 5],
        key="languageLevel",
        index=0,
        placeholder="Elige una opción")

    'Seleccionado: ', languageLevels[optionLanguageLevel-1] if optionLanguageLevel != "Seleccionar" else "Sin seleccionar"

    ###  Nivel de cómputo
    st.write("""
             ### Nivel de cómputo:
             """)

    '**1:** No tiene'
    '**2:** 1'
    '**3:** 2'
    '**4:** 3'
    '**5:** 4'

    optionComputingLevel = st.selectbox(
        'Opciones',
        ['Seleccionar',1, 2, 3, 4, 5],
        key="computingLevel",
        index=0,
        placeholder="Elige una opción")

    'Seleccionado: ', computingLevels[optionComputingLevel-1] if optionComputingLevel != "Seleccionar" else "Sin seleccionar"

###  Es extranjero
    st.write("""
             ### Es extranjero:
             """)

    '**1:** Si'
    '**2:** No'

    optionIsForeign = st.selectbox(
        'Opciones',
        ['Seleccionar',1, 2],
        key="isForeign",
        index=0,
        placeholder="Elige una opción")

    'Seleccionado: ', isForeigns[optionIsForeign-1] if optionIsForeign != "Seleccionar" else "Sin seleccionar"

    def save():
        if(
        name == '' or
        optionGender == "Seleccionar" or 
        optionAge == "Seleccionar" or
        optionBirthDistrict == "Seleccionar" or
        optionCurrentDistrict == "Seleccionar" or
        optionCivilStatus == "Seleccionar" or
        optionTypeInstitution == "Seleccionar" or
        optionProvenanceLevel == "Seleccionar" or
        optionDisability == "Seleccionar" or
        optionEnrolledCycle == "Seleccionar" or
        optionRepeatedCourses == "Seleccionar" or
        optionLanguageLevel == "Seleccionar" or
        optionComputingLevel == "Seleccionar" or
        optionIsForeign == "Seleccionar"):
            st.error("Debes llenar todos los campos")
        else:
            data={      
                        "name": name,
                        "gender":optionGender,
                        "age": optionAge,
                        "birthDistrict": optionBirthDistrict ,
                        "currentDistrict": optionCurrentDistrict,
                        "civilStatus": optionCivilStatus,
                        "typeInstitution": optionTypeInstitution,
                        "provenanceLevel": optionProvenanceLevel,
                        "disability": optionDisability,
                        "enrolledCycle": optionEnrolledCycle,
                        "repeatedCourses": optionRepeatedCourses,
                        "languageLevel": optionLanguageLevel,
                        "computingLevel": optionComputingLevel,
                        "isForeign": optionIsForeign,
                    }

            json_data = json.dumps(data)
            r = requests.post(
                    api+'save', data = json_data, headers={"Content-Type":"application/json"}, 
                    timeout=8000
                )

            if r.status_code == 200:
                response_data = r.json()
                if(response_data['success'] == True):
                    predictionAction()
            else:
                st.error('Error de servidor')

    cols = st.columns(4)
    cols[0].button('Guardar', on_click=save)

    if 'showResponse' not in st.session_state:
        st.session_state.showResponse = False

    if 'messageResponse' not in st.session_state:
        st.session_state.messageResponse = ''

    def predictionAction():
        r = requests.post(
                api+'predict', headers={"Content-Type":"application/json"}, 
                timeout=8000)
        messageResponse = ''
        if r.status_code == 200:
            response_data = r.json()
            if(response_data['sucess'] == True):
                #for prediction in response_data['prediction']:
                message = "DESERTARA"
                if(response_data['prediction'][0]['prediction']==0):
                    message = "NO DESERTARA"
                messageResponse= "Alumno: " + response_data['prediction'][0]['name'] + " se predice que " + message
            else:
                messageResponse= "No existe información"
        else:
            messageResponse = 'Error de servidor'
        st.session_state.showResponse = True
        st.session_state.messageResponse = messageResponse

    #st.button('Predecir', on_click=predictionAction)
    if st.session_state.showResponse:
        st.write("""
                 ### Predicción:
                 """)
        st.write(st.session_state.messageResponse)
elif (showForm == 1):    
    st.write("""
             # MÉTRICAS
             """)
    showInformation = False
    #key_field_count = ""
    #key = ""
    #count = 0
    results = {}
    r = requests.post(
                api, headers={"Content-Type":"application/json"}, 
                timeout=8000)
    
    if r.status_code == 200:
        showInformation = True
        response_data = r.json()
        results = response_data
        # results = response_data['result']
        # max_count = response_data['max_count']
        # key = list(max_count.keys())[0]
        # field_count = max_count[key]
        # key_field_count = list(field_count.keys())[0]
        # count = field_count[key_field_count]
    else:
        showInformation = False
        st.error('Error de servidor')

    if(showInformation):
        #st.write("""
        #    #### Exactitud:
        #    """)
        #st.write(results['score_train'])
        st.write("""
            #### Precisión:
            """)
        precision = round(results['precision'] * 100, 2)
        st.write(precision)
        st.write("""
            #### Sensibilidad(Recall):
            """)
        recall = round(results['recall'] * 100, 2)
        st.write(recall)
        st.write("""
            #### Puntaje F1:
            """)
        f1 = round(results['f1'] * 100, 2)
        st.write(f1)
        #st.write("""
        #    #### Área bajo la curva:
        #    """)
        #st.write(results['auc'])
        # st.write("""
        #      ## La pregunta que mas desertados tiene es:
        #      """)
        # st.write(fields[key])
        # st.write("""
        #      #### Con la respuesta:
        #      """)
        # st.write(listFieldsGeneral[key][(int(key_field_count)-1)]+ " con un total de "+ str(count) +" respuesta(s)")

        # second_key = results[1][0]
        # second_key_field_count = list(results[1][1].keys())[0]
        # second_count = results[1][1][second_key_field_count]
        
        # st.write("""
        #      ## La segunda pregunta que mas desertados tiene es:
        #      """)
        # st.write(fields[second_key])
        # st.write("""
        #      #### Con la respuesta:
        #      """)
        # st.write(listFieldsGeneral[second_key][(int(second_key_field_count)-1)]+ " con un total de "+ str(second_count) +" respuesta(s)")

        # third_key = results[2][0]
        # third_key_field_count = list(results[2][1].keys())[0]
        # third_count = results[2][1][third_key_field_count]
        
        # st.write("""
        #      ## La tercera pregunta que mas desertados tiene es:
        #      """)
        # st.write(fields[third_key])
        # st.write("""
        #      #### Con la respuesta:
        #      """)
        # st.write(listFieldsGeneral[third_key][(int(third_key_field_count)-1)]+ " con un total de "+ str(third_count) +" respuesta(s)")
else:
    st.write("""
             # LISTADO DE ALUMNOS
             """)
    showList = False
    results = {}
    r = requests.post(
                api+'/list', headers={"Content-Type":"application/json"}, 
                timeout=8000)
    
    if r.status_code == 200:
        showList = True
        response_data = r.json()
        results = response_data['result']
    else:
        showList = False
        st.error('Error de servidor')

    if(showList):
        # Crear un DataFrame con los datos
        df = pd.DataFrame(results, columns=['Nombre', 'Ciclo', 'Fecha Registro','Desertará'])

        # Convertir el código de ciclo a texto descriptivo
        ciclo_dict = {
            1: 'I-II',
            2: 'III-IV',
            3: 'V-VI',
            4: 'VII-VIII',
            5: 'IX-X'
        }
        df['Ciclo'] = df['Ciclo'].map(ciclo_dict)
        df['Fecha Registro'] = df['Fecha Registro'].str.replace('T', ' ')
        df['Desertará'] = df['Desertará'].map({1: 'Sí', 0: 'No'})

        # Mostrar los datos en una tabla con Streamlit
        st.dataframe(df, width=900, height=600)