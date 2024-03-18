tekst = input()

start_keyword1 = tekst.index("#")
end_keyword1 = tekst.index(" ",start_keyword1) #tekst[start_keyword1 :-1].index(" ")

start_keyword2 = tekst.index("#", end_keyword1)
end_keyword2 = tekst.index(" ",start_keyword2)

print(tekst[start_keyword1 + 1:end_keyword1])
print(tekst[start_keyword2 + 1:end_keyword2])

