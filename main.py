from dijsktra import Graph

def run_united_states():
  
  
  # if list element distance is the same then discard
  
  edges = [
    ("LA","SLC",222),
    ("LA","LV",169),
    ("LA", "FL", 676),
    ("LV","FL", 99),
    ("LV","NY",617),
    ("LV","CH",254),
    ("LV","VC",327),
    ("LV","SL",69),
    ("VC","NY",603),
    ("VC","BO",561),
    ("MN","NY",237),
    ("CH","NY",226),
    ("FL","NY",299),
    ("FL","BO",465)

      ]
    
  graph = Graph(edges)
  start = 'LA'
  stop = 'CH'
  path = graph.dijsktra_shortest_path(start, stop)
  print (path)
  print ("There is/are " + str(len(path)-2) + " layover(s)")
  i=0
  total_cost=0
  while i < len(path):
    total_cost += edges[0][2]
    i+=1 
  print("The cost is $" + str(total_cost))
  
  

def run_romania():
  edges = [
    ("Ar", "Si",140),
    ("Ar","Ti",118),
  ]

  graph = Graph(edges)
  start = 'A'
  stop = 'E'
  path = graph.dijsktra_shortest_path(start, stop)
  print (path)

def run_video_graph():
  edges = [ 
    ("A","B",6),
    ("A","D",1),
    ("D","E",1),
    ("B","E",2),
    ("E", "C",5),
    ("B", "C",5),
    ("D","B", 2),

    ]
  graph = Graph(edges)
  start = 'A'
  stop = 'E'
  path = graph.dijsktra_shortest_path(start, stop)
  print (path)


    
def run_sample():
  edges = [
    ('X', 'A', 7),
    ('X', 'B', 2),
    ('X', 'C', 3),
    ('X', 'E', 4),
    ('A', 'B', 3),
    ('A', 'D', 4),
    ('B', 'D', 4),
    ('B', 'H', 5),
    ('C', 'L', 2),
    ('D', 'F', 1),
    ('F', 'H', 3),
    ('G', 'H', 2),
    ('G', 'Y', 2),
    ('I', 'J', 6),
    ('I', 'K', 4),
    ('I', 'L', 4),
    ('J', 'L', 1),
    ('K', 'Y', 5),
  ]
  
  graph = Graph(edges)
  start = 'Y'
  stop = 'X'
  path = graph.dijsktra_shortest_path(start, stop)
  print (path)
  

def main():
  #run_sample()
  #run_video_graph()
  #run_romania()
  run_united_states()

if __name__ == "__main__":
  main()
  