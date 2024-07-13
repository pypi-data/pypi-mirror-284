# -*- coding: utf-8 -*-
"""
本模块功能：SIAT公共转换函数，获取雅虎证券代码英文名称
所属工具包：证券投资分析工具SIAT 
SIAT：Security Investment Analysis Tool
创建日期：2024年7月12日
最新修订日期：
作者：王德宏 (WANG Dehong, Peter)
作者单位：北京外国语大学国际商学院
作者邮件：wdehong2000@163.com
版权所有：王德宏
用途限制：仅限研究与教学使用，不可商用！商用需要额外授权。
特别声明：作者不对使用本工具进行证券投资导致的任何损益负责！
"""
#==============================================================================
#关闭所有警告
import warnings; warnings.filterwarnings('ignore')

#==============================================================================
if __name__=='__main__':
    test_yahoo_access()
    
def test_yahoo_access():
    """
    功能：测试雅虎财经是否可达
    """
    url="https://finance.yahoo.com"
    result=test_website(url)
    
    return result    

if __name__=='__main__':
    url="https://finance.yahoo.com"
    test_website(url)
    
def test_website(url):
    import requests
    try:
        response = requests.get(url)
        if response.status_code == 200:
            #print(f"Website {url} is accessible")
            return True
        else:
            #print(f"Website {url} access failed，Code：{response.status_code}")
            return False
    except requests.exceptions.RequestException:
        print(f"Website {url} is inaccessible")
        return False
 
if __name__=='__main__':
    s = "Hello, world. Python is fun!"
    split_string(s)
 
def split_string(s):
    import re
    # 使用正则表达式匹配空格、逗号或句点
    return re.split(r'[ ,.]', s)

if __name__=='__main__':
    s = "Hello, world. Python is fun!"
    filter_string(s)
    
def filter_string(s):
    #排除证券名称中的多余空格、逗号和句号
    slist=split_string(s)
    s1=''
    for sl in slist:
        if sl != '':
            if s1=='':
                s1=sl
            else:
                s1=s1+' '+sl
            
    return s1
#==============================================================================
if __name__=='__main__':
    ticker='1155.KL'
    ticker='MSFT'
    ticker='G13.SI'
    ticker='S63.SI'
    ticker='SUS.ST'
    ticker='600519.SS'
    ticker='U11.SI'
    ticker='1295.KL'
    ticker='BMW.DE'
    ticker='MBG.DE'
    ticker='005930.KS'
    ticker='LI'
    ticker='600599.SS'
    ticker='600123.SS'
    ticker='600123.ss'
    ticker='600999.ss'
    ticker='600111.ss'
    ticker='600333.ss'
    ticker='600444.ss'
    ticker='600777.ss'
    
    yahoo_name1(ticker)
    
    #极端测试
    inamelist=[]
    for i in range(100,150+1):
        icode=str(600000+i)+'.SS'
        iname=yahoo_name1(icode)
        print(icode+':',iname)
        inamelist=inamelist+[iname]
    
    #发现问题后单独测试
    ticker='600087.SS'
    yahoo_name1(ticker)
    
    yahoo_name1(ticker,short_name=True)
    
    ticker_name(ticker)
    
def yahoo_name1(ticker,short_name=False,add_suffix=True,maxlen=80):
    """
    功能：从雅虎财经取得全球证券名称，仅限英文。需要去掉常用词，如Corporation
    优点：对未定义的证券代码也可给出英文名称，即使在中文语言环境中
    现存问题：需要访问雅虎，且耗时稍长
    """
    #测试雅虎
    if not test_yahoo_access():
        return ticker
    
    #需要去掉的单词，注意顺序不要轻易颠倒！子串包含的，要长文在前！
    remove_list=['Corporation','Berhad','Bhd','PLC','plc','Plc', \
                 ', Inc.','Inc.', \
                 'AG ST','AG','NA O.N.', \
                 'Aktiengesellschaft','(publ)', \
                 ', LLC','LLC', \
                 'Co., Ltd.','Co., Ltd','Co.,Ltd.','Co.,Ltd','Co,.Ltd','co.,ltd', \
                 'Co. LTD','CO.,LTD','Co., Limited', \
                 'Ltd.','Ltd', \
                 'Company', \
                 'Incorporated', \
                 'Corp., Ltd.','Corp.','Corp','AB', \
                'Limited', \
                
                #强行缩短名称长度，去掉不影响名称的花哨词语
                '(Group)','Group', \
                'Science & Technology','High-Tech','High Technology', \
                
                #扫尾漏网之逗号句点
                 '.',',']
        
    """
    remove_list=['Corporation','Berhad','Bhd','PLC','plc','Limited', \
                 'Inc', \
                 'AG ST','AG','NA O.N.', \
                 'Aktiengesellschaft','(publ)', \
                 'LLC', \
                 'Co., Ltd.','Ltd.','Ltd', \
                 'Company', \
                 'Incorporated','Corp.','AB']
    """
    #去掉ticker中的.US后缀
    ticker=ticker.upper()
    ticker1=ticker.replace('.US', "")
    
    import yfinance as yf
    ticker_info = yf.Ticker(ticker1)
    
    try:
        t_info=ticker_info.info
    except:
        pass
        return ticker
    
    try:
        if short_name:
            t_name0=t_info['shortName']
        else:
            t_name0=t_info['longName']
            if len(t_name0) > maxlen:
                t_name0=t_info['shortName']
    except:
        pass
        return ticker #未找到ticker
    
    #过滤逗号句点?过滤也可能带来更多复杂性！
    #t_name1=filter_string(t_name0)
    t_name1=t_name0
    
    for r in remove_list:
        t_name1=t_name1.replace(r, "")

    #排除前后空格        
    t_name=t_name1.strip()
    
    #增加交易所后缀
    if add_suffix:
        tlist=ticker.split('.')
        if len(tlist)==2:
            sid=tlist[1]
            if sid not in ['SS','SZ','BJ']:
                t_name=t_name+'('+sid+')'
    
    return t_name

#==============================================================================
if __name__=='__main__':
    ticker='1155.KL'
    ticker='MSFT'
    ticker='G13.SI'
    ticker='S63.SI'
    ticker='SUS.ST'
    ticker='600519.SS'
    ticker='U11.SI'
    ticker='1295.KL'
    ticker='BMW.DE'
    ticker='MBG.DE'
    ticker='005930.KS'
    ticker='LI'
    ticker='600599.SS'
    ticker='600123.SS'
    ticker='600123.ss'
    ticker='600999.ss'
    ticker='600111.ss'
    ticker='600333.ss'
    ticker='600444.ss'
    ticker='600777.ss'
    
    yahoo_name2(ticker)
    
    #极端测试
    inamelist=[]
    for i in range(0,50+1):
        icode=str(600000+i)+'.SS'
        iname=yahoo_name2(icode)
        print(icode+':',iname)
        inamelist=inamelist+[iname]
    
    #发现问题后单独测试
    ticker='600088.SS'
    yahoo_name1(ticker)
    yahoo_name2(ticker)
    
    yahoo_name2(ticker,short_name=True)
    
    ticker_name(ticker)
    
def yahoo_name2(ticker,short_name=False,add_suffix=True,maxlen=80):
    """
    功能：从雅虎财经取得全球证券名称，仅限英文。需要去掉常用词，如Corporation
    优点：对未定义的证券代码也可给出英文名称，即使在中文语言环境中
    现存问题：需要访问雅虎，且耗时稍长
    """
    #定义需要去掉的单词，注意顺序不要轻易颠倒！子串包含的，要长文在前！前置留空格的为避免误删
    remove_list=[' CORPORATION',' BERHAD',' BHD',' PLC',' INC',' AG ST',' NA O N', \
                 ' AKTIENGESELLSCHAFT','(PUBL)',' LLC', \
                 ' CO LTD',' CO LIMITED',' LTD',' LIMITED',' COMPANY',' INCORPORATED', \
                 ' CORP LTD',' CORP',' AB', \
                 '(GROUP)',' GROUP', \
                     
                 ' SCIENCE & TECHNOLOGY',' HIGH-TECH',' HIGH TECHNOLOGY']
    
    
    #测试雅虎
    if not test_yahoo_access():
        return ticker
        
    #去掉ticker中的.US后缀
    ticker=ticker.upper()
    ticker1=ticker.replace('.US', "")
    
    import yfinance as yf
    ticker_info = yf.Ticker(ticker1)
    
    try:
        t_info=ticker_info.info
    except:
        pass
        return ticker
    
    try:
        if short_name:
            t_name0=t_info['shortName']
        else:
            t_name0=t_info['longName']
            if len(t_name0) > maxlen:
                t_name0=t_info['shortName']
    except:
        pass
        return ticker #未找到ticker
    
    #去掉逗号和句点
    name1=t_name0.replace(',',' ')
    name2=name1.replace('.',' ')
    
    #将字符串中的多个空格变为单个空格
    name3=replace_multiple_spaces(name2)
    
    #将字符串字母全部大写
    name4=name3.upper()
    
    name5=name4
    for ss in remove_list:
        name5=name5.replace(ss,'')

    name6=name5.strip()
    
    name7=t_name0[:len(name6)]

    #增加交易所后缀
    t_name=name7
    if add_suffix:
        tlist=ticker.split('.')
        if len(tlist)==2:
            sid=tlist[1]
            if sid not in ['SS','SZ','BJ']:
                t_name=t_name+'('+sid+')'
    
    return t_name
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================