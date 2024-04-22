def cky(G,l):
    T = []
    for i in range(len(l)+1):
       T.append([[] for _ in range(len(l)+1)])
    for i in range(len(l)):
        for llave in G.keys():
          for a in G[llave]:
               if a == l[i:i+1]:
                    T[i+1][i].append(llave)

    for m in range(2,len(l)+1):
      for i in range(0,len(l) - m+1):
        for j in range(i+1,i+m):
            for llave in G.keys():
                for a in G[llave]:
                    if len(a) > 1:
                        if a[0] in T[j][i] and a[1] in T[i+m][j]:
                            T[i+m][i].append(llave)
    return T

def main():
  c = int(input())
  for _ in range(c):
    l = input()
    n = [int(i) for i in l.split()]
    G = {}
    j = 0
    while j < n[0]:
      l = input()
      l = l.split()
      G[l[0]] = []
      for i in range(1,len(l)):
        G[l[0]].append(l[i])
      j+=1
    i = 0
    while i < n[1]:
      l = input()
      ans = cky(G,l)
      if "S" in ans[len(l)][0]:
        print('yes')
      else:
        print('no')
      i+=1
main()