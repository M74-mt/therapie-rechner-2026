import streamlit as st

# [cite_start]Datenbasis aus der therapie_preise_2026.sql [cite: 2]
preise = {
    "MT (Manuelle Therapie)": 34.80,
    "KG (Krankengymnastik)": 29.00,
    "KGG (Gerätegestützte KG)": 54.50,
    "NFA (Naturmoor)": 36.20,
    "FA (Warmpackung)": 15.80,
    "US (Ultraschall)": 14.30,
    "ML30 (Lymphdrainage 30min)": 35.10,
    "ML45 (Lymphdrainage 45min)": 52.70,
    "ML60 (Lymphdrainage 60min)": 70.20,
    "HL (Heißluft)": 7.50,
    "M (Massage)": 21.10,
    "EIS (Eisbehandlung)": 12.90,
    "ELO (Elektrotherapie)": 8.30,
    "EXT (Extension)": 8.80,
}

# Funktion zum Zurücksetzen der Eingaben
def reset_form():
    for i in range(1, 5):
        st.session_state[f"sel_{i}"] = "Keine Auswahl"
        st.session_state[f"anz_{i}"] = 0

st.set_page_config(page_title="Heilmittel-Rechner", page_icon="🩺")

st.title("🩺 Therapie-Rechner 2026")
st.markdown("Berechnung nach dem Schlüssel: **Gesamtpreis / 45**")

# Reset Button oben rechts platzieren
if st.button("Formular zurücksetzen 🔄"):
    reset_form()
    st.rerun()

gesamtpreis = 0.0
auswahl_optionen = ["Keine Auswahl"] + list(preise.keys())

# Erstellung der 4 Eingabezeilen
for i in range(1, 5):
    col1, col2 = st.columns([3, 1])
    with col1:
        # Nutzung von session_state für die Auswahl
        st.selectbox(f"Anwendung {i}", auswahl_optionen, key=f"sel_{i}")
    with col2:
        # Nutzung von session_state für die Anzahl
        st.number_input("Anzahl", min_value=0, step=1, key=f"anz_{i}")
    
    # Preisberechnung
    wahl = st.session_state[f"sel_{i}"]
    anzahl = st.session_state[f"anz_{i}"]
    
    if wahl != "Keine Auswahl":
        gesamtpreis += preise[wahl] * anzahl

st.divider()

# Ergebnisanzeige
c_res1, c_res2 = st.columns(2)
with c_res1:
    st.metric("Gesamtpreis", f"{gesamtpreis:,.2f} €")

with c_res2:
    # Kaufmännische Rundung: Preis / 45
    anzahl_behandlungen = int(gesamtpreis / 45 + 0.5)
    st.metric("Anzahl Behandlungen", anzahl_behandlungen)

[cite_start]st.caption("Basis: Preisliste 2026 [cite: 2]")
