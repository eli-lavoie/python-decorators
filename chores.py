def kids(chore):
    chore_by_kids = chore() 
    chore_by_kids += " by the kids."
    return chore_by_kids

def mom(chore):
    chore_by_mom = chore()
    chore_by_mom += " by Mom."
    return chore_by_mom

def dad(chore):
    chore_by_dad = chore()
    chore_by_dad += " by Dad."
    return chore_by_dad

@kids
def garbage():
    return "The garbage was taken out"

@kids
def dust():
    return "The house was dusted"

@mom
def groom():
    return "The dog was brushed"

@dad
def laundry():
    return "The dirty laundry was cleaned"