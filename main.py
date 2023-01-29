def Main():
  wörter = open('worter.txt','r').readlines()
  gussed = []
  heüfikeit = {}
  möglich = []
  gelöst = False
  buchtaben = int(input('wie Viele Buchstaben Hat das wort?\r\n'))
  for i in wörter:
    i = i.replace('\n','')
    if len(i) == buchtaben:
      möglich.append(i.lower())
  def getheufikeit():
    heüfikeit = {}
    for a in möglich:
      for b in a:
        b = b.lower()
        if b in heüfikeit:
          heüfikeit[b] += 1
        else:
          heüfikeit[b] = 1
    return heüfikeit
  def getbest(arg):
    best = ''
    temp = 0
    for i in heüfikeit:
      if heüfikeit[i] > temp:
        if not i in gussed:
          temp = heüfikeit[i]
          best = i
    gussed.append(best)
    return temp, best
  #main Loop
  def remove(arg1,arg2,buchstabe):
    temp = []
    temp2 = []
    for b in arg2:
      temp.append(b)
    for i in arg1:
      counter = 0
      possibil = True
      for a in i:
        
          if temp[counter] == '_':
            if a == buchstabe:
              possibil = False
          elif temp[counter] == a:
            pass
          else:
            if a in temp[counter]:
              temp[counter].append(a)
            possibil = False
          counter += 1
        
      if possibil == True:
        temp2.append(i)
    return temp2
  while gelöst == False:
    heüfikeit = getheufikeit()
    print(möglich)
    print(heüfikeit)
    try:
      besterheu, bester = getbest(heüfikeit)
    except:
      return
    print(f'Es Gibt {len(möglich)} Mögliche Wörter')
    if len(möglich) == 1:
      print(f'dass wort ist:{möglich[0]}')
      gussed = True
    else:
      if besterheu == 0:
        print(f'Die Möglichen Lösungen Sind: {möglich}')
        print('fertig')
        gussed = True
      else:
        bekannt = input(f'Guss:{bester} Bitte geb nun die bekanten ein(alle unbekanten als _)')
        möglich = remove(möglich,bekannt,bester)
if __name__ == '__main__':
  while True:
    Main()
  
  
  
  
