import time as t

def choice():
    #iccid1 = int(input("Enter the sample iccid1 number to increment :"))
    #iccid2 = int(input("Enter the sample iccid2 number to increment :"))
    #imsi1 = int(input("Enter the sample imsi1 number to increment :"))
    #imsi2 = int(input("Enter the sample imsi2 number to increment :"))
    #msisdn1 = int(input("Enter the sample msisdn1 number to increment :"))
    #msisdn2 = int(input("Enter the sample msisdn2 number to increment :"))
    iccid1 = "1000"
    iccid2 = "2000"
    imsi1 = "3000"
    imsi2 = "4000"
    msisdn1 = "5000"
    msisdn2 = "6000"
    test = """delete from resourcemanagement.sim_allocation where sim_id in (select id from resourcemanagement.sim where msisdn between 'REPLACE_MSISDN1' and 'REPLACE_MSISDN2');
delete from resourcemanagement.sim_allocation where sim_id in (select id from resourcemanagement.sim where imsi between 'REPLACE_IMSI1' and 'REPLACE_IMSI2');
delete from resourcemanagement.sim_allocation where sim_id in (select id from resourcemanagement.sim where iccid between 'REPLACE_ICCID1' and 'REPLACE_ICCID2');
delete from resourcemanagement.sim where iccid between 'REPLACE_ICCID1' and 'REPLACE_ICCID2';
delete from resourcemanagement.sim where imsi between 'REPLACE_IMSI1' and 'REPLACE_IMSI2';
delete from resourcemanagement.msisdn where msisdn between 'REPLACE_MSISDN1' and 'REPLACE_MSISDN2';
delete from restgw.tbl_subscriber where subscription_id_data2 between 'REPLACE_ICCID1' and 'REPLACE_ICCID2';
delete from restgw.tbl_subscriber where subscription_id_data0 between 'REPLACE_IMSI1' and 'REPLACE_IMSI2';
delete from restgw.tbl_subscriber where subscription_id_data1 between 'REPLACE_MSISDN1' and 'REPLACE_MSISDN2';
delete from simlcmanagement.subscription_tag_association where subscription_id in (select id from simlcmanagement.subscription_identity where iccid  between 'REPLACE_ICCID1' and 'REPLACE_ICCID2');
delete from resourcemanagement.ip_address  where id in (select id from simlcmanagement.subscription_identity where imsi between 'REPLACE_IMSI1' and 'REPLACE_IMSI2');
delete from simlcmanagement.subscription_tag_association where subscription_id in(select id from simlcmanagement.subscription_identity where imsi between 'REPLACE_IMSI1' and 'REPLACE_IMSI2');
delete from simlcmanagement.subscription_identity where imsi between 'REPLACE_IMSI1' and 'REPLACE_IMSI2';"""

    log_message = str(test.replace("REPLACE_IMSI1",str(imsi1)))
    log_message = str(log_message.replace("REPLACE_IMSI2",str(imsi2)))
    log_message = str(log_message.replace("REPLACE_MSISDN1",str(msisdn1)))
    log_message = str(log_message.replace("REPLACE_MSISDN2",str(msisdn2)))
    log_message = str(log_message.replace("REPLACE_ICCID1",str(iccid1)))
    log_message = str(log_message.replace("REPLACE_ICCID2",str(iccid2)))
    print (log_message)
    file = open("C:\\WORK\\Devops\\git\\sim_delete_db\\delete_from_db.txt", "w")
    file.write(log_message)
    file.close()
    

def main():
    choice()
main()