# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    
    #base case: permutation of a single letter, return that letter    
    if(len(sequence) <= 1):
        return [sequence]
    
    else:
        list_to_return = []
        
        for l in range(len(sequence)): #say letter is 'a'
            letter = sequence[l]
            sub_sequence = sequence[slice(l)] + sequence[slice(l+1,len(sequence))]  #sub_sequence is 'bc'
            sub_permutations = get_permutations(sub_sequence) #returns a list: ['bc', 'cb']
            
            for perm in sub_permutations:
                this_perm = letter + perm
                if(not(this_perm in list_to_return)):
                    list_to_return.append(this_perm)
            
        return list_to_return
            
    

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'aaa'
    print('Input:', example_input)
    #print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)


