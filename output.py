import pickle

# Load candidate and jury data
with open("data.csv", "w", encoding="utf-8") as outfile:
    outfile.write('identifiant;nom;genre;universite;directeur_these;resultat;concours')
    
    with open('BaseCandidat', 'rb') as base_candidate_file, open('BaseJury', 'rb') as base_jury_file:
        candidates = pickle.load(base_candidate_file)
        jury = pickle.load(base_jury_file)
        
        total_candidates = len(candidates)
        total_admitted = 0
        
        # Statistics counters
        director_count = 0
        admitted_with_director = 0
        admitted_without_director = 0
        count_paris1 = 0
        admitted_paris1 = 0
        count_rennes1 = 0
        admitted_rennes1 = 0
        count_male = 0
        admitted_male = 0
        count_female = 0
        admitted_female = 0
        
        # Specific conditions
        condition1 = 0
        condition2 = 0
        admitted_condition2 = 0
        condition3 = 0
        admitted_condition3 = 0
        condition4 = 0
        admitted_condition4 = 0
        
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
                
                # Count admissions
                if outcome.lower() == "admis":
                    total_admitted += 1
                
                # Check thesis director in jury
                if thesis_director in jury["11"]:
                    director_count += 1
                    if outcome.lower() == "admis":
                        admitted_with_director += 1
                else:
                    if outcome.lower() == "admis":
                        admitted_without_director += 1
                
                # Count by university
                if university.lower() == 'paris_1':
                    count_paris1 += 1
                    if outcome.lower() == "admis":
                        admitted_paris1 += 1
                
                if university.lower() == 'rennes_1':
                    count_rennes1 += 1
                    if outcome.lower() == "admis":
                        admitted_rennes1 += 1
                
                # Count by gender
                if gender.lower() == "c'est une femme":
                    count_female += 1
                    if outcome.lower() == "admis":
                        admitted_female += 1
                
                if gender.lower() == "c'est un homme":
                    count_male += 1
                    if outcome.lower() == "admis":
                        admitted_male += 1
                
                # Specific conditions
                if gender.lower() == "c'est un homme" and thesis_director in jury["11"] and (university.lower() == 'paris_1' or university.lower() == 'paris_2'):
                    condition1 += 1
                
                if gender.lower() == "c'est une femme" and thesis_director in jury["11"] and university.lower() != 'paris_1' and university.lower() != 'paris_2':
                    condition2 += 1
                    if outcome.lower() == "admis" or outcome.lower() == "admissible":
                        admitted_condition2 += 1
                
                if "a" in name.lower():
                    condition3 += 1
                    if outcome.lower() == "admis" or outcome.lower() == "admissible":
                        admitted_condition3 += 1
                else:
                    condition4 += 1
                    if outcome.lower() == "admis" or outcome.lower() == "admissible":
                        admitted_condition4 += 1
        
        # Calculate percentages
        result_q2 = round((total_admitted / total_candidates) * 100, 2)
        result_q3_1 = round((admitted_with_director / director_count) * 100, 2)
        result_q3_2 = round((admitted_without_director / (total_candidates - director_count)) * 100, 2)
        result_q3_3 = round((admitted_paris1 / count_paris1) * 100, 2)
        result_q3_4 = round((admitted_rennes1 / count_rennes1) * 100, 2)
        result_q3_5 = round((admitted_male / count_male) * 100, 2)
        result_q3_6 = round((admitted_female / count_female) * 100, 2)
        result_q4_2 = round((admitted_condition2 / condition2) * 100, 2)
        result_q4_3 = round((admitted_condition3 / condition3) * 100, 2)
        result_q4_4 = round((admitted_condition4 / condition4) * 100, 2)
        
        # Print results
        print("Question 2:")
        print("La proportion des candidats qui ont été admis est de " + str(result_q2) + "%")
        print("\nQuestion 3:")
        print("La probabilité d'être admis sachant que le candidat a son directeur de thèse dans le jury est de " + str(result_q3_1) + "%")
        print("La probabilité d'être admis sachant que le candidat n'a pas son directeur de thèse dans le jury est de " + str(result_q3_2) + "%")
        print("La probabilité d'être admis sachant que le candidat a fait sa thèse à Paris 1 est de " + str(result_q3_3) + "%")
        print("La probabilité d'être admis sachant que le candidat a fait sa thèse à Rennes 1 est de " + str(result_q3_4) + "%")
        print("La probabilité d'être admis sachant que le candidat est un homme est de " + str(result_q3_5) + "%")
        print("La probabilité d'être admis sachant que le candidat est une femme est de " + str(result_q3_6) + "%")
        print("\nQuestion 4:")
        print("La probabilité d'être admis sachant que le candidat est un homme, a son directeur de thèse dans le jury et a fait sa thèse à Paris 1 ou Paris 2 est de " + str(condition1) + "%")
        print("La probabilité d'être admis sachant que le candidat est une femme, a son directeur de thèse dans le jury et n'a pas fait sa thèse à Paris 1 ou Paris 2 est de " + str(result_q4_2) + "%")
        print("La probabilité d'être admis sachant que le candidat a au moins une fois la lettre 'a' dans son nom ou son prénom est de " + str(result_q4_3) + "%")
        print("La probabilité d'être admis sachant que le candidat n'a pas la lettre 'a' dans son nom ni dans son prénom est de " + str(result_q4_4) + "%")
        
        # Write results to file
        outfile.write("\n\nQuestion 2:")
        outfile.write("\nLa proportion des candidats qui ont été admis est de " + str(result_q2) + "%")
        outfile.write("\n\nQuestion 3:")
        outfile.write("\nLa probabilité d'être admis sachant que le candidat a son directeur de thèse dans le jury est de " + str(result_q3_1) + "%")
        outfile.write("\nLa probabilité d'être admis sachant que le candidat n'a pas son directeur de thèse dans le jury est de " + str(result_q3_2) + "%")
        outfile.write("\nLa probabilité d'être admis sachant que le candidat a fait sa thèse à Paris 1 est de " + str(result_q3_3) + "%")
        outfile.write("\nLa probabilité d'être admis sachant que le candidat a fait sa thèse à Rennes 1 est de " + str(result_q3_4) + "%")
        outfile.write("\nLa probabilité d'être admis sachant que le candidat est un homme est de " + str(result_q3_5) + "%")
        outfile.write("\nLa probabilité d'être admis sachant que le candidat est une femme est de " + str(result_q3_6) + "%")
        outfile.write("\n\nQuestion 4:")
        outfile.write("\nLa probabilité d'être admis sachant que le candidat est un homme, a son directeur de thèse dans le jury et a fait sa thèse à Paris 1 ou Paris 2 est de " + str(condition1) + "%")
        outfile.write("\nLa probabilité d'être admis sachant que le candidat est une femme, a son directeur de thèse dans le jury et n'a pas fait sa thèse à Paris 1 ou Paris 2 est de " + str(result_q4_2) + "%")
        outfile.write("\nLa probabilité d'être admis sachant que le candidat a au moins une fois la lettre 'a' dans son nom ou son prénom est de " + str(result_q4_3) + "%")
        outfile.write("\nLa probabilité d'être admis sachant que le candidat n'a pas la lettre 'a' dans son nom ni dans son prénom est de " + str(result_q4_4) + "%")
