import common

def Set_CCD():
    msg = common.cmd.CCD
    return msg


def Get_CCD(recv_data):
    # CCDP
    recv = list(recv_data)
    recv, cmd = Get_Data(recv, 0, 3)
    recv, result = Get_Data(recv, 0, 1)
    
    if result == "P":
        return True
    else:
        return False


def Set_CAI(value):
    #  CAI104Part000040040000500500006006000070070000800800009009
    cmd = common.cmd.CAI_default
    result = Get_Value(value)
    return cmd+result if result != None else None
    

def Get_CAI(recv_data):
    # CAIP00000100021
    recv = list(recv_data)
    recv, cmd = Get_Data(recv, 0, 3)
    recv, result = Get_Data(recv, 0, 1)

    if result == "P":
        return True
    elif result =="F":
        return False


def Set_CRP():
    #  CRP1140
    return common.cmd.CRP_default


def Get_CRP(recv_data):
    # CRPP00009201349012004000010010000200200003003000040040000500500006006
    recv = list(recv_data)
    recv, cmd = Get_Data(recv, 0, 3)
    recv, result = Get_Data(recv, 0, 1)

    if result == "P":
        return True
    elif result =="F":
        return False
    
    
def Set_TRR(value):
    #  TRR104Part000040040000500500006006000070070000800800009009
    cmd = common.cmd.TRR_default
    result = Get_Value(value)
    return cmd+result if result != None else None


def Get_TRR(recv_data):
    # TRRP00004PartR00000026P,-1,2410,689,72,405,-2515
    recv = list(recv_data)
    recv, cmd = Get_Data(recv, 0, 3)
    recv, result = Get_Data(recv, 0, 1)

    if result == "P":
        return True
    elif result =="F":
        return False
    

def Shift(recv_data):
    recv = list(recv_data)
    recv, cmd = Get_Data(recv, 0, 3)
    recv, result = Get_Data(recv, 0, 1)

    if result == "P":
        recv, _ = Get_Data(recv, 0, 19)
        recv, positionData = Get_Data(recv, 0, len(recv) -1)
        
        result = []
        values = ''.join(positionData).split(common.com.delimiter)
        for value in values:
                result.append(round(float(value)/1000, 3))
        return result

    elif result =="F":
        return False
    
  
def Set_SPP():
    # SPP0010010000560000
    msg = common.cmd.SPP_default
    return msg


def Set_PoseSPP(value):
    cmd = common.cmd.SPP_default_res
    result = Get_Value(value)
    return cmd+result if result != None else None
    

def Get_SPP(recv_data):
    # SPPPSTRG
    recv = list(recv_data)
    recv, cmd = Get_Data(recv, 0, 2)
    recv, pt = Get_Data(recv, 0, 1) # permanent # Temporary
    recv, result = Get_Data(recv, 0, 1)

    if result == "P":   
        recv, msg = Get_Data(recv, 0, 1)
        if msg == "U":
            return True
        elif msg == "S":
            return True
        else:
            return False

    elif result == "F":
        return False     

    
# ---------------------------------------------------------------------------------

def Get_Value(value):
    if(value):
        try:
            if value.get('_type') == "Pose":
                # x, y, z, rx, ry, rz
                # {'nsync': 0, '_type': 'Pose', 'rx': 0.0, 'x': 1067.366, 'ry': 73.248, 'y': -12.859, 'rz': -0.69, 'z': 1609.909, 'mechinfo': 1, 'crd': 'base', 'j1': 0.0, 'j2': 0.0, 'j3': 0.0, 'j4': 0.0, 'j5': 0.0, 'j6': 0.0}
                
                vSendMsg :str = ""
                
                for values in common.com.valueList:
                    
                    temp: float = value.get(values)
                    valInt = temp * 10000 
                    vSendMsg += ('%08d' % valInt) 
                
                return vSendMsg
        except:
            return None    
    else:
        return None


def Get_Data(list, start, end):
    temp = end
    for i, str in enumerate(list):
        temp -= len(str.encode())
        if temp == 0:
            end = i + 1
            break
        
    data = ''.join(list[start: end])
    cut = list[end:]
    return cut, data
    