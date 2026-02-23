import pickle

# Load candidate data and calculate admission proportion
with open('BaseCandidat', 'rb') as base_candidate_file:
    candidates = pickle.load(base_candidate_file)
    total_candidates = len(candidates)
    admitted_count = 0
    
    for student_id in candidates:
        path_info = 'InformationCandidats/' + student_id + '.txt'
        with open(path_info, 'r', encoding='utf-8') as info_file:
            outcome = candidates[student_id][1]
            if outcome == "admis":
                admitted_count += 1
    
    proportion = (admitted_count / total_candidates) * 100
    print("Proportion of admitted candidates: " + str(proportion) + "%")
  

