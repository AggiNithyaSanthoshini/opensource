vignesh, charan = input().split()
win_conditions = {
    'R':'S',
    'P':'R',
    'S':'P'
}
if vignesh == charan:
    print("NULL")
elif win_conditions[vignesh]==charan:
    print("Vignesh")
else:
    print("Charan")
