import hashlib
import json

def  integrity_check(file, file_checksum,file_name):
    with open(file, 'rb') as f:
        digest = hashlib.file_digest(f, 'sha256').hexdigest()
    f.close()

    with open(file_checksum,'rb') as f:
        data = json.load(f)
    f.close()

    if digest == data[file_name]:
        return {"valid":True,"checksum":digest,"filename":file_name}
    else:
        return {"valid":False,"checksum":digest,"filename":file_name}
        

def integrity_check_all(initial:bool = False ):
        # Check the integrity of all the files
        # If initial is set to True then it will only return the overall status.
    integrity_array = []
    try:
        check = integrity_check('requirements.txt', 'integrity.json', 'requirements')
        integrity_array.append(check)
        check = integrity_check('app.py', 'integrity.json', 'core')
        integrity_array.append(check)
        if initial:
            for checks in integrity_array:
                if checks['valid']:
                    continue
                else:
                    return True
            return True
        else:
            return True
    except NameError:
        print('error')
        exit(-1)