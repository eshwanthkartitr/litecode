Select teacher_id,count(Distinct subject_id) as cnt from Teacher
Group by teacher_id