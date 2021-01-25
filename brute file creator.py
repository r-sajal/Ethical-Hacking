####################################################################################################################
'''
You can Read about every single detail in depth on https://rsajal.medium.com
Link to Github - https://github.com/r-sajal/Ethical-Hacking
'''
####################################################################################################################

# important libraries
import itertools # efficient looping
import string    # string functions
import time      # time checking


def password_wordlist(start_range=8,end_range=10,file_name="brute.txt"):
    # string with all characters needed or have potential for being password
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '@' + '#' + '$' + '.'
    # attempts counter
    attempts = 0
    # open file 
    f = open(file_name,'a')

    for password_length in range(start_range, end_range):
        for guess in itertools.product(chars,repeat=password_length): 
            attempts += 1
            guess = ''.join(guess)
            f.write(guess) # write in file
            f.write("\n")
            print(guess, attempts)

    # close file        
    f.close()



start_range = 8
end_range = 10
file_name = "brute_password_list.txt"


start_time = time.time()
# Main function Call
password_wordlist(start_range,end_range,file_name)

end_time = time.time()

print(end_time-start_time) # print the total time for operation 

##### Code by Sajal Rastogi
