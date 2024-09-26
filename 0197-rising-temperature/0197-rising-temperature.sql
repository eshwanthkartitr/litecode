Select a2.id from Weather as a1
Join Weather as a2 On a1.recordDate+1 = a2.recordDate and a1.temperature < a2.temperature