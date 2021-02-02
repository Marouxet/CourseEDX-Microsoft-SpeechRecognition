import argparse
import wer


# create a function that calls wer.string_edit_distance() on every utterance
# and accumulates the errors for the corpus. Then, report the word error rate (WER)
# and the sentence error rate (SER). The WER should include the the total errors as well as the
# separately reporting the percentage of insertions, deletions and substitutions.
# The function signature is
# num_tokens, num_errors, num_deletions, num_insertions, num_substitutions = wer.string_edit_distance(ref=reference_string, hyp=hypothesis_string)


def score(ref_trn=None, hyp_trn=None):

    # Lectura de archivos .trf
    filehand_ref = open(ref_trn, 'r')
    filehand_hyp = open(hyp_trn,'r')

    # Conteo de la cantidad de frases
    number_sentences = 0

    # Variable para contar las frases con errores
    sentences_error = 0

    # Palabras dentro del archivo REF
    reference_words = 0

    # Errores globales
    errors = 0 
    sust = 0
    inser = 0
    delet = 0

    print('\nResultados:\n')
    # Loop dentro del archio REF 
    while True:
        line_r = filehand_ref.readline()
        

        if not line_r:
            break

        number_sentences += 1
        line_list_r = line_r.split()

        # Separo una línea en PRHASE e ID
        phrase_ID = line_list_r.pop(-1)
        phrase_words_r = line_list_r
        
        reference_words = reference_words + len(phrase_words_r)

        # LOOP dentro de archivo HYP para cada linea del Archivo REF, usando el ID como tag
        
        while True:
            line_h = filehand_hyp.readline()
            line_list_h = line_h.split()

            if line_list_h[-1] == phrase_ID:
                line_list_h.pop(-1)
                phrase_words_h = line_list_h
                num_tokens, num_errors, num_deletions, num_insertions, num_substitutions = wer.string_edit_distance(ref=phrase_words_r, hyp=phrase_words_h)
                
                errors = errors + num_errors 
                sust = sust + num_substitutions
                inser = inser + num_insertions
                delet = delet + num_deletions

                WER =  (num_substitutions + num_insertions + num_deletions) / len(phrase_words_r)

                if not num_errors == 0:
                    sentences_error += 1

                print('ID:', phrase_ID, '\n'
                'Palabras de referencia:', phrase_words_r, '\n' 
                'Palabras Adivinadas:', phrase_words_h,'\n'
                'E:' , num_errors, 'D:', num_deletions, 'S:', num_substitutions, 'I:', num_insertions)   

                break
    
    sentences_error_perc = round(sentences_error/number_sentences * 100)
    WER_global = round(errors / reference_words * 100)
    Del_global = round(delet / reference_words * 100)
    Sust_global = round(sust / reference_words * 100)
    Ins_global = round(inser / reference_words * 100)
    # Salida en formato text
    print('El numero de sentencias es:',number_sentences, '\nEl numero de Sentencias con errores es:', sentences_error, '\n'
    'El porcentaje de sentencias con errores es', sentences_error_perc, '% \n'
    'El numero total de palabras en el archivo REF es', reference_words, '\n'
    'Errores totales:', errors,'WER:', Sust_global, '% \n'
    'Sustituciones totales:', sust, Sust_global, ' % \n'
    'Inserciones totales:', inser, Ins_global, ' % \n'
    'Supreciones totales:', delet, Del_global, ' % \n')
    
    return


if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Evaluate ASR results.\n"
                                                 "Computes Word Error Rate and Sentence Error Rate")
    parser.add_argument('-ht', '--hyptrn', help='Hypothesized transcripts in TRN format', required=True, default=None)
    parser.add_argument('-rt', '--reftrn', help='Reference transcripts in TRN format', required=True, default=None)
    args = parser.parse_args()

    if args.reftrn is None or args.hyptrn is None:
        RuntimeError("Must specify reference trn and hypothesis trn files.")

    score(ref_trn=args.reftrn, hyp_trn=args.hyptrn)
