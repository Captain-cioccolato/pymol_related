from pymol import cmd
#please select only CA, C, N as backbone_
def calculate_chain_length(selection):
    model = cmd.get_model(selection)
    total_length = 0.0
    #t=0
    #print(len(model.atom))
    for i in range(3,len(model.atom) - 1):
        atom1 = model.atom[i-3]
        atom2 = model.atom[i ]
        #print(atom1.name, atom2.name)
        if atom1.name in ['CA'] and atom2.name in ['CA']:
            distance = cmd.get_distance(f"{selection} and index {atom1.index}", f"{selection} and index {atom2.index}")
            total_length += distance
            #cmd.show(atom1, 'cartoon')  
            #cmd.show(atom2, 'cartoon')
            #t+=1
    print(f"Total length of the polypeptide chain: {total_length:.2f} Å")
    #print(t)

# Call the function with your selection
calculate_chain_length("backbone_for_measure")