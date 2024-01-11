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

#Viola scuro
#7a5ea8



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
       
else:
     st.warning("Inserire Email ") 
    

conn = st.connection("gsheets", type=GSheetsConnection)

# Lettura dei dati esistenti da Google Sheets
existing_data = conn.read(worksheet="Foglio1", usecols=list(range(4)), ttl=5)
existing_data = existing_data.dropna(how="all")


giocatori = [
    
    {"nome": "Annalisa Cantatore (7 crediti)", "crediti": 7},
    {"nome": "Anton Luca Leggiero (9 crediti)", "crediti": 9},
    {"nome": "Camilla Marcone (3 crediti)", "crediti": 3},
    {"nome": "Castrese Izzo (5 crediti)", "crediti": 5},
    {"nome": "Chiara Iannicelli (6 crediti)", "crediti": 6},
    {"nome": "Clarissa Fionda (4 crediti)", "crediti": 4},
    {"nome": "Daniele Fotso (5 crediti)", "crediti": 5},
    {"nome": "Edoardo Cesaroni (6 crediti)", "crediti": 6},
    {"nome": "Elena Kiseleva (7 crediti)", "crediti": 7},
    {"nome": "Eleonora Carta (3 crediti)", "crediti": 3},
    {"nome": "Emanuele Dias Fernandes (5 crediti)", "crediti": 5},
    {"nome": "Eugenio Francesco Pensa (4 crediti)", "crediti": 4},
    {"nome": "Fabio Ciccarelli (3 crediti)", "crediti": 3},
    {"nome": "Fabio Di Corpo (7 crediti)", "crediti": 7},
    {"nome": "Federica Lavini (5 crediti)", "crediti": 5},
    {"nome": "Flavia Sarcinelli (11 crediti)", "crediti": 11},
    {"nome": "Francesco Antonelli (9 crediti)", "crediti": 9},
    {"nome": "Francesco Arpino (9 crediti)", "crediti": 9},
    {"nome": "Francesco Cartisano (5 crediti)", "crediti": 5},
    {"nome": "Francesco Tarantino (9 crediti)", "crediti": 9},
    {"nome": "Francesco Tonnarini (8 crediti)", "crediti": 8},
    {"nome": "Gabriele La Motta (8 crediti)", "crediti": 8},
    {"nome": "Giacomo Bacchetta (5 crediti)", "crediti": 5},
    {"nome": "Giada De Cupis (9 crediti)", "crediti": 9},
    {"nome": "Gianpio Tomasso (1 credito)", "crediti": 1},
    {"nome": "Giorgia Scaglione (1 credito)", "crediti": 1},
    {"nome": "Giovanni Caldarini (1 credito)", "crediti": 1},
    {"nome": "Giovanni Perugini (11 crediti)", "crediti": 11},
    {"nome": "Giulia Arcifa (2 crediti)", "crediti": 2},
    {"nome": "Giulia Di Giuseppantonio (7 crediti)", "crediti": 7},
    {"nome": "Giulia Milone (7 crediti)", "crediti": 7},
    {"nome": "Giulia Ragazzo (8 crediti)", "crediti": 8},
    {"nome": "Giuseppe Della Greca (9 crediti)", "crediti": 9},
    {"nome": "Giuseppe Maiese (9 crediti)", "crediti": 9},
    {"nome": "Giuseppe Pio Petillo (1 credito)", "crediti": 1},
    {"nome": "Graziana Antonacci (9 crediti)", "crediti": 9},
    {"nome": "Linda Lezzi (4 crediti)", "crediti": 4},
    {"nome": "Lorenzo Brecevich (5 crediti)", "crediti": 5},
    {"nome": "Lorenzo Saccucci (6 crediti)", "crediti": 6},
    {"nome": "Ludovico Pomanti (8 crediti)", "crediti": 8},
    {"nome": "Marco Bellomo (7 crediti)", "crediti": 7},
    {"nome": "Marco Ponzuoli (8 crediti)", "crediti": 8},
    {"nome": "Matteo Cargini (1 credito)", "crediti": 1},
    {"nome": "Michela Casale (6 crediti)", "crediti": 6},
    {"nome": "Michele Vitulli (6 crediti)", "crediti": 6},
    {"nome": "Mihai Rosu (7 crediti)", "crediti": 7},
    {"nome": "Pietro Colaguori (5 crediti)", "crediti": 5},
    {"nome": "Rebecca Villani (1 credito)", "crediti": 1},
    {"nome": "Riccardo Cegna (4 crediti)", "crediti": 4},
    {"nome": "Roberta Ioffredo (11 crediti)", "crediti": 11},
    {"nome": "Sara Valletta (11 crediti)", "crediti": 11},
    {"nome": "Silvia Ricciarello (4 crediti)", "crediti": 4},
    {"nome": "Stefano Candela (8 crediti)", "crediti": 8},
    {"nome": "Valentina Alfano (7 crediti)", "crediti": 7},
    {"nome": "Valentina Giuliani (9 crediti)", "crediti": 9},
    {"nome": "Valentina Nerone (10 crediti)", "crediti": 10},
    {"nome": "Valerio Fiorentino (7 crediti)", "crediti": 7},
    {"nome": "Valerio Scansalegna (8 crediti)", "crediti": 8},
    {"nome": "Victoria Martellotta (4 crediti)", "crediti": 4},
]


#agg nome su 

def seleziona_giocatori():
    
    st.title("FantaJesaper")
    giocatori_selezionati = []
    crediti_totali = 0
    numeri = 0 
    
    widget_counter = 0

    while crediti_totali < 20:
        giocatori_disponibili = [g for g in giocatori if g["crediti"] <= (20 - crediti_totali)]
        giocatore_scelto = st.selectbox("Seleziona un giocatore:", [g["nome"] for g in giocatori_disponibili], key=f"giocatore_select_{widget_counter}", index=None)

        for giocatore in giocatori_disponibili:
            if giocatore["nome"] == giocatore_scelto:
                crediti_totali += giocatore["crediti"]
                giocatori_selezionati.append(giocatore)
                giocatori.remove(giocatore)
                break

        st.write(f"Hai ancora {20-crediti_totali} Crediti ")

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


