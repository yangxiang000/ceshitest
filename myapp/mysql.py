import pymysql


def sql(sqlstr):
    db = pymysql.connect("192.168.31.252", 'root', '111111', 'test')
    cursor = db.cursor()
    try:
        cursor.execute(sqlstr)
        db.commit()
        print('创建成功')
    except:
        db.rollback()
        print('创建失败')
    db.close()


if (__name__ == '__main__'):
    # sql(
    #     "create table HB_pay_status (id int primary key ,brwOrdNo char(100),merchId char(100),brwOrdD char(100),ordType char(100),payType char(100),merNo char(100),depId char(100),depNm char(100),productNm char(100),productId char(100),payAmt char(100),loanAmt char(100),loanMonth char(100),mblNo char(100),cusNm char(100),usrProv char(100),mngModel char(100),busTyp char (100),depProvNo char(100),oprId char(100),oprMblNo char(100),rpyDay char(100),appId char(100),appNm char(100),pkgTyp char(100),provinceRate char(100),bonusAmount char(100),needPayFlag char(100));")
    sql(
        "create table HB_pay_status (id int primary key auto_increment,brwOrdNo char(100),brwOrdDt char(100),ordTyp char(100),appId char(100),appNm char(100));")
