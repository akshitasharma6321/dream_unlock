
def assess_skills(skills):
    return min (10,len(skills))
def peer_review (submission):
 # demo me 8.5/10
    return 8.5
def innovation_index (project):
    return 9.0
def evaluate_talent(student):
    score=0
    score+=   assess_skills(student['skills'])*0.40
   score+= peer_review(student['submission'])*0.30
   score+= innovation_index(student['project'])*0.30
  if score>=8.5:
  return f"TOP"
return f"CONTINUE"
 
#Test run 
student={'skills':['Design',Commerce','coding'],
'submission':'video.mp4','project':'sustainable idea'}
print(evaluate_talent(student))