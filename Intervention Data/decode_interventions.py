from datetime import datetime
import csv
countries = ["Denmark","Italy","Germany","Spain",\
             "United_Kingdom","France","Norway",\
             "Belgium","Austria","Sweden","Switzerland",\
             "Greece","Portugal","Netherlands"]

interventions = ['mask wearing','public events','border closure',\
                 'schools + universities','self-isolation if ill',\
                 'lockdown','social distancing encouraged']

debug = int(input("debug (1 if yes, 0 if no):"))
if debug: countries = ["Debug"]

def intx(s):
    if s[0]=='"': s = s[1:]
    if s[-1]=='"': s = s[:-1]
    x = 0
    for i in s:
        if i==',': continue
        x = x*10 + ord(i)-ord('0')
    return x

def sortlines(a,b):
    a_date = int(a[3].strftime('%Y%m%d'))
    b_date = int(b[3].strftime('%Y%m%d'))
    if a_date > b_date: return 1
    if a_date < b_date: return -1
    if a[1] < b[1]: return -1
    if a[1] > b[1]: return 1
    return 0

def datediff(a,b):
    return abs((a-b).days)

for country in countries:
    pop = 0
    table = []
    try:
        inn = open("interventions_"+country+".csv",'r')
        spamreader = csv.reader(inn, delimiter=',', quotechar='"')
        for row in spamreader: table.append(row)
        inn.close()
    except:
        print("an error occured with interventions_"+country+".csv")
        continue
    else:
        print("interventions_"+country+".csv opened successfully")

    # table: 5 columns x n rows
    table = table[1:]
    if debug:
        print("table:")
        print(table)
        input()

    # data: dictionary
    data = {}
    for intervention in interventions: data[intervention] = []
    cnt = 0

    # trim unwanted data
    for row in range(len(table)):
        cnt += 1
        table[row] = table[row][:5]

        for col in range(len(table[row])):
            if isinstance(table[row][col],str):
                table[row][col] = table[row][col].strip()
        if '' in table[row]: continue

        table[row][0] = table[row][0].lower()
        table[row][2] = table[row][2].lower()

        if table[row][2] in interventions:
            cnt -= 1
            arr = table[row]
            if isinstance(arr[1],str): arr[1] = intx(arr[1])
            arr[3] = datetime.strptime(arr[3], '%d.%m.%Y')
            if isinstance(arr[4],str): arr[4] = intx(arr[4])
            data[ arr[2] ].append(arr)
            pop = max(pop, arr[1])
        elif 'if ill' in table[row][2]:
            cnt -= 1
            table[row][2] = interventions[4]
            arr = table[row]
            if isinstance(arr[1],str): arr[1] = intx(arr[1])
            arr[3] = datetime.strptime(arr[3], '%d.%m.%Y')
            if isinstance(arr[4],str): arr[4] = intx(arr[4])
            data[ arr[2] ].append(arr)
            pop = max(pop, arr[1])
    if debug:
        print("data:")
        print(data)
        input()
    print("number of ignored lines:",cnt)

    # sort data
    for intervention in interventions:
        data[intervention].sort(sortlines)
    if debug:
        print("sorted data:")
        print(data)
        input()

    # 1-0 sequences
    cumsum = {}
    start = datetime.strptime('31.12.2019', '%d.%m.%Y')
    end = datetime.strptime('03.12.2020', '%d.%m.%Y')
    endl = datediff(start,end)
    for intervention in interventions:
        cumsum[intervention] = [0 for i in range(endl)]
        for line in data[intervention]:
            if line[0]==country.lower():
                delta = pop * line[4]
                for i in range(datediff(start,line[3]),endl):
                    cumsum[intervention][i] = delta

            else:
                delta = line[1] * (-1)**(line[4]+1)
                for i in range(datediff(start,line[3]),endl):
                    cumsum[intervention][i] += delta
    if debug:
        print("cumsum:")
        print(cumsum)
        input()

    # reduce cumsum to float
    for intervention in interventions:
        for i in range(endl):
            if cumsum[intervention][i]==0:continue
            if cumsum[intervention][i]==pop:
                cumsum[intervention][i]=1
                continue
            cumsum[intervention][i] = float(cumsum[intervention][i])/pop
            if cumsum[intervention][i]>1 or cumsum[intervention][i]<0:
                print("error, i=",i,"intervention=",intervention," cumsum=",cumsum[intervention][i])

    if debug:
        print("reduced cumsum:")
        print(cumsum)
        input()

    # output
    out = open("inter_seq_"+country+".csv",'w')
    outx = csv.writer(out,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    outx.writerow(interventions)
    for i in range(endl):
        arr = []
        for intervention in interventions:
            arr.append(str(cumsum[intervention][i]))
        outx.writerow(arr)
    out.close()








