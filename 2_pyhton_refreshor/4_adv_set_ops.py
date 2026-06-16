art = {"Nikhil" , "Vinayak" , "Puneet" , "Trishank"}
science = {"Nikhil" , "Vinayak" , "Adam" , "Anne"}
art_only = art.difference(science)
science_only = science.difference(art)
all = art.union(science_only)
both = art.intersection(science)
print(f"Art only: {art_only}\nScience only: {science_only}\nAll: {all}\n Both: {both}")
this is what i have done 