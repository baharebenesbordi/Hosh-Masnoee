def my_final_grade_calculation(filename):
    results = {}
    
    with open(filename, 'r') as file:
        for line in file:
            
            data = line.strip().split(',')
            name = data[0].strip().lower()  
            
            
            quizzes = list(map(int, data[1:7]))  
            assignments = list(map(int, data[7:11]))  
            midterm = int(data[11]) 
            final = int(data[12])  
            
            
            quizzes.sort()
            quizzes = quizzes[2:]  
            
            
            assignments.sort()
            assignments = assignments[1:]  
            
           
            quizzes_average = sum(quizzes) / len(quizzes) * 0.25
            assignments_average = sum(assignments) / len(assignments) * 0.25
            midterm_weighted = midterm * 0.25
            final_weighted = final * 0.25
            
            
            total_score = quizzes_average + assignments_average + midterm_weighted + final_weighted
            
            
            if total_score >= 60:
                results[name] = "pass"
            else:
                results[name] = "fail"
    
    return results
print(my_final_grade_calculation("nomarat.txt"))