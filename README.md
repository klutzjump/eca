# eca
View elementary cellular automata in your terminal!


    syntax:
        
        pyeca [rule] [cols] [steps]
        
    args:
        
        rule: rule specified using Wolfram notation (1-256)
        
        cols: character width of automaton
        
        steps: number of steps/iterations to compute
        
    optional flags:
    
        --initial or -i: initial state specified with 1s and 0s
        
        --out or -o: character (1s) used as output to terminal
        
    example:
    
        $./eca.py 110 80 24
        
        (uses rule 110, set width to 80 columns, set length to 24 rows)



![image](https://user-images.githubusercontent.com/64670342/164933876-b3e68a53-0a77-4fc6-8338-dc88879c4173.png)
