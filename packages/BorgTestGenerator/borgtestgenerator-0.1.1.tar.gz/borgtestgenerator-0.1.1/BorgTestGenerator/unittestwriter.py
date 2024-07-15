#coding: utf-8
from .agents.py3_unit_tests_writer import py3UnitTestFileWriter
import os

class unittestwriter(py3UnitTestFileWriter):
    def __init__(self, assistant_id=None):
        super().__init__(assistant_id)
        #self.check_and_retreive()

    def check_and_retreive(self):
        if (type(self.assistant) == None) or (self.assistant.assistant_id == None):
            self.search_and_retreive_assistant()
        return self
    
    def run_generation(self, vector_store_name, files_to_upload):
        try:
            print("Début de la génération...")
            self.upload_files(vector_store_name, files_to_upload)
            self.create_new_thread()
            self.create_new_user_message()
            self.run()
            self.print_assistant_result()
            print("Génération terminée avec succès.")
        except FileNotFoundError as fnf_error:
            print(f"Erreur : {fnf_error}")
        except Exception as e:
            print(f"Erreur inattendue : {e}")
        return self

        
    def save_generation(self, output_filename, overwrite=False):
        if os.path.exists(output_filename):
            if overwrite:
                os.remove(output_filename)
            else:
                print(f"Le fichier {output_filename} existe déjà !")
                return self
            
        print("Sauvegarde de la réponse de l'assistant...")
        self.save_assistant_response_to_file(output_filename, remove_block_delimiters=True)
        print(f"Réponse de l'assistant sauvegardée dans le fichier : {output_filename}")

        return self



"""
from unittestwriter import unittestwriter
utw = unittestwriter()
utw.run_generation("vector_store_name", ["unittestwriter.py"])
utw.save_generation("test_unittestwriter.py")
"""