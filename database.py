import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection
from streamlit_image_select import image_select


#Questo 

st.set_page_config(page_icon="logo.png")
logo = "logo.png"
# Controllo IF
is_aut = False
is_somma_valori = False

# Carica i dati
file_path = "lista_email.xlsx"
df = pd.read_excel(file_path)

def authenticate(email, password):
    # Verifica se esiste una riga con l'email e la password fornite
    return not df[(df['Lista'] == email) & (df['Password'] == password)].empty

# Creazione della colonna per il logo nella sidebar
sidebar_col = st.sidebar.image(logo, use_column_width=True)

# Campi di input per email e password nella sidebar
email = st.sidebar.text_input("Email:")
password = st.sidebar.text_input("Password:", type="password")

# Bottone di accesso nella sidebar
if st.sidebar.button("Login"):
    # Controllo di autenticazione
    if authenticate(email, password):
        st.sidebar.success("Accesso riuscito!")
        is_aut = True
        # Qui puoi aggiungere ulteriori sezioni del tuo codice per il contenuto principale
    else:
        st.sidebar.error("Accesso fallito. Verifica email e password.")




conn = st.connection("gsheets", type=GSheetsConnection)

# Lettura dei dati esistenti da Google Sheets
existing_data = conn.read(worksheet="Foglio1", usecols=list(range(4)), ttl=5)
existing_data = existing_data.dropna(how="all")





giocatori = [
             {"nome": "Annalisa Cantatore", "crediti": 7},
    {"nome": "Anton Luca Leggiero", "crediti": 9},
    {"nome": "Camilla Marcone", "crediti": 3},
    {"nome": "Castrese Izzo", "crediti": 5},
    {"nome": "Chiara Iannicelli", "crediti": 6},
    {"nome": "Clarissa Fionda", "crediti": 4},
    {"nome": "Daniele Fotso", "crediti": 5},
    {"nome": "Edoardo Cesaroni", "crediti": 6},
    {"nome": "Elena Kiseleva", "crediti": 7},
    {"nome": "Eleonora Carta", "crediti": 3},
    {"nome": "Emanuele Dias Fernandes", "crediti": 5},
    {"nome": "Eugenio Francesco Pensa", "crediti": 4},
    {"nome": "Fabio Ciccarelli", "crediti": 3},
    {"nome": "Fabio Di Corpo", "crediti": 7},
    {"nome": "Federica Lavini", "crediti": 5},
    {"nome": "Flavia Sarcinelli", "crediti": 11},
    {"nome": "Francesco Antonelli", "crediti": 9},
    {"nome": "Francesco Arpino", "crediti": 9},
    {"nome": "Francesco Cartisano", "crediti": 5},
    {"nome": "Francesco Tarantino", "crediti": 9},
    {"nome": "Francesco Tonnarini", "crediti": 8},
    {"nome": "Gabriele La Motta", "crediti": 8},
    {"nome": "Giacomo Bacchetta", "crediti": 5},
    {"nome": "Giada De Cupis", "crediti": 9},
    {"nome": "Gianpio Tomasso", "crediti": 1},
    {"nome": "Giorgia Scaglione", "crediti": 1},
    {"nome": "Giovanni Caldarini", "crediti": 1},
    {"nome": "Giovanni Perugini", "crediti": 11},
    {"nome": "Giulia Arcifa", "crediti": 2},
    {"nome": "Giulia Di Giuseppantonio", "crediti": 7},
    {"nome": "Giulia Milone", "crediti": 7},
    {"nome": "Giulia Ragazzo", "crediti": 8},
    {"nome": "Giuseppe Della Greca", "crediti": 9},
    {"nome": "Giuseppe Maiese", "crediti": 9},
    {"nome": "Giuseppe Pio Petillo", "crediti": 1},
    {"nome": "Graziana Antonacci", "crediti": 9},
    {"nome": "Linda Lezzi", "crediti": 4},
    {"nome": "Lorenzo Brecevich", "crediti": 5},
    {"nome": "Lorenzo Saccucci", "crediti": 6},
    {"nome": "Ludovico Pomanti", "crediti": 8},
    {"nome": "Marco Bellomo", "crediti": 7},
    {"nome": "Marco Ponzuoli", "crediti": 8},
    {"nome": "Matteo Cargini", "crediti": 1},
    {"nome": "Michela Casale", "crediti": 6},
    {"nome": "Michele Vitulli", "crediti": 6},
    {"nome": "Mihai Rosu", "crediti": 7},
    {"nome": "Pietro Colaguori", "crediti": 5},
    {"nome": "Rebecca Villani", "crediti": 1},
    {"nome": "Riccardo Cegna", "crediti": 4},
    {"nome": "Roberta Ioffredo", "crediti": 11},
    {"nome": "Sara Valletta", "crediti": 11},
    {"nome": "Silvia Ricciarello", "crediti": 4},
    {"nome": "Stefano Candela", "crediti": 8},
    {"nome": "Valentina Alfano", "crediti": 7},
    {"nome": "Valentina Giuliani", "crediti": 9},
    {"nome": "Valentina Nerone", "crediti": 10},
    {"nome": "Valerio Fiorentino", "crediti": 7},
    {"nome": "Valerio Scansalegna", "crediti": 8},
    {"nome": "Victoria Martellotta", "crediti": 4},
        ]



def seleziona_giocatori():

    #team_options = [ "", "BD", "Audit", "Marketing"]
    #selected_team = st.selectbox("Selezione l'area", options=team_options, index=None)


    #mandato_options = ["", "Mandato I", "Mandato II "]
    giocatori_selezionati = []
    crediti_totali = 0
    numeri = 0 
    while crediti_totali < 20:
        giocatore_scelto = st.selectbox("Seleziona un giocatore:", [g["nome"] for g in giocatori], key=crediti_totali)

        for giocatore in giocatori:
            if giocatore["nome"] == giocatore_scelto:
                crediti_totali += giocatore["crediti"]
                giocatori_selezionati.append(giocatore)
                giocatori.remove(giocatore)
                break

        st.write(f"Hai ancora {20-crediti_totali} Crediti ")

        if crediti_totali <= 20:
            continua_selezione = st.checkbox("Vuoi selezionare un altro giocatore?", key=crediti_totali + 1)
            if continua_selezione:
                numeri += 1
            if not continua_selezione:
                break

    st.sidebar.write("Il tuo Team:")
    for giocatore in giocatori_selezionati:
        st.sidebar.write(f"- {giocatore['nome']} ({giocatore['crediti']} crediti)")

    submit_button = st.button("Aggiorna il team")

    if submit_button :
        # Ottieni l'indice della riga corrispondente all'email fornita
        index_to_update = existing_data[existing_data['Email'] == email].index

        if crediti_totali < 20:
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
    st.title("FantaJesapper")
    
    seleziona_giocatori()
    

if __name__ == "__main__":
    main()

























