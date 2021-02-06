import os

def get_imlist(path): 
    return [os.path.join(path,f) for f in os.listdir(path) if (f.endswith('.jpg') or f.endswith('.png') or f.endswith('.gif'))]

img_list = get_imlist("F:\\SP2021\\MCM\MCM_C\\2021MCM_ProblemC_Files\\2021MCM_ProblemC_Files")

print(img_list)


