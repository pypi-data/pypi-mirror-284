from . import utils,Sobjects

def create_parsedLine(context,line=None,field=None,value=None,type=None,has_end_event=False):
    parsedLine = create_update_parsedLine(context,line,obj=None,field=field,value=value,type=type)
    append_parsedLines(context,parsedLine)
    if has_end_event == True:
        append_openParsedLines_increaseIdent(context,parsedLine)
    return parsedLine

def create_update_parsedLine(context,line=None,obj=None,field=None,value=None,type=None):
    def append_list(obj,field,val):
        if field in obj:
            obj[field].append(val)
        else:
            obj[field] = [val]

    if line == None: line = context['line']
    try:
        chunks = context['chunks'] if 'chunks' in context else []
    except Exception as e:
        a=1

    if obj == None:
        obj = {
            'type' : type,
            'ident' : context['ident'],
            'exception' :False
        }
        if len(chunks)>3:  obj['Id'] = chunks[3]

    append_list(obj,'lines',line)
  #  append_list(obj,'CPUTime',context['DEF:CPU time'])
 #   append_list(obj,'SOQLQueries',context['DEF:SOQL queries'])
 #   append_list(obj,'cmtCPUTime',context['CMT:CPU time'])
 #   append_list(obj,'cmtSOQLQueries',context['CMT:SOQL queries'])
    append_list(obj,'totalQueries',context['totalQueries'])
    append_list(obj,'time',chunks[0].split(' ')[0])

    limitsIndexes = {}
    for key in context['LU'].keys():
        limitsIndexes[key] = len(context['LU'][key])-1
    append_list(obj,'limitsIndexes',limitsIndexes)

    try:
        if len(chunks)>1:  append_list(obj,'timeStamp',int ((chunks[0].split('(')[1]).split(')')[0]))
        else:  append_list(obj,'timeStamp',0)
    except Exception as e:
        a=1
    if obj['type'] is None:
        a=1

  #  if chunkNum != None:
  #      a=1
    if field is not None:  obj[field] =  value 

    if context['timeZero'] == 0:  context['timeZero'] = obj['timeStamp'][0]

    obj['elapsedTime'] = obj['timeStamp'][0] #- _context['timeZero']

    return obj

def append_openParsedLines_increaseIdent(context,obj,increase=True):
    append_openParsedLines(context,obj)
    if increase == True: context['ident'] = context['ident'] + 1
  #  append_parsedLines(context,obj)
  #  context['parsedLines'].append(obj)

def end_parsedLine(context,type,value,key='key',endsWith=None,decrease=True):
    return pop_openParsedLines_and_decreaseIdent_and_updateParsedLine(context,type,value,key,endsWith,decrease)

def pop_openParsedLines_and_decreaseIdent_and_updateParsedLine(context,type,value,key='key',endsWith=None,decrease=True):
    obj = pop_openParsedLines(context,type=type,key=key,value=value,endsWith=endsWith)
    if obj == None:
        a=1
    else:
        if decrease == True:   context['ident'] = obj['ident']
        create_update_parsedLine(context,context['line'],obj)
    return obj

def append_openParsedLines(context,parsedLine):
    context['openParsedLines'].append(parsedLine)
def append_parsedLines(context,parsedLine):
    context['parsedLines'].append(parsedLine)    

def copy_last_parsedLine(context):
    obj = context['parsedLines'][-1].copy()
    context['parsedLines'].append(obj)
    return obj

def find_in_parsedLines(context,values):
    '''
    - values: an object wiht key, value pairs
    '''
    for line in reversed(context['parsedLines']):
        for key in values.keys():
            if key not in line:
                break
            if line[key]!=values[key]:
                break
        return line
    return None    

def pop_openParsedLines(context,type,value,key='key',endsWith=False):
    openParsedLines = context['openParsedLines']
    try:
        for i,obj in reversed(list(enumerate(openParsedLines))):
            if obj['type'] == type:
                if key not in obj:      continue

                if endsWith == True:
                    if obj[key].endswith(value) or obj[key].startswith(value):
                        openParsedLines.pop(i)
                        return obj    
                else:
                    if obj[key] == value:
                        openParsedLines.pop(i)
                        return obj
    except Exception as e:    print(e) 

    return None           

def find_in_openParsedLines(context,field,value,endsWith=False,delete=True,startsWith=False):
 #   obj = find_inList(context['openParsedLines'],field,value,endsWith,delete,startsWith)

#def find_inList(theList,field,value,endsWith=False,delete=True,startsWith=False):
    try:
        rvs = context['openParsedLines']
        for i,obj in reversed(list(enumerate(rvs))):
            if field in obj:
                if startsWith == True:
                    if obj[field].startswith(value):
                        if delete == True:
                            rvs.pop(i)
                        return obj    
                if endsWith == True:
                    if obj[field].endswith(value):
                        if delete == True:
                            rvs.pop(i)
                        return obj    
                else:
                    if obj[field] == value:
                        if delete==True:
                            rvs.pop(i)
                        return obj
    except Exception as e:
        print(e) 
    return None

def is_in_operation(context,text,contains=False):
    if context['chunks_lenght']<2: return False
    if contains and text in context['chunks'][1]: return True
    elif context['chunks'][1] == text: return True
    return False

def create_LU_limits():
  LU = {
    'SOQL queries': {'v': 0},
    'query rows': {'v': 0},
    'SOSL queries': {'v': 0},
    'DML statements': {'v': 0},
    'Publish Immediate DML': {'v': 0},
    'DML rows': {'v': 0},
    'CPU time': {'v': 0},
    'heap size': {'v': 0},
    'callouts': {'v': 0},
    'Email Invocations': {'v': 0},
    'future calls': {'v': 0},
    'queueable jobs added to the queue': {'v': 0},
    'Mobile Apex push calls': {'v': 0}
  }
  return LU

def append_limits(context,package,limits):
    if package not in context['LU']:
        context['LU'][package] = []
    context['LU'][package].append(limits)

def clone_and_appendLimit(context,limit,value,package='(default)'):
  #  package = '(default)'
    if package not in context['LU']:
        context['LU'][package] = []
    if len(context['LU'][package])>0:
        limits = context['LU'][package][-1].copy()
    else:
        limits = create_LU_limits()
    limits[limit] = {'v':value}
    append_limits(context,package,limits)
   # context['LU'][package].append(limits)

def parseWfRule(pc):
  #  line = context['line']
    context = pc['context']
    chunks = context['chunks'] 

    if is_in_operation(context,'WF_RULE_EVAL',contains=True):
        if 'BEGIN' in chunks[1]:
            create_parsedLine(context,field='output',value='Workflow',type='RULE_EVAL',has_end_event=True)
           # obj = create_update_parsedLine(context,line,field='output',value='Workflow',type='RULE_EVAL')
           # append_openOpenParsedLines_append_parsedLines_increaseIdent(context,obj)
            return True

        if 'END' in chunks[1]:
            end_parsedLine(context,type='RULE_EVAL',key='output',value='Workflow')
            return True

    if is_in_operation(context,'WF_CRITERIA',contains=True):
        if 'BEGIN' in chunks[1]:
           # parsedLine = create_update_parsedLine(context,line,type='WF_CRITERIA')
            parsedLine = create_parsedLine(context,type='WF_CRITERIA',has_end_event=True)

            colon_split=chunks[2].split(':')
            colon_space = colon_split[1].strip().split(' ')
            parsedLine['ObjectName'] = colon_split[0][1:]
            parsedLine['RecordName'] = colon_space[0]
            if len(colon_space)>1:
                parsedLine['RecordID'] = colon_space[1]
            else:
                parsedLine['RecordID'] = ""

            parsedLine['rulename'] = chunks[3]
            parsedLine['rulenameId'] = chunks[4]
            parsedLine['output'] = parsedLine['rulename']

           # append_openOpenParsedLines_append_parsedLines_increaseIdent(context,parsedLine)
            return True

        if 'END' in chunks[1]:
            obj =end_parsedLine(context,type='WF_CRITERIA',key='type',value='WF_CRITERIA')   
            obj['result'] = chunks[2]
            obj['output'] = f"{obj['ObjectName']}: {obj['rulename']} --> {obj['result']}"
            return True
  
    if is_in_operation(context,'WF_RULE_NOT_EVALUATED'):
        parsedLine = end_parsedLine(context,type='WF_CRITERIA',key='type',value='WF_CRITERIA')   
        parsedLine['output'] = f"{parsedLine['rulename']} --> Rule Not Evaluated"
        return True

    if is_in_operation(context,'WF_ACTION'):
        obj = find_in_openParsedLines(context,'output','Workflow',delete=False)
        obj['action'] = chunks[2]
        return True

def parseExceptionThrown(pc):
 #  line = context['line']
    context = pc['context']
    chunks = context['chunks']

  #  if context['chunks_lenght']>1 and chunks[1] == 'EXCEPTION_THROWN':
    if is_in_operation(context,'EXCEPTION_THROWN'):
        parsedLine = create_parsedLine(context,type='EXCEPTION',field='output',value=chunks[3],has_end_event=False)
        context['exception'] = True
        context['exception_msg'] = parsedLine['output']

      #  append_to_parsedLines(context,parsedLine)

      #  context['parsedLines'].append(obj)
        context['file_exception'] = True
        if context['line_index'] != len(context['lines'])-1:
            next = 1
            next_index = context['line_index']+next

            nextline = context['lines'][context['line_index']+next]
            while '|' not in nextline and context['line_index']+next != len(context['lines'])-1:
                if nextline != '':
                    parsedLine = copy_last_parsedLine(context)
                #  parsedLine = context['parsedLines'][-1].copy()
                #  append_to_parsedLines(context,parsedLine)
                # context['parsedLines'].append(parsedLine)
                    parsedLine['output'] = nextline
                next = next + 1
                nextline = context['lines'][context['line_index']+next]
        return True

    if is_in_operation(context,'FATAL_ERROR'):
   # if context['chunks_lenght']>1 and chunks[1] == 'FATAL_ERROR':
        obj = create_parsedLine(context,type='EXCEPTION',field='output',value=chunks[2],has_end_event=False)
        context['exception'] = True
        context['exception_msg'] = obj['output']

    #    context['parsedLines'].append(obj)
        context['file_exception'] = True
        next = 1
        nextline = context['lines'][context['line_index']+next]
        while '|' not in nextline:
            if nextline != '':
                parsedLine = copy_last_parsedLine(context)
               # obj = context['parsedLines'][-1].copy()
               # context['parsedLines'].append(obj)
                parsedLine['output'] = nextline
            next = next + 1
            nextlineIndex = context['line_index']+next
            if nextlineIndex >= len(context['lines']):
                break
            else:
                nextline = context['lines'][nextlineIndex]
        return True

    return False

def parseUserDebug(pc):
    context = pc['context']

    chunks = context['chunks']

    if is_in_operation(context,'USER_DEBUG'):
        obj = create_parsedLine(context,type='DEBUG',has_end_event=False)
        obj['timeStamp'].append(obj['timeStamp'][0])
        obj['type'] = 'DEBUG'
        obj['subType'] = chunks[3]
        obj['output'] = chunks[4]
        if obj['subType'] == 'ERROR':
            context['exception'] = True
            context['exception_msg'] = obj['output']

        obj['apexline'] = chunks[2][1:-1]
        if context['line_index']<(len(context['lines'])-1):
            next = 1
            nextline = context['lines'][context['line_index']+next]
            while '|' not in nextline:
                obj = copy_last_parsedLine(context)
              #  obj = context['parsedLines'][-1].copy()
              #  context['parsedLines'].append(obj)
                obj['output'] = nextline
                next = next + 1
                next_index = context['line_index']+next
                if next_index == len(context['lines']):
                    break
                nextline = context['lines'][next_index]
        if  obj['output'].startswith('*** '):
            def add_to_LU(string,limit):
                if obj['output'].startswith(string):
                    chs = chunks[4].split(':')[1].strip().split(' ')
                    clone_and_appendLimit(context,limit,chs[0])
                    obj['isLimitInfo'] = True
                    return True
                return False

            if  add_to_LU('*** getCpuTime()','CPU time'): return True
            if  add_to_LU('*** getQueries()','SOQL queries'): return True
            if  add_to_LU('*** getQueryRows()','query rows'): return True
            if  add_to_LU('*** getDmlStatements()','DML statements'): return True
            if  add_to_LU('*** getDmlRows()','DML rows'): return True
            if  add_to_LU('*** getHeapSize()','heap size'): return True

        if 'Usage report.' in obj['output']:
            chs = chunks[4].split(':')
            clone_and_appendLimit(context,'heap size',chs[3].strip())
            chs1 = chs[1].split(';')
            clone_and_appendLimit(context,'CPU time',chs1[0].strip())
            obj['isLimitInfo'] = True

            return True

        if  obj['output'].startswith('CPU Time:'):
            chs = chunks[4].split(' ')
            clone_and_appendLimit(context,'CPU time',chs[2])
            obj['isLimitInfo'] = True

        if obj['output'].startswith('CPQCustomHookImplementation'):
            if obj['output'].endswith('PreInvoke'):
                context['CPQCustomHookImplementation'] = 'Started'
            if obj['output'].endswith('PostInvoke'):
                context['CPQCustomHookImplementation'] = 'Finished'

        return True

    return False

def parse_limit_usage(pc):
    context = pc['context']

   # line = context['line']
    chunks = context['chunks']   
    if is_in_operation(context,'CUMULATIVE_LIMIT_USAGE') or is_in_operation(context,'CUMULATIVE_LIMIT_USAGE_END'):
        context['TESTING_LIMITS'] = False

    if is_in_operation(context,'TESTING_LIMITS'):
        context['TESTING_LIMITS'] = True

    if is_in_operation(context,'LIMIT_USAGE_FOR_NS'):
        if 'TESTING_LIMITS' in context and context['TESTING_LIMITS'] == True: 
            return
      #  obj = create_update_parsedLine(context,line,type='LU')
        package = chunks[2]
  #      if 'TESTING_LIMITS' in context and context['TESTING_LIMITS'] == True: 
  #          package = 'test-'+package
      #  if package not in context['LU']:context['LU'][package]=[]
        next = 1
        nextline = context['lines'][context['line_index']+next]
        limits = {}
        while '|' not in nextline:
            if 'out of' in nextline:
                sp1 = nextline.split(':')
                limit = sp1[0].strip()
                if 'Number of' in limit: limit = limit.split('Number of ')[1]
                else: limit = limit.split('Maximum ')[1]
                sp2 = sp1[1].strip().split(' ')

                limits[limit] = {'v':int(sp2[0]),'m':int(sp2[3])}
            next = next + 1
            nextline = context['lines'][context['line_index']+next]
        if limits['heap size']['v'] == 0:
            if 'LU' in context:
                if package in context['LU']:
                    limits['heap size']['v'] = context['LU'][package][-1]['heap size']['v']

        append_limits(context,package,limits)
        return True
      #  context['LU'][package].append(limits)

def parseLimits(pc):
    context = pc['context']

  #  line = context['line']
    chunks = context['chunks'] 

    if is_in_operation(context,'LIMIT_USAGE'):
        if chunks[3] == 'SOQL':
       #     context[f'DEF:SOQL queries'] = chunks[4]
            clone_and_appendLimit(context,'SOQL queries',chunks[4])
            return True
        if chunks[3] == 'SOQL_ROWS':
            clone_and_appendLimit(context,'query rows',chunks[4])

        return True

 #   if '|LIMIT_USAGE|' in line and '|SOQL|' in line: 
 #       context[f'DEF:SOQL queries'] = chunks[4]
 #       return True

 #   if is_in_operation(context,'LIMIT_USAGE_FOR_NS'):
  #      obj = create_parsedLine(context,line,type='LIMIT',has_end_event=False)
  #      obj['output'] = f"{chunks[1].lower()}  {chunks[2]}"
       # context['parsedLines'].append(obj)

     #   limits = chunks[2]
     #   if limits == '(default)':         limitsNS = 'DEF:'
     #   elif limits == 'vlocity_cmt':     limitsNS = 'CMT:'
     #   else:                             limitsNS = f"{limits}:"

    #    next = 1
    #    nextline = context['lines'][context['line_index']+next]
    #    while '|' not in nextline and 1==2:
    #        if 'SOQL queries' in nextline:
    #            nlchunks = nextline.split(' ')
    #            if f'{limitsNS}SOQL queries' not in context:
    #                context[f'{limitsNS}SOQL queries'] = 0
    #            if int(context[f'{limitsNS}SOQL queries']) < int(nlchunks[6]):
    #                context[f'{limitsNS}SOQL queries'] = nlchunks[6]
    #        if 'CPU time' in nextline:
    #            nlchunks = nextline.split(' ')
    #            if f'{limitsNS}CPU time' not in context:
    #                context[f'{limitsNS}CPU time'] = 0
    #            if int(context[f'{limitsNS}CPU time']) < int(nlchunks[5]):
    #                context[f'{limitsNS}CPU time'] = nlchunks[5]
    #        next = next + 1
    #        nextline = context['lines'][context['line_index']+next]
   #     return True

def parseSOQL(pc):
  #  line = context['line']
    context = pc['context']

    chunks = context['chunks']
    if is_in_operation(context,'SOQL_EXECUTE_BEGIN'):


        obj = create_parsedLine(context,type="SOQL",has_end_event=True)
        obj['query'] = chunks[4]

        next_line_index = context['line_index']+1
        nextline = context['lines'][next_line_index]
        while '|' not in nextline:
            obj['query'] = obj['query'] +' ' + nextline.strip()
            next_line_index = next_line_index + 1 
            nextline = context['lines'][next_line_index]

        obj['object'] = obj['query'].lower().split(' from ')[1].strip().split(' ')[0]
        obj['apexline'] = chunks[2][1:-1]

        soql = obj['query'].lower()
        ch_so = obj['query'].split("'")
        if len(ch_so)>1:
            posibles = ch_so[1::2]

            ids = [posible for posible in posibles if Sobjects.checkId(posible) ]
            idss = set(ids)
            if len(idss)>0:
                obj['where_ids'] = ",".join(idss)


        obj['for_update'] = ' for update' in soql

        if 'where' in soql:
            soql = soql.split('where')[0]
        _from = soql.split(' from ')[-1].strip()
        _from = _from.split(' ')[0]

        obj['from'] = _from
        obj['output'] = f"Select: {obj['from']} --> No SOQL_EXECUTE_END found"

      #  append_openOpenParsedLines_append_parsedLines_increaseIdent(context,obj,increase=False)
        return True

    if context['chunks_lenght']>1 and chunks[1] == 'SOQL_EXECUTE_END':
        context['totalQueries'] = context['totalQueries'] + 1
        obj = end_parsedLine(context,type="SOQL",key='type',value='SOQL',decrease=True)
        obj['rows'] = chunks[3].split(':')[1]

        if pc['full_soql']:
          #  query = obj['query']
          #  query = query.replace(' from ',' FROM ')
          #  query = query.replace(' From ',' FROM ')
          #  qs = query.split(' FROM ')
          #  print(qs)
          #  query = f"{qs[0]}{utils.CYELLOW} FROM {utils.CEND}{qs[1]}"
            obj['output'] = f"{obj['query']} --> {utils.CYELLOW}{obj['rows']}{utils.CEND}"
        else:
            for_uptate = "for update" if obj['for_update'] else ""
            ids = f"w:{obj['where_ids']}" if 'where_ids' in obj else ""

            if context['output_format']=='JSON':
                obj['output'] = f"Select {for_uptate}: {obj['from']} --> {obj['rows']} rows {ids}"
            else:
                obj['output'] = f"Select {for_uptate}: {obj['from']} --> {obj['rows']} rows {utils.CFAINT}{utils.CYELLOW}{ids}{utils.CEND}"

        return True

    return False

def parseMethod(pc):
    context = pc['context']

   # line = context['line']
    chunks = context['chunks'] 
    if context['chunks_lenght']>1 and 'METHOD_' in  chunks[1]:
        if len(chunks)<4:
            print(context['line'])
            return

        operation = chunks[1]
       ## method = getMethod(line)
        method = chunks[3] if len(chunks) == 4 else chunks[4]

        if 'PricingPlanHelper.processMatrixRow' in method:
            a=1
        if '(' in method:
            method = method.split('(')[0]

        if 'ENTRY' in operation:
            obj = create_parsedLine(context,type='METHOD',has_end_event=False)
            obj['method'] = method
            obj['apexline'] = chunks[2][1:-1] if chunks[2]!='[EXTERNAL]' else 'EX'
            obj['output'] = obj['method']

            if '.getInstance' in obj['method']:
                pass
            else:
                append_openParsedLines_increaseIdent(context,obj)
            return True

        else:
            obj = find_in_openParsedLines(context,'method',method)
            if obj == None:
                obj = find_in_openParsedLines(context,'method',f"{method}",endsWith=True)
                apexline = chunks[2][1:-1]
                if obj != None and apexline != obj['apexline']:
                    obj == None
            if obj == None:
                obj = find_in_openParsedLines(context,'method',f"{method}",startsWith=True)
                apexline = chunks[2][1:-1]
                if obj != None and apexline != obj['apexline']:
                    obj == None
            if obj is not None:
                context['ident'] = obj['ident']
                create_update_parsedLine(context,obj=obj)

            else:
                obj = create_parsedLine(context,type='NO_ENTRY',has_end_event=False)
                obj['method'] = chunks[-1]
                obj['apexline'] = chunks[2][1:-1] if chunks[2]!='[EXTERNAL]' else 'EX'
            #    context['parsedLines'].append(obj)

            if 'method' in obj:
                obj['output']=obj['method']
            else:
                obj['output']=obj['Id']
            return True

    return False

def parseVariableAssigment(pc):

    context = pc['context']
    limit = pc['var']

 #   line = context['line']
    chunks = context['chunks'] 

    if is_in_operation(context,'VARIABLE_ASSIGNMENT'):
        if len(chunks) >= 5:
            if 'ExecutionException' in chunks[4] or 'ExecutionException' in chunks[4]:
                obj = create_parsedLine(context,type='VAR_ASSIGN',has_end_event=False)
                obj['type'] = 'VAR_ASSIGN'
                obj['subType'] = 'EXCEPTION'
                obj['output'] = chunks[4]
                obj['apexline'] = chunks[2][1:-1] if chunks[2]!='[EXTERNAL]' else 'EX'

               # context['EXP_VAR'] = True

                next = 1
                nextline = context['lines'][context['line_index']+next]
                while ('VARIABLE_ASSIGNMENT' in nextline or '[EXTERNAL]' in nextline) and 'HEAP_ALLOCATE' not in nextline:
                    chunks = nextline.split('|')
                    obj = create_parsedLine(context,line=nextline,type='VAR_ASSIGN',has_end_event=False)
                    obj['type'] = 'VAR_ASSIGN'
                    obj['subType'] = 'EXCEPTION'
                    try:
                        obj['output'] = chunks[4]                
                    except Exception as e:
                        print(e)
                    obj['apexline'] = chunks[2][1:-1] if chunks[2]!='[EXTERNAL]' else 'EX'
                    next = next + 1
                    nextline = context['lines'][context['line_index']+next]
                return True
        if (limit!=None):
            if chunks[3] != 'this': 
                obj = create_parsedLine(context,type='VAR',has_end_event=False)
                obj['type'] = 'VAR'
                obj['subType'] = 'VAR'  
                obj['output'] = f"{chunks[3]} = {chunks[4]}"

                if limit != -1:
                    obj['output'] = obj['output'] [0:limit]

                obj['apexline'] = chunks[2][1:-1]

        return True
    return False

def parseDML(pc):
    context = pc['context']

  #  line = context['line']
    chunks = context['chunks']

    if is_in_operation(context,'DML_BEGIN'):
        obj = create_parsedLine(context,type="DML",has_end_event=True)
        obj['OP'] = chunks[3]
        obj['Type'] = chunks[4]
        obj['Id'] = chunks[2]
        obj['Rows'] = chunks[5]
        obj['apexline'] = chunks[2][1:-1]
        obj['output'] = f"{obj['OP']} {obj['Type']} --> {obj['Rows']}" 
      #  append_openOpenParsedLines_append_parsedLines_increaseIdent(context,obj)
        return True

    if is_in_operation(context,'DML_END'):
        end_parsedLine(context,'DML',key='Id',value=chunks[2])
        return True

    return False

def parseVariableScope(pc):
    context = pc['context']

    line = context['line']
    chunks = context['chunks']

    if is_in_operation(context,'VARIABLE_SCOPE_BEGIN'):
        obj = create_parsedLine(context,type='VSB',has_end_event=False)
        obj['output'] = chunks[4]
        return True

def executeAnonymous(pc):
    context = pc['context']

    if context['line'].startswith('Execute Anonymous'):
        obj = create_parsedLine(context,type='EA',has_end_event=False)
        obj['output'] = context['line'].split(':')[1]

        a=1
        return True

def parseCallOutResponse(pc):
    context = pc['context']

    line = context['line']
    chunks = context['chunks']

    if is_in_operation(context,'CALLOUT_RESPONSE'):
        obj = create_parsedLine(context,line,type='CALLOUT',has_end_event=False)
     #   obj['string'] = chunks[3]
        obj['apexline'] = chunks[2][1:-1]

      #  context['parsedLines'].append(obj)  
        obj['output'] = chunks[3]
        return True

    return False

def parseConstructor(pc):
    context = pc['context']

 #   line = context['line']
    chunks = context['chunks']

    if is_in_operation(context,'CONSTRUCTOR_ENTRY'):
        obj = create_parsedLine(context,field='output',value=chunks[5],type='CONSTRUCTOR',has_end_event=True)
        obj['apexline'] = chunks[2][1:-1] if chunks[2]!='[EXTERNAL]' else 'EX'
     #   append_openOpenParsedLines_append_parsedLines_increaseIdent(context,obj)
        return True

    if is_in_operation(context,'CONSTRUCTOR_EXIT'):
        end_parsedLine(context,type='CONSTRUCTOR',key='output',value=chunks[5])
        return True

    return False

def parseCodeUnit(pc):
    context = pc['context']

#    line = context['line']
    chunks = context['chunks']

    if is_in_operation(context,'CODE_UNIT_STARTED'):
        obj = create_parsedLine(context,type='CODE_UNIT',has_end_event=True)
        obj['output'] = chunks[4] if len(chunks)>4 else chunks[3]
     #   append_openOpenParsedLines_append_parsedLines_increaseIdent(context,obj)
        return True

    if is_in_operation(context,'CODE_UNIT_FINISHED'):
        end_parsedLine(context,'CODE_UNIT',key='output',value=chunks[2])
        return True

    return False

def parseNamedCredentials(pc):
    context = pc['context']

#    line = context['line']
    chunks = context['chunks']

    if is_in_operation(context,'NAMED_CREDENTIAL_REQUEST'):
        create_parsedLine(context,field='output',value=chunks[2],type='NAMED_CRD',has_end_event=True)
       # append_openOpenParsedLines_append_parsedLines_increaseIdent(context,obj)
        return True

    if is_in_operation(context,'NAMED_CREDENTIAL_RESPONSE'):
        end_parsedLine(context,type='NAMED_CRD',key='type',value='NAMED_CRD')
        return True

    return False

def parseFlow(pc):
    context = pc['context']

  #  line = context['line']
    chunks = context['chunks']
    debugList = context['parsedLines']

    if is_in_operation(context,'FLOW_START_INTERVIEW_BEGIN'):
        obj = create_parsedLine(context,type='FLOW_START_INTERVIEW',has_end_event=True)
        obj['interviewId'] = chunks[2]
        obj['Name'] = chunks[3]
        obj['output'] = obj['Name']
      #  append_openOpenParsedLines_append_parsedLines_increaseIdent(context,obj)
        return True

    if is_in_operation(context,'FLOW_START_INTERVIEW_END'):
        interviewId = chunks[2]
        end_parsedLine(context,'FLOW_START_INTERVIEW',key='interviewId',value=interviewId)
        return True

    if is_in_operation(context,'FLOW_ELEMENT_ERROR'):
        obj = create_update_parsedLine(context,type='FLOW_ELEMENT_ERROR')
        obj['message'] = chunks[2]
        obj['elementType'] = chunks[3] if len(chunks)>3 else ''
        obj['elementName'] = chunks[4] if len(chunks)>4 else ''
        obj['output'] = utils.CRED+ f"{obj['message']} in {obj['elementType']}:{obj['elementName']}" + utils.CEND
        #THIS IS NOT CORRECT
        debugList.append(obj)
        context['exception'] = True
        context['exception_msg'] = obj['output']
        return True
    
    if is_in_operation(context,'FLOW_ELEMENT_BEGIN'):
        obj = create_parsedLine(context,type='FLOW_ELEMENT',has_end_event=True)
        obj['interviewId'] = chunks[2]
        obj['elementType'] = chunks[3]
        obj['elementName'] = chunks[4]
        obj['output'] = f"{obj['elementType']}-{obj['elementName']}"
     #   append_openOpenParsedLines_append_parsedLines_increaseIdent(context,obj)
        return True

    if is_in_operation(context,'FLOW_ELEMENT_END'):
        interviewId = chunks[2]
        end_parsedLine(context,'FLOW_ELEMENT',key='interviewId',value=interviewId)

    if is_in_operation(context,'FLOW_RULE_DETAIL'):
        values = {
            'type':'FLOW_ELEMENT',
            'elementType':'FlowDecision',
            'interviewId':chunks[2],
            'elementName':chunks[3]
        }
        obj = find_in_parsedLines(context,values)
        obj['ruleName'] = chunks[3]
        obj['result'] = chunks[4]
        obj['output'] = f"{obj['elementType']}-{obj['elementName']} -- {obj['ruleName']}->{obj['result']}"
        return True

    return False

def parseUserInfo(pc):
    context = pc['context']

    if is_in_operation(context,'USER_INFO'):
        obj = create_parsedLine(context,context['line'],field='output',value=context['chunks'][4],type='USER_INFO',has_end_event=False)
      #  context['parsedLines'].append(obj)
        return True
    return False

def appendEnd(pc):
    context = pc['context']


    #in case there is no line parsed
    if context['parsedLines'][-1]['type'] == 'LOGDATA':
        return
    for line in reversed(context['lines']):
        if '|' in line:
            break

    if 'CPQCustomHookImplementation' in context and  context['CPQCustomHookImplementation'] == 'Started':
        obj = create_parsedLine(context,line,type='EXCEPTION',field='output',value="CPQCustomHookImplementation did not finish",has_end_event=False)
        context['exception'] = True
        context['exception_msg'] = obj['output']

       # context['parsedLines'].append(obj)
        context['file_exception'] = True
        
    lastline = line
    obj = create_update_parsedLine(context,lastline,type="END")
    obj['output'] = 'Final Limits'
    context['parsedLines'].append(obj)