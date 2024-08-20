from pymol import cmd

def select_backbone_for_measure(region='sele'):
    cmd.select('backbone_for_measure', f'{region} and name C+N+CA')

# Run the function when the script is executed
if __name__ == '__main__':


    select_backbone_for_measure()
