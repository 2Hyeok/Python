import os
inFp, outFp = None, None
inStr, outStr = '',''
i = 0
secu = 0
secuYN = input('1. 암호화 2. 암호해석 중 선택 : ')
inFname = input('입력 파일명 입력')
outFname = input('출력 파일명 입력')
try:
    if not os.path.exists(inFname):
        raise Exception('{0}은 미존재 파일'.format(inFname))
except Exception as err:
    print('예외 발생:{0}'.format(err))
else:
    if secuYN=='1':
        secu = 100
    elif secuYN=='2':
        secu = -100
    inFp = open('C:/Users/asdfg/OneDrive/바탕 화면/교육/1차/실습/'+inFname, 'r', encoding='utf-8')
    outFp = open('C:/Users/asdfg/OneDrive/바탕 화면/교육/1차/실습/'+outFname, 'w', encoding='utf-8')
    while True:
        inStr = inFp.readline() # 한 라인씩 읽어 옴
        if not inStr: # 파일의 끝까지 읽으면 빠져 나옴
            break
        outStr = ""
        for i in inStr:
            outStr += chr(ord(i) + secu)
            
            
        outFp.write(outStr) # 암호(해독)한 내용을 파일에 저장
    inFp.close()
    outFp.close()
    print('%s ----> %s 변환 완료' %(inFname, outFname))
