def dna_comparison(f1,f2,str_input,threshold):
    file_1_ls = []
    file_2_ls = []
    segment_index_ls = []
    file_1_similarities = []
    file_2_similarities = []
    n_list = []
    
    if str_input:
        file1 = f1
        file2 = f2
        for c in file1:
            file_1_ls.extend(c)
        for c in file2:
            file_2_ls.extend(c)
    else:
        file1 = open(f1,"r")
        file2 = open(f2,"r")
        for l in file1:
            for c in l:
                file_1_ls.extend(c)
        for l in file2:
            for c in l:
                file_2_ls.extend(c)
            
    for i in range(len(file_1_ls)):
        current_segment = []
        add_el = False
        for n in range(len(file_2_ls)):
            while i<len(file_1_ls)-1 and n<len(file_2_ls)-1 and (file_1_ls[i]==file_2_ls[n] and file_1_ls[i+1]==file_2_ls[n+1]) and (not i in file_1_similarities) and (not n in file_2_similarities):
                current_segment.append((i, n))
                file_1_similarities.append(i)
                file_2_similarities.append(n)
                i+=1
                n+=1
        
            
        if len(current_segment)>1:
            current_segment.append((i,i - (current_segment[0][0]-current_segment[0][1])))
        
        if len(current_segment)>=threshold: 
            segment_index_ls.append(current_segment)
    
    n = 1
    for ls in segment_index_ls:
        segment_str = ""
        for index in ls:
            segment_str += file_1_ls[index[0]]
        print("---Shared Segment #{0}---".format(n))
        print("FILE 1 INDEX: {0}-{1}".format(ls[0][0],ls[-1][0]))
        print("FILE 2 INDEX: {0}-{1}".format(ls[0][1],ls[-1][1]))
        print(segment_str)
        n+=1
