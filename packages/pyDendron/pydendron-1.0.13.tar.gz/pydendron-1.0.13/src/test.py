#To convert MDB files to CSV files using Python on your local machine,
#you can use the pandas library along with the pyodbc library
#for connecting to the MDB database.

import pandas as pd
import pyodbc

# Set the path to your MDB file
mdb_file_path = '/Users/meignier/Dendro/dataset/sylphe/didier/SylpheDidier.mdb'

# Set the path for the output CSV file
csv_file_path = './output.csv'

# Establish a connection to the MDB file
conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + mdb_file_path
conn = pyodbc.connect(conn_str)

# Fetch the table names from the MDB file
cursor = conn.cursor()
table_names = [table.table_name for table in cursor.tables(tableType='TABLE')]
cursor.close()

# Iterate over each table and convert it to CSV
for table_name in table_names:
    # Read the table into a DataFrame
    query = f'SELECT * FROM [{table_name}]'
    df = pd.read_sql(query, conn)

    # Save the DataFrame as a CSV file
    table_csv_file_path = f'{csv_file_path}_{table_name}.csv'
    df.to_csv(table_csv_file_path, index=False)

# Close the connection to the MDB file
conn.close()

# import panel as pn
# import threading

# class Compute:
#     def __init__(self):
#         self.results = []

#     def long_task(self, stop_event):
#         self.results.clear()
#         count = 0
#         while not stop_event.is_set():
#             print("Task running...")
#             # Simuler un calcul et stocker les résultats
#             self.results.append(count)
#             count += 1
#             stop_event.wait(1)  # Attendre 1 seconde
#         print("Task stopped")

# # Initialiser les éléments nécessaires pour le threading
# stop_event = threading.Event()
# task_thread = None

# # Créer une instance globale de Compute
# compute_instance = Compute()

# # Définir les fonctions pour démarrer et arrêter la tâche
# def start_task(event):
#     global stop_event, task_thread, compute_instance
#     if task_thread and task_thread.is_alive():
#         print("Task already running")
#         return
#     stop_event.clear()
#     task_thread = threading.Thread(target=compute_instance.long_task, args=(stop_event,))
#     task_thread.start()

# def stop_task(event):
#     global stop_event, task_thread
#     stop_event.set()
#     if task_thread:
#         task_thread.join()

# def show_results(event):
#     global compute_instance
#     if task_thread and task_thread.is_alive():
#         print("Task is still running. Please stop it first.")
#     else:
#         print("Results:", compute_instance.results)

# # Configuration de l'interface graphique avec Panel
# start_button = pn.widgets.Button(name="Start Task")
# start_button.on_click(start_task)

# stop_button = pn.widgets.Button(name="Stop Task")
# stop_button.on_click(stop_task)

# results_button = pn.widgets.Button(name="Show Results")
# results_button.on_click(show_results)

# # Disposition des widgets dans une colonne
# layout = pn.Column(start_button, stop_button, results_button)

# # Lancer le tableau de bord Panel
# layout.servable()
