from . import common
from . import visionfunc
from . import socketfunc


# functions
def VisionRecv(recv):
    status = False
    cmd = ''.join(list(recv)[0:3])
    if recv is not None:
        
        if common.cmd.CCD == cmd:
            status = visionfunc.Get_CCD(recv)
            if status:
                common.logd("[vision] " + "Calibration Initialization Successful")
            else:
                common.logd("[vision] " + "Calibration Initialization Failed")

        elif common.cmd.CAI == cmd:
            status = visionfunc.Get_CAI(recv_data=recv)
            if status:
                common.logd("[vision] " + "Calibration CAI Successful")
            else:
                common.logd("[vision] " + "Calibration CAI Failed")
                
        elif common.cmd.CRP == cmd:
            status = visionfunc.Get_CRP(recv_data=recv)
            if status:
                common.logd("[vision] " + "Calibration CPR Successful")
            else:
                common.logd("[vision] " + "Calibration CPR Failed")  
                
        elif common.cmd.TRR == cmd:
            status = visionfunc.Get_TRR(recv_data=recv)
            if status:
                common.logd("[vision] " + "Trigger Robotics complete")
            else:
                common.logd("[vision] " + "Trigger Robotics error")    
                
        elif common.cmd.SPP == cmd:
            status = visionfunc.Get_SPP(recv_data=recv)
            if status:
                common.logd("[vision] " + "Set Parameters Successful")
            else:
                common.logd("[vision] " + "Set Parameters Failed")

    return status




def CalibX_com():
    status = False
    apiResult: dict = common.res_api(path='/project/robot/po_cur', query={'crd': 0, 'mechinfo': 1})
    visionMsg = visionfunc.Set_CAI(apiResult)
    
    if visionMsg:
        if socketfunc.send_msg(visionMsg):
            status = True
    else:
        common.logd("[Failed][vision] CalibX_func/send_msg failed")
        return status

    recv = socketfunc.recv_msg()
    if recv:
        if VisionRecv(recv):
            status = True
        else:
            common.logd("[Failed][vision] CalibX_func/recv_msg/VisionRecv failed")     
    else:
        common.logd("[Failed][vision] CalibX_func/recv_msg failed")
        
    return status


def CalibStart():
    # vision open
    try:
        if not socketfunc.open():
            return common.cmd.fail

        status = CalibStart_func()
        socketfunc.is_close()
        
        if status:
            return common.cmd.calibStart_return
        else:
            return common.cmd.fail

    except:
        socketfunc.is_close()
        return common.cmd.fail
        

def CalibStart_func():
    # visionSend : 'CCD' 전송
    if not socketfunc.send_msg(common.cmd.CCD):
        common.logd("[Failed][vision] CalibStart/send_msg failed")
        return False
    
    # visionRecv : CCDP or CCDF 
    recv = socketfunc.recv_msg()
    if recv:
        if not VisionRecv(recv):
            common.logd("[Failed][vision] CalibStart/recv_msg/VisionRecv failed")
            return False
    else:
        common.logd("[Failed][vision] CalibStart/vision recv_msg failed")
        return False
    
    if CalibX_com():
        common.logd(common.cmd.calibStart_return)
    else:
        common.logd("[Failed][vision] CalibX_Com failed")
        return False
    
    return True  



def CalibX():
    try:
        if not socketfunc.open():
            return common.cmd.fail
        
        status = CalibX_func();
        socketfunc.is_close()
        if status:
            return common.cmd.calibX_return
        else:
            common.logd("[Failed][vision] CalibX failed")
            return common.cmd.fail
    except:
        socketfunc.is_close()
        return common.cmd.fail
    



def CalibX_func():
    if CalibX_com():
        return True 
    else:
        common.logd("[Failed][vision] CalibX_func failed")
        return False



def CalibEnd():
    try:
        if not socketfunc.open():
            return common.cmd.fail
   
        status = CalibEnd_func()
        socketfunc.is_close()
        
        if status:
            return common.cmd.calibEnd_return
        else:
            common.logd("[Failed][vision] CalibEnd failed")
            return common.cmd.fail
    except:
        socketfunc.is_close()
        return common.cmd.fail
    


def CalibEnd_func():
    status: bool = False
    if CalibX_com():
        visionMsg = visionfunc.Set_CRP()
        if visionMsg:
            if socketfunc.send_msg(visionMsg):
                status = True
        else:
            common.logd("[Failed][vision] CalibEnd/send_msg failed")
            return False

        recv = socketfunc.recv_msg()
        if recv:
            if VisionRecv(recv):
                status = True
            else:
                common.logd("[Failed][vision] recv_msg/VisionRecv failed")
                return False    
        else:
            common.logd("[Failed][vision] recv_msg failed")
            return False
        
        common.logd(common.cmd.calibEnd_return)  
    else:
        common.logd("[Failed][vision] CalibX failed")
        return False
    
    return status



def ModelPos():
    # vision open
    try:
        if not socketfunc.open():
            return common.cmd.fail

        status = ModelPos_func()
        socketfunc.is_close()
        
        if status:
            # complete
            return common.cmd.calibEnd_return
        else:
            return common.cmd.fail
    except:
        socketfunc.is_close()
        return common.cmd.fail



def ModelPos_func():
    status = False
    apiResult: dict = common.res_api(path='/project/robot/po_cur', query={'crd': 0, 'mechinfo': 1})
    visionMsg = visionfunc.Set_TRR(apiResult)
    
    if visionMsg:
        if socketfunc.send_msg(visionMsg):
            status = True
    else:
        common.logd("[Failed][vision] ModelPos_func/send_msg failed")
        return status

    recv = socketfunc.recv_msg()
    if recv:
        if VisionRecv(recv):
            status = True
        else:
            common.logd("[Failed][vision] ModelPos_func/recv_msg/VisionRecv failed")     
    else:
        common.logd("[Failed][vision] ModelPos_func/recv_msg failed")

    return status


def ModelLeg():
    # vision open
    try:
        if not socketfunc.open():
            return common.cmd.fail
    
        status = ModelLeg_func()
        socketfunc.is_close()
        
        if status:
            # complete
            return common.cmd.calibEnd_return
        else:
            return common.cmd.fail
        
    except:
        socketfunc.is_close()
        return common.cmd.fail
    
    


def ModelLeg_func():
    status: bool = False
    status = True
    visionMsg = visionfunc.Set_SPP()
    
    if visionMsg:
        if socketfunc.send_msg(visionMsg):
            status = True
    else:
        common.logd("[Failed][vision] ModelLeg_func/send_msg failed")
        return False
    
    # SPPPUI08
    recv = socketfunc.recv_msg()
    if recv:
        if VisionRecv(recv):
            status = True
        else:
            common.logd("[Failed][vision] ModelLeg_func/recv_msg/VisionRecv failed")     
    else:
        common.logd("[Failed][vision] ModelLeg_func/recv_msg failed")
        return False
    
    apiResult: dict = common.res_api(path='/project/robot/po_cur', query={'crd': 0, 'mechinfo': 1})
    visionMsg = visionfunc.Set_PoseSPP(apiResult)
    if visionMsg:
        if socketfunc.send_msg(visionMsg):
            status = True
    else:
        common.logd("[Failed][vision] ModelLeg_func/send_msg failed")
        return False
    
    recv = socketfunc.recv_msg()
    if recv:
        if VisionRecv(recv):
            status = True
        else:
            common.logd("[Failed][vision] ModelLeg_func/recv_msg/VisionRecv failed")     
    else:
        common.logd("[Failed][vision] ModelLeg_func/recv_msg failed")
        return False
    
    return status



def Trigger():
    try:
        if not socketfunc.open():
            return common.cmd.fail    
    
        result = Trigger_func()
        socketfunc.is_close()
        
        if result:
            return result
        else:
            return common.cmd.fail
    
    except:
        socketfunc.is_close()
        return common.cmd.fail
    


def Trigger_func():
    result = []
    apiResult: dict = common.res_api(path='/project/robot/po_cur', query={'crd': 0, 'mechinfo': 1})
    visionMsg = visionfunc.Set_TRR(apiResult)
    if visionMsg:
        if socketfunc.send_msg(visionMsg):
            pass
    else:
        common.logd("[Failed][vision] Trigger_func/send_msg failed")
        return False
    
    recv = socketfunc.recv_msg()
    if recv:
        if VisionRecv(recv):
            result = visionfunc.Shift(recv)
        else:
            common.logd("[Failed][vision] Trigger_func/recv_msg/VisionRecv failed")     
    else:
        common.logd("[Failed][vision] Trigger_func/recv_msg failed")
        return False
    
    return result

