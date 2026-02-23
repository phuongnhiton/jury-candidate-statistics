import pickle

# Read candidate and jury data from pickled files
with open("data.csv", "w", encoding="utf-8") as outfile:
    outfile.write('identifiant;nom;genre;universite;directeur_these;resultat;concours')
    
    with open('BaseCandidat', 'rb') as base_candidate_file:
        candidates = pickle.load(base_candidate_file)
    
    with open('BaseJury', 'rb') as base_jury_file:
        jury = pickle.load(base_jury_file)
    
    # Process each candidate
    for student_id in candidates:
        path_info = 'InformationCandidats/' + student_id + '.txt'
        outfile.write('\n')
        
        with open(path_info, 'r', encoding='utf-8') as info_file:
            result = info_file.readlines()
            name = result[0].split(' --- ')[0].split("s'appelle ")[1]
            gender = result[0].split(' --- ')[1].split('####')[0]
            university = result[1].split(': ')[1].split('####')[0]
            thesis_director = result[2].split(': ')[1].split('####')[0]
            outcome = candidates[student_id][1]
            competition = candidates[student_id][0]
            
            str_output = student_id + ';' + name + ';' + gender + ';' + university + ';' + thesis_director + ';' + outcome + ';' + competition
            outfile.write(str_output)

                
