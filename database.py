import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection



#Questo 

st.set_page_config(page_icon="logo.png")


background_image = '''
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("");
    background-size: 100vw 100vh;  
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
'''


st.markdown(background_image, unsafe_allow_html=True)


logo = "logo2.png"
# Controllo IF
is_aut = False
is_somma_valori = False
# Creazione della colonna per il logo nella sidebar
sidebar_col = st.sidebar.image(logo, use_column_width=True)

# Campo di input per l'email nella sidebar
email = st.sidebar.text_input("Email:")

# Bottone di accesso nella sidebar
if st.sidebar.button("Accedi"):
        st.sidebar.success(f"Benvenut {email}")
        is_aut = True
       
elif not is_aut:
     st.warning("Inserire Email ") 



conn = st.connection("gsheets", type=GSheetsConnection)

# Lettura dei dati esistenti da Google Sheets
existing_data = conn.read(worksheet="Foglio1", usecols=list(range(4)), ttl=5)
existing_data = existing_data.dropna(how="all")


giocatori = [
    {"nome": "Alessia Fiasca(5 crediti)", "crediti": 5},
    {"nome": "Anita Gentilini (5 crediti)", "crediti": 5},
    {"nome": "Alessandro Belotti (5 crediti)", "crediti": 5},
    {"nome": "Alessandro D'Annibale (5 crediti)", "crediti": 5},
    {"nome": "Anatolie Russu (6 crediti)", "crediti": 6},
    {"nome": "Andrea Sapone (10 crediti)", "crediti": 10},
    {"nome": "Annalisa Cantatore (5 crediti)", "crediti": 5},
    {"nome": "Anton Luca Leggiero (5 crediti)", "crediti": 5},
    {"nome": "Camilla Marcone (5 crediti)", "crediti": 5},
    {"nome": "Castrese Izzo (5 crediti)", "crediti": 5},
    {"nome": "Chiara Iannicelli (5 crediti)", "crediti": 5},
    {"nome": "Clarissa Fionda (5 crediti)", "crediti": 5},
    {"nome": "Daniele Fotso (5 crediti)", "crediti": 5},
    {"nome": "Edoardo Cesaroni (5 crediti)", "crediti": 5},
    {"nome": "Elena Kiseleva (5 crediti)", "crediti": 5},
    {"nome": "Eleonora Carta (5 crediti)", "crediti": 5},
    {"nome": "Emanuele Dias Fernandes (8 crediti)", "crediti": 8},
    {"nome": "Eugenio Francesco Pensa (5 crediti)", "crediti": 5},
    {"nome": "Fabio Ciccarelli (8 crediti)", "crediti": 8},
    {"nome": "Fabio Di Corpo (5 crediti)", "crediti": 5},
    {"nome": "Federica Lavini (6 crediti)", "crediti": 6},
    {"nome": "Flavia Sarcinelli (10 crediti)", "crediti": 10},
    {"nome": "Francesco Antonelli (5 crediti)", "crediti": 5},
    {"nome": "Francesco Arpino (9 crediti)", "crediti": 9},
    {"nome": "Francesco Cartisano (5 crediti)", "crediti": 5},
    {"nome": "Francesco Tarantino (8 crediti)", "crediti": 8},
    {"nome": "Francesco Gargano (5 crediti)", "crediti": 5},
    {"nome": "Francesco Tonnarini (6 crediti)", "crediti": 6},
    {"nome": "Gabriele La Motta (6 crediti)", "crediti": 6},
    {"nome": "Giacomo Bacchetta (5 crediti)", "crediti": 5},
    {"nome": "Giada De Cupis (5 crediti)", "crediti": 5},
    {"nome": "Giorgia Scaglione (5 crediti)", "crediti": 5},
    {"nome": "Giovanni Caldarini (5 crediti)", "crediti": 5},
    {"nome": "Giovanni Perugini (10 crediti)", "crediti": 10},
    {"nome": "Giulia Arcifa (5 crediti)", "crediti": 5},
    {"nome": "Giulia Di Giuseppantonio (5 crediti)", "crediti": 5},
    {"nome": "Giulia Milone (5 crediti)", "crediti": 5},
    {"nome": "Giulia Ragazzo (5 crediti)", "crediti": 5},
    {"nome": "Giuseppe Della Greca (5 crediti)", "crediti": 5},
    {"nome": "Giuseppe Maiese (8 crediti)", "crediti": 8},
    {"nome": "Giuseppe Pio Petillo (5 crediti)", "crediti": 5},
    {"nome": "Graziana Antonacci (6 crediti)", "crediti": 6},
    {"nome": "Linda Lezzi (5 crediti)", "crediti": 5},
    {"nome": "Lorenzo Brecevich (5 crediti)", "crediti": 5},
    {"nome": "Lorenzo Saccucci (7 crediti)", "crediti": 7},
    {"nome": "Ludovico Pomanti (8 crediti)", "crediti": 8},
    {"nome": "Marco Bellomo (5 crediti)", "crediti": 5},
    {"nome": "Marco Ponzuoli (5 crediti)", "crediti": 5},
    {"nome": "Matteo Cargini (5 crediti)", "crediti": 5},
    {"nome": "Michela Casale (5 crediti)", "crediti": 5},
    {"nome": "Michele Vitulli (8 crediti)", "crediti": 8},
    {"nome": "Mihai Rosu (5 crediti)", "crediti": 5},
    {"nome": "Pietro Colaguori (5 crediti)", "crediti": 5},
    {"nome": "Rebecca Villani (5 crediti)", "crediti": 5},
    {"nome": "Riccardo Cegna (5 crediti)", "crediti": 5},
    {"nome": "Roberta Ioffredo (10 crediti)", "crediti": 10},
    {"nome": "Sara Valletta (10 crediti)", "crediti": 10},
    {"nome": "Silvia Ricciarello (5 crediti)", "crediti": 5},
    {"nome": "Stefano Candela (7 crediti)", "crediti": 7},
    {"nome": "Valentina Alfano (8 crediti)", "crediti": 8},
    {"nome": "Valentina Giuliani (6 crediti)", "crediti": 6},
    {"nome": "Valentina Nerone (8 crediti)", "crediti": 8},
    {"nome": "Valerio Fiorentino (5 crediti)", "crediti": 5},
    {"nome": "Valerio Scansalegna (5 crediti)", "crediti": 5},
    {"nome": "Victoria Martellotta (7 crediti)", "crediti": 7},
]


#agg nome su 

def seleziona_giocatori():
    
    st.title("FantaJesaper")
    giocatori_selezionati = []
    crediti_totali = 0
    numeri = 0 
    
    widget_counter = 0

    while crediti_totali < 25:
        giocatori_disponibili = [g for g in giocatori if g["crediti"] <= (20 - crediti_totali)]
        giocatore_scelto = st.selectbox("Seleziona un giocatore:", [g["nome"] for g in giocatori_disponibili], key=f"giocatore_select_{widget_counter}", index=None)

        for giocatore in giocatori_disponibili:
            if giocatore["nome"] == giocatore_scelto:
                crediti_totali += giocatore["crediti"]
                giocatori_selezionati.append(giocatore)
                giocatori.remove(giocatore)
                break

        st.write(f"Hai ancora {25-crediti_totali} Crediti ")

        # Creazione di una variabile che cambia ogni volta che il checkbox viene premuto
        continua_selezione = st.checkbox("Vuoi selezionare un altro giocatore?", key=f"continua_selezione_{widget_counter + 1}")

        if continua_selezione:
            numeri += 1

        #Aumento 
        widget_counter += 1

        if not continua_selezione:
            break

    st.write("Il tuo Team:")
    for giocatore in giocatori_selezionati:
        st.write(f"- {giocatore['nome']}")

    submit_button = st.button("Aggiorna il team")

    if submit_button :
        # Ottieni l'indice della riga corrispondente all'email fornita
        index_to_update = existing_data[existing_data['Email'] == email].index

        if crediti_totali <= 20:
            # Ottieni i nomi dei giocatori selezionati come una lista di stringhe
            giocatori_selezionati_nomi = [giocatore["nome"] for giocatore in giocatori_selezionati]
            # Converti la lista di nomi in una stringa separata da virgole
            giocatori_selezionati_stringa = ", ".join(giocatori_selezionati_nomi)

            # Aggiorna solo la colonna "Giocatore II" della riga corrispondente
            existing_data.loc[index_to_update, "Giocatore I "] = giocatori_selezionati_stringa
            conn.update(worksheet="Foglio1", data=existing_data)
            st.success("Foglio di Google Sheets aggiornato con successo!")
        else:
            st.warning("I giocatori selezionati hanno un costo maggiore di quanto puoi spendere")




def main(): 

    seleziona_giocatori()
    

if __name__ == "__main__":
    main()


