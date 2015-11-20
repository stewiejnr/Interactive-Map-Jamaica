def data_creator(parish,num_proj):
    lst = []
    lst2 = []
    for i in range(0,num_proj):
        proj_name = raw_input('Project Name ')
        
        url = raw_input('Url ')
        temp_dict = str({'url':url})
        f = temp_dict.strip('}')
        temp_dict2 = str({'name':proj_name})
        s = temp_dict2.strip('{')
        t1 = f+','+s
        
        lst.append([t1])
        
    print '{"parish_name":"'+parish+'","number_projects": "'+str(num_proj)+'", "projects":'
    print lst

