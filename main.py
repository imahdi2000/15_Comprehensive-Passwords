upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
digit = ["0","1","2","3","4","5","6","7","8","9"]
weird = [".","?","!","&","#",";",":","-","_","*"]

def password_check(password):
    pass_list = [x for x in password]
    alphack = [i for i in upper if i in pass_list]
    if 0 >= len(alphack):
        print "Need Capital Letters"
    betack = [i for i in lower if i in pass_list]
    if 0 >= len(betack):
        return "Need Lowercase Letters"
    digitck = [i for i in digit if i in pass_list]
    if 0 >= len(digitck):
        return "Need Numbers"
    return True

def password_strength(password):
    if (password_check == True):
        pass_list = [x for x in password]
        score = 0
        alpha = [i for i in upper if i in pass_list]
        score += len(alpha)*1.5
        beta = [i for i in lower if i in pass_list]
        score += len(beta)
        digits = [i for i in digit if i in pass_list]
        score += len(digits)*1.2
        w = [i for i in weird if i in pass_list]
        score += len(w)*2
        if score > 10:
            score = 10
        return score
    else:
        return password_check(password)




print "----Checking For Password Requirements-----"
print password_check("Ab2")
print "-------------------------------------"
print password_check("abc")
print "-------------------------------------"
print password_check("123")
print "------- Password Strength  ----------"
print password_strength("Ab2")
print password_strength("abc")
print password_strength("#1iluvCS")
