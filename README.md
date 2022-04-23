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
    
        let's use rule 110 and make a pattern 80 cols by 24 rows
        
        eca.py 110 80 24
        
        ![image](https://user-images.githubusercontent.com/64670342/164933697-283d0fe9-b2f1-45f7-840f-0db1f3a36d39.png)

