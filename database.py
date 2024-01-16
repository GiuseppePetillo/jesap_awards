import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import os



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


giocatori = [
    {"nome": "Alessandro Belotti (5 crediti)", "crediti": 5, "foto": 'alessandro_belotti.jpg'},
    {"nome": "Alessia Fiasca (5 crediti)", "crediti": 5, "foto": 'alessia_fiasca.jpg'},
    {"nome": "Anatolie Russu (6 crediti)", "crediti": 6, "foto": 'anatolie_russu.jpg'},
    {"nome": "Andrea Sapone (10 crediti)", "crediti": 10, "foto": 'andrea_sapone.jpg'},
    {"nome": "Anita Gentilini (5 crediti)", "crediti": 5, "foto": 'anita_gentilini.jpg'},
    {"nome": "Alessandro D'Annibale (5 crediti)", "crediti": 5, "foto": 'alessandro_dannibale.jpg'},
    {"nome": "Annalisa Cantatore (5 crediti)", "crediti": 5, "foto": 'annalisa_cantatore.jpg'},
    {"nome": "Anton Luca Leggiero (5 crediti)", "crediti": 5, "foto": 'antonluca_leggiero.jpg'},
    {"nome": "Camilla Marcone (5 crediti)", "crediti": 5, "foto": 'camilla_marcone.jpg'},
    {"nome": "Castrese Izzo (5 crediti)", "crediti": 5, "foto": 'castrese_izzo.jpg'},
    {"nome": "Chiara Iannicelli (5 crediti)", "crediti": 5, "foto": 'chiara_iannicelli.jpg'},
    {"nome": "Clarissa Fionda (5 crediti)", "crediti": 5, "foto": 'clarissa_fionda.jpg'},
    {"nome": "Daniele Fotso (5 crediti)", "crediti": 5, "foto": 'daniele_fotso.jpg'},
    {"nome": "Edoardo Cesaroni (5 crediti)", "crediti": 5, "foto": 'edoardo_cesaroni.jpg'},
    {"nome": "Elena Kiseleva (5 crediti)", "crediti": 5, "foto": 'elena_kiseleva.jpg'},
    {"nome": "Eleonora Carta (5 crediti)", "crediti": 5, "foto": 'eleonora_carta.jpg'},
    {"nome": "Emanuele Dias Fernandes (8 crediti)", "crediti": 8, "foto": 'emanuele_dias_fernandes.jpg'},
    {"nome": "Eugenio Francesco Pensa (5 crediti)", "crediti": 5, "foto": 'eugenio_francesco_pensa.jpg'},
    {"nome": "Fabio Ciccarelli (8 crediti)", "crediti": 8, "foto": 'fabio_ciccarelli.jpg'},
    {"nome": "Fabio Di Corpo (5 crediti)", "crediti": 5, "foto": 'fabio_di_corpo.jpg'},
    {"nome": "Federica Lavini (6 crediti)", "crediti": 6, "foto": 'federica_lavini.jpg'},
    {"nome": "Flavia Sarcinelli (10 crediti)", "crediti": 10, "foto": 'flavia_sarcinelli.jpg'},
    {"nome": "Francesco Antonelli (5 crediti)", "crediti": 5, "foto": 'francesco_antonelli.jpg'},
    {"nome": "Francesco Arpino (9 crediti)", "crediti": 9, "foto": 'francesco_arpino.jpg'},
    {"nome": "Francesco Cartisano (5 crediti)", "crediti": 5, "foto": 'francesco_cartisano.jpg'},
    {"nome": "Francesco Tarantino (8 crediti)", "crediti": 8, "foto": 'francesco_tarantino.jpg'},
    {"nome": "Francesco Gargano (5 crediti)", "crediti": 5, "foto": 'francesco_gargano.jpg'},
    {"nome": "Francesco Tonnarini (6 crediti)", "crediti": 6, "foto": 'francesco_tonnarini.jpg'},
    {"nome": "Gabriele La Motta (6 crediti)", "crediti": 6, "foto": 'gabriele_la_motta.jpg'},
    {"nome": "Giacomo Bacchetta (5 crediti)", "crediti": 5, "foto": 'giacomo_bacchetta.jpg'},
    {"nome": "Giada De Cupis (5 crediti)", "crediti": 5, "foto": 'giada_de_cupis.jpg'},
    {"nome": "Giorgia Scaglione (5 crediti)", "crediti": 5, "foto": 'giorgia_scaglione.jpg'},
    {"nome": "Giovanni Caldarini (5 crediti)", "crediti": 5, "foto": 'giovanni_caldarini.jpg'},
    {"nome": "Giovanni Perugini (10 crediti)", "crediti": 10, "foto": 'giovanni_perugini.jpg'},
    {"nome": "Giulia Arcifa (5 crediti)", "crediti": 5, "foto": 'giulia_arcifa.jpg'},
    {"nome": "Giulia Di Giuseppantonio (5 crediti)", "crediti": 5, "foto": 'giulia_di_giuseppantonio.jpg'},
    {"nome": "Giulia Milone (5 crediti)", "crediti": 5, "foto": 'giulia_milone.jpg'},
    {"nome": "Giulia Ragazzo (5 crediti)", "crediti": 5, "foto": 'giulia_ragazzo.jpg'},
    {"nome": "Giuseppe Della Greca (5 crediti)", "crediti": 5, "foto": 'giuseppe_della_greca.jpg'},
    {"nome": "Giuseppe Maiese (8 crediti)", "crediti": 8, "foto": 'giuseppe_maiese.jpg'},
    {"nome": "Giuseppe Pio Petillo (5 crediti)", "crediti": 5, "foto": 'giuseppe_pio_petillo.jpg'},
    {"nome": "Graziana Antonacci (6 crediti)", "crediti": 6, "foto": 'graziana_antonacci.jpg'},
    {"nome": "Linda Lezzi (5 crediti)", "crediti": 5, "foto": 'linda_lezzi.jpg'},
    {"nome": "Lorenzo Brecevich (5 crediti)", "crediti": 5, "foto": 'lorenzo_brecevich.jpg'},
    {"nome": "Lorenzo Saccucci (7 crediti)", "crediti": 7, "foto": 'lorenzo_saccucci.jpg'},
    {"nome": "Ludovico Pomanti (8 crediti)", "crediti": 8, "foto": 'ludovico_pomanti.jpg'},
    {"nome": "Marco Bellomo (5 crediti)", "crediti": 5, "foto": 'marco_bellomo.jpg'},
    {"nome": "Marco Ponzuoli (5 crediti)", "crediti": 5, "foto": 'marco_ponzuoli.jpg'},
    {"nome": "Matteo Cargini (5 crediti)", "crediti": 5, "foto": 'matteo_cargini.jpg'},
    {"nome": "Michela Casale (5 crediti)", "crediti": 5, "foto": 'michela_casale.jpg'},
    {"nome": "Michele Vitulli (8 crediti)", "crediti": 8, "foto": 'michele_vitulli.jpg'},
    {"nome": "Mihai Rosu (5 crediti)", "crediti": 5, "foto": 'mihai_rosu.jpg'},
    {"nome": "Pietro Colaguori (5 crediti)", "crediti": 5, "foto": 'pietro_colaguori.jpg'},
    {"nome": "Rebecca Villani (5 crediti)", "crediti": 5, "foto": 'rebecca_villani.jpg'},
    {"nome": "Riccardo Cegna (5 crediti)", "crediti": 5, "foto": 'riccardo_cegna.jpg'},
    {"nome": "Roberta Ioffredo (10 crediti)", "crediti": 10, "foto": 'roberta_ioffredo.jpg'},
    {"nome": "Sara Valletta (10 crediti)", "crediti": 10, "foto": 'sara_valletta.jpg'},
    {"nome": "Silvia Ricciarello (5 crediti)", "crediti": 5, "foto": 'silvia_ricciarello.jpg'},
    {"nome": "Stefano Candela (7 crediti)", "crediti": 7, "foto": 'stefano_candela.jpg'},
    {"nome": "Valentina Alfano (8 crediti)", "crediti": 8, "foto": 'valentina_alfano.jpg'},
    {"nome": "Valentina Giuliani (6 crediti)", "crediti": 6, "foto": 'valentina_giuliani.jpg'},
    {"nome": "Valentina Nerone (8 crediti)", "crediti": 8, "foto": 'valentina_nerone.jpg'},
    {"nome": "Valerio Fiorentino (5 crediti)", "crediti": 5, "foto": 'valerio_fiorentino.jpg'},
    {"nome": "Valerio Scansalegna (5 crediti)", "crediti": 5, "foto": 'valerio_scansalegna.jpg'},
    {"nome": "Victoria Martellotta (7 crediti)", "crediti": 7, "foto": 'victoria_martellotta.jpg'},
]


st.markdown(background_image, unsafe_allow_html=True)


conn = st.connection("gsheets", type=GSheetsConnection)

# Lettura dei dati esistenti da Google Sheets
existing_data = conn.read(worksheet="Foglio1", usecols=list(range(4)), ttl=5)
existing_data = existing_data.dropna(how="all")

logo = "logo2.png"
# Controllo IF

is_somma_valori = False
# Creazione della colonna per il logo nella sidebar
sidebar_col = st.sidebar.image(logo, use_column_width=True)

is_aut = False


 # Campo di input per l'email nella sidebar
email = st.text_input("Email:")

# Bottone di accesso nella sidebar

if email and  email in  existing_data.values:
    st.success(f"Benvenut {email}")
    is_aut = True
    st.title("FantaJesaper")
    giocatori_selezionati = []
    crediti_totali = 0
    numeri = 0 
        
    widget_counter = 0

    while crediti_totali <= 25:
            giocatori_disponibili = [g for g in giocatori if g["crediti"] <= (25 - crediti_totali)]
            giocatore_scelto = st.selectbox("Seleziona un giocatore:", [g["nome"] for g in giocatori_disponibili], key=f"giocatore_select_{widget_counter}", index=None)

            for giocatore in giocatori_disponibili:
                if giocatore["nome"] == giocatore_scelto:
                    crediti_totali += giocatore["crediti"]
                    giocatori_selezionati.append(giocatore)
                    giocatori.remove(giocatore)

                    # Display the player's image
                    player_photo_path = f"photos/{giocatore['foto']}" 
                    if(giocatore['foto'] in os.listdir("photos")):
                        st.image(player_photo_path, caption=giocatore["nome"], use_column_width=False, width=200)
                    
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

    st.markdown("<h2>Il tuo Team:</h2>", unsafe_allow_html=True)

    for giocatore in giocatori_selezionati:
            st.write(f"- {giocatore['nome']}")

    submit_button = st.button("Aggiorna il team")

    if submit_button :
            # Ottieni l'indice della riga corrispondente all'email fornita
            index_to_update = existing_data[existing_data['Email'] == email].index
            st.write(index_to_update)

            if crediti_totali <= 20:
                # Ottieni i nomi dei giocatori selezionati come una lista di stringhe
                giocatori_selezionati_nomi = [giocatore["nome"] for giocatore in giocatori_selezionati]
                # Converti la lista di nomi in una stringa separata da virgole
                giocatori_selezionati_stringa = ", ".join(giocatori_selezionati_nomi)

                # Aggiorna solo la colonna "Giocatore I" della riga corrispondente
                existing_data.loc[index_to_update, "Giocatore I "] = giocatori_selezionati_stringa
                conn.update(worksheet="Foglio1", data=existing_data)
                st.success("Foglio di Google Sheets aggiornato con successo!")
            else:
                st.warning("I giocatori selezionati hanno un costo maggiore di quanto puoi spendere")
            
    else:
            st.warning("Email non valida, inserire un'email presente nel foglio Google Sheet") 
         

    






#agg nome su 




    






