import os
from PIL import Image
S="/mnt/user-data/uploads/Maquettes/Images/Paysagiste/"
D="/home/claude/atout-vert-idf/images/"
os.makedirs(D,exist_ok=True)
m={"chantier terrasse en bois.jpg":"terrasse-bois","chantier allée dallée.jpg":"allee-dallee","conception chantier.jpg":"conception","maçonerie paysagère.jpg":"maconnerie","robot tonte de pelouse.jpg":"robot-tonte","Équipe et matériel elagage.jpg":"equipe-elagage","alléé pavés carrelage extérieure.jpg":"allee-paves","Étêtage taille de réduction.jpg":"etetage","Abattage par démontage.jpg":"abattage","Bois de chauffage.jpg":"bois-chauffage","photo de chantier élégage urgence.jpg":"elagage-urgence","imgi_2_tonte.jpg":"tonte","imgi_1_taille-haies.jpg":"taille-haies","imgi_4_creation-espace-vert.jpg":"creation","imgi_6_plantation.jpg":"plantation"}
for f,n in m.items():
    im=Image.open(S+f).convert("RGB"); w,h=im.size
    mw=1600 if n in("terrasse-bois","allee-dallee","conception") else 1000
    if w>mw: im=im.resize((mw,round(h*mw/w)),Image.LANCZOS)
    im.save(D+n+".jpg",quality=80,optimize=True,progressive=True)
    print(n,w,h,"->",im.size,os.path.getsize(D+n+".jpg")//1024,"Ko")
six=["terrasse-bois","allee-dallee","conception","maconnerie","robot-tonte","equipe-elagage"]
sh=Image.new("RGB",(1200,600),"white")
for i,n in enumerate(six):
    t=Image.open(D+n+".jpg"); t.thumbnail((400,300)); sh.paste(t,((i%3)*400,(i//3)*300))
sh.save("/tmp/w/sheet.jpg",quality=70)
